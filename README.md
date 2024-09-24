# alarmmonitor-client
A python http client for a raspberry to connect to a specific Alarmmonitor.
This client repeatedly checks for an existing connection to the Webserver and listens to incomming emergencies.
If an emergency occours, it gives a signal to a power socket which is connected to the TV and powers it up.
An addition would be a sensor, to detect if someone is entering the garage, to show the news and traffic problems in the sleep mode of the alarmmonitor.


### starting the client
Bevor starting, the "request" library has to be installed.
If not by default, the command is the followng:
sudo apt-get install python3-requests

To execute the programm its:
python3 http_client.py

## Changing to a SSE Client
I will try to solve this by using a sse client. This should connect to the server and wait for events send by the server. I hope, like this I could identify and react to emergency calls.


## References
https://requests.readthedocs.io/en/latest/user/quickstart/
https://requests.readthedocs.io/en/latest/user/advanced/
https://github.com/blaulichtSMS/docs/blob/master/alarm_api_v1.md
https://de.wikipedia.org/wiki/HTTP-Statuscode