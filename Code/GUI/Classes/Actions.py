from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from functools import partial
from Code.GUI.Classes.ActionsConfiguration import ActionsConfiguration
from . import RightCheckbox
from Code.Database.Sqlite.MySqlite import MySqlite
from Code.GUI.Classes.Action import Action


class Actions(MDScreen):
    current_department = ''
    actions_list = ObjectProperty(None)

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def on_enter(self, *args):
        self.load_actions()

    def swap_actions(self, *args):
        pass

    def add_action(self, *args):
        self.manager.current = 'actions_creation'

    def remove_actions(self, *args):
        for item in RightCheckbox.RightCheckbox.chosen_items:
            if isinstance(item, Action):
                self.actions_list.remove_widget(item)
                MySqlite().remove_action(item.title)

    def go_back(self, *args):
        self.manager.current = 'departments_manager'

    def go_to_actions_configuration(self, title, *args):
        ActionsConfiguration.current_action = title
        ActionsConfiguration.back = 'actions'
        self.manager.current = 'actions_configuration'

    def load_actions(self, *args):
        # clear old data
        self.actions_list.clear_widgets()

        # get data from outer side (database)
        for item in MySqlite().get_actions(self.current_department):
            title, description = item
            elem = Action(title, description)
            elem.bind(on_press=partial(self.go_to_actions_configuration, title))
            self.actions_list.add_widget(elem)
