import requests
import json


class Translate(object):
    """Translations and conjugations for a specified language"""

    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        return 'eng'

    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        return 'en'

    def translate(self, text):
        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={0}&tl={1}&dt=t&q={2}"
        url = url.format('en', self.iso6391(), text)
        response = requests.get(url)
        return json.loads(response.text)[0][0][0]

    def conjugate(self, verb):
        url = 'http://api.ultralingua.com/api/conjugations/{0}/{1}'
        url = url.format(self.iso6392(), verb)
        response = requests.get(url)
        response = json.loads(response.text)
        conjugations = self.reformat_conjugation_response(response)
        return conjugations

    def reformat_conjugation_response(self, response):
        """
        Reformats the response returned by the conjugation api
        :param response: The response returned by the conjugation api
        :return: Reformatted response
        """
        root = response[0]['root']
        conjugations = []
        for result in response:
            grammar = result['partofspeech']
            tense = grammar['tense']
            person = grammar.get('person') and '-'+grammar.get('person')
            number = grammar.get('number') and '-'+grammar.get('number')
            grammar = tense+(person or '')+(number or  '')
            conjugation = result['surfaceform']
            conjugations.append((conjugation, grammar))
        return {root: conjugations}


class French(Translate):
    """Subclass of translate, translating for French"""

    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        return 'fra'

    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        return 'fr'


class Spanish(Translate):
    """Subclass of translate, translating for Spanish"""

    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        return 'spa'

    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        return 'es'


class German(Translate):
    """Subclass of translate, translating for German"""

    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        return 'deu'

    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        return 'de'


class Italian(Translate):
    """Subclass of translate, translating for Italian"""

    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        return 'ita'

    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        return 'it'


class Portuguese(Translate):
    """Subclass of translate, translating for Portuguese"""

    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        return 'por'

    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        return 'pt'


if __name__ == '__main__':
    Translate = Translate()
    Translate.translate('hello')
