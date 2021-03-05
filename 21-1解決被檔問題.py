import pprint
import cloudscraper  #https://github.com/VeNoMouS/cloudscraper

url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=235214594'

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
jsonData = scraper.get(url).json()

pprint.pprint(jsonData[0])