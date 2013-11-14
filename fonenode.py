#Python wrapper for the Fonenode API (fonenode.com/docs)
#
# https://github.com/aitoehigie/python_fonenode
#
# @author Pascal Ehigie Aito (@pystar) <aitoehigie@gmail.com>
# @version 0.0.1
#Dependencies:
#Python requests library. Kindly get and install from http://www.python-requests.org/

auth_id = "auth_id"
auth_secret = "auth_secret"
#Get the above values from your fonenode user dashboard
base_url = "http://api.fonenode.com/v1/"

import requests

def create_response(text):
    payload = dict(text=text)
    requests.post("http://api.fonenode.com/v1/responses", auth=(auth_id, auth_secret),
    data=payload)

def list_responses(limit=20):
    payload = dict(limit=limit)
    return requests.get("http://api.fonenode.com/v1/responses", auth=(auth_id, auth_secret),
data=payload)

def get_response_details(response_id):
    payload = dict(response_id=response_id)
    return requests.get("http://api.fonenode.com/v1/responses",
    auth=(auth_id, auth_secret), data=payload)


	

