import json
import os
import requests

d_ulr = "https://developer.api.autodesk.com/"
client_id = os.environ["client_id"]
client_secret = os.environ["client_secret"]


def get_token(event, context):
    url = f"{d_ulr}authentication/v1/authenticate"

    payload = f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}&scope=viewables:read"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)


if __name__ == "__main__":
    print(get_token(None,None))