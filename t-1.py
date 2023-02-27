from kivy.lang import Builder
#from kivymd.uix.Picker import MDDatePicker
from kivymd.uix.button import MDFlatButton,MDIconButton,MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.taptargetview import MDTapTargetView

Window.size = (400,650)

KV = '''

MDScreenManager:
	MDScreen:
		MDCard:
			size_hint: (.7,.15)
			pos_hint: {'center_y':.85,'center_x':.5}
			background_color: 'black'

	
			radius: 50,50,50,50
			MDLabel:
				text: 'Hello Mr. Abdullah'
				valign:'center'
				halign: 'center'
				font_style: 'H2'
				pos_hint: {'center_y':.5,'center_x':.5}
				font_color: 'gray'
				font_size: '30dp'

		


		MDCard:
			size_hint: (.5,.5)
			pos_hint: {'center_y':.4,'center_x':.5}
			background_color: 'black'
			line_color: 'gray'
			md_bg_color: '#111111'
			#orientation: 'vertical'
		MDTextFieldRect:
			hint_text: 'first num'
			hint_text_color: 'black'
			size_hint:(None,None)
			width: '80dp'
			height: '30dp'
			background_color: 'gray'
			bubble_color: 'black'
			cursor_color: 'black'
			foreground_color: 'black'
			selection_color: 'black'
			radius: 50,50,50,50
			pos_hint: {'center_y':.5,'center_x':.379}
			
			halign: 'center'
			valign: 'center'
			multiline: False
			line_anim: False

		MDTextFieldRect:

			hint_text: 'Sec num'
			size_hint:(None,None)
			hint_text_color: 'black'
			line_anim: False
			width: '80dp'
			height: '30dp'
			background_color: 'gray'
			radius: 50,50,50,50
			pos_hint: {'center_y':.5,'center_x':.62}
			halign: 'center'
			valign: 'center'
			multiline: False
			cursor_color: 'black'

		MDLabel:
			size_hint: (None,None)
			text: 'Result'
			font_style: 'H2'
			pos_hint: {'center_y':.35,'center_x':.5}
			font_size: '20sp'
			line_color: 'white'
			halign: 'center'
			valign: 'center'
			radius: 50,50,50,50

		MDIconButton:
			icon: 'account'
			pos_hint:{'center_x':.5,'center_y':.2}
			#on_press: app.
	
'''






class InsideApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_palette = 'Orange'
		return Builder.load_string(KV)


InsideApp().run()