# Question2:
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a
# dictionary of information about each city and include the country that the city is in, its approximate
# population, and one fact about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information you have stored
# about it.
cities = { 
    "Karachi":{"country":"Pakistan","popullation":"16 million","fact":"cheapest city of the world"},
    "London":{"country":"England","popullatin":"9 million","fact":"smallest city of England"},
    "Islamabad":{"country":"Pakistan","popullation":"1 million","fact":"capital of Pakistan"}}
a = input("enter any city name:").title()
print(cities[a])