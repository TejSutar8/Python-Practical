# Program to print current date in given format

from datetime import datetime

# Get current date and time
now = datetime.now()

# Format: "Sun May 29 02:26:23 IST 2017"
formatted_date = now.strftime("%a %b %d %H:%M:%S IST %Y")

print("Current date and time:", formatted_date)
