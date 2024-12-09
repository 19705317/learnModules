import os
import sys # gives us the current paths important to the Python interpreter
import datetime # gives us today's date
import requests




cpu_cores = os.cpu_count()
print(cpu_cores)

print(f"Current path: {sys.path}")
print(sys.version)

print(f"Today's date: {datetime.date.today()}")

request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc.status_code)
print(request_bbc.content)