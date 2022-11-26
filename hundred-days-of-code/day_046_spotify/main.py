import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
div_list = soup.find(name="div", class_="o-chart-results-list-row-container")
print(div_list)
# song_tags = soup.find_all(name="h3", id="title-of-a-story")
# song_list = [song.getText() for song in song_tags]
# print(song_list)