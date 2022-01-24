from Code.GUI.Classes.ListItemWithCheckbox import ListItemWithCheckbox
from kivymd.uix.list import IconLeftWidget
from Code.GUI.Classes.RightCheckbox import RightCheckbox


class DaysItem(ListItemWithCheckbox):
    def __init__(self, start, finish, department, day, **kwargs):
        super().__init__(**kwargs)
        self.text = str(start) + ' --- ' + str(finish) + " --------- " + str(department)
        self.start = start
        self.day = day
        self.finish = finish
        self.department = department
        self.add_widget(IconLeftWidget(icon=self.my_icon))
        self.add_widget(RightCheckbox())
