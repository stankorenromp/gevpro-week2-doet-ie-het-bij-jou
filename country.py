class Country:

    def __init__(self, name):
        self.name=name

    def __str__(self):
        return 'Hello from ' + self.name 
        
    def readcountry():
    	file = open('countries_list.txt', 'r')
    	countrylist = []
    	for country in file:
    		countrylist.append(country)
        return countrylist
        
def main():
	countrylist = readcountry()
	print(countrylist)
    
if __name__ == "__main__":
	main()

