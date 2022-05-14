import requests

class chuck_joke:

    url = 'https://api.chucknorris.io/jokes/random'

    def api():
        try:
            response = requests.request('get', chuck_joke.url)
            response_json = response.json()
            if response.status_code != 200:
                return 'An error has occurred, not 200'
            else:
                return response_json
        except:
            return 'An error has occurred, exeption'