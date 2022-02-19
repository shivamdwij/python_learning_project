select 
count(website_session_id),
(count(case when lp = 1 then website_session_id else null end) )/count(website_session_id) as per_lander_page,
count(case when fp = 1 then website_session_id else null end)/count(case when lp = 1 then website_session_id else null end)  as per_mr_fuzzy_page,
count(case when cp = 1 then website_session_id else null end)/count(case when fp = 1 then website_session_id else null end) as per_cart_page
 from (
select
website_session_id,
max(lander_2_page) as lp,
max(mr_fuzzy_page) as fp,
max(cart_page) as cp
 from (   
select website_sessions.website_session_id,
website_pageviews.pageview_url,
website_pageviews.created_at,
case when website_pageviews.pageview_url= "/lander-2" then 1 else 0  end as lander_2_page,
case when website_pageviews.pageview_url= "/the-original-mr-fuzzy" then 1 else 0 end as mr_fuzzy_page,
case when website_pageviews.pageview_url= "/cart" then 1 else 0 end as cart_page
	from website_sessions 
    left join website_pageviews on website_sessions.website_session_id=website_pageviews.website_session_id 	
    where website_sessions.created_at between '2014-01-01' and '2014-04-01' 
    and website_pageviews.pageview_url in ('/lander-2','/the-original-mr-fuzzy','/cart')
    group by 1,3) pageview_flag
    group by 1) as session_id_level_table;