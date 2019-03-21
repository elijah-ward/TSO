
from tso.importer import weather_importer

#TODO: Make this class inherit from our Dynamic_Constraint class?

class WeatherConstraint():
	"""Custom constraint to check if weather conditions are sufficiently good

	Dynamic constraint that checks current weather conditions at runtime and determines
	how favourable these conditions are for observing

	Attributes
	----------
	location: str
		Attribute that determines current location of weather report.
		Used primarily for error checking
	condition: str
		Current meteorological condition. E.g. Cloudy, Clear, Rainy etc...
	visibility: int
		Current location's visibility distance. Given in meters
	humidity: int
		Current humidity levels at current location
	coverage: float
		Current cloud coverage. 
	
	
	"""

	def __init__(self, conditions):
		"""Custom dynamic constraint that evaluates current weather conditions
		
		"""

		self.location = conditions[0]
		self.condition = conditions[1]
		self.visibility = conditions[2]
		self.humidity = conditions[3]
		self.coverage = conditions[4]


	def compute_constraint(self):
		"""

		"""
		try:
			assert self.location == 'Volcano', "Incorrect location, please try again"
		except AssertionError as e:
			print(e)

		if self.condition == 'Clear':
			return 1

		else:
			cloud_coverage = self.coverage
			return 1.00 - (cloud_coverage/100)

		#TODO: High humidity may also have an effect on viewing capabilities
		# considering expanding this constraint to accomodate this fact


#Simple smoke test. Robust tests incoming

conditions = getWeather()
cons = WeatherConstraint(conditions)
test = cons.compute_constraint() 
print (test)




