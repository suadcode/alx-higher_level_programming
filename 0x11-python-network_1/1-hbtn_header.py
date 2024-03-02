#!/usr/bin/python3
"""A Python script that takes in a URL and displays the value of the X-Request-Id variable in the response header."""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

