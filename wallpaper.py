from PIL import Image, ImageDraw, ImageFont
import os
import ctypes


class Wallpaper(object):

    def make_wallpaper(self, image_path, text):
        """
        Creates our language learning wallpaper and sets it
        as the Desktop image.
        """

        if not image_path:
            image_path = self.get_wallpaper_path()

        # Load wallpaper
        wallpaper = Edit(image_path)
        wallpaper.resize()

        # Add phrase
        phrase = Text(wallpaper)
        phrase.set_text(text['phrase'])
        phrase.set_font('OpenSans-Light.ttf', 26)
        phrase.set_fill()
        phrase.set_position(100, 100)

        wallpaper.write_text(phrase.position, phrase.text, phrase.fill, phrase.font)

        # Add translation
        translation = Text(wallpaper)
        translation.set_text(text['translation'])
        translation.set_font('OpenSans-Light.ttf', 26)
        translation.set_fill()
        # Get translation position from phrase position
        translation_x = phrase.position[0] + 20
        translation_y = phrase.position[1] + phrase.font_size()[1] + 5
        translation.set_position(translation_x, translation_y)

        wallpaper.write_text(translation.position, translation.text, translation.fill, translation.font)

        # Add verb
        verb = Text(wallpaper)
        verb.set_text(text['verb'])
        verb.set_font('OpenSans-Regular.ttf', 19)
        verb.set_fill()
        # Get verb position from phrase position
        verb_x = phrase.position[0] + 8
        verb_y = translation.position[1] + translation.font_size()[1] + 20
        verb.set_position(verb_x, verb_y)

        wallpaper.write_text(verb.position, verb.text, verb.fill, verb.font)

        # Add conjugations
        next_conjugation_x = verb.position[0]
        for text in text['conjugations']:

            # Add tense
            tense = Text(wallpaper)
            tense.set_text(text['tense'])
            tense.set_font('OpenSans-Regular.ttf', 14)
            tense.set_fill()
            tense_x = next_conjugation_x
            tense_y = verb.position[1] + verb.font_size()[1] + 13
            tense.set_position(tense_x, tense_y)

            wallpaper.write_text(tense.position, tense.text, tense.fill, tense.font)

            conjugation = Text(wallpaper)
            conjugation.set_text(text['conjugations'])
            conjugation.set_font('OpenSans-Light.ttf', 12)
            conjugation.set_fill()
            # Get conjugation position from phrase position
            conjugation_x = next_conjugation_x
            conjugation_y = tense_y + 22
            conjugation.set_position(conjugation_x, conjugation_y)
            # Set the x co-ordinate for next conjugation based on the position and size of this co-ordinate
            next_conjugation_x = conjugation.position[0] + conjugation.font_size()[1] + 20

            wallpaper.write_text(conjugation.position, conjugation.text, conjugation.fill, conjugation.font)

        wallpaper.save()
        self.set_wallpaper()

    def get_wallpaper_path(self):
        """
        Gets the image path for the current desktop image.
        """
        # Haven't figured out how to get the current wallpaper,
        # so for the moment we default a stored image.
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images', 'default.jpg')

    def set_wallpaper(self):
        """
        Sets wallpaper.jpg as the Desktop background for a windows PC.
        """
        # Get the full path of wallpaper.jpg
        parent_dir = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(parent_dir, 'wallpaper.png')
        # Set wallpaper.jpg as the Desktop background
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)


class Edit(object):

    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.draw = ImageDraw.Draw(self.image)

    def save(self):
        """
        Saves the edited image.
        """
        parent_dir = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(parent_dir, 'wallpaper.png')
        self.image.save(image_path, quality=100)

    def write_text(self, position, text, fill, font):
        """
        Write text onto self.image.
        :param position: Tuple containing x and y co-ordinates for the text
        :param text: The text we are writing to self.image
        :param fill: Tuple containing rgb co-ordinates for color of the text
        :param font: The text font stored in /fonts
        """
        self.draw.text(position, text=text, fill=fill, font=font)

    def resize(self):
        """
        Resizes the image to fit the resolution of the screen.
        This must be done prior to adding text, to avoid skewing
        """
        image_width, image_height = self.image.size
        image_ratio = image_width/image_height
        screen_width, screen_height = (1366, 768)
        screen_ratio = screen_width/screen_height

        # If the image is too skinny...
        if image_ratio < screen_ratio:
            # ...we set the image width to be equal to the screen width...
            new_image_width = screen_width
            # ...and set the image height proportionally...
            new_image_height = int(image_height * (screen_width / image_width))
            # ... and resize the image.
            self.image = self.image.resize((new_image_width, new_image_height), Image.ANTIALIAS)

            # We must now crop the top and bottom of the picture to ensure that the
            # image ratio is equal to the screen ratio.
            pixels_to_cut = int((new_image_height - screen_height) / 2)
            left = 0
            top = pixels_to_cut
            right = new_image_width
            bottom = new_image_height - pixels_to_cut
            # Crop the image
            self.image = self.image.crop((left, top, right, bottom))

        # Else if the image is too fat ...
        elif image_ratio > screen_ratio:
            # ...we set the image width to be equal to the screen width...
            new_image_height = screen_height
            # ...and set the image height proportionally...
            new_image_width = image_width * (screen_height / screen_height)
            # ... and resize the image.
            self.image = self.image.resize((new_image_width, new_image_height), Image.ANTIALIAS)

            # We must now crop the left and right of the picture to ensure that the
            # image ratio is equal to the screen ratio.
            pixels_to_cut = int((new_image_width - screen_width) / 2)
            left = pixels_to_cut
            top = 0
            right = new_image_width - pixels_to_cut
            bottom = new_image_height
            # Crop the image
            self.image = self.image.crop((left, top, right, bottom))

        # Else the image ratios are the same size ...
        else:
            # ...but still transform the image to ensure it is the same size as our screen...
            self.image = self.image.resize((screen_width, screen_height), Image.ANTIALIAS)

        # Reset draw
        self.draw = ImageDraw.Draw(self.image)


class Text(object):
    """
    A slightly redundant class which creates a text object that
    contains all information necessary for writing text to a PIL Image
    """

    def __init__(self, image):
        self.draw = image.draw
        self.text = None
        self.fill = None
        self.font = None
        self.position = None

    def set_text(self, text):
        self.text = text

    def set_fill(self):
        self.fill = (255, 255, 255, 255)

    def set_font(self, font_name, font_size):
        font_path = os.path.dirname(os.path.realpath(__file__))+'\\fonts\\'
        self.font = ImageFont.truetype(font_path + font_name, font_size)

    def font_size(self):
        return self.draw.textsize(self.text, self.font)

    def set_position(self, x, y):
        self.position = (x, y)
