from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from Code.Database.Sqlite.MySqlite import MySqlite
import datetime
from Code.GUI.Classes.DaysItem import DaysItem
from functools import partial
from Code.GUI.Classes.ActionsConfiguration import ActionsConfiguration
from . import Actions


class Today(MDScreen):
    current_day = ''
    days_title = ObjectProperty(None)
    today_list = ObjectProperty(None)

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def go_back(self, *args):
        self.manager.current = 'schedule'

    def switch_type(self, *args):
        pass

    def on_enter(self, *args):
        today_str = str(datetime.datetime.today().date())
        self.days_title.title = today_str
        self.current_day = MySqlite().get_days_title_by_date(today_str)
        self.load_items()

    def go_to_actions_configuration(self, title, department_title, *args):
        ActionsConfiguration.current_action = title
        Actions.Actions.current_department = department_title
        ActionsConfiguration.back = "today"
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