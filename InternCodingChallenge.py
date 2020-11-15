#!/usr/bin/env python3
import requests
import sys

# Request parameters
url = 'https://dludtke.zendesk.com/api/v2/tickets.json?page[size]=25'
user = input("Please enter your username: ")
pwd = input("Please enter your password: ")

# User options
print("\nWelcome to the CLI ticket viewer!\n")
print("To view all tickets, please press enter.")
print("To view a single ticket, please specify the ticket ID.")
print("To exit, please press x.\n")
userselection = input(": ")

# Print all tickets
if userselection == "":
    print("\nPrinting all tickets.\n")
    while url:
        # HTTP get request
        response = requests.get(url, auth=(user, pwd))

        # Check for HTTP codes other than 200
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()

        # Decode the JSON response into a dictionary and use the data
        data = response.json()

        for ticket in data['tickets']:
            print("ID: ",ticket['id']," SUBJECT: ",ticket['subject'])

        if data['meta']['has_more']:
            url = data['links']['next']
        else:
            url = None
# Exit the CLI ticket viewer
elif userselection == "x":
    print("\nExiting. Goodbye!\n")
    sys.exit()
# Print the user selected ticket
else:
    print("\nTicket ID requsted\n.")
    # Do the HTTP get request
    url = 'https://dludtke.zendesk.com/api/v2/tickets/'+userselection+'.json'
    print(url)
    response = requests.get(url, auth=(user, pwd))

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    
    print("ID: ",data['ticket']['id']," SUBJECT: ",data['ticket']['subject'],"\nCONTENT: \n",data['ticket']['description'])
