from kivy.lang import Builder
from kivy.app import App

KV = '''
#:import Clipboard kivy.core.clipboard.Clipboard
Label:
	Button:
		on_release:
			#self.text = Clipboard.paste()
			Clipboard.copy('Data2')

'''

class Main(App):
	def build(self):
		return Builder.load_string(KV)
Main().run()