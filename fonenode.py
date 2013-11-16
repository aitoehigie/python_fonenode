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
base_url = "https://api.fonenode.com/v1/"

import requests

def create_response(text, voice="woman", retries=1, get_digits="true", ):
    #This function creates a response that you can attach \
    to a call or number
    payload = dict(text=text)
    response = requests.post("https://api.fonenode.com/v1/responses", auth=(auth_id, auth_secret),
    data=payload)
    return response

def list_responses(limit=20):
    #This response is to list all created responses.
    payload = dict(limit=limit)
    response = requests.get("https://api.fonenode.com/v1/responses", auth=(auth_id, auth_secret),
    data=payload)
    return response

def get_response_details(response_id):
    #This function is to get your response details
    payload = dict(response_id=response_id)
    response = requests.get("https://api.fonenode.com/v1/responses",
    auth=(auth_id, auth_secret), data=payload)
    return response

def get_billing_history(limit=20):
    #This function is used to get your billing history.
    response = requests.get("https://api.fonenode.com/v1/billing",
    auth = (auth_id, auth_secret))
    return response

def update_number_response(response_id):
    #This function is used to attach or change the 
    #response of a number. The response actions will be 
    #fired when an inbound call is made to the number.
    payload = dict(response_id=response_id)
    response = requests.put("https://api.fonenode.com/v1/numbers/", 
    data=payload, auth=(auth_id, auth_secret))
    return response

def deactivate_number(number_id):
    #This function is used to release a number earlier purchased
    payload = dict(number_id=number_id)
    response = requests.delete("https://api.fonenode.com/v1
    /numbers/", data=payload, auth=(auth_id, auth_secret))
    return response

def renew_number(number_id, months=1):
    #This function is used to renew a number earlier purchased.
    payload = dict(number_id=number_id, months=months)
    response = requests.put("https://api.fonenode.com/v1/numbers
    /", data=payload, auth=(auth_id, auth_secret))
    return response



	

