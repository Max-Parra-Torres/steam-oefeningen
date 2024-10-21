# In order to work with API some tools are required such as requests so we need to first install them in our system.
# Command to install requests: 'pip3 install requests'
#once we have it installed, we need to import it into our code using 'import requests'

import requests
import json

# APIs use many different request types.
# GET, the most common type, retrieves data.
# We'll focus on GET requests since we're just working on retrieving data for now.

# When we make an API request, the response includes a status code that tells us whether the request was successful.
# Status codes are important for immediately identifying if something went wrong.
# To make a GET request, we use the requests.get() function, passing in the URL we want to request.
# Let's start by requesting an API endpoint that doesn't exist, so we can see what an error status code looks like:

response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print(response.status_code)

# The 404 status code is probably familiar - it's what a server returns when it can't find the requested file.
# Here, we asked for this-api-doesnt-exist which (unsurprisingly) didn't exist!

