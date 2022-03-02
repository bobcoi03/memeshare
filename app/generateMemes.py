import requests

class GenerateMemes:
	def __init__(self):
		self.subreddits = ["memes","dankmemes","me_irl","wholesomememes"]
		
	def generate_memes(self, amount=1):

		lists_of_url_imgs = []

		for subreddit in range(len(self.subreddits)):

			url = f"https://meme-api.herokuapp.com/gimme/{self.subreddits[subreddit]}/{amount}"

			data = requests.get(url)

			data_dict = data.json()

			for memes in range(len(data_dict["memes"])):
				lists_of_url_imgs.append(data_dict["memes"][memes]["url"])
				
		return lists_of_url_imgs

	'''RETURN LIST OF IMAGE URLS OF RANDOM MEMES FROM SUBREDDITS'''