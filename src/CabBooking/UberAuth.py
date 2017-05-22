from uber_rides.session import Session
from uber_rides.client import UberRidesClient

TOKEN = "8a0G7qoinHyFakeTokenJ7-HUBQQB1robjgS4MwyFLP5kya3" # <----- Replace this dummy Toekn with your own Server Token
session = Session(server_token=TOKEN)
client = UberRidesClient(session)

Work_Lat=28.510536
Work_Long=77.087022
response = client.get_products(Work_Lat,Work_Long)
products = response.json.get('products')

response = client.get_price_estimates(
    start_latitude=37.770,
    start_longitude=-122.411,
    end_latitude=37.791,
    end_longitude=-122.405,
    seat_count=2
)

print(products)

