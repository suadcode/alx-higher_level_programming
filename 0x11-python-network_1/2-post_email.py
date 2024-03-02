#!/usr/bin/python3
"""A Python script that sends a POST request with email as a parameter and displays the body of the response."""

if __name__ == '__main__':
    import urllib.parse
    import urllib.request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    # Data to be sent in the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read()
        print(body.decode('utf-8'))

