from kivymd.uix.screen import MDScreen
from . import Actions
from Code.Database.Sqlite.MySqlite import MySqlite
from kivy.properties import ObjectProperty


class ActionsConfiguration(MDScreen):
    current_action = ''
    actions_title = ObjectProperty(None)
    actions_description = ObjectProperty(None)
    back = 'actions'

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def go_back(self, title, *args):
        self.manager.current = title

    def on_enter(self, *args):
        action_data = MySqlite().get_actions(Actions.Actions.current_department)
        for item in action_data:
            title, description = item
            if title == self.current_action:
                self.actions_title.text = title
                self.actions_description.text = description

