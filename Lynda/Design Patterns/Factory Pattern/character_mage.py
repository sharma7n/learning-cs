# Mage class

from character import Character
from job_priest import Priest
from job_wizard import Wizard

class Mage( Character ):

	def __init__(self, name, job):
		self.name = name
		self.job = self.create_job(job)
		
	def create_job(self, job):
		if job == "dps": return Wizard()
		if job == "tank": return Priest()
		return None