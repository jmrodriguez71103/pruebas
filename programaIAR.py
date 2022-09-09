import json
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField


class programaIAR(MDApp):
	with open('data.json') as file:
		data = json.load(file)

	def open_direction (self, direction):
		direction = self.data[direction]
		return direction


	def save(self):
		if (self.root.ids.cambio_x.text == "" and self.root.ids.cambio_y.text == ""):
			self.data["x"] = self.root.ids.pos_x.text
			self.data["y"] = self.root.ids.pos_y.text
			with open('data.json', 'w') as file:
				json.dump(self.data, file)
		else:
			self.data["x"] = self.root.ids.cambio_x.text
			self.data["y"] = self.root.ids.cambio_y.text
			with open('data.json', 'w') as file:
				json.dump(self.data, file)
	 		
	def mod_x_add(self):
		#direc = direction.replace('"', '')
		if (int(self.root.ids.pos_x.text) >= 0 and int(self.root.ids.pos_x.text) < 180):
			self.root.ids.pos_x.text = str(int(self.root.ids.pos_x.text) + int(self.root.ids.grados.text))
		
		elif (int(self.root.ids.pos_x.text) > 180):
			self.root.ids.pos_x.text = "180"
			
		elif (int(self.root.ids.pos_x.text) < 0):
			self.root.ids.pos_x.text = "0"

		
	def mod_x_remove(self):
		if (int(self.root.ids.pos_x.text) > 0 and int(self.root.ids.pos_x.text) <= 180):
			self.root.ids.pos_x.text = str(int(self.root.ids.pos_x.text) - int(self.root.ids.grados.text))
		
		elif (int(self.root.ids.pos_x.text) > 180):
			self.root.ids.pos_x.text = "180"
			
		elif (int(self.root.ids.pos_x.text) < 0):
			self.root.ids.pos_x.text = "0"
		
	def mod_y_add(self):
		if (int(self.root.ids.pos_y.text) >= 0 and int(self.root.ids.pos_y.text) < 180):
			self.root.ids.pos_y.text = str(int(self.root.ids.pos_y.text) + int(self.root.ids.grados.text))
		
		elif (int(self.root.ids.pos_y.text) > 180):
			self.root.ids.pos_y.text = "180"
			
		elif (int(self.root.ids.pos_y.text) < 0):
			self.root.ids.pos_y.text = "0"		
	
	def mod_y_remove(self):
		if (int(self.root.ids.pos_y.text) > 0 and int(self.root.ids.pos_y.text) <= 180):
			self.root.ids.pos_y.text = str(int(self.root.ids.pos_y.text) - int(self.root.ids.grados.text))

		elif (int(self.root.ids.pos_y.text) > 180):
			self.root.ids.pos_y.text = "180"
			
		elif (int(self.root.ids.pos_y.text) < 0):
			self.root.ids.pos_y.text = "0"
	
	def build (self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "BlueGray"
		self.text_x = self.open_direction("x")
		self.text_y = self.open_direction("y")
		#self.text_x, self.text_y = self.open_x(), self.open_y()
		return Builder.load_file('pantallaPrin.kv')

		


programaIAR().run()
