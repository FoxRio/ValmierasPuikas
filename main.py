import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class VerisWindow(Screen):
    pass


class KaratavuWindow(Screen):
    pass


class ValterkalninsWindow(Screen):
    pass


class EzerinaWindow(Screen):
    pass


class SimanaWindow(Screen):
    pass


class StavieWindow(Screen):
    pass


class SeminarsWindow(Screen):
    pass


class ValmiermuizaWindow(Screen):
    pass


class ZilaiskalnsWindow(Screen):
    pass


class PargaujaWindow(Screen):
    pass


class StacijaWindow(Screen):
    pass


class KracesWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("mymain.kv")


class MyMainApp(App):
    def build(self):
        Window.clearcolor = (1, 69/255, 0, 0.7)
        return kv


if __name__ == "__main__":
    MyMainApp().run()
