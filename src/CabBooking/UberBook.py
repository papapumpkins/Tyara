from uber_rides.session import Session
from uber_rides.client import UberRidesClient

TOKEN = "8a0G7qoinHynJ7-HUBQQB1robjgS4MwyFLP5kya3" # <----- Replace this dummy Toekn with your own Server Token
session = Session(server_token=TOKEN)
client = UberRidesClient(session)

#Securitas Pvt. Ltd.
Work_Lat=28.510536
Work_Long=77.087022

#University Hostel
Home_Long = 77.185979
Home_Lat =28.547510

#Custom Loction Data
def get_custom_location_coord(location_string):
    return 0
    #Will be added soon
    #Use Google Geocoding API to send string and get lat & long of first search result
'''
#Book a ride depending on request type
def book_ride(request_type):
    if(request_type==1):
        #Book Ride from Home to Work
        # 1. Tell the price.
        # 2. Ask for confirmation
        # 3. Book it!
        
        #Step 1:
        
        
    elif(request_type==2):
        #Book Ride from Work to Home
        #Same flow as above :D 
    
    else:
        #Express error - politely :p 
        return ("I didn't really get your request. Can you repeat it for me ? ")

'''

response = client.get_products(Work_Lat,Work_Long)
products = response.json.get('products')

response = client.get_price_estimates(
    start_latitude=Work_Lat,
    start_longitude=Work_Long,
    end_latitude=Home_Lat,
    end_longitude=Home_Long,
    seat_count=1
)


print(products)
print(response)




