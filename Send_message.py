import password
from password import password
# import library to make the request to the web page
import requests
# Make a secure authentication b/w Client and Server using json
import json

# we've to make api request to that Url
url = "https://www.fast2sms.com/dev/bulk"

# Create a dictionary for message data
# here we've provided our and Customer data
my_data = {
         # This is your sender id 
        'sender_id': 'FSTSMS',
         # Put your message
         'message':f'Your random password for heypython generated!.It is {password}'.,
         
         'language':'english',
         'route': 'p',
         # Send the message to the number
    
         'numbers':'7021087442'
        
        }
# first we'll make request to the Fast2SMS, then it'll authorize us using API key then decide whether to make request to the 
# header is making secure authentication to Fast2sms account
headers = {
    'authorization':'08TmvcTlFbUWhT1w3q9RgegfWOZ5YDhe5l0pwmkGvYnunddWrvvLcwF5lPLW',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cache-Control': "no-cache"

    }
        
# make a post request to send a data to fast2sms. It store in request body
response = requests.request("POST",url,data = my_data,headers = headers)
#load json data from source in dictionary format
returned_msg = json.loads(response.text)

# print the send message--> message is key
# We want Customer to see the message
print(returned_msg['message'])

# Here fast2sms only send message value!
# If you try to access the number and other data it'll give key-error
# Json has only permission of loading message!


        
        
        
        
        