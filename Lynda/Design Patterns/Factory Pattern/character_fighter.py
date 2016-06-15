# Fighter class

from character import Character
from job_archer import Archer
from job_knight import Knight

class Fighter( Character ):

	def __init__(self, name, job):
		self.name = name
		self.job = self.create_job(job)
		
	def create_job(self, job):
		if job == "dps": return Archer()
		if job == "tank" : return Knight()
		return None