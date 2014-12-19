import os
import requests
from time import sleep


if __name__ == '__main__':
    while True:
      # ping all my sites
      for project, url in os.environ.items():
        if url.startswith('http'):
            res = requests.get(url)
            print 'GET %s' % url
            print '  HTTP %d' % res.status_code
      # sleep io
      sleep(60 * 30)
