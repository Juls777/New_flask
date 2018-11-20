# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:17:31 2018

@author: Tom
"""

from urllib.request import *
from flask import Flask, render_template, request, redirect, url_for

#Initialize Flask instance
app = Flask(__name__)

example_data = urlopen('http://localhost:8983/solr/wiki/select?q=&wt=python&start=0&rows=10')
response = eval(example_data.read())

print(response['response']['numFound'], "documents found.")

# Print the name of each document.

print("Printing 100 top documents:")

for i, document in enumerate(response['response']['docs']):
      print("  Document title ", i, "=", document['title'])


#Use "query" variable from the URL. If no variable is given,
#use empty string instead. GET and POST methods are allowed.
@app.route("/search", defaults={"query": ""}, methods=["GET", "POST"])
@app.route("/search/<query>", methods=["GET", "POST"])
def search(query):

    if request.method == "POST":
        #Get query from the POST form.
        query = request.form["query"]
        
        #Redirect to the same page with the query in the url.
        #ALWAYS REDIRECT AFTER POSTING!
        return redirect(url_for("search", query=query))

    matches = []

    #If an entry name contains the query, add the entry to matches.
    if query != "":
        for entry in example_data:
            if query.lower() in entry["name"].lower():
                matches.append(entry)
 
    #Render index.html with matches variable. 
    return render_template("index.html", matches=matches)
