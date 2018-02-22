import unittest
import os

from wallpaper import Edit, Wallpaper


class TestEdit(unittest.TestCase):

    def test_resize(self):
        self.edit = Edit('images\\1200x800.jpg')
        self.edit.resize()
        self.assertEqual(self.edit.image.size, (1366, 768))

    def test_save(self):
        self.edit = Edit('images\\1200x800.jpg')
        self.edit.save()
        # check last time file was touched.


class TestWallpaper(unittest.TestCase):

    def test_get_wallpaper_path(self):
        path = Wallpaper().get_wallpaper_path()
        self.assertTrue(os.path.isfile(path))

    def test_make_wallpaper(self):
        image_path = 'images\\default.jpg'
        text = {'phrase': 'Hello World',
                'translation': 'Bonjour le monde',
                'verb': 'Hello   Bonjour',
                'conjugations': [{
                                  'tense': 'PRESENT',
                                  'conjugations': 'I speak\n'
                                                  'you speak\n'
                                                  'he/she/it speaks\n'
                                                  'we speak\n'
                                                  'you speak\n'
                                                  'they speak\n'
                                }, {
                                  'tense': 'PAST',
                                  'conjugations': 'I speak\n'
                                                  'you speak\n'
                                                  'he/she/it speaks\n'
                                                  'we speak\n'
                                                  'you speak\n'
                                                  'they speak\n'
                                }, {
                                  'tense': 'FUTURE',
                                  'conjugations': 'I speak\n'
                                                  'you speak\n'
                                                  'he/she/it speaks\n'
                                                  'we speak\n'
                                                  'you speak\n'
                                                  'they speak\n'
                                }]
                }

        Wallpaper().make_wallpaper(image_path, text)

        # Now go check that it looks right


if __name__ == '__main__':
    unittest.main()
