from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config
from kivymd.app import MDApp
from kivy.animation import Animation
from kivy.graphics import Color, Line
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from math import cos, sin, pi
from kivy.clock import Clock
import time
import datetime
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_file('clock.kv')


# class Ticks(Widget):
#     def __init__(self, **kwargs):
#         super(Ticks, self).__init__(**kwargs)
#         self.bind(pos=self.update_clock)
#         self.bind(size=self.update_clock)
#
#     def update_clock(self, *args):
#         self.canvas.clear()
#         with self.canvas:
#             time = datetime.datetime.now()
#             Color(0.2, 0.5, 0.2)
#             Line(points=[self.center_x, self.center_y, self.center_x+0.8*self.r*sin(pi/30*time.second), self.center_y+0.8*self.r*cos(pi/30*time.second)], width=1, cap="round")
#             Color(0.3, 0.6, 0.3)
#             Line(points=[self.center_x, self.center_y, self.center_x+0.7*self.r*sin(pi/30*time.minute), self.center_y+0.7*self.r*cos(pi/30*time.minute)], width=2, cap="round")
#             Color(0.4, 0.7, 0.4)
#             th = time.hour*60 + time.minute
#             Line(points=[self.center_x, self.center_y, self.center_x+0.5*self.r*sin(pi/360*th), self.center_y+0.5*self.r*cos(pi/360*th)], width=3, cap="round")
#
#
class MyLayout(BoxLayout):
    your_time = StringProperty()

    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        Clock.schedule_interval(self.set_time, 0.1)

    def build(self):
        ScreenManager().add_widget(MenuScreen(name='menu'))
        ScreenManager().add_widget(BataryaScreen(name='batarya'))

    def set_time(self, dt):
        self.your_time = time.strftime("%d/%m/%Y %H:%M")


class Gui(App):

    def build(self):
        return MyLayout()


class MenuScreen(Screen):
    pass


class BataryaScreen(Screen):
    pass


#
# class MyClockWidget(FloatLayout):
#     pass

#
# class MyClockApp(App):
#     def build(self):
#         clock = MyClockWidget()
#         Clock.schedule_interval(clock.ticks.update_clock, 1)
#         return clock
#
#
# if __name__ == '__main__':
#     MyClockApp().run()

if __name__ == "__main__":
    Gui().run()