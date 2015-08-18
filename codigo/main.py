from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.uix.widget import Widget


import os
import numpy

class ElegirArchivoVentana(FloatLayout):
	load = ObjectProperty(None)
	cancel = ObjectProperty(None)
	
class EscribirClaveVentana(FloatLayout):
	clave = ObjectProperty(None)
	text_input = ObjectProperty(None)
	cancel = ObjectProperty(None)
	
class Root(FloatLayout):
	miau = "hola"
	labelPruebas = StringProperty()
	loadfile = ObjectProperty(None)
	savefile = ObjectProperty(None)
	
	def dismiss_popup(self):
		self._popup.dismiss()
	
	def ElegirArchivo(self):
		print self.labelPruebas, "hola miau"
		content = ElegirArchivoVentana(load=self.load, cancel=self.dismiss_popup)
		self._popup = Popup(title="Load file text", content=content,size_hint=(0.9, 0.9))
		self._popup.open()

	def EscribirClave(self):
		content = EscribirClaveVentana(clave=self.clave, cancel=self.dismiss_popup)
		self._popup = Popup(title="Save file text", content=content,size_hint=(0.9, 0.9))
		self._popup.open()
		
	def ProcesaTodo(self, mensaje):
		print "Procesar archivo"
		print mensaje
		self.labelPruebas = mensaje

	def load(self, path, filename):
		print self.miau
		self.miau = "cambio miau"
		if len(filename) == 1:
			with open(os.path.join(path, filename[0])) as stream:
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