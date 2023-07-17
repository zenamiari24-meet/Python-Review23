def create_youtube_video(title,description):
	youtubevideo= {"title":title,"description":description,"likes":0,"dislikes":0, "comments":{}}
	return youtubevideo

def like(youtubevideo):
	youtubevideo["likes"] += 1
	return youtubevideo

def dislike(youtubevideo):
	youtubevideo["dislikes"] += 1
	return youtubevideo
	

def add_comments(youtubevideo, username, comment_text):
   if "comments"not in youtubevideo:
   	youtubevideo["comments"] = {}
   youtubevideo["comments"] [username] = comment_text
   return youtubevideo

youtubevideo = create_youtube_video("My Video", "Youtuber in the making :()")
print(youtubevideo)

youtubevideo = likr(youtubevideo)
print(youtubevideo)

youtubevideo = dislike(youtubevideo)
print(youtubevideo)

youtubevideo = add_comments(youtubevideo, "hello", "hi", "amayzing")
print(youtubevideo)

youtubevideo = int(youtubevideo["Likes"]) + 494
print(youtubevideo)
	



	
