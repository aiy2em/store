from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

'''Valid properties (Avialable For MDLabel) are ['_background_origin', '_background_x', '_background_y', 
'_capitalizing', '_md_bg_color', '_text', '_text_color_str', 'adaptive_height', 
'adaptive_size', 'adaptive_width', 'anchors', 'angle', 'background', 
'background_hue', 'background_origin', 'background_palette', 'base_direction', 
'bold', 'can_capitalize', 'canvas_bg', 'center', 'center_x', 'center_y', 
'children', 'cls', 'color', 'device_ios', 'disabled', 'disabled_color', 
'disabled_outline_color', 'ellipsis_options', 'font_blended', 
'font_context', 'font_family', 'font_features', 'font_hinting', 
'font_kerning', 'font_name', 'font_size', 'font_style', 'halign', 
'height', 'id', 'ids', 'is_shortened', 'italic', 'line_color', 
'line_height', 'line_width', 'markup', 'max_lines', 'md_bg_color', 
'mipmap', 'motion_filter', 'opacity', 'opposite_colors', 'outline_color', 
'outline_width', 'padding', 'padding_x', 'padding_y', 'parent', 
'parent_background', 'pos', 'pos_hint', 'radius', 'refs', 'right', 
'shorten', 'shorten_from', 'size', 'size_hint', 'size_hint_max', 
'size_hint_max_x', 'size_hint_max_y', 'size_hint_min', 'size_hint_min_x', 
'size_hint_min_y', 'size_hint_x', 'size_hint_y', 'specific_secondary_text_color', 
'specific_text_color', 'split_str', 'strikethrough', 'strip', 'text', 
'text_color', 'text_language', 'text_size', 'texture', 'texture_size', 
'theme_cls', 'theme_text_color', 'top', 'underline', 
'unicode_errors', 'valign', 'widget_style', 'width', 'x', 'y']'''

class Example(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Orange"
		return (
			MDScreen(

				MDLabel(
					id="label",
					adaptive_size=True,
					pos_hint={"center_x": .5, "center_y": .5},
					text="MDLabel",
					#allow_selection=True,
					#allow_copy=True,
					padding=("4dp", "4dp"),
				)
			)
		)
	def on_start(self):
		self.root.ids.label.bind(on_copy=self.on_copy)
	def on_copy(self, instance_label: MDLabel):
		print("The text is copied to the clipboard")

Example().run()