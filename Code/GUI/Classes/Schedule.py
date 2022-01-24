from kivymd.uix.screen import MDScreen


class Schedule(MDScreen):
    def __draw_shadow__(self, origin, end, context=None):
        pass

    def go_back(self, *args):
        self.manager.current = 'start_page'
