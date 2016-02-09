import requests
import json

def create_customer(data=None, access_token=''):
    """
    creates new customer at Asaas. Data is a json style dictionary with client's data that you wish to save
    """
    url = 'https://www.asaas.com/api/v2/customers'
    headers = {'access_token': access_token}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response

def get_customer(customer_id='', access_token=''):
    """
    Retrieve already created customer from your account at Asaas.
    """
    url = 'https://www.asaas.com/api/v2/customers/' + customer_id
    headers = {'access_token': access_token}
    response = requests.get(url, headers=headers)

def update_customer(customer_id='', data=None, access_token=''):
    """
    Update existing customer' information
    """
    url = 'https://www.asaas.com/api/v2/customers/' + customer_id
    headers =	{'access_token': access_token}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response

def delete_customer(customer_id='', access_token=''):
    """
    Delete customer from asaas acount
    """
    url = 'https://www.asaas.com/api/v2/customers/' + customer_id
    headers =	{'access_token': access_token}
    response = requests.delete(url, headers=headers)
    return response

def list_customers(customer_id='', access_token=''):
    """
    List all customers registered in your account
    """
    url = 'https://www.asaas.com/api/v2/customers'
    headers =   {'access_token': access_token}
    response = requests.get(url, headers=headers)
    return response
