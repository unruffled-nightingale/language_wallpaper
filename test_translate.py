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
        self.assertEqual(self.lang.tenses(), ['present', 'future', 'imperfect'])

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

    def test_clean_proverb(self):
        proverb = 'A simple proverb (with some brackets).\n\n'
        result = self.lang.clean_proverb(proverb)
        expected = 'A simple proverb.'
        self.assertEqual(result, expected)


class TestFrench(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lang = French()

    def test_iso6391(self):
        self.assertEqual(self.lang.iso6391(), 'fr')

    def test_iso6392(self):
        self.assertEqual(self.lang.iso6392(), 'fra')

    def test_tenses(self):
        self.assertEqual(self.lang.tenses(), ['present', 'future', 'imperfect'])

    def test_translate(self):
        result = self.lang.translate('speak')
        expected = 'parler'
        self.assertEqual(result, expected)

    def test_request_conjugations(self):
        self.lang.request_conjugations('parler', 'present')

    def test_request_persons(self):
        result = self.lang.request_persons('parler', 'present')
        expected = ['firstsingular', 'secondsingular', 'thirdsingular', 'firstplural', 'secondplural', 'thirdplural']
        self.assertEqual(result, expected)

    def test_request_pronoun(self):
        result = self.lang.request_pronouns('firstsingular')
        expected = ['je']
        self.assertEqual(result, expected)

    def test_get_conjugations(self):
        result = self.lang.get_conjugations('parler', 'present')
        expected = [{
            'conjugation': 'je parle',
            'person': 'firstsingular'
        }, {
            'conjugation': 'tu parles',
            'person': 'secondsingular'
        }, {
            'conjugation': 'il/elle/on parle',
            'person': 'thirdsingular'
        }, {
            'conjugation': 'nous parlons',
            'person': 'firstplural'
        }, {
            'conjugation': 'vous parlez',
            'person': 'secondplural'
        }, {
            'conjugation': 'ils/elles parlent',
            'person': 'thirdplural'
        }]
        self.assertEqual(result, expected)

    def test_conjugate(self):
        result = self.lang.conjugate('parler')
        expected = [{
            'tense': 'present',
            'conjugations': [{
                'person': 'firstsingular',
                'conjugation': 'je parle'
            }, {
                'person': 'secondsingular',
                'conjugation': 'tu parles'
            }, {
                'person': 'thirdsingular',
                'conjugation': 'il/elle/on parle'
            }, {
                'person': 'firstplural',
                'conjugation': 'nous parlons'
            }, {
                'person': 'secondplural',
                'conjugation': 'vous parlez'
            }, {
                'person': 'thirdplural',
                'conjugation': 'ils/elles parlent'
            }]
        }, {
            'tense': 'future',
            'conjugations': [{
                'person': 'firstsingular',
                'conjugation': 'je parlerai'
            }, {
                'person': 'secondsingular',
                'conjugation': 'tu parleras'
            }, {
                'person': 'thirdsingular',
                'conjugation': 'il/elle/on parlera'
            }, {
                'person': 'firstplural',
                'conjugation': 'nous parlerons'
            }, {
                'person': 'secondplural',
                'conjugation': 'vous parlerez'
            }, {
                'person': 'thirdplural',
                'conjugation': 'ils/elles parleront'
            }]
        }, {
            'tense': 'imperfect',
            'conjugations': [{
                'person': 'firstsingular',
                'conjugation': 'je parlais'
            }, {
                'person': 'secondsingular',
                'conjugation': 'tu parlais'
            }, {
                'person': 'thirdsingular',
                'conjugation': 'il/elle/on parlait'
            }, {
                'person': 'firstplural',
                'conjugation': 'nous parlions'
            }, {
                'person': 'secondplural',
                'conjugation': 'vous parliez'
            }, {
                'person': 'thirdplural',
                'conjugation': 'ils/elles parlaient'
            }]
        }]
        self.assertEqual(result, expected)

    def test_get_verbs(self):
        result = self.lang.get_verbs("Je parle")
        expected = ['parler']
        self.assertEqual(result, expected)

    def test_proverb(self):
        result = self.lang.proverb()
        self.assertTrue(len(result) < 101)
        self.assertTrue(type(result) == str)


class TestSpanish(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lang = Spanish()

    def test_iso6391(self):
        self.assertEqual(self.lang.iso6391(), 'es')

    def test_iso6392(self):
        self.assertEqual(self.lang.iso6392(), 'spa')

    def test_tenses(self):
        self.assertEqual(self.lang.tenses(), ['present', 'future', 'imperfect'])

    def test_translate(self):
        result = self.lang.translate('speak')
        expected = 'hablar'
        self.assertEqual(result, expected)

    def test_request_conjugations(self):
        self.lang.request_conjugations('hablar', 'present')

    def test_request_persons(self):
        result = self.lang.request_persons('hablar', 'present')
        expected = ['firstsingular', 'secondsingular', 'thirdsingular', 'firstplural', 'secondplural', 'thirdplural']
        self.assertEqual(result, expected)

    def test_request_pronoun(self):
        result = self.lang.request_pronouns('firstsingular')
        expected = ['yo']
        self.assertEqual(result, expected)

    def test_get_conjugations(self):
        result = self.lang.get_conjugations('hablar', 'present')
        expected = [{
            'person': 'firstsingular',
            'conjugation': 'yo hablo'
        }, {
            'person': 'secondsingular',
            'conjugation': 'tú hablas'
        }, {
            'person': 'thirdsingular',
            'conjugation': 'él/ella/Vd habla'
        }, {
            'person': 'firstplural',
            'conjugation': 'nosotros hablamos'
        }, {
            'person': 'secondplural',
            'conjugation': 'vosotros habláis'
        }, {
            'person': 'thirdplural',
            'conjugation': 'ellos/ellas/Vds hablan'
        }]
        self.assertEqual(result, expected)

    def test_conjugate(self):
        result = self.lang.conjugate('hablar')
        expected = [{
            'tense': 'present',
            'conjugations': [{
                'conjugation': 'yo hablo',
                'person': 'firstsingular'
            }, {
                'conjugation': 'tú hablas',
                'person': 'secondsingular'
            }, {
                'conjugation': 'él/ella/Vd habla',
                'person': 'thirdsingular'
            }, {
                'conjugation': 'nosotros hablamos',
                'person': 'firstplural'
            }, {
                'conjugation': 'vosotros habláis',
                'person': 'secondplural'
            }, {
                'conjugation': 'ellos/ellas/Vds hablan',
                'person': 'thirdplural'
            }]
        }, {
            'tense': 'future',
            'conjugations': [{
                'conjugation': 'yo hablaré',
                'person': 'firstsingular'
            }, {
                'conjugation': 'tú hablarás',
                'person': 'secondsingular'
            }, {
                'conjugation': 'él/ella/Vd hablará',
                'person': 'thirdsingular'
            }, {
                'conjugation': 'nosotros hablaremos',
                'person': 'firstplural'
            }, {
                'conjugation': 'vosotros hablaréis',
                'person': 'secondplural'
            }, {
                'conjugation': 'ellos/ellas/Vds hablarán',
                'person': 'thirdplural'
            }]
        }, {
            'tense': 'imperfect',
            'conjugations': [{
                'conjugation': 'yo hablaba',
                'person': 'firstsingular'
            }, {
                'conjugation': 'tú hablabas',
                'person': 'secondsingular'
            }, {
                'conjugation': 'él/ella/Vd hablaba',
                'person': 'thirdsingular'
            }, {
                'conjugation': 'nosotros hablábamos',
                'person': 'firstplural'
            }, {
                'conjugation': 'vosotros hablabais',
                'person': 'secondplural'
            }, {
                'conjugation': 'ellos/ellas/Vds hablaban',
                'person': 'thirdplural'
            }]
        }]
        self.assertEqual(result, expected)

    def test_get_verbs(self):
        result = self.lang.get_verbs("Yo hablo")
        expected = ['hablar']
        self.assertEqual(result, expected)

    def test_proverb(self):
        result = self.lang.proverb()
        self.assertTrue(len(result) < 101)
        self.assertTrue(type(result) == str)


if __name__ == '__main__':
    unittest.main()
