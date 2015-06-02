#Python wrapper for the Fonenode API (fonenode.com/docs)
#
# https://github.com/aitoehigie/python_fonenode
#
# @author Pascal Ehigie Aito (@pystar) <aitoehigie@gmail.com>
# @version 0.0.1
#Dependencies:
#Python requests library. Kindly get and install from http://www.python-requests.org/

auth_id = ""
auth_secret = ""
#Get the above values from your fonenode user dashboard
base_url = "https://api.fonenode.com/v1/"
sms_url = ""
#this should be set to the user defined endpoint that would handle responses from the fonenode server
sender = 
#this should be your sms enabled fonenode number


import requests

def create_response(text, voice="woman", retries=1, get_digits="true" ):
    #This function creates a response that you can attach \
    #to a call or number
    payload = dict(text=text)
    response = requests.post("https://api.fonenode.com/v1/responses", verify=False, auth=(auth_id, auth_secret),
    data=payload)
    return response

def delete_response(response_id):
    #This function is used to delete a response previously created.
    payload = dict(response_id=response_id)
    response = requests.delete("https://api.fonenode.com/v1/responses", data=payload, auth=(auth_id, auth_secret), verify=False)
    return response    

def list_responses(limit=20):
    #This function is used to list all created responses.
    payload = dict(limit=limit)
    response = requests.get("https://api.fonenode.com/v1/responses", auth=(auth_id, auth_secret),
    data=payload, verify=False)
    return response

def get_response_details(response_id):
    #This function is to get your response details
    payload = dict(response_id=response_id)
    response = requests.get("https://api.fonenode.com/v1/responses",
    auth=(auth_id, auth_secret), data=payload, verify=False)
    return response

def get_billing_history(limit=20):
    #This function is used to get your billing history.
    response = requests.get("https://api.fonenode.com/v1/billing",
    auth = (auth_id, auth_secret), verify=False)
    return response

def update_number_response(response_id):
    #This function is used to attach or change the 
    #response of a number. The response actions will be 
    #fired when an inbound call is made to the number.
    payload = dict(response_id=response_id)
    response = requests.put("https://api.fonenode.com/v1/numbers/", 
    data=payload, auth=(auth_id, auth_secret), verify=False)
    return response

def deactivate_number(number_id):
    #This function is used to release a number earlier purchased
    payload = dict(number_id=number_id)
    response = requests.delete("https://api.fonenode.com/v1\
    /numbers/", data=payload, auth=(auth_id, auth_secret), verify=False)
    return response

def renew_number(number_id, months=1):
    #This function is used to renew a number earlier purchased.
    payload = dict(number_id=number_id, months=months)
    response = requests.put("https://api.fonenode.com/v1/numbers\
    /", data=payload, auth=(auth_id, auth_secret), verify=False)
    return response

def purchase_number(number_id, months=1):
    #This function is used to purchase a number from available numbers.
    payload = dict(number_id=number_id, months=1)
    response = requests.post("https://api.fonenode.com/v1/numbers", data=payload,
    auth = (auth_id, auth_secret), verify=False)
    return response

def get_number(number_id):
    #This function returns details about a number
    payload = dict(number_id=number_id)
    response = requests.get("https://api.fonenode.com\
    /v1/numbers", data=payload, verify=False)
    return response

def get_own_numbers(limit=20, offset=0):
    #This function returns the number you own
    payload = dict(limit=limit, offset=offset)
    response = requests.get("https://api.fonenode.com/v1\
    /numbers", data=payload, verify=False)
    return response

def available_numbers(limit=20, offset=0):
    #This function returns numbers available for purchase
    #for inbound calls.
    payload = dict(limit=limit, offset=offset)
    response = requests.get("https://api.fonenode.com\
    /v1/numbers/available", data=payload, verify=False)
    return response

def call_details(call_id):
    #This function gets details about a call.
    payload = dict(call_id=call_id)
    response = requests.get("https://api.fonenode.com\
    /v1/calls", data=payload, verify=False)
    return response

def list_calls(limit=20, offset=0):
    #This function lists inbound and outband calls
    #via your account.
    payload = dict(limit=limit, offset=offset)
    response = requests.get("https://api.fonenode.com/\
    v1/calls/", data=payload, auth=(auth_id, auth_secret), verify=False)   
    return response

def call(to="to", response_id="response_id", from_who="who"):
    #This function is used to make calls to one or 
    #more numbers using a response already created.
    payload = {"to":to, "response_id":response_id, "from":from_who}
    response = requests.post("https://api.fonenode.com/v1/calls",\
    data=payload, auth=(auth_id, auth_secret), verify=False)
    return response

def quick_call(to="to", text="text", from_who="who", voice="woman"):
    #This function is used to make a quick call without creating a response.
    #payload = dict(to=to, text=text, voice=voice)
    payload = {"to":to, "text":text, "from":from_who, "voice":voice}
    response = requests.post("https://api.fonenode.com/v1/calls/quick",\
    data=payload, auth=(auth_id, auth_secret), verify=False)
    return response

####SMS features for SMS enabled fonenode numbers

def received_messages(limit=20):
    #This function is used to return all received messages
    response = requests.get("https://api.fonenode.com/v1/sms/inbox", \
    auth = (auth_id, auth_secret), verify=False)
    return response

def received_message(message_id):
    #This function returns the details of the received message with the specified message_id passed in as an argument
    #puzzling behavior. look into why it returns all messages and not the specified one
    payload = dict(message_id=message_id)
    response = requests.get("https://api.fonenode.com/v1/sms/inbox", \
    data = payload, auth = (auth_id, auth_secret), verify = False)
    return response

def send_sms(to, text, sender=sender):
    #this function sends sms using fonenode
    payload = {"to":to, "text":text, "from":sender}
    response = requests.post("https://api.fonenode.com/v1/sms", \
    data = payload, auth = (auth_id, auth_secret), verify=False)
    return response

def sent_messages(limit=20):
    #this function returns all sent messages
    response = requests.get("https://api.fonenode.com/v1/sms/outbox", \
    auth = (auth_id, auth_secret), verify=False)
    return response

def get_numbers():
    #this function lists all numbers attached to a fonenode account
    response = requests.get("https://api.fonenode.com/v1/numbers", \
    auth = (auth_id, auth_secret), verify=False)
    return response

def attach_number(number_id, sms_url=sms_url):
    #this function attaches a fonenode number to an SMS endpoint
    payload = {"id": number_id, "sms_url": sms_url}
    response = requests.put("https://api.fonenode.com/v1/numbers/"+number_id, \
    data = payload, auth = (auth_id, auth_secret), verify = False)
    return response

def sms_to_call():
    #this function would immediately call any number that \
    #sends an sms to the fonenode number \
    #I cant implement this now because I havent defined a \
    #proper sms endpoint
    return








 






	

