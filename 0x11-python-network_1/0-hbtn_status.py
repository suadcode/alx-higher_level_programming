#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    
    # Make a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the response content
        body = response.content
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content: {}'.format(body.decode('utf-8')))
    else:
        print('Failed to fetch the URL. Status code: {}'.format(response.status_code))

