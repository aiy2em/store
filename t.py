from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.utils import asynckivy

KV = '''
ScreenManager:
	elzeft:

<elzeft>:
	name: 'screen'
	MDLabel:
		id: label_text
		text: 'Hello Mr. Abdullah'
		font_style: 'H2'
		pos_hint: {'center_y':.5}
		halign: 'center'

'''
class elzeft(Screen):
	pass

sm = ScreenManager()
sm.add_widget(elzeft(name = 'screen'))

class Main(MDApp):
	def build(self):
		self.string = Builder.load_string(KV)
		self.refresh_sentence()
		return self.string
    def refresh_sentence(self):
		async refresh_sentence():
			for x in range(1,10):
				await asynckivy.sleep(1)
				text_of_label = self.string.get_screen('screen').ids.label_text
				text_of_label.text = str(x)
			text_of_label.text = "Happy Birthday !!"
		
        asynckivy.start(refresh_sentence())	

Main().run()