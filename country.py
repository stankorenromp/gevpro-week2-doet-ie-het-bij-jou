from flag_color import *

#Class to create a country object with a name and color attribute.
class Country:

	def __init__(self, name, FlagColor):
		self.name = name
		self.FlagColor = FlagColor
		
	def getName(self):
		return self.name

	def __str__(self):
		return 'Hello from ' + self.name 
	
	def getKleuren(self):
		return self.FlagColor
        
#Function which reads countries_list.txt and returns a list with country-objects.
def readcountry():
	file = open('countries_list.txt', 'r')
	countrylist = []
	for country in file:
		vlag = FlagColor()
		rood,groen,blauw = vlag.SetColor()
		kleuren = QColor(rood,groen,blauw)
		strippedcountry = country.strip("\n")
		countryobject = Country(strippedcountry, kleuren)
		countrylist.append(countryobject)
	
	return countrylist


