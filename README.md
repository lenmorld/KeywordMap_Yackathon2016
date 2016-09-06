# Salamanders' Keyword Map @ Yackathon 2016
Yelp Yackathon 2016 - Data Mashup with Yelp Dataset and Publicly Available Dataset

Project: API Keyword Search + Google Map + Public Dataset

How it works:
User enters a keywords, search keyword from Yelp user reviews
count the number of occurences of that keyword per area
using Montreal area codes (e.g H2L)

As an extra,
get public information per area, including
- number of accidents
- public works and traffic
- average temprature
See the correlation between people's happiness (based on keyword used on reviews)
and environment coniditions


Programming:
- used Apache Drill to query Big Data (Yelp Dataset) using SQL commands
- used Python to process the query results
- Javascript, jQuery, AJAX to load the results to the map (Google Maps API)
- Bootstrap HTML CSS for the UI


![alt text](screens/results2.PNG?raw=true "Menu")



