import requests

class GenerateMemes:
	def __init__(self):
		self.subreddits = ["memes","dankmemes","me_irl","wholesomememes"]
		
	def generate_memes(self):

		lists_of_url_imgs = []

		for subreddit in range(len(self.subreddits)):

			url = f"https://meme-api.herokuapp.com/gimme/{self.subreddits[subreddit]}/50"

			data = requests.get(url)

			data_dict = data.json()

			for memes in range(len(data_dict["memes"])):
				lists_of_url_imgs.append(data_dict["memes"][memes]["url"])
				
		return lists_of_url_imgs

data = GenerateMemes()

print(data.generate_memes())

