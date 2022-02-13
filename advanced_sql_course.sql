SELECT 
    utm_campaign,
    utm_content,
    http_referer,
    COUNT(DISTINCT website_session_id) as no_of_sessions
FROM
    website_sessions
WHERE
    created_at < '2012-04-12'
GROUP BY 1 , 2 , 3
ORDER BY 4 DESC;

SELECT 
    COUNT(DISTINCT ws.website_session_id) AS count_of_sessions,
    COUNT(DISTINCT od.order_id) AS count_of_orders,
    (COUNT(DISTINCT od.order_id) / COUNT(DISTINCT ws.website_session_id))*100 AS sess_to_od_convo_rt
FROM
    website_sessions AS ws
        LEFT JOIN
    orders AS od ON ws.website_session_id = od.website_session_id
WHERE
    ws.created_at < '2012-04-14'
        AND ws.utm_source = 'gsearch'
        AND utm_campaign = 'nonbrand'
ORDER BY 3 DESC;

SELECT 
    MIN(DATE(ws.created_at)) AS week_strt_date,
    COUNT(DISTINCT website_session_id)
FROM
    website_sessions AS ws
WHERE
    ws.created_at < '2012-05-12'
        AND ws.utm_source = 'gsearch'
        AND ws.utm_campaign = 'nonbrand'
GROUP BY WEEK(ws.created_at) , YEAR(ws.created_at);


select 
device_type,
count(distinct ws.website_session_id) as no_of_sessions,
count(distinct od.order_id) as no_of_orders,
(count(distinct od.order_id)/count(distinct ws.website_session_id))*100 as sess_to_or_convo_rt
from 
website_sessions as ws
left join orders as od
on ws.website_session_id=od.website_session_id
where
ws.created_at < '2012-05-11'
        AND ws.utm_source = 'gsearch'
        AND ws.utm_campaign = 'nonbrand'
	group by 1;

select 
min(date(ws.created_at)) as start_of_week,
count(distinct case when ws.device_type = 'desktop' then ws.website_session_id else null end) as d_top_sessions,
count(distinct case when ws.device_type = 'mobile' then ws.website_session_id else null end) as m_sessions
	from website_sessions as ws
	where
	ws.created_at > '2012-04-15'
	AND
	ws.created_at < '2012-06-09'
	AND ws.utm_source = 'gsearch'
	AND ws.utm_campaign = 'nonbrand'
	group by year(ws.created_at),
			 week(ws.created_at);	


# Page view Url and their respective session volumes

SELECT 
    pageview_url, COUNT(DISTINCT website_session_id) AS sessions
FROM
    website_pageviews
WHERE
    created_at < '2012-06-09'
GROUP BY 1
ORDER BY 2 DESC;

# Sessions against each landing page
CREATE TEMPORARY TABLE first_page_view
select  website_session_id, min(website_pageview_id) as pvs
from 
website_pageviews
where created_at<'2012-06-12'
group by 1;

select website_pageviews.pageview_url, count(distinct pvs)
 from 
 first_page_view
 left join website_pageviews on first_page_view.pvs = website_pageviews.website_pageview_id
 where website_pageviews.created_at< '2012-06-12'
 group by 1
 order by 2 desc;
 
 
 
    



