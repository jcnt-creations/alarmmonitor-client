import requests

def http_get_request(url):
    try:
        # Send a GET request to the provided URL
        response = requests.get(url)
        
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

if __name__ == "__main__":
    # Example URL (replace with your desired endpoint)
    url = "http://www.whitedisplay.com/"
    
    # Make an HTTP GET request to the specified URL
    http_get_request(url)
