from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from Code.Database.Sqlite.MySqlite import MySqlite


class DepartmentsCreation(MDScreen):
    departments_title = ObjectProperty(None)
    departments_description = ObjectProperty(None)

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def go_back(self, *args):
        self.manager.current = 'departments_manager'

    def on_leave(self, *args):
        self.departments_title.text = ''
        self.departments_description.text = ''

    def create_department(self, *args):
        MySqlite().insert_department(
            self.departments_title.text,
            self.departments_description.text
        )
