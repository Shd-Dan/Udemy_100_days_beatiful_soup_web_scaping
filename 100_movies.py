import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Write your code below this line 👇
""" Steps:
1) Read the website
2) Create soup object
"""
response = requests.get(URL)
movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")
movies = soup.find_all(name="h3", class_="title")

text_movies = [movie.getText() for movie in movies][::-1]
# encoding error raised not mentioned in lesson
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for item in text_movies:
        file.write(f"{item}\n")
