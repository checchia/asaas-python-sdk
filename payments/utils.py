import requests
import json

def create_payment(data=None, access_token=''):
    """creates new payment
    """
    url = 'https://www.asaas.com/api/v2/payments'
    headers = {'access_token': access_token}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return {'status_code': response.status_code, 'content': response.content})

def get_payment(payment_id='', access_token=''):
    """
    get existing payment based on payment id
    """
    url = 'https://www.asaas.com/api/v2/payments/' + payment_id
    headers = {'access_token': access_token}
    response = requests.get(url, headers = headers)
    return {'status_code': response.status_code, 'content': response.content})

def update_payment(payment_id='', data=None, access_token=''):
    """
    update informations on existing payments based on payment id
    """
    url = 'https://www.asaas.com/api/v2/payments/' + payment_id
    headers = {'access_token' : access_token}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return {'status_code': response.status_code, 'content': response.content})

def delete_payment(payment_id='', api_key=''):
    """
    delete existing payment based on payment id
    """
    url = 'https://www.asaas.com/api/v2/payments/' + payment_id
    headers = {'access_token': api_key}
    response = requests.delete(url, data=json.dumps(data), headers=headers)
    return {'status_code': response.status_code, 'content': response.content})

def get_all_payments(api_key=''):
    """
    list all payments
    """
    url = 'https://www.asaas.com/api/v2/payments/'
    headers =	{'access_token': api_key}
    response = requests.get(url, data=json.dumps(data), headers=headers)
    return {'status_code': response.status_code, 'content': response.content})

def get_customer_payments(customer_id='', access_token=''):
    """
    get all payments from a customer based on his customer id
    """
    url = 'https://www.asaas.com/api/v2/customers/' + customer_id + '/payments'
    headers = {'access_token' : access_token, 'content-type' : 'application/json'}
    response = requests.get(url, headers=headers)
    return {'status_code': response.status_code, 'content': response.content})

def get_subscription_payments(subscription_id='', access_token=''):
    """
    get all payments from a subscription based on its subscription id
    """
    url = 'https://www.asaas.com/api/v2/subscriptions/' + subscription_id + '/payments'
    headers = {'access_token' : access_token, 'content-type' : 'application/json'}
    response = requests.get(url, headers=headers)
    return {'status_code': response.status_code, 'content': response.content})
