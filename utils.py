import requests
#########################################################################################################
"""
    FIX FOR CALLING MODELS OUTSIDE A MODULE
"""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "staff_record_api.settings")
import django
django.setup()

from django.core.management import call_command
#############################################################################################################

from base.models import StaffRecords

"""
    SERVER ENDPOINTS
"""
url_one = 'https://management-main.vercel.app/'
url_two = 'https://servicemanagement.vercel.app/'


"""
    DATA SKELETON
"""
data = {
    'staff_id':'',
    'last_name':'',
    'first_name':'',
    'email':'',
    'confirmation_status':'',
    'staff_position':'',
    'staff_salary':'',
    'date_joined':''

}


""" 
    MAKE REQUEST TO THE FIRST SERVER 
"""
response_one = requests.get(url_one)

print(f"STATUS CODE FROM SERVER ONE: {response_one.status_code}")
print(f"RESPONSE FROM SERVER ONE: {response_one.json()}")
response_two = requests.get(url_two)
print(f"STATUS CODE FOR SERVER TWO: {response_two.status_code}")

print("RESPONSE ONE DATA")
for record_one in response_one.json():
    data['staff_id'] = record_one['staff_id']
    data['last_name'] = record_one['last_name']
    data['first_name'] = record_one['first_name']
    data['email'] = record_one['email']

    for record_two in response_two.json():
        if record_one['staff_id'] == record_two['staff_id']:
            data['confirmation_status'] = record_two['confirmation_status']
            data['staff_position'] = record_two['staff_position']
            data['staff_salary'] = record_two['staff_salary']
            data['date_joined'] = record_two['date_joined']
    
    print(data)
        
    
    


# print("RESPONSE TWO DATA")
# for record_two in response_two.json():
#     print(record_two) 

"""
    MAKE REQUEST TO THE SECOND SERVER
"""
# print(f"RESPONSE FOR SERVER TWO: {response_two.json()}")



