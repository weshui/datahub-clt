# This class is the Postgresql statement generator

class Generator:

	def __init__(self):
		self.generator = None
		self.simple_template = "SELECT {} FROM {} WHERE {}"


	def _simple_select(self, entity, table, condition):
		return self.simple_template.format(entity, table, condition)

	



