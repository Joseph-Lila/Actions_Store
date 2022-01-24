from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from Code.GUI.Classes.Day import Day
from functools import partial
from Code.GUI.Classes.DaysConfiguration import DaysConfiguration


class TimeManager(MDScreen):
    days_list = ObjectProperty(None)
    day_titles = [
        "Monday 1",
        "Tuesday 1",
        "Wednesday 1",
        "Thursday 1",
        "Friday 1",
        "Saturday 1",
        "Sunday 1",
        "Monday 2",
        "Tuesday 2",
        "Wednesday 2",
        "Thursday 2",
        "Friday 2",
        "Saturday 2",
        "Sunday 2",
    ]

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def on_enter(self, *args):
        self.load_days()

    def go_back(self, *args):
        self.manager.current = 'schedule'

    def go_to_days_configuration_screen(self, title, *args):
        DaysConfiguration.current_day = title
        self.manager.current = 'days_configuration'

    def load_days(self, *args):
        # clear old data
        self.days_list.clear_widgets()

        # get data from outer side (database)
        for item in self.day_titles:
            elem = Day(item)
            elem.bind(on_press=partial(self.go_to_days_configuration_screen, item))
            self.days_list.add_widget(elem)
