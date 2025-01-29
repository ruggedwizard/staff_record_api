import requests


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