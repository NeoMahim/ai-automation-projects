import datetime
import json
import urllib.request
today = datetime.date.today()
print("Today is:",today)

url = "https://zenquotes.io/api/random"
response = urllib.request.urlopen(url)
data =json.loads(response.read())
quote = data[0]['q']
author = data[0]['a']
print("Quote:",quote)
print("- "+ author)