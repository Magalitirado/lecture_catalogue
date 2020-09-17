#from .classe_mobilite import *

class Mobilite(object):

	def __init__(self, identite, annee, semestre, ville, pays, cours, mail):
		self._identite = identite
		self._annee = annee
		self._semestre = semestre
		self._ville = ville
		self._pays = pays
		self._cours = cours
		self._mail = mail

	@property
	def identite(self):
		return self._identite

	@property
	def annee(self):
		return self._annee

	@property
	def semestre(self):
		return self._semestre
	
	@property
	def ville(self):
		return self._ville

	@property
	def pays(self):
		return self._pays
	
	@property
	def cours(self):
		return self._cours

	@property
	def mail(self):
		return self._mail
