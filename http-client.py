import requests
import json

def http_get_request(url):
    try:
        # Send a GET request to the provided URL
        response = requests.get(url)
        print(requests.session)
        
        # Print the status code of the response
        print(f"Status Code: {response.status_code}")
        
        # If the request was successful, print the content of the response
        if response.status_code == 200:
            print("Response Content:")
            print(response.text)
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

def http_post_request(url):
    body = json.dumps({"test":"Test", "otherTest":"second entry"})
    print(body.keys());

if __name__ == "__main__":
    # Example URL (replace with your desired endpoint)
    # url = "https://dashboard.blaulichtsms.net/#/login?token=f587305d-cdfb-4a29-b70a-8b24ff48fee9NwtpaiySqd"
    url = "https://api-staging.blaulichtsms.net/blaulicht/api/alarm/v1/list"

    # Make an HTTP GET request to the specified URL
    # http_get_request(url)
    http_post_request(url)


#https://requests.readthedocs.io/en/latest/user/advanced/#http-verbs
#https://github.com/blaulichtSMS/docs/blob/master/alarm_api_v1.md