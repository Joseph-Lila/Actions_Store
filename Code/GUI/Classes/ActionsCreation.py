from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from Code.GUI.Classes.Actions import Actions
from Code.Database.Sqlite.MySqlite import MySqlite


class ActionsCreation(MDScreen):
    actions_title = ObjectProperty(None)
    actions_description = ObjectProperty(None)

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def go_back(self, *args):
        self.manager.current = 'actions'

    def on_leave(self, *args):
        self.actions_title.text = ''
        self.actions_description.text = ''

    def create_action(self, *args):
        MySqlite().insert_action(
            Actions.current_department,
            self.actions_title.text,
            self.actions_description.text
        )
