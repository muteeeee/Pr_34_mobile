import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class myApp(App):
    def build(self):
        s = Scatter()
        fl = FloatLayout(size=(400, 200))
        s.add_widget(fl)

        button1 = Button(
            text="FIRST",
            font_size=20,
            on_press=self.btn_press,
            background_color=[1, 0, 1, 1],
            background_normal='',
            size_hint=(.5, .25),
            pos=(200, 20))
        fl.add_widget(button1)

        button2 = Button(
            text="SECOND",
            font_size=20,
            on_press=self.btn_press,
            background_color=[0, 0, 1, 1],
            background_normal='',
            size_hint=(.5, .25),
            pos=(200, 65))
        fl.add_widget(button2)

        button3 = Button(
            text="THIRD",
            font_size=20,
            on_press=self.btn_press,
            background_color=[0, 1, 1, 1],
            background_normal='',
            size_hint=(.5, .25),
            pos=(200, 110))
        fl.add_widget(button3)

        button4 = Button(
            text="FORTH",
            font_size=20,
            on_press=self.btn_press,
            background_color=[0, 1, 0, 1],
            background_normal='',
            size_hint=(.5, .25),
            pos=(200, 155))
        fl.add_widget(button4)

        button5 = Button(
            text="FIFTH",
            font_size=20,
            on_press=self.btn_press,
            background_color=[1, 1, 0, 1],
            background_normal='',
            size_hint=(.5, .25),
            pos=(200, 200))
        fl.add_widget(button5)

        button6 = Button(
            text="SIXTH",
            font_size=20,
            on_press=self.btn_press,
            background_color=[1, 0.5333, 0, 1],
            background_normal='',
            size_hint=(.5, .25),
            pos=(200, 245))
        fl.add_widget(button6)

        button7 = Button(
            text="SEVENTH",
            font_size=20,
            on_press=self.btn_press,
            background_color=[1, 0, 0, 1],
            background_normal='',
            size_hint=(.5, .25),
            pos=(200, 290))
        fl.add_widget(button7)

        return s

    def btn_press(self, instance):
        if instance.text == 'FIRST':
            instance.text = '#ff00ff'
        elif instance.text == 'SECOND':
            instance.text = '#0000ff'
        elif instance.text == 'THIRD':
            instance.text = '#00ffff '
        elif instance.text == 'FORTH':
            instance.text = '#00ff00'
        elif instance.text == 'FIFTH':
            instance.text = '#ffff00'
        elif instance.text == 'SIXTH':
            instance.text = '#f8800'
        elif instance.text == 'SEVENTH':
            instance.text = '#ff0000'



if __name__ == "__main__":
    myApp().run()