
import opencage
import phonenumbers
from phonenumbers import geocoder
from phoneNumber import Number
import folium

pepnumber = phonenumbers.parse(Number)
location = geocoder.description_for_number(pepnumber, 'en')
print(location)

from phonenumbers import carrier
service_provider = carrier.name_for_number(pepnumber, 'en')
from opencage.geocoder import OpenCageGeocode

key = 'a0f2ec5bb4bf471e920cd3fa0ff27790'

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
# print (result)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=4)
folium.Marker([lat, lng], popup= location).add_to(myMap)

myMap.save('myMap.html')