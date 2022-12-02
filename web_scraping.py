import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.00606000000005&lon=-75.29093999999998#.YHC8YuhKjIU')
soup = BeautifulSoup(page.content, 'html.parser')


week = soup.find(id= 'seven-day-forecast')
# print(week)

items = (week.find_all(class_='tombstone-container'))

# print(items[0])


# print(items[0].find(class_='period-name').get_text())

# print(items[0].find(class_='short-desc').get_text())

# print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
print(period_names)

short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
print(short_descriptions)

temperatures = [item.find(class_='temp').get_text() for item in items]
print(temperatures)


# now to use pandas

weather_staff = pd.DataFrame(
    {
        'period': period_names,
        'short_descriptions': short_descriptions,
        'temperatures': temperatures,

    })

print(weather_staff)

weather_staff.to_csv('weather.csv')


print('amogus')







