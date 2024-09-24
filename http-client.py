import json
import requests

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
    data = {
        "username":"Test-Joshua", 
        "password":"TestMonitor123!!", 
        "customerID": "100251", 
        "startDate": "2024-09-15T14:00:00.000Z", 
        "endDate":"2024-09-15T15:00:00.000Z"
        }
    #print(body.keys());
    print("post")
    print(data)
    print(data.keys())
    body = json.dumps(data)
    requests.head

def test_url():
    r = requests.get('https://api.github.com/repos/psf/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
    if r.status_code == requests.codes.ok:
        print(r.headers['content-type'])
    commit_data = r.json()
    print(commit_data.keys())

def getSession(url):
    #url='https://httpbin.org/cookies'
    s=requests.Session()
    r=s.get(url)
    print(r.text)

if __name__ == "__main__":
    # Example URL (replace with your desired endpoint)
    url = "https://dashboard.blaulichtsms.net/#/login?token=f587305d-cdfb-4a29-b70a-8b24ff48fee9NwtpaiySqd"
    #testBase = "https://api-staging.blaulichtsms.net/blaulicht"
    #listUrl = "/api/alarm/v1/list"
    #url = testBase + listUrl

    # Make an HTTP GET request to the specified URL
    # http_get_request(url)
    # http_post_request(url)

    #verbs= requests.options(url)
    #print(verbs.status_code)
    #print(verbs.headers["allow"])
    #test_url()
    #http_post_request(url)

    getSession(url)



#https://requests.readthedocs.io/en/latest/user/advanced/#http-verbs
#https://github.com/blaulichtSMS/docs/blob/master/alarm_api_v1.md