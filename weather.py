import requests
city = input("Enter city: ")
api =f"https://wttr.in/{city}?format=3"
res = requests.get(api)
print(res.text)