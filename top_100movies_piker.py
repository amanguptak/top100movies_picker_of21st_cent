from bs4 import BeautifulSoup
import requests
import json
response=requests.get("https://www.digitalspy.com/movies/a34901966/the-100-greatest-blockbusters-of-the-21st-century/")
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")
print(soup.title)
movie = soup.find_all(name="h2",class_= "body-h2" )


moviesname=[i.get_text() for i in movie]
top_movies_list=moviesname[::-1]
print(top_movies_list)
with open("movies.json","w") as movies:
    json.dump(top_movies_list,movies,indent=4)

with open("movies.txt","w") as movies:
    for mov in top_movies_list:
        movies.write(f"{mov}\n")
