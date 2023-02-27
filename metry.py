from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog

KV = '''
MDScreenManager:

    MDScreen:
        name:'screen1'
        
        MDFloatingActionButton:
            icon: 'exit-run'
            pos_hint:{'center_x':.05,'center_y':.95}
            size_hint:(.05,.068)
            shadow_color: '#000000'
            icon_size: '25sp'
            icon_color:'#3ab7ff'
            md_bg_color: '#70e6f6'
            on_press:
                exit()
        MDLabel:
            text: 'Welcome Screen'
            font_style: 'H2'
            font_size: '50sp'
            pos_hint:{'center_x': .5 , 'center_y': .6}
            valign: 'center'
            halign: 'center'
        MDFloatingActionButton:
            pos_hint:{'center_x': .5 , 'center_y': .4}
            icon: 'arrow-right-bold'
            md_bg_color: '#70e6f6'
            icon_size: '40sp'
            icon_color: '#3ab7ff'
            on_press:
                root.current = 'screen2'
                root.transition.direction = 'left'
        ProgressBar:
            value: 30
            pos_hint: {'center_y':.02}

    MDScreen:
        name:'screen2'
        fullscreen: True
        
        MDLabel:
            text: 'Username Screen'
            font_style: 'H2'
            font_size: '50sp'
            pos_hint:{'center_x': .5 , 'center_y': .8}
            valign: 'center'
            halign: 'center'

        MDTextField:
            id: text_field
            pos_hint: {'center_x':.5,'center_y':.5}
            hint_text: 'Username'
            size_hint: (.7,.1)
            helper_text: 'Required'
            helper_text_mode: 'on_error'
            right_icon_color: '#70e6f6'
            icon_right: 'account-box'
            required: True if text_field.text == ' ' else False
        MDFloatingActionButton:
            pos_hint:{'center_x': .05 , 'center_y': .1}
            icon: 'arrow-left-bold'
            md_bg_color: '#70e6f6'
            icon_size: '40sp'
            icon_color: '#3ab7ff'
            on_press:
                root.current = 'screen1'
                root.transition.direction = 'right'
        ProgressBar:
            value: 60
            pos_hint: {'center_y':.02}




'''

class MainApp(MDApp):
    def build(self):
        self.string = Builder.load_string(KV)
        return self.string
MainApp().run()