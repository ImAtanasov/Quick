import requests
import json

username = 'XXX'
token = '6c7ce159ecc01af342628dd0e76d2a5c19a5a78e'

login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(username,token))
login = requests.get('https://api.github.com/user', auth=(username,token))


cont = login.content
json_text = cont.decode('utf8').replace("'", '"')
data = json.loads(json_text)


name = data['login']
company = data['company']
location = data['location']
email = data['email']
id = data['id']


username = 'XXX'
token = 'XXX'
params={"name":name, "email" : email, "address" :location }
headers = { "Content-Type" : "application/json" }
domain = "abv-relations521"


login = requests.post("https://"+ domain +".freshdesk.com/api/v2/contacts", auth=(username,token),data = json.dumps(params), headers = headers)

print(login.headers)

