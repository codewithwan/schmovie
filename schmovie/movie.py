import requests
from googletrans import Translator

class Omdb:
    def __init__(self, api_key):
        self.base_url = "http://www.omdbapi.com/"
        self.api_key = api_key
        self.translator = Translator()

    def search_movie(self, title):
        params = {'apikey': self.api_key, 't': title}
        response = requests.get(self.base_url, params=params)
        
        if response.status_code == 200:
            result = response.json()
            if 'Plot' in result:
                result['Plot'] = self.translate_plot(result['Plot'])
            return result
        else:
            return None

    def translate_plot(self, plot):
        translated = self.translator.translate(plot, src='en', dest='id')
        return translated.text
