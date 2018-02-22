import requests
import json
from random import randint, choice
from bs4 import BeautifulSoup
import re


class AnalyseText(object):

    def __init__(self, text, iso6391):
        self.text = text
        self.iso6391 = iso6391
        self.part_of_speech = self.get_part_of_speech()
        self.verbs = self.get_verbs()

    def get_part_of_speech(self):
        url = 'https://api.textgain.com/1/tag?q={0}&lang={1}&key=***'.format(self.text, self.iso6391)
        response = requests.get(url)
        return json.loads(response.text)['text'][0][0]

    def get_verbs(self):
        return [e['word'] for e in self.part_of_speech if e['tag'] == 'VERB']

    def lemmatize_word(self, word):
        """
        Requests phrase structure from meaningcloud API.
        Returns lingustic breakdown of sentence
        """
        url = "http://api.meaningcloud.com/parser-2.0"
        payload = "key=3ded5f1530cd52563ff2969719f72896&of=json&lang={0}&txt={1}".format(self.iso6391, word)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, data=payload, headers=headers)
        response = json.loads(response.text)
        return response['token_list'][0]['token_list'][0]['token_list'][0]['analysis_list'][0]['lemma']


class Language(object):
    """Translations and conjugations for a specified language"""

    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        return None

    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        return None

    def tenses(self):
        """Returns the tenses for conjugation"""
        return ['present', 'future', 'imperfect']

    def translate(self, text):
        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={0}&tl={1}&dt=t&q={2}"
        url = url.format('auto', self.iso6391(), text)
        response = requests.get(url)
        return json.loads(response.text)[0][0][0]

    def request_conjugations(self, verb, tense):
        url = 'http://api.ultralingua.com/api/conjugations/{0}/{1}?tense={2}'.format(self.iso6392(), verb, tense)
        response = requests.get(url)
        response = json.loads(response.text)
        return response

    def request_pronouns(self, person):
        url = 'http://api.ultralingua.com/api/pronouns/{0}/{1}'.format(self.iso6392(), person)
        response = requests.get(url)
        response = json.loads(response.text)
        return response

    def request_persons(self, verb, tense):
        url = 'http://api.ultralingua.com/api/persons/{0}/{1}/{2}'.format(self.iso6392(), verb, tense)
        response = requests.get(url)
        response = json.loads(response.text)
        return response

    def get_conjugations(self, verb, tense):
        conjugations = []
        for e in self.request_conjugations(verb, tense):
            person = e['partofspeech']['person']+e['partofspeech']['number']
            pronoun = '/'.join(self.request_pronouns(person))
            conjugation = pronoun + ' ' + e['surfaceform']
            conjugations.append({'person': person, 'conjugation': conjugation})
        return conjugations

    def conjugate(self, verb):
        conjugations = []
        for tense in self.tenses():
            conjugations.append({'tense': tense, 'conjugations': self.get_conjugations(verb, tense)})
        return conjugations

    def get_verbs(self, text):
        at = AnalyseText(text, self.iso6391())
        return [at.lemmatize_word(e) for e in at.verbs]

    def proverb(self):
        url = "https://en.wikiquote.org/wiki/{0}_proverbs".format(self.__class__.__name__)
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        soup = soup.find_all('div', {'class': 'mw-parser-output'})[0]
        proverbs = []
        for soup in soup.find_all('ul', recursive=False):
            try:
                proverbs.append(soup.find('li', recursive=False).find('i', recursive=False).text)
            except AttributeError:
                # Occasionally we cannot find a <i> tag which throws an attribute error when calling .text
                # In this instance, we just skip the proverb.
                pass
        proverbs = [e for e in proverbs if len(e) < 100]
        return choice(proverbs)

    def quote(self):
        return None


class English(Language):
    """Subclass of translate, translating for French"""

    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        return 'eng'

    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        return 'en'

    def quote(self):
        page = randint(1, 100)
        url = 'https://www.goodreads.com/quotes?page={0}'.format(page)
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        # Scrape quotes from the website
        quotes = [re.findall('(?<=“).*(?=”)', e.text)[0] for e in soup.find_all('div', {'class': 'quoteText'})]
        # Remove any quotes that are None, or are longer than 100 characters
        quotes = [quote for quote in quotes if quote is not None and len(quote) < 100]
        return choice(quotes)


class French(Language):
    """Subclass of translate, translating for French"""

    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        return 'fra'

    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        return 'fr'


class Spanish(Language):
    """Subclass of translate, translating for Spanish"""

    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        return 'spa'

    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        return 'es'


class German(Language):
    """Subclass of translate, translating for German"""

    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        return 'deu'

    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        return 'de'


class Italian(Language):
    """Subclass of translate, translating for Italian"""

    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        return 'ita'

    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        return 'it'


class Portuguese(Language):
    """Subclass of translate, translating for Portuguese"""

    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        return 'por'

    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        return 'pt'
