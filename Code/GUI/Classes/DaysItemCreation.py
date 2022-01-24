from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from Code.Database.Sqlite.MySqlite import MySqlite
from Code.GUI.Classes.DaysConfiguration import DaysConfiguration


class DaysItemCreation(MDScreen):
    spinner = ObjectProperty(None)
    finish = ObjectProperty(None)
    start = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.spinner.dropdown_cls.max_height = self.spinner.height * 2

    def on_enter(self, *args):
        self.load_items()

    def on_leave(self, *args):
        self.start.text = ''
        self.finish.text = ''

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def go_back(self, *args):
        self.manager.current = 'days_configuration'

    def create_days_item(self, *args):
        MySqlite().insert_days_item(
            self.start.text,
            self.finish.text,
            self.spinner.text,
            'standard',
            DaysConfiguration.current_day
        )

    def load_items(self, *args):
        self.spinner.values = [item[0] for item in MySqlite().get_departments()]
