from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.garden import FileChooserThumbView
#from kivy.core.window import Window

import os
#import numpy problemas con el apk

import auxiliar

Config.set('kivy', 'keyboard_mode', 'systemandmulti')


class ElegirArchivoVentana(FloatLayout):
	load = ObjectProperty(None)
	cancel = ObjectProperty(None)
	
class EscribirClaveVentana(FloatLayout):
	clave = ObjectProperty(None)
	text_input = ObjectProperty(None)
	cancel = ObjectProperty(None)
	
class Root(FloatLayout):
	labelPruebas = StringProperty()
	loadfile = ObjectProperty(None)
	savefile = ObjectProperty(None)
	filename = StringProperty()
	
	def dismiss_popup(self):
		self._popup.dismiss()
	
	def ElegirArchivo(self):
		print self.labelPruebas
		content = ElegirArchivoVentana(load=self.load, cancel=self.dismiss_popup)
		self._popup = Popup(title="Elige un archivo (imagen)", content=content,size_hint=(1.0, 1.0))
		self._popup.open()

	def EscribirClave(self):
		content = EscribirClaveVentana(clave=self.clave, cancel=self.dismiss_popup)
		self._popup = Popup(title="Escribe algo", content=content,size_hint=(1.0, 1.0))
		self._popup.open()
		
	def ProcesaTodo(self, mensaje):
		print "Procesar archivo"
		print mensaje
		self.labelPruebas = mensaje
		
	def Recuperar(self):
		print 'recuperar'
		print self.filename
		self.labelPruebas = "{} pixeles disponibles".format(auxiliar.capacidad(self.filename))
		

	def load(self, path, filename):
		if len(filename) == 1:
			with open(os.path.join(path, filename[0])) as stream:
				#checar extension
				self.filename = os.path.join(path, filename[0])
				print "cargar"

		self.dismiss_popup()

	def clave(self, mensaje):
		print mensaje
		print 'salvar'
		print self.loadfile
		self.ProcesaTodo(mensaje)
		self.dismiss_popup()
		
class Editor(App):
	pass

Factory.register('Root', cls=Root)
Factory.register('ElegirArchivoVentana', cls=ElegirArchivoVentana)
Factory.register('EscribirClaveVentana', cls=EscribirClaveVentana)

if __name__ == '__main__':
	Editor().run()