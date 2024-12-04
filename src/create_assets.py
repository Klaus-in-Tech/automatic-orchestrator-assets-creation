import pandas as pd
import requests
import os

from auth import authenticate_uipath_orchestrator

access_token = authenticate_uipath_orchestrator()
orchestrator_url = os.environ.get('ORCHESTRATOR_URL')
assets_url = f'{orchestrator_url}/odata/Assets'
organization_unit_id = os.environ.get('X_UIPATH_ORGANIZATIONUNITID')
excel_file_path = 'K:\\_PROJECTS\\automatic-asset-creation\\assets.xlsx'

# Read the Excel file into a DataFrame
assets = pd.read_excel(excel_file_path, sheet_name='Sheet1')


# Set up your UiPath Orchestrator details
def create_uipath_orchestrator_assets():
    value_scope = 'Global'
    value_type = 'Text'
    # Set the headers for the request
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-UIPATH-OrganizationUnitId': organization_unit_id,
    }

    # Loop through each row in the DataFrame
    for index, row in assets.iterrows():
        asset_name = row['Asset Name']
        asset_value = row['Asset Value']
        # Setting up the asset details
        payload = {
            'Name': asset_name,
            'ValueScope': value_scope,
            'ValueType': value_type,
            'StringValue': asset_value,
            'IntValue': 0,
        }

        # Check if the asset value is an integer
        if isinstance(asset_value, int):
            payload['IntValue'] = asset_value
            payload['ValueType'] = 'Integer'
            payload['StringValue'] = ''
        # Send the POST request to create the assets
        response = requests.post(assets_url, json=payload, headers=headers)

        # Check if the request was successful
        if response.status_code == 201:
            # Extract the assets from the response
            assets_info = response.json()
            print(
                'Assets Info:', assets_info.get('Name'), assets_info.get('StringValue'), assets_info.get('IntValue')
            )
        else:
            print('Failed to create assets from UiPath Orchestrator.')
            print('Response Code:', response.status_code)
            print('Response Body:', response.text)


# Call the function to create assets
create_uipath_orchestrator_assets()
