from flask import Flask, render_template, request, redirect, url_for
from urllib.request import *

#Initialize Flask instance
app = Flask(__name__)

example_data = [
    {"name": "Cat sleeping on a bed", "source": "cat.jpg"},
    {"name": "Misty forest", "source": "forest.jpg"},
    {"name": "Bonfire burning", "source": "fire.jpg"},
    {"name": "Old library", "source": "library.jpg"},
    {"name": "Sliced orange", "source": "orange.jpg"}
]

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

@app.route("/solr", defaults={"query": ""}, methods=["GET", "POST"])
@app.route("/solr/<query>", methods=["GET", "POST"])
def solr(query):

    if request.method == "POST":
        #Get query from the POST form.
        query = request.form["query"]
        
        #Redirect to the same page with the query in the url.
        #ALWAYS REDIRECT AFTER POSTING!
        return redirect(url_for("solr", query=query))

    matches = []

# Now open a connection to the server and get a response. The wt query parameter tells Solr to return 
# results in a format that Python can understand.
connection = urlopen('http://localhost:8983/solr/wiki/select?q=text:' + query + '&wt=python&start=0&rows=100&fi=title,id')
response = eval(connection.read())

# Now interpreting the response is just a matter of pulling out the information that you need.
print(response['response']['numFound'], "documents found.")

# Print the name of each document.

print("Printing 100 top documents:")

for i, document in enumerate(response['response']['docs']):
      #print("  Document title ", i, "=", document['title'])
        match = {"title":document['title'], "text": document['id']}
        matches.append(match)
   
#Render index.html with matches variable.
return render_template("solr.html", matches=matches) #change solr.html!!!
    
