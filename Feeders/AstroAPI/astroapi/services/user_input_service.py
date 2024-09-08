#!/usr/bin/env python3

# Step 1: Receive input from Webflow API
# Assume Webflow API is sending a POST request with birth details

def get_user_data_from_webflow(api_url, api_key):
	"""
	Function to retrieve user data from Webflow forms via API.
	api_url: the endpoint for the Webflow form
	api_key: the API key for authentication
	"""
	headers = {
		'Authorization': f'Bearer {api_key}',
		'Content-Type': 'application/json'
	}
	
	response = requests.get(api_url, headers=headers)
	
	# Assuming the response contains birth data
	if response.status_code == 200:
		return response.json()  # Return the user data in JSON format
	else:
		print("Error fetching data from Webflow")
		return None
	