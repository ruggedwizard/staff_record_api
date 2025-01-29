import requests

# Define the endpoints
endpoint1 = "https://management-main.vercel.app/"
endpoint2 = "https://servicemanagement.vercel.app/"

# Make requests to the endpoints
response1 = requests.get(endpoint1)
response2 = requests.get(endpoint2)

# Check if the requests were successful
if response1.status_code == 200 and response2.status_code == 200:
    # Parse the JSON responses
    data1 = response1.json()
    data2 = response2.json()

    # Assuming both responses contain a list of objects with a unique 'staff_id'
    # Create a list to store the combined objects
    staff_list = []

    # Process data from the first endpoint
    for item in data1:
        staff_id = item.get('staff_id')
        if staff_id:
            staff_list.append({
                'staff_id': staff_id,
                'data_from_endpoint1': item  # Store the entire object or specific fields
            })

    # Process data from the second endpoint
    for item in data2:
        staff_id = item.get('staff_id')
        if staff_id:
            # Check if the staff_id already exists in the list
            existing_staff = next((staff for staff in staff_list if staff['staff_id'] == staff_id), None)
            if existing_staff:
                # Update the existing object with data from the second endpoint
                existing_staff['data_from_endpoint2'] = item
            else:
                # Add a new object to the list
                staff_list.append({
                    'staff_id': staff_id,
                    'data_from_endpoint2': item
                })

    # Print the combined list of objects
    print(staff_list)
else:
    print(f"Failed to retrieve data. Status codes: Endpoint1={response1.status_code}, Endpoint2={response2.status_code}")