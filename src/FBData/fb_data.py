#app_id = "1246943782093049"
#https://graph.facebook.com/endpoint?key=value&amp;access_token=app_id|app_secret
#app_id = 3130f330b5371fab727f7d12ede9b1c9

import facebook
import requests

graph = facebook.GraphAPI(access_token="",version="2.7")
access_token_request=requests.get("https://graph.facebook.com/me?access_token=1246943782093049|YNTLdZFGz4fJ1qEzYM6COs8NhVU")
#access_token_request=requests.get("https://graph.facebook.com/me?fields=id,name")
access_token_request = access_token_request.json()
#print(access_token_request)

def get_fb_data():
    personal_token_request = requests.get("https://graph.facebook.com/me?fields=id,name")
    name_token = personal_token_request[0][1]
    name = str(name_token)
    return ("You have logged in as " + name)
