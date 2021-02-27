from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window



class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class VerisWindow(Screen):
    def play_music(self, fails):
        music = SoundLoader.load(fails)
        if music:
            music.play()    # nospēlējas līdz galam. Neapstājas, ja iziet.
                            # Bail iedomāties, kas notiek, ja palaiž vairākas reizē
                            #nvm checked viss slikti



class KaratavuWindow(Screen):
    def play_music(self, fails):
        music = SoundLoader.load(fails)
        if music:
            music.play()


class ValterkalninsWindow(Screen):
    def play_music(self, fails):
        music = SoundLoader.load(fails)
        if music:
            music.play()


class EzerinaWindow(Screen):
    def play_music(self, fails):
        music = SoundLoader.load(fails)
        if music:
            music.play()


class SimanaWindow(Screen):
    def play_music(self, fails):
        music = SoundLoader.load(fails)
        if music:
            music.play()


class StavieWindow(Screen):
    def play_music(self, fails):
        music = SoundLoader.load(fails)
        if music:
            music.play()


class SeminarsWindow(Screen):
    def play_music(self, fails):
        music = SoundLoader.load(fails)
        if music:
            music.play()


class ValmiermuizaWindow(Screen):
    def play_music(self, fails):
        music = SoundLoader.load(fails)
        if music:
            music.play()


class ZilaiskalnsWindow(Screen):
    def play_music(self, fails):
        music = SoundLoader.load(fails)
        if music:
            music.play()


class PargaujaWindow(Screen):
    def play_music(self, fails):
        music = SoundLoader.load(fails)
        if music:
            music.play()


class StacijaWindow(Screen):
    def play_music(self, fails):
        music = SoundLoader.load(fails)
        if music:
            music.play()


class KracesWindow(Screen):
    def play_music(self, fails):
        music = SoundLoader.load(fails)
        if music:
            music.play()


class WindowManager(ScreenManager):
    def play_music(self, fails):
        music = SoundLoader.load(fails)
        if music:
            music.play()


kv = Builder.load_file("mymain.kv")


class MyMainApp(App):
    def build(self):
        Window.clearcolor = (1, 69/255, 0, 0.7)
        return kv


if __name__ == "__main__":
    MyMainApp().run()
