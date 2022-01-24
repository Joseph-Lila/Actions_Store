from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, RiseInTransition
from Code.GUI.Classes.Start_page import StartPage
from Code.GUI.Classes.Actions import Actions
from Code.GUI.Classes.Schedule import Schedule
from Code.GUI.Classes.Today import Today
from Code.GUI.Classes.DepartmentsManager import DepartmentsManager
from Code.GUI.Classes.DepartmentsCreation import DepartmentsCreation
from Code.GUI.Classes.ActionsCreation import ActionsCreation
from Code.GUI.Classes.ActionsConfiguration import ActionsConfiguration
from Code.GUI.Classes.TimeManager import TimeManager
from Code.GUI.Classes.DaysConfiguration import DaysConfiguration
from Code.GUI.Classes.DaysItemCreation import DaysItemCreation
from kivy.core.audio import SoundLoader
import os
import time
from kivymd.utils import asynckivy
from random import shuffle
from Code.Database.Sqlite.MySqlite import MySqlite


class GUILogic(MDApp):
    index = 0
    track_length = 0
    current_track = None
    delta_t = 0

    def __init__(self, **kwargs):
        self.title = "LLK"
        self.icon = r'Sources\Pictures\ico\icon1.ico'
        self.manager = ScreenManager(transition=RiseInTransition())
        super().__init__(**kwargs)
        MySqlite().create_tables()
        MySqlite().add_days()
        MySqlite().go_forward_with_data()

    def play_music(self, folder_music='Sources/Audio/mp3/'):
        async def _play_music():
            while True:
                await asynckivy.sleep(0.01)
                if not self.current_track:
                    self.current_track = SoundLoader.load(sounds[self.index])
                    self.track_length = self.current_track.length
                    self.current_track.play()
                    self.delta_t = time.time()
                else:
                    if time.time() - self.delta_t > self.track_length:
                        self.current_track = None
                        if self.index < len(sounds) - 1:
                            self.index += 1
                        else:
                            break

        sounds = [f'{folder_music}/{track}' for track in os.listdir(folder_music)]
        shuffle(sounds)
        asynckivy.start(_play_music())

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        self.manager.add_widget(StartPage(name='start_page'))
        self.manager.add_widget(Actions(name='actions'))
        self.manager.add_widget(TimeManager(name='time_manager'))
        self.manager.add_widget(Schedule(name='schedule'))
        self.manager.add_widget(Today(name='today'))
        self.manager.add_widget(DepartmentsManager(name='departments_manager'))
        self.manager.add_widget(DepartmentsCreation(name='departments_creation'))
        self.manager.add_widget(ActionsCreation(name='actions_creation'))
        self.manager.add_widget(ActionsConfiguration(name='actions_configuration'))
        self.manager.add_widget(DaysConfiguration(name='days_configuration'))
        self.manager.add_widget(DaysItemCreation(name='days_item_creation'))
        return self.manager
