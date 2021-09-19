import flex as flex
import pyowm
from pyowm.utils.config import get_default_config
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button


class City_WeatherApp(App):
    textinput1 = None
    button1 = None
    button2 = None
    button3 = None
    button4 = None
    button5 = None
    button6 = None

    def on_enter(self, value):
        #print('User pressed enter in', self, value.text)
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        owm = pyowm.OWM('c027c4867327d7960036032d0dd23c8f', config_dict)

        mgr = owm.weather_manager()
        message_text = self.textinput1.text
        observation = mgr.weather_at_place(message_text)
        w = observation.weather

        weather_info1 = "В " + message_text + " сейчас " + w.detailed_status
        weather_info2 = "Temperature " + str(w.temperature('celsius')["temp"])
        weather_info3 = "Wind speed " + str(w.wind()["speed"])
        weather_info4 = "Humidity " + str(w.humidity)
        weather_info5 = "Rain " + str(w.rain)
        self.button1.text = weather_info1
        self.button2.text = weather_info2
        self.button3.text = weather_info3
        self.button4.text = weather_info4
        self.button5.text = weather_info5

    def build(self):
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        owm = pyowm.OWM('c027c4867327d7960036032d0dd23c8f', config_dict)

        mgr = owm.weather_manager()
        message_text = 'Санкт-Петербург'
        observation = mgr.weather_at_place(message_text)
        w = observation.weather

        weather_info1 = "В " + message_text + "\n" + "сейчас " + w.detailed_status
        weather_info2 = "Temperature " + str(w.temperature('celsius')["temp"])
        weather_info3 = "Wind speed " + str(w.wind()["speed"])
        weather_info4 = "Humidity " + str(w.humidity)
        weather_info5 = "Rain " + str(w.rain)

        layout = BoxLayout(orientation='vertical')
        self.textinput1 = TextInput(text=message_text, multiline=False, font_size='25', halign='center')
        self.textinput1.bind(on_text_validate=self.on_enter)

        self.button1 = Button(text=weather_info1, font_size='20', halign='center')
        self.button2 = Button(text=weather_info2, font_size='20')
        self.button3 = Button(text=weather_info3, font_size='20')
        self.button4 = Button(text=weather_info4, font_size='20')
        self.button5 = Button(text=weather_info5, font_size='20')
        self.button6 = Button(text='*** show me city weather please! ***', font_size='25')
        self.button6.bind(on_press=self.on_enter)

        layout.add_widget(self.button1)
        layout.add_widget(self.button2)
        layout.add_widget(self.button3)
        layout.add_widget(self.button4)
        layout.add_widget(self.button5)
        layout.add_widget(self.textinput1)
        layout.add_widget(self.button6)
        # return a Button() as a root widget
        return layout


if __name__ == '__main__':
    City_WeatherApp().run()
