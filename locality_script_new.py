import pymysql
import pandas as pd
import sys
import math
from tqdm import tqdm
import inflect



# numer of nearest locality results for each latlon
top_n = 10	

# input filename
in_filename = "locality.csv"

# output filename
filename = "locality_results.csv"


# clean cos angle to range [-1,1] for acos function

def clean_cos(cos_angle):
    return min(1,max(cos_angle,-1))

# ACOS(COS(RADIANS(90-lat1)) *COS(RADIANS(90-lat2)) +SIN(RADIANS(90- lat1)) *SIN(RADIANS(90- lat2)) *COS(RADIANS(lon1-lon2))) *6371

def getDistance(lat1,lon1,lat2,lon2):
    try:
        dist = math.acos(clean_cos(math.cos(math.radians(90-lat1))*math.cos(math.radians(90-lat2)) + math.sin(math.radians(90-lat1))*math.sin(math.radians(90-	lat2))*math.cos(math.radians(lon1-lon2)))) * 6371
    except Exception as e:
        print("Error while calculating distance between latlons and error is {}".format(e))
        dist = -1
    return dist
    


# connect to aryan

db_opts = {
    'user': 'phpmyadmin',
    'password': '10ca1j0y',
    'host': 'dbro.gc.magicpin.in',
    'database': 'aryan'
}

try:
    db = pymysql.connect(**db_opts)
    cursor = db.cursor()
except Exception as e:
    print("Error while connecting to SQL and error is {}".format(e))
    sys.exit(1)
    


latlon_info = {}

latlonSqlFetchQuery = "select lat,lon,name,city,state,country from aryan.locality where is_shadowed=0 and POI=0 and state is not null and country is not null and city is not null"
cursor.execute(latlonSqlFetchQuery)
rows = cursor.fetchall()
for row in rows:
    latlon_info[(row[0],row[1])] = (row[2],row[3],row[4],row[5])
    


# columns = id, lat, lon

data = pd.read_csv(in_filename,encoding='ISO-8859-1')

# test data
# data = pd.DataFrame({"id":[1,2,3],"lat":[27.66,28.503,28.535291],"lon":[77.74,77.097,77.2509375]})


data = data.dropna().reset_index(drop=True)


if top_n > len(latlon_info):
    top_n = len(latlon_info)


prefixes = {}
p = inflect.engine()
for i in range(top_n):
    if i==0:
        prefix = "min_dis"
    else:
        prefix = p.ordinal(i+1) + "_min_dis"
    prefixes[i] = prefix


output_df = pd.DataFrame()

for row in tqdm(data.itertuples(),total=data.shape[0],leave=False,desc="Calculating"):
    dist_map = {}
    lat1 = float(row.lat)
    lon1 = float(row.lon)
    
    for item in latlon_info.keys():
        lat2 = item[0]
        lon2 = item[1]
        dist = getDistance(lat1,lon1,lat2,lon2)
        if dist == -1:
        	continue
        dist_map[(lat2,lon2)] = dist
    
    sorted_dist_map = {k: v for k, v in sorted(dist_map.items(), key=lambda item: item[1])}
    nearest_latlons = list(sorted_dist_map.keys())[:top_n]
    cols = {}
    cols.update({"id": row.id, "lat": lat1, "lon": lon1,
                "address": row.address, "found_locality_in_address": "not found"})
    flag=True
    for index, _latlon in enumerate(nearest_latlons):
        nearest_lat = _latlon[0]
        nearest_lon = _latlon[1]
        info = latlon_info[(nearest_lat,nearest_lon)]
        
        distance = sorted_dist_map[(nearest_lat,nearest_lon)]
        distance_column_name = prefixes[index]
        
        locality = info[0] + " | " + info[1] + " | " + info[2] + " | " + info[3]
        locality_column_name = "locality_" + str(index+1)
	        
        cols.update({distance_column_name:distance,locality_column_name:locality})
        if str(info[0]).lower() in str(row.address).lower() and flag:
            cols["found_locality_in_address"] = locality_column_name
            print(locality_column_name)
            flag = False
    output_df = output_df.append(pd.DataFrame([cols]),ignore_index=True)



output_df.to_csv(filename,index=False,encoding='utf-8')


print("Finished")
