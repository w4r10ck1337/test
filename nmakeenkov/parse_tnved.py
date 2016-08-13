#!/usr/bin/python3
import sys
from html.parser import HTMLParser

class HtmlGetter(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.waiting_for_data = 0
    self.result = []

  def handle_starttag(self, tag, attrs):
    if tag == 'span':
      for attr in attrs:
        if attr[0] == 'id':
          if attr[1].startswith('clipData'):
            self.waiting_for_data = 2
            self.result.append([])

  def handle_data(self, data):
    if self.waiting_for_data:
      data = data.strip()
      if len(data):
        self.result[-1].append(data)
        self.waiting_for_data -= 1


def main():
  with open('tnved.html', 'r') as f:
    text = f.read()
    parser = HtmlGetter()
    parser.feed(text)
    with open('tnved.csv', 'w') as tnved:
      print("id\tname", file=tnved)
      for x in parser.result:
        if len(x) == 2:
          print("{}\t{}".format(x[0], x[1]), file=tnved)

if __name__ == '__main__':
  main()
