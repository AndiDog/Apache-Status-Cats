#!/usr/bin/env python
import urllib

def download(filename, url):
    with open(filename, "wb") as output:
        input = urllib.urlopen(url)
        try:
            output.write(input.read())
        finally:
            input.close()

download("503.jpg", "http://blog.stackoverflow.com/wp-content/uploads/error-lolcat-problemz.jpg")