import os
import requests
from time import sleep

while True:
  # ping all my sites
  [requests.get(url) for project, url in os.environ.items() if url.startswith('http')]
  # sleep io
  sleep(60)
