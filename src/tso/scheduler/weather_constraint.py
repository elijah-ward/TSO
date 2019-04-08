
from tso.importer.weather_importer import WeatherImporter as WeImp
from astroplan import Constraint
from datetime import datetime, timedelta, timezone

#TODO: Make this class inherit from our Dynamic_Constraint class?

class WeatherConstraint(Constraint):
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

	def __init__(self, start_time, end_time):
		"""Custom dynamic constraint that evaluates current weather conditions
		
		"""
		today_date = datetime.utcnow().date()
		start_datetime = datetime.strptime(start_time,'%Y-%m-%d %H:%M')
		end_datetime = datetime.strptime(end_time, '%Y-%m-%d %H:%M')
		start_date = start_datetime.date()
		end_date = end_datetime.date()
		delta = end_date - start_date
		today_delta = end_date - today_date
		self.days = delta.days
		self.start_time = start_datetime.time()
		self.end_time = end_datetime.time()
		self.start_date = start_date
		self.end_date = end_date
		if today_delta.days == 0:
			self.start_today = True
		else:
			self.start_today = False


	def compute_constraint(self,times,observer,targets):
		"""

		"""
		# Check if schedule is only for current day
		if self.start_today & self.days == 0:
			weatherInfo = WeImp.getWeather()
			# Check if location is CFHT
			try:
				assert weatherInfo[0] == 'Volcano', "Incorrect location, please try again"
			except AssertionError as e:
				print(e)

			# If weather is clear, observation is possible
			if weatherInfo[1] == 'Clear':
				return True
			# If weather is cloudy observation only possible under specified threshold
			elif weatherInfo[1] == 'Clouds':
				if weatherInfo[4] <= 50.0:
					return True
				else: 
					return False
			# If weather is rainy, observation only possible with very minimal cloud coverage
			elif weatherInfo[1] == 'Rain':
				if weatherInfo[4] <= 15.0:
					return True
				else:
					return False
			# Otherwise weather is too severe for any kind of observation
			else:
				return False

		# Checks for when schedule is for a single day in the future
		elif self.days == 0:
			today = datetime.utcnow().date()
			delta = end_date - today
			# If schedule starts more than 5 days away from current date, ignore weather as no forecast is available
			if delta.days > 5:
				return True
			# Otherwise day being scheduled has to be retrieved from weather data imported
			else:
				weatherInfo = WeImp.getWeather(days=delta.days)
				sched_day = weatherInfo[delta.days]
				# Collect day's overall cloud coverage to be used later to compute avg cloud coverage for the day
				cc_sum = 0
				# Go through the hour intervals 
				for interval in sched_day:
					if interval['Time'] <= self.end_time:
						cc_sum += interval['Cloud Coverage']
				#Calculate day's average cloud coverage
				cc_avg = cc_sum/len(sched_day)
				# If cloud coverage 
				if cc_avg < 40.0:
					return True
				else:
					return False
		#ToDo:
		else:
			return True






		#TODO: High humidity may also have an effect on viewing capabilities
		# considering expanding this constraint to accomodate this fact


#Simple smoke test. Robust tests incoming

start_time = "2019-07-04 19:00"
end_time = "2019-07-04 23:00"
constraint = WeatherConstraint(start_time, end_time)




