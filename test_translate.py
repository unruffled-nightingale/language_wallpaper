import unittest

from translate import English, French, Spanish, Italian, German, Portuguese


class TestEnglish(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lang = English()

    def test_iso6391(self):
        self.assertEqual(self.lang.iso6391(), 'en')

    def test_iso6392(self):
        self.assertEqual(self.lang.iso6392(), 'eng')

    def test_tenses(self):
        pass

    def test_translate(self):
        result = self.lang.translate('parler')
        expected = 'speak'
        self.assertEqual(result, expected)

    def test_request_conjugations(self):
        self.lang.request_conjugations('speak', 'present')

    def test_request_persons(self):
        result = self.lang.request_persons('speak', 'present')
        expected = ['firstsingular', 'secondsingular', 'thirdsingular', 'firstplural', 'secondplural', 'thirdplural']
        self.assertEqual(result, expected)

    def test_request_pronoun(self):
        result = self.lang.request_pronouns('firstsingular')
        expected = ['I']
        self.assertEqual(result, expected)

    def test_get_conjugations(self):
        result = self.lang.get_conjugations('speak', 'present')
        expected = [{'person': 'firstsingular', 'conjugation': 'I speak'},
                    {'person': 'secondsingular', 'conjugation': 'you speak'},
                    {'person': 'thirdsingular', 'conjugation': 'he/she/it speaks'},
                    {'person': 'firstplural', 'conjugation': 'we speak'},
                    {'person': 'secondplural', 'conjugation': 'you speak'},
                    {'person': 'thirdplural', 'conjugation': 'they speak'}]
        self.assertEqual(result, expected)

    def test_conjugate(self):
        result = self.lang.conjugate('speak')
        expected = [{
            'present': [{
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
        }, {
            'future': [{
                'conjugation': 'I will speak',
                'person': 'firstsingular'
            }, {
                'conjugation': 'you will speak',
                'person': 'secondsingular'
            }, {
                'conjugation': 'he/she/it will speaks',
                'person': 'thirdsingular'
            }, {
                'conjugation': 'we will speak',
                'person': 'firstplural'
            }, {
                'conjugation': 'you will speak',
                'person': 'secondplural'
            }, {
                'conjugation': 'they will speak',
                'person': 'thirdplural'
            }]
        }, {
            'imperfect': [{
                'conjugation': 'I was speaking',
                'person': 'firstsingular'
            }, {
                'conjugation': 'you were speaking',
                'person': 'secondsingular'
            }, {
                'conjugation': 'he/she/it was speaking',
                'person': 'thirdsingular'
            }, {
                'conjugation': 'subcode/message were speaking',
                'person': 'anypersonplural'
            }]
        }]
        self.assertEqual(result, expected)

    def test_get_verbs(self):
        result = self.lang.get_verbs(' I like speaking')
        expected = ['like', 'speak']
        self.assertEqual(result, expected)

    def test_proverb(self):
        result = self.lang.proverb()
        self.assertTrue(len(result) < 101)
        self.assertTrue(type(result) == str)




if __name__ == '__main__':
    unittest.main()
