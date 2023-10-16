"""
Hit Counter Service

Start the Hit Counter Service and initializes logging
"""
import os
from hitcounter import app, routes

# Pull options from environment
DEBUG = os.getenv("DEBUG", "False") == "True"
PORT = os.getenv("PORT", "8080")

######################################################################
#   M A I N
######################################################################
if __name__ == "__main__":
    print("".center(70, "*"))
    print("  H I T   C O U N T E R   S E R V I C E ".center(70, "*"))
    print("".center(70, "*"))
    app.run(host="0.0.0.0", port=int(PORT), debug=DEBUG)
