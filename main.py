import requests
import json
import time

api_key = "your api key"
api_url = "http://your-pterodactyl-ip/api/application/servers"

existing_servers = []

while True:
    response = requests.get(
        api_url, headers={"Authorization": f"Bearer {api_key}"})
    server_data = json.loads(response.text)["data"]

    for server in server_data:
        if server["attributes"]["name"] not in existing_servers:
            existing_servers.append(server["attributes"]["name"])
            print(f"New server created: {server['attributes']['name']}")

    time.sleep(1)
