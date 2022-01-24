from Code.GUI.Classes.ListItemWithCheckbox import ListItemWithCheckbox
from kivymd.uix.list import IconLeftWidget
from Code.GUI.Classes.RightCheckbox import RightCheckbox


class Action(ListItemWithCheckbox):
    def __init__(self, title_, description_, **kwargs):
        super().__init__(**kwargs)
        self.text = title_
        self.title = title_
        self.description = description_
        self.add_widget(IconLeftWidget(icon=self.my_icon))
        self.add_widget(RightCheckbox())
