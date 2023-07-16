def create_youtube_video(title,description):
	youtubevideo= {"title":title,"description":description,"likes":0,"dislikes":0, "comments":{}}
	return youtubevideo

def like(youtubevideo):
	youtubevideo["likes"] += 1
	return youtubevideo

def dislike(youtubevideo):
	youtubevideo["dislikes"] += 1
	return youtubevideo
	

def add_comments():
	



	