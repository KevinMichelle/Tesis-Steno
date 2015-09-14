__version__ = '1.0'

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


class ElegirArchivoVentana(FloatLayout):
	CargarArchivo = ObjectProperty(None)
	cancel = ObjectProperty(None)
	
class EscribirMensajeVentana(FloatLayout):
	GuardarMensaje = ObjectProperty(None)
	text_input = ObjectProperty(None)
	cancel = ObjectProperty(None)
	
class MostrarMensaje(FloatLayout):
	mensajerecuperado = StringProperty()
	cancel = ObjectProperty(None)
	
class Root(FloatLayout):
	labelPruebas = StringProperty()
	mensaje = StringProperty()
	loadfile = ObjectProperty(None)
	savefile = ObjectProperty(None)
	filename = StringProperty()
	label1 = StringProperty()
	label2 = StringProperty()
	label3 = StringProperty()
	
	def dismiss_popup(self):
		self._popup.dismiss()
	
	def ElegirArchivo(self):
		print self.labelPruebas
		content = ElegirArchivoVentana(CargarArchivo=self.CargarArchivo, cancel=self.dismiss_popup)
		self._popup = Popup(title="Elige un archivo (imagen)", content=content,size_hint=(1.0, 1.0))
		self._popup.open()

	def EscribirMensaje(self):
		content = EscribirMensajeVentana(GuardarMensaje=self.GuardarMensaje, cancel=self.dismiss_popup)
		print self.mensaje, "MIAU"
		self._popup = Popup(title="Escribe algo", content=content,size_hint=(1.0, 1.0))
		self._popup.open()
		
	def Ocultar(self):
		if ((self.mensaje != '' or self.mensaje is not None) and (self.filename != '' or self.filename is not None)):
			auxiliar.image_steganography(self.filename, self.mensaje, True)
			self.label3 = "Mensaje ocultado"
		
	def Recuperar(self):
		print "recuperar", len(self.filename)
		if len(self.filename) > 0:
			self.mensajerecuperado = auxiliar.search_image_steganography(self.filename)
			content = MostrarMensaje(GuardarMensaje=self.GuardarMensaje, cancel=self.dismiss_popup, mensajerecuperado = self.mensajerecuperado)
			self._popup = Popup(title="Mensaje recuperado", content=content, size_hint=(1.0, 1.0))
			self._popup.open()
			#self.labelPruebas = "{} pixeles disponibles".format(auxiliar.capacidad(self.filename))
		

	def CargarArchivo(self, path, filename):
		if len(filename) == 1:
			with open(os.path.join(path, filename[0])) as stream:
				#checar extension
				self.filename = os.path.join(path, filename[0])
				print "cargar"

		self.dismiss_popup()

	def GuardarMensaje(self, mensaje):
		self.mensaje = mensaje
		self.dismiss_popup()
		
class Editor(App):
	pass

Factory.register('Root', cls=Root)
Factory.register('ElegirArchivoVentana', cls=ElegirArchivoVentana)
Factory.register('EscribirMensajeVentana', cls=EscribirMensajeVentana)
Factory.register('MostrarMensaje', cls=MostrarMensaje)

if __name__ == '__main__':
	Editor().run()
