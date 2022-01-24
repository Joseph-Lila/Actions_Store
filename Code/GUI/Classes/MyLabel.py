from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle


"""
This class is a children of Label.
It allows adding the background-color to such element as a Label...
"""


class MyLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(100/255, 35/255, 200/255, 255/255)
            Rectangle(pos=self.pos, size=self.size)
