from tso.importer.weather_importer import WeatherImporter
import pytest

class TestWeatherImporter():


	def test_location(self):
		weather = WeatherImporter.getWeather()
		assert weather[0] == "Volcano"

	def test_current_weather(self):
		weather = WeatherImporter.getWeather(days=0)
		assert len(weather) == 5

	def test_current_weather_info(self):
		conditions = ['Thunderstorm', 'Drizzle', 'Rain', 'Snow', 'Atmosphere', 'Clear', 'Clouds']
		weather = WeatherImporter.getWeather(days=0)
		assert weather[1] in conditions
		assert isinstance(weather[3],int)
		assert isinstance(weather[4], float)

	def test_future_weather(self):

		for n in range(1,6):
			weather = WeatherImporter.getWeather(days=n)
			assert len(weather) == (n+1)

	#def test_future_weather_info(self):


