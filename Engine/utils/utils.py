""" Define utility functions """
import requests
from requests.exceptions import RequestException
import re

URL_VALIDATION_REGEX = r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"

def get_url(url):
    """ Retrieve the contents of a url """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        print("An error occured fetching url: ", e)

def get_image_url(url):
    """ Retrieve the content bytes of an image url """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except RequestException as e:
        print("An error occured fetching url: ", e)

def validate_url(url):
    """ Validate a url to make sure its properly formatted """
    match = re.match(URL_VALIDATION_REGEX, url)
    return True if match else False