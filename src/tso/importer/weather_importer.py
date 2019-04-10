import requests
from datetime import datetime, timedelta, timezone
from pytz import timezone
from astropy.table import Table


class WeatherImporter():

    def getWeather(lat='19.49', lon='-155.28', days = 5):
        """Retrieves and returns valuable weather conditions for astrological viewing

        This method uses the open weather API to access real time meteorological
        conditions for a desired location.

        Parameters
        ----------
        lat: str, optional
            Latitude of desired location. Default is latitude for CFHT
        lon: str, optional
            Longitude of desire location. Default is longitude for CFHT
        days: int, optional
            Specifies number of days forecast information will be collected for. Default is 0 which retrieves only current weather data
            Limited to max 5 days.

        Returns
        -------
        list:
            If days=1 list of size 5 and contains (Location Name, Current Condition, Visibility, humidity and Cloud coverage)
            Otherwise returns list of size days + 1. Where all elements except the first are lists of dictionaries. Each of these
            lists represent a one day forecast. Info for these forecasts are every 3 hours and this info is stored in
            each dictionary.

        """
        weatherRows = []
        weatherInfo = []
        if days == 0:

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

        else:
            url = 'http://api.openweathermap.org/data/2.5/forecast?appid=086d1c78483ff520ad56869bf76e2423&lat=' +lat + '&lon=' + lon + '&units=metric'
            json_data = requests.get(url).json()
            loc_Name = json_data['city']['name']
            weatherInfo.append(loc_Name)
            data_list = json_data['list']
            # Set up current local time used for comparisson later
            t = datetime.now()
            tz = timezone("US/Hawaii")
            t1 = tz.localize(t)
            today = t1.date()
            #Makes a list of weather info for each day
            for n in range(days):
                dates_list = []

                # Make a Dictionary entry for each 3 hour interval in a day
                for i in data_list:
                    currentDict = {}
                    ts = i['dt']
                    date = datetime.utcfromtimestamp(int(ts)).date()
                    time = datetime.utcfromtimestamp(int(ts)).time().strftime('%H:%M:%S')

                    # Formatting all of tomorrow's weather
                    if n == 0:
                        if date == today + timedelta(days=1):
                            currentDict["Date"] = date.strftime('%Y-%d-%m')
                            currentDict["Time"] = time
                            currentDict["Weather"] = i['weather'][0]['main']
                            currentDict["Humidity"] = i['main']['humidity']
                            currentDict["Cloud Coverage"] = i['clouds']['all']
                            dates_list.append(currentDict)
                            weatherRows.append((currentDict["Date"], currentDict["Time"], currentDict["Weather"], currentDict["Humidity"], currentDict["Cloud Coverage"]))



                    # Formatting all weather info for two days from now
                    elif n == 1:
                        if date == today + timedelta(days=2):
                            currentDict["Date"] = date.strftime('%Y-%d-%m')
                            currentDict["Time"] = time
                            currentDict["Weather"] = i['weather'][0]['main']
                            currentDict["Humidity"] = i['main']['humidity']
                            currentDict["Cloud Coverage"] = i['clouds']['all']
                            dates_list.append(currentDict)
                            weatherRows.append((currentDict["Date"], currentDict["Time"], currentDict["Weather"], currentDict["Humidity"], currentDict["Cloud Coverage"]))



                    # Formatting all weather info for three days from now
                    elif n == 2:
                        if date == today + timedelta(days=3):
                            currentDict["Date"] = date.strftime('%Y-%d-%m')
                            currentDict["Time"] = time
                            currentDict["Weather"] = i['weather'][0]['main']
                            currentDict["Humidity"] = i['main']['humidity']
                            currentDict["Cloud Coverage"] = i['clouds']['all']
                            dates_list.append(currentDict)
                            weatherRows.append((currentDict["Date"], currentDict["Time"], currentDict["Weather"], currentDict["Humidity"], currentDict["Cloud Coverage"]))



                    # Formatting all weather info for four days from now
                    elif n ==3:
                        if date == today + timedelta(days=4):
                            currentDict["Date"] = date.strftime('%Y-%d-%m')
                            currentDict["Time"] = time
                            currentDict["Weather"] = i['weather'][0]['main']
                            currentDict["Humidity"] = i['main']['humidity']
                            currentDict["Cloud Coverage"] = i['clouds']['all']
                            dates_list.append(currentDict)
                            weatherRows.append((currentDict["Date"], currentDict["Time"], currentDict["Weather"], currentDict["Humidity"], currentDict["Cloud Coverage"]))


                    else:
                        if date == today + timedelta(days=5):
                            currentDict["Date"] = date.strftime('%Y-%d-%m')
                            currentDict["Time"] = time
                            currentDict["Weather"] = i['weather'][0]['main']
                            currentDict["Humidity"] = i['main']['humidity']
                            currentDict["Cloud Coverage"] = i['clouds']['all']
                            dates_list.append(currentDict)
                            weatherRows.append((currentDict["Date"], currentDict["Time"], currentDict["Weather"], currentDict["Humidity"], currentDict["Cloud Coverage"]))

                weatherInfo.append(dates_list)

            weatherTable = Table(rows=weatherRows, names=('Date', 'Time', 'Weather', 'Humidity', 'Cloud Coverage'))
            print('\n\t\t--- WEATHER SUMMARY ---\n', weatherTable, '\n')
            return weatherInfo



#conditions = ['Thunderstorm', 'Drizzle', 'Rain', 'Snow', 'Atmosphere', 'Clear', 'Clouds']
# weather = WeatherImporter.getWeather(days=5)
# print(weather)
#   print ("n = " + str(n) + " Length = " + str(len(weather)))





