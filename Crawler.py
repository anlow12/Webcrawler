import requests
from bs4 import	BeautifulSoup

class CrawlerCore():

	def __init__(self, website):
		self.website = website


class CrawlerLeg(CrawlerCore):

	def __init__(self, website):
		super().__init__(website)

	def getURL(self):
		f = open('input.txt')
		print(f.readline())
		f.close()

def Main():

	crawlerleg1 = CrawlerLeg("reddit")

	sourceCode = requests.get('https://www.reddit.com/r/gaming/')

	plainText = sourceCode.text
	soup = BeautifulSoup(plainText, "html.parser" )

	g = open('output.txt', 'w')
	g.write(str(soup))
	g.close() 

	for link in soup.findAll('div', {'class': "entry unvoted"}): #makes sure testing is replaced with something else
		print(link.p.a.get_text())




if __name__ == '__main__':
	Main()



