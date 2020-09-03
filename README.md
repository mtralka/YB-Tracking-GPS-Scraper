# YB Tracking GPS Route Scraper

[YB Tracking](https://www.ybtracking.com/) GPS units are industry standard for marine systems. Each unit comes with 
their own visual webmap interface. However, the data driving these maps are **not** easily publicably accessable. Alternative websites
that track AIS data and provide bulk downloading are hidden behind **massive** paywalls. This script aims circumnavigate these problems.

### What's needed

- Ship name

- Route identifier

Both of these are publicaly visible in the URL of a ship's webmap interface.

![URL Example](/example/URL_Keywords.png)


### Program Outputs

	point_identifiers.json

- master list of route point-identifiers. Does **not** contain Lat / Lng or other data points


	full_route.geojson

- All route points with the following variables:
	
	latFormatted, altitude, datetime, temp, at, lng, tz, lngFormatted, course, , lat, speed])
	*availability may vary by GPS unit*


### Required Python Libraries

- requests, json, datetime, time, pytz
- pandas, geopandas, shapely
