import translate
from wallpaper import Wallpaper
from random import choice

class Main(object):

    def __init__(self, known_language, translated_language, image_path=None):
        self.known_language = getattr(translate, known_language)()
        self.translated_language = getattr(translate, translated_language)()
        self.image_path = image_path

    def main(self):

        # Get text
        phrase = self.known_language.proverb()
        translation = self.translated_language.translate(phrase)
        verbs = self.translated_language.get_verbs(translation)
        verb = choice(verbs)
        translated_verb = self.translated_language(verb)
        conjugations = [self.stringify_conjugations(e) for e in self.translated_language.conjugate(verb)]

        text = {'phrase': phrase,
                'translation': translation,
                'verbs': verb+'  '+translated_verb,
                'conjugation': conjugations}

        # Make wallpaper
        Wallpaper().make_wallpaper(self.image_path, text)

    def stringify_conjugations(self, conjugations):
        conjugation = {
            'tense': 'present',
            'conjugations': [{
                'conjugation': 'I speak',
                'person': 'firstsingular'
            }, {
                'conjugation': 'you speak',
                'person': 'secondsingular'
            }, {
                'conjugation': 'he/she/it speaks',
                'person': 'thirdsingular'
            }, {
                'conjugation': 'we speak',
                'person': 'firstplural'
            }, {
                'conjugation': 'you speak',
                'person': 'secondplural'
            }, {
                'conjugation': 'they speak',
                'person': 'thirdplural'
            }]
        }
        tense = conjugation['tense'].upper()
        conjugations = '\n'.join([e['conjugation'] for e in conjugation['conjugations']])
        return tense + '\n' + conjugations

if __name__ == '__main__':
    main = Main('English', 'French')
    a = main.stringify_conjugations(1)
    print(a)






