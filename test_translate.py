import unittest

from translate import French, Spanish, Italian, German, Portuguese


class TestFrench(unittest.TestCase):

    def test_translate_simple(self):
        french = French()
        result = french.translate('speak')
        self.assertEqual(result, 'parler')

    def test_translate_hard(self):
        french = French()
        result = french.translate('He was scared that he had left early')
        self.assertEqual(result, "Il avait peur qu'il soit parti tôt")

    def test_conjugate(self):
        french = French()
        result = french.conjugate('parler')
        print(result)


class TestSpanish(unittest.TestCase):

    def test_translate_simple(self):
        spanish = Spanish()
        result = spanish.translate('speak')
        self.assertEqual(result, 'hablar')

    def test_translate_hard(self):
        spanish = Spanish()
        result = spanish.translate('He was scared that he had left early')
        self.assertEqual(result, "Tenía miedo de haberse ido temprano")

    def test_conjugate(self):
        spanish = Spanish()
        result = spanish.conjugate('hablar')
        print(result)


class TestItalian(unittest.TestCase):

    def test_translate_simple(self):
        italian = Italian()
        result = italian.translate('speak')
        self.assertEqual(result, 'parlare')

    def test_translate_hard(self):
        italian = Italian()
        result = italian.translate('He was scared that he had left early')
        self.assertEqual(result, "Tenía miedo de haberse ido temprano")

    def test_conjugate(self):
        italian = Italian()
        result = italian.conjugate('parlare')
        print(result)


class TestGerman(unittest.TestCase):

    def test_translate_simple(self):
        german = German()
        result = german.translate('speak')
        self.assertEqual(result, 'sprechen')

    def test_translate_hard(self):
        german = German()
        result = german.translate('He was scared that he had left early')
        self.assertEqual(result, "Tenía miedo de haberse ido temprano")

    def test_conjugate(self):
        german = German()
        result = german.conjugate('sprechen')
        print(result)


class TestPortuguese(unittest.TestCase):

    def test_translate_simple(self):
        portuguese = Portuguese()
        result = portuguese.translate('speak')
        self.assertEqual(result, 'falar')

    def test_translate_hard(self):
        portuguese = Portuguese()
        result = portuguese.translate('He was scared that he had left early')
        self.assertEqual(result, "Tenía miedo de haberse ido temprano")

    def test_conjugate(self):
        portuguese = Portuguese()
        result = portuguese.conjugate('falar')
        print(result)



if __name__ == '__main__':
    unittest.main()
