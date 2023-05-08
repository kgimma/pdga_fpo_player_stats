import requests

def fetch_url(url):
    """Send a request to the web page and get the response"""
    return requests.get(url)
