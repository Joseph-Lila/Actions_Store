from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    chosen_items = []

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def on_active(self, *args):
        if self.active:
            self.chosen_items.append(self.parent.parent)
        else:
            self.chosen_items.remove(self.parent.parent)
