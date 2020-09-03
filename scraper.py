import requests, json, datetime, time
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import pytz

ROUTE_URL = 'https://app.yb.tl/APIX/Blog/GetPositions?'
POINT_URL = 'https://app.yb.tl/APIX/Blog/GetPosition'

# --------------EDIT ME-------------- #
NAME = 'sorlandet' # Ship name
EVENT = '5987' # Route identifier
# ----------------------------------- #

route_params = { 'keyword' : NAME, 'event' : EVENT, '_' : int(datetime.datetime.now(tz=pytz.utc).timestamp() * 1000) }
r = requests.get( url= ROUTE_URL , params= route_params)

print( f'Status: {r}')

# Save master-route point identifiers to json
# these have no gps / sensor data, just route identifiers
with open('point_identifiers.json' , 'w' ) as f:
    json.dump( r.json() , f)

# Open JSON again
with open('point_identifiers.json') as f:
    point_identifiers = json.load(f)

# filter to only route positions
point_identifiers = point_identifiers['positions']

# initialize dataFrame with proper headers
df = pd.DataFrame( columns= ['latFormatted', 'altitude', 'datetime', 'temp', 'at', 'lng', 'tz', 'lngFormatted', 'course', 'id', 'lat', 'speed'])

for point in point_identifiers:

    point_params = { 'keyword' : NAME, 'id' : point['id'], '_' : point['at'] }
    r = requests.get( url = POINT_URL, params= point_params)

    print( f'Status: {r}')
    
    df = df.append( r.json()['position'] , ignore_index  = True)

    time.sleep(.1) # adjust as needed to bypass API restrictions


geo = [Point(pos) for pos in zip( df['lng'] , df['lat'] )]
gpd = gpd.GeoDataFrame( df , geometry= geo )

gpd.to_file("full_route.json", driver="GeoJSON")