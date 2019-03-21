import requests 



def getWeather(lat='19.49', lon='-155.28'):
	"""Retrieves and returns valuable weather conditions for astrological viewing

	This method uses the open weather API to access real time meteorological 
	conditions for a desired location. 

	Parameters
	----------
	lat: str, optional
		Latitude of desired location. Default is latitude for CFHT
	lon: str, optional
		Longitude of desire location. Default is longitude for CFHT

	Returns
	-------
	list 
		A list of size 5 and contains (Location Name, Current Condition, Visibility, humidity and Cloud coverage)

	"""
	weatherInfo = []
	url = ' http://api.openweathermap.org/data/2.5/weather?appid=086d1c78483ff520ad56869bf76e2423&lat='+lat+'&lon='+lon+'&units=metric'
	json_data = requests.get(url).json()
	loc_Name = json_data['name']
	weatherInfo.append(loc_Name)
	current_condition = json_data['weather'][0]['main']
	weatherInfo.append(current_condition)
	if 'visibility' not in json_data:
		current_visibility = 'NA'
	else:
		current_visibility = int(json_data['visibility'])
	weatherInfo.append(current_visibility)
	current_humidity = json_data['main']['humidity']
	weatherInfo.append(int(current_humidity))
	cloud_coverage = json_data['clouds']['all']
	weatherInfo.append(float(cloud_coverage))
	return weatherInfo


		






