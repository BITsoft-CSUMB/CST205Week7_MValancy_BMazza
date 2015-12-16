"""
School: CSU, Monterey Bay
Course: CST 205 Multimedia Design and Programming
Instructor: Allie Xiong
Assignment: Lab #16: URLs and HTML
Authors: Matthew Valancy (Crenshaw) & Brittany Mazza
Date: December 9-15, 2015
Filename: lab16.py
Python Version: 2.2.1 (JES 4.3)
Version: 1
"""
import urllib


# Part 1 (Written by professor)
# Slight alteration made to pass "path" in.
def makePage(path):
  file = open(path + "/superweb.html", "wt")
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  <body>
  <h1>MY PYTHON PAGE!!!</h1>
  </body>
  </html>""")

  file.close()


# Part 2
def aggPage(htmlFilePath):
  """
  Aggregate data from path and add the data to the specified html file.
  """
  htmlContent = urllib.urlopen('https://www.reddit.com/r/twitter').read()
  matchString = '<p class=\"title\">'
  matchStringLen = len(matchString)
  collectedData = []

  done = False
  index = 0 # moving index searching for titles
  while not done:
    # what we are looking for is inbetween > and </a> at the end after a <p class="title"> is found
    index = htmlContent.find(matchString, index)
    if index == -1:
      done = True
      continue

    endindex = htmlContent.find("</a>", index)
    titleStart = htmlContent.rfind(">", index, endindex) + 1
    match = htmlContent[titleStart:endindex]

    collectedData.append(match)
    index = endindex

  output = ""
  for data in collectedData:
    output += data + "<br>"
  htmlFile = open(htmlFilePath + "output.html", "a+")
  htmlFile.write(output)
  htmlFile.close()
