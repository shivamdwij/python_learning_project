# IO a file

# open_file = open("C:\\Users\\MAGICPIN\\Desktop\\myfile_new.txt",'w')
# open_file.write("I created this file")
# open_file.close

with open("C:\\Users\\MAGICPIN\\Desktop\\myfile_new.txt",mode='r') as f:
    print(f.read())