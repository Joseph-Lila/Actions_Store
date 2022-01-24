from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from Code.GUI.Classes.Department import Department
from Code.Database.Sqlite.MySqlite import MySqlite
from . import RightCheckbox
from . import Actions
from functools import partial


class DepartmentsManager(MDScreen):
    departments_list = ObjectProperty(None)

    def on_enter(self, *args):
        self.load_departments()

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def go_back(self, *args):
        self.manager.current = 'start_page'

    def go_to_action_screen(self, title, *args):
        Actions.Actions.current_department = title
        self.manager.current = 'actions'

    def add_department(self):
        self.manager.current = 'departments_creation'

    def remove_departments(self):
        for item in RightCheckbox.RightCheckbox.chosen_items:
            if isinstance(item, Department):
                self.departments_list.remove_widget(item)
                MySqlite().remove_department(item.title)

    def load_departments(self):
        # clear old data
        self.departments_list.clear_widgets()

        # get data from outer side (database)
        for item in MySqlite().get_departments():
            title, description = item
            elem = Department(title, description)
            elem.bind(on_press=partial(self.go_to_action_screen, title))
            self.departments_list.add_widget(elem)

