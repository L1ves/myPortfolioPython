import urllib2
import json

GOOGLE_API_KEY = "{***}"
target = "***"
api_response =
urllib2.urlopen(
"https://www.googleapis.com/plus/v1/people?query="+target+"&key="+GOOGLE_API_KEY
).read()
api_response = api_response.split("\n")
for line in api_response:
    if "displayName" in line:
        print line
