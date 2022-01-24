from kivymd.uix.screen import MDScreen
from Code.Database.Sqlite.MySqlite import MySqlite
from kivy.properties import ObjectProperty
from Code.GUI.Classes.DaysItem import DaysItem
from . import RightCheckbox
from Code.GUI.Classes.ActionsConfiguration import ActionsConfiguration
from functools import partial
from . import Actions


class DaysConfiguration(MDScreen):
    current_day = ''
    days_title = ObjectProperty(None)
    today_list = ObjectProperty(None)

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def go_back(self, *args):
        self.manager.current = 'time_manager'

    def on_enter(self, *args):
        self.days_title.title = self.current_day
        self.load_items()

    def switch_type(self, *args):
        pass

    def add_item(self, *args):
        self.manager.current = 'days_item_creation'

    def remove_item(self, *args):
        for item in RightCheckbox.RightCheckbox.chosen_items:
            if isinstance(item, DaysItem):
                self.today_list.remove_widget(item)
                MySqlite().remove_day_item(self.current_day, item.start)

    def go_to_actions_configuration(self, title, department_title, *args):
        ActionsConfiguration.current_action = title
        Actions.Actions.current_department = department_title
        ActionsConfiguration.back = "days_configuration"
        self.manager.current = 'actions_configuration'

    def load_items(self, *args):
        self.today_list.clear_widgets()

        ans = MySqlite().get_days_configs_by_days_title(self.current_day)
        for item in ans:
            start, finish, department_id, type_ = item
            department_title = MySqlite().get_department_title_by_id(department_id)
            actions_title = MySqlite().get_actions(department_title)
            if len(actions_title) > 0:
                actions_title = actions_title[0][0]
            if department_title is not None:
                elem = DaysItem(start, finish, department_title, self.current_day)
                if actions_title is not None and actions_title != []:
                    elem.bind(on_press=partial(self.go_to_actions_configuration, actions_title, department_title))
                self.today_list.add_widget(elem)
