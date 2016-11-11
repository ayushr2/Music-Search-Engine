from flask import Flask, request
from app import app
import twitter
import spotify
import wiki_search
# static url
@app.route('/')
def index():
    return "<h1/>Welcome to music search engine"



@app.route('/search',methods=['GET'])
def search():
    tweets=""
    wiki=""
    playlist=""
    recs=""
    result=""
    if 'q' in request.args:
        wiki=wiki_search.search(request.args['q'])
        playlist="<a href="+spotify.get_playlist(request.args['q'])+">here</a>"
        tweets=twitter.search(request.args['q'])
        recs=spotify.get_recommendations(request.args['q'])
        result= "<h2/>Summary:<br/></h2/>"+wiki+ "<br/><h2/>For Playlist Click "+playlist+ "</h2/><h2/>TWEETS:<br/></h2/>"+ tweets+"<br/><h2/>RECOMENDED FOR YOU</h2/>"+"<h2/>"+recs+"</h2/>" 
        return result
    return "WRONG"

