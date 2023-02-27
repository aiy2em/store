from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.label import Label


KV = '''
Screen: 
    name: 'screen_1'
    BoxLayout:
        id: layout
        orientation: "vertical"
        size: root.width, root.height
        Button:
            text:"hello"
            on_press: app.add_the_label()
'''





class UiApp(App):

    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen

    def add_the_label(self):
        self.button = Label(text="you have just added me")
        self.screen.ids.layout.add_widget(self.button)

UiApp().run()