SELECT 
    website_pageviews.pageview_url,
    count(website_sessions.website_session_id),
    count(orders.order_id),
  count(orders.order_id)/count(website_sessions.website_session_id) as sessions_to_order_convo_rt
FROM
    website_sessions
        LEFT JOIN
    website_pageviews ON website_sessions.website_session_id = website_pageviews.website_session_id
    left join
    orders on website_sessions.website_session_id=orders.website_session_id
WHERE
    website_pageviews.pageview_url IN ('/billing-2' , '/billing')
        AND website_pageviews.created_at > '2012-09-10'  -- /billing-2 went live
        AND website_pageviews.created_at < '2012-11-10'
        group by 1;