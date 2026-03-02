# LinkedIn Learning Python course by Joe Marini
# Example file for retrieving data from the internet
#
import urllib.request

web_url = urllib.request.urlopen("http://www.example.com")
print("Result code:", web_url.getcode())
data = web_url.read()
print(data)