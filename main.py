import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput  
from kivy.uix.label import Label
from kivy.uix.button import Button

class StartScreen(Widget):
	def __init__(self, **kwargs):
		super(StartScreen,self).__init__(**kwargs)
		self.StartGame = Button(text="Start Game")
		self.StartGame.bind(on_press=self.on_press)
		self.add_widget(self.StartGame)

	def on_press(self,instance):

		return LoginScreen()

class LoginScreen(GridLayout):
		def __init__(self, **kwargs):
			super(LoginScreen,self).__init__(**kwargs)
			self.cols = 2


			
class MyApp(App):
    def build(self):
        return StartScreen()



if __name__ == '__main__':
    MyApp().run()