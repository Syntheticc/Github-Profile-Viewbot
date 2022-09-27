import random
import requests

sendurl = "profileviewcounterlinkhere"

URL = "https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt"
response = requests.get(URL)
open("user_agents.txt", "wb").write(response.content)
lines = open('user_agents.txt').read().splitlines()
myline = random.choice(lines)

user_agent = {'User-agent': myline}

print(myline)
i = 0

while i < 10000000:
  i = i + 1
  response = requests.get(sendurl, headers = user_agent)
  print("sent")