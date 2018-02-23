import translate
from wallpaper import Wallpaper
from random import choice


class Main(object):

    def __init__(self, known_language, translated_language, image_path=None):
        self.known_language = getattr(translate, known_language)()
        self.translated_language = getattr(translate, translated_language)()
        self.image_path = image_path

    def main(self):
        """
        Top level function which constructs our wallpaper.
        We construct the text using the languages module,
        and update our image with the wallpaper module.
        """
        # Get text
        phrase = self.known_language.proverb()
        translation = self.translated_language.translate(phrase)
        verbs = self.translated_language.get_verbs(translation)
        translated_verb = choice(verbs).title()
        known_verb = self.known_language.translate(translated_verb).title()
        conjugations = [self.stringify_conjugations(e) for e in self.translated_language.conjugate(translated_verb)]

        text = {'phrase': phrase,
                'translation': translation,
                'verb': known_verb+'  '+translated_verb,
                'conjugations': conjugations}

        # Make wallpaper
        Wallpaper().make_wallpaper(self.image_path, text)

    def stringify_conjugations(self, conjugation):
        """
        Joins the list of conjugtaions together with a new line.
        :param conjugation: A list of conjugations
        :return: A string of conjugations separated by a newline
        """
        tense = conjugation['tense'].upper()
        conjugations = '\n'.join([e['conjugation'] for e in conjugation['conjugations']])
        return {'tense': tense, 'conjugations': conjugations}


if __name__ == '__main__':
    main = Main('English', 'French')
    main.main()






