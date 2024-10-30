# In order to work with API some tools are required such as requests so we need to first install them in our system.
# Command to install requests: 'pip3 install requests'
#once we have it installed, we need to import it into our code using 'import requests'

import requests

# APIs use many different request types.
# GET, the most common type, retrieves data.
# We'll focus on GET requests since we're just working on retrieving data for now.

# When we make an API request, the response includes a status code that tells us whether the request was successful.
# Status codes are important for immediately identifying if something went wrong.
# To make a GET request, we use the requests.get() function, passing in the URL we want to request.
# Let's start by requesting an API endpoint that doesn't exist, so we can see what an error status code looks like:

#----
# response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
# print(response.status_code)
#----

# The 404 status code is probably familiar - it's what a server returns when it can't find the requested file.
# Here, we asked for this-api-doesnt-exist which (unsurprisingly) didn't exist!

# In the following request you will see status_code 200, which means everything went well
# and (if there is any) the data will have been returned.
# This is the most common code you will receive because most of the time you will successfully connect.

#----
# response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu/")
# print(response.status_code)
#----

# If we replace status_code with text, we will get a formatted string we can use.
# It being a string means we cannot pull any data from it just yet.

#----
# response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu/")
# print(response.text)
#----

# You can see that the output gives us something that closely resembles a dictionary in python.
# It is not yet a dictionary, it is JSON.
# You can see " KEY : 'VALUE' "
# We will be using a certain function to convert this JSON text into an actual python dictionary so that we can use
# the information

#----
# response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu/")
# pikachu = response.json()
# print(pikachu['weight'])
#----

# In the code above we have made a new variable named pikachu.
# In pikachu we put response.json()
# This transforms JSON into a python dict. This function is part of the requests import.
# Then with pikachu['weight'] we now get the value of the key weight which is 60
# We extracted the value out of the API, great success!
