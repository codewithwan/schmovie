
# SCH_Movie
This project is a Python library that accesses the OMDb API to retrieve information about movies based on user-input titles. Additionally, the library includes a feature to translate movie plots from English to Indonesian using googletrans.

By utilizing this project, users can easily search for information about their favorite movies and obtain a summary of the plot in the Indonesian language.




## API 
Python Basic API wrapper
```http
  http://www.omdbapi.com/
```

## Installation

Install my-project with npm

```bash
  pip install schmovie
```
    

## Usage

Basic Usage :

```python
from schmovie.movie import Omdb

omdb = Omdb("YOUR_API_KEY")
movie_title = input("Search Movie : ")
result = omdb.search_movie(movie_title)
    
print(f"Judul: {result['Title']}")
print(f"Tahun: {result['Year']}")
print(f"Rating: {result['imdbRating']}")
print(f"Plot: {result['Plot']}")
```


## Authors

- [@codewithwan](https://github.com/codewithwan)

