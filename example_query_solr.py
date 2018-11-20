from urllib.request import *

connection = urlopen('http://localhost:8983/solr/wiki/select?q=text:cheese&wt=python&start=0&rows=100')
response = eval(connection.read())

print(response['response']['numFound'], "documents found.")

# Print the name of each document.

print("Printing 100 top documents:")

for i, document in enumerate(response['response']['docs']):
      print("  Document title ", i, "=", document['title'])
