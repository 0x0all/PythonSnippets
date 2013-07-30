import urllib
import json

# Extract a page worth of twitter data
data = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
data = json.load(data)

n_data = len(data['results'])
geo = [data['results'][i]['geo'] for i in range(n_data)]
tweets = [data['results'][i]['text'] for i in range(n_data)]
people = [data['results'][i]['from_user_name'] for i in range(n_data)]

# Use OAuth for a lot more data
