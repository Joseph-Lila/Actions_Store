from kivymd.uix.list import OneLineAvatarIconListItem


class Day(OneLineAvatarIconListItem):
    def __init__(self, title, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.text = title
        self.week_number = self.title.split(' ')[-1]
