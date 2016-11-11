import wikipedia
import json
import urllib2

def search(query):
	stuff = ""
	wiki_search = wikipedia.summary(query)
	return wiki_search
