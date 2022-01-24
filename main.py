from kivy.config import Config


Config.set('kivy', 'keyboard_mode', 'systemanddock')
Config.set("graphics", "width", 500)
Config.set("graphics", "height", 850)


from Code.Logic.GUILogic import GUILogic
from kivy.lang import Builder


Builder.load_file("Code/KV_FILES/StartPage.kv")
Builder.load_file("Code/KV_FILES/Schedule.kv")
Builder.load_file("Code/KV_FILES/Actions.kv")
Builder.load_file("Code/KV_FILES/Today.kv")
Builder.load_file("Code/KV_FILES/DepartmentsManager.kv")
Builder.load_file("Code/KV_FILES/DepartmentsCreation.kv")
Builder.load_file("Code/KV_FILES/ActionsCreation.kv")
Builder.load_file("Code/KV_FILES/ActionsConfiguration.kv")
Builder.load_file("Code/KV_FILES/TimeManager.kv")
Builder.load_file("Code/KV_FILES/DaysConfiguration.kv")
Builder.load_file("Code/KV_FILES/DaysItemCreation.kv")


def main():
    GUILogic().run()


if __name__ == "__main__":
    main()
