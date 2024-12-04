import requests
import simplejson as json
import os

# Set up your UiPath Orchestrator details
client_id = os.environ.get('CLIENT_ID')
grant_type = os.environ.get('GRANT_TYPE')
refresh_token = os.environ.get('REFRESH_TOKEN')  # Replace with your refresh token


def authenticate_uipath_orchestrator():
    # Construct the URL for authentication
    auth_url = os.environ.get('AUTH_URL')

    # Set up the payload for authentication
    payload = {
        'grant_type': grant_type,
        'client_id': client_id,
        'refresh_token': refresh_token,
    }

    # Set the headers for the request
    headers = {'Content-Type': 'application/json'}
    # Send the POST request to authenticate
    response = requests.post(auth_url, json=payload, headers=headers)

    # Check if the authentication was successful
    if response.status_code == 200:
        # Extract the access token from the response
        token_info = response.json()
        access_token = token_info['access_token']
        print('Authentication successful!')
        return access_token
    else:
        print('Failed to authenticate with UiPath Orchestrator.')
        print('Response Code:', response.status_code)
        print('Response Body:', response.text)
        return None


if __name__ == '__main__':
    # Authenticate and get the access token
    token = authenticate_uipath_orchestrator()
