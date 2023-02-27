from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, FadeTransition, Screen, SlideTransition
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDIconButton, MDRectangleFlatButton, MDRaisedButton, MDRoundFlatButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList,OneLineListItem,TwoLineListItem,ThreeLineListItem,OneLineIconListItem,IconLeftWidget
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog

#Window.fullscreen = True
#Window.maximize()
Window.size = (400,700)

KV = '''
ScreenManager:
	Welcome_Screen:
	Screen_1:
<Welcome_Screen>:
	name: 'Welcome_Screen'
	MDFloatLayout:
		MDLabel:
			text: 'Welcome to Admin'
			pos_hint: {'center_x':.5,'center_y':.8}
			halign: 'center'
			valign: 'center'
			font_style: 'H2'
			font_size: '40sp'
		
		MDCard:
			pos_hint: {'center_x':.5,'center_y':.0}
			size_hint: (1,.2)
			md_bg_color: 'black'
			radius: 100,100,0,0

		MDFillRoundFlatIconButton:
			pos_hint: {'center_x':.5,'center_y':.05}
			text: 'ENTER'
			icon: 'home'
			on_press:
				root.manager.current = 'Screen_1'
				root.manager.transition.direction = 'left'

<Screen_1>:
	name: 'Screen_1'
	









'''

class Welcome_Screen(MDScreen):
	pass
class Screen_1(MDScreen):
	pass

sm = ScreenManager()
sm.add_widget(Welcome_Screen(name = 'Welcome_Screen'))
sm.add_widget(Screen_1(name = 'Screen_1'))

class The_App(MDApp):
	def build(self):
		self.theme_cls.theme_style = 'Light'
		self.theme_cls.primary_palette = 'Cyan'
		self.screen = Builder.load_string(KV)
		return self.screen

The_App().run()