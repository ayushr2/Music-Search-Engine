import spotipy
import spotipy.util as util

spotify=spotipy.Spotify()

def get_playlist(query):
	str1=""
	results=spotify.search(q=query,type='playlist')
	str1=results[u'playlists'][u'items'][2][u'external_urls'][u'spotify']
	return str1
	
def get_recommendations(query):
	genres_list=[]
	song_artist=[]
	recs=[]
	str1=""
	artist=spotify.search(q=query,type='artist')
	song=spotify.search(q=query,type='track')
	genres_list=artist[u'artists'][u'items'][0][u'genres']
	song_artist=song[u'tracks'][u'items'][5][u'artists'][0][u'name']
	song_genres= spotify.search(q=song_artist,type='artist') [u'artists'][u'items'][0][u'genres']
	for genre in song_genres:
		if genre in genres_list:
			pass
		else:
			genres_list.append(genre)
	count =1
	for genre in genres_list:
		results=spotify.search(q=genre,type='playlist') [u'playlists'][u'items'][2][u'external_urls'][u'spotify']
		if results not in recs:
			recs.append(results)
			str1+="<a href="+results+">"+str(count)+"</a>"+"\t"
			count+=1

	return str1
