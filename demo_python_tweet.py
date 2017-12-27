# coding: utf-8

print "======================================================"
print "MySQL5.7.12 Basic CRUD Operations by Python"
print "MySQL Innovation Daysデモ"
print "======================================================"

from requests_oauthlib import OAuth1Session
import json
import mysqlx

api_key      = "A6cgtknTq4IqSB2RhmZ77jJ"
api_secret   = "A03jmfaNyPYbCl2oveRq9xc"
token        = "304982400-gt1awHIiH1oNA"
token_secret = "DDPxVFjcK6CqcITN7ACKBT9"

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
params = {'count':'3',}

auth = OAuth1Session(api_key, api_secret, token, token_secret)
res = auth.get(url, params = params)

mySession = mysqlx.getSession({
'host': 'localhost', 'port': 33060,
'dbUser': 'demo_user', 'dbPassword': 'password'} )
myDb = mySession.getSchema('NEW57')
# Create a new collection 'my_collection'
myColl = myDb.createCollection('X_PYTHON')
# Insert documents

timeline = json.loads(res.text)
for tweet in timeline:
  myColl.add(tweet).execute()
# print(tweet["text"])

# Drop the collection
# mySession.dropCollection('NEW57','X_PYTHON')

