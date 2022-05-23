import requests
responses = requests.get("http://www.autonewschina.com/en/more.asp?c=68")

for response in responses.history:
    print(response.url)