# 3. Write a Python script to print the current date in following format "Sun May 29 02:26:23 IST 2017"
import datetime
import time

def print_formatted_date():
    now = datetime.datetime.now()
    # Format: Day Mon DD HH:MM:SS IST YYYY
    formatted = now.strftime('%a %b %d %H:%M:%S IST %Y')
    print(formatted)

if __name__ == "__main__":
    print_formatted_date()
