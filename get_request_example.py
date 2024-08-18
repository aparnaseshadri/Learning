import requests

# Replace with your API endpoint
url = "https://api.example.com/data"

try:
    # Send a GET request to the endpoint
    response = requests.get(url)
   
    # Raise an exception if the request was unsuccessful
    response.raise_for_status()
   
    # Convert the JSON response to a Python dictionary
    result = response.json()
   
    # Print the result (or process it as needed)
    print(result)

except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)
