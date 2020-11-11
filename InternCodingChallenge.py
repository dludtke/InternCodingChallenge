#!/usr/bin/env python3
import requests

# Set the request parameters
url = 'https://dludtke.zendesk.com/api/v2/tickets.json'
user = input("Enter your username: ")
pwd = input("Enter your password: ")
id = input("Enter ticket ID (optional): ")
#print(type(id))

# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
ticket_list = data['tickets']

# Parse tickets
if id == "": 
    for ticket in ticket_list:
        print("ID: ",ticket['id']," SUBJECT: ",ticket['subject'])
else:
    #print("ID: ",id," SUBJECT: ",ticket_list[id]['subject'])
    for ticket in ticket_list:
        if ticket['id'] == int(id):
            print("ID: ",ticket['id']," SUBJECT: ",ticket['subject'])