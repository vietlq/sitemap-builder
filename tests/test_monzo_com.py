#!/usr/bin/env python3

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        print("The attributes: ", attrs)

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass

parser = MyHTMLParser()
with open('tests/test_monzo_com.html', 'rb') as fh:
    monzo_com_html = fh.read().decode('utf-8')
parser.feed(monzo_com_html)
