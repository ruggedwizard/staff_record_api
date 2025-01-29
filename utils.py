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
#############################################################################################################################

"""
SERVER ENDPOINTS
"""
url_one = 'https://management-main.vercel.app/'
url_two = 'https://servicemanagement.vercel.app/'
# """
#     DATA SKELETON
# """
# data = {
#     'staff_id':'',
#     'last_name':'',
#     'first_name':'',
#     'email':'',
#     'confirmation_status':'',
#     'staff_position':'',
#     'staff_salary':'',
#     'date_joined':''
# }

""" 
    MAKE REQUEST TO THE FIRST SERVER 
"""

def fetch_response(url_one:str, url_two:str):
    response_one = requests.get(url_one)
    response_two = requests.get(url_two)

    data1 = response_one.json()
    data2 = response_two.json()

    combined_data = {}

    for item in data1:
        staff_id = item['staff_id']
        if staff_id:
            if staff_id not in combined_data:
                combined_data[staff_id] = {}
            combined_data[staff_id].update(item)
    
    for item in data2:
        staff_id = item['staff_id']
        if staff_id:
            if staff_id not in combined_data:
                combined_data[staff_id] = {}
            combined_data[staff_id].update(item)
    
    staff_list = [value for key, value in combined_data.items()]

   
    return staff_list
print("###################################################################")
print(fetch_response(url_one,url_two))
###################################################################################################################################




