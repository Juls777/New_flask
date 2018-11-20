# Making a query is a simple matter. First, tell Python you will need to make HTTP connections.
from urllib.request import *

# Now open a connection to the server and get a response. The wt query parameter tells Solr to return 
# results in a format that Python can understand.
connection = urlopen('http://localhost:8983/solr/wiki/select?q=text:cheese&wt=python&start=0&rows=100')
response = eval(connection.read())

# Now interpreting the response is just a matter of pulling out the information that you need.
print(response['response']['numFound'], "documents found.")

# Print the name of each document.

print("Printing 100 top documents:")

for i, document in enumerate(response['response']['docs']):
      print("  Document title ", i, "=", document['title'])
