from gettext import lngettext
import phonenumbers
from myphone import myNumber
from phonenumbers import carrier
from phonenumbers import geocoder

import folium

# separate phone number into parts
number = phonenumbers.parse(myNumber)
print(number)

# extract country location
location = geocoder.description_for_number(number, "en")
print(location)


# validate phone number
valid = phonenumbers.is_valid_number(number)
possible = phonenumbers.is_possible_number(number)

print("Is this a valid number? (True or False): ", valid)
print("Is this a possible number? (True or False): ", possible)


from opencage.geocoder import OpenCageGeocode

# API key
Key = "e7f6456637f5484aa9efac4a35a3519e"

geocoder1 = OpenCageGeocode(Key)
query = str(location)

results = geocoder1.geocode(query)
# print(results)

# get lat, long location from API
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print("Latitude: ", lat,", Longitude: ", lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng], popup = location).add_to((myMap))

# save map to HTML file
myMap.save("location.html")