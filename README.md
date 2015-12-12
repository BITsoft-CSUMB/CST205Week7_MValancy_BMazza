# Lab #15: Python Standard Library (2 hours)

This is a pair project. Work with ONE partner. If you are working in a group of four, divide into two groups of two. If you have a group of three, it's ok to keep the size as three members. Each pair creates one product collaboratively, each student submit identical product using their iLearn account.

Let's learn about the Python Standard Library.

http://docs.python.org/library/

Getting familiar with how to use the standard library and to read the documentation is a really important part of learning any new programming language. This week we'll be learning how to use the Python Standard Library to read and write html in more detail. The goal of today's lab is to get familiar with how to use the documentation to find the functions you need. This lab is also a little shorter to give you some time to catch up on previous labs.

## Problem 1:

Use a function from the random library to simulate rolling dice. Write a function that rolls a single die and then use that function to build a program that let's the user play craps. The basic rules of craps are:

1. A player rolls two six-sided dice and adds the numbers rolled together.
2. On this first roll, a 7 or an 11 automatically wins, and a 2, 3, or 12 automatically loses, and play is over. If a 4, 5, 6, 8, 9, or 10 are rolled on this first roll, that number becomes the "point.”
3. The player continues to roll the two dice again until one of two things happens: either they roll the "point" again, in which case they win; or they roll a 7, in which case they lose.

Playing craps can include a number of variations on this game, and also typically involves betting on various outcomes; those aspects of the game are not required for this lab, however have some fun writing this game.

## Problem 2:

Have some fun with different library functions by figuring out how to get Python to:

* Print out a calendar of the month you were born
* Tell you how many days it is until your next birthday
* What day of the week was the Declaration of Independence ratified by the Continental Congress? (write a program that prints out Monday, Tuesday, etc)

# Lab #16: URLs and HTML (3 hours)

This is a pair project. Work with ONE partner. If you are working in a group of four, divide into two groups of two. If you have a group of three, it's ok to keep the size as three members. Each pair creates one product collaboratively, each student submit identical product using their iLearn account.

HTML (hypertext markup language) is how we format text for the web. In Python we can both process existing HTML and create our own. Today's lab gives you a chance to do both. You'll be mining an existing webpage for data to create your own (simpler page). 

## First: The basics of writing html
A lot of you probably have some familiarity with html. Also, there is an [html tutorial on Code Academy](https://www.codecademy.com/courses/web-beginner-en-HZA3b/0/1?curriculum_id=50579fb998b470000202dc8b) that will give you the basics. (<- HELPFUL LINK)

For this class, the webpages we create will be straight out of the early 90s. Black text on a white background with a few images. Fancy webpages will include colored text and layout with tables!

To write a webpage, you need to:

1. Create a file named with an .html extension (I am going to call mine superweb.html)
2. Open the file for writing: file = open("superweb.html", "wt")
3. Use the file.write() command to write out strings with the html needed to build your page
4. When you are done, open your .html file using a web browser to check out your new page
5. Of course, you'll want to use functions to organize your code or you'll just end up with one super-long write command (not a good idea).

Here is an example of the simplest page you could write. (You may have to specify the full path the html file)

```python
def makePage():
  file = open("superweb.html", "wt")
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
```

Go ahead and copy this code into JES. Run the function and look at the page created. Make sure you understand how it is working

## Scraping HTML from existing sites

In the headline lab, we saved a local, static copy of the Otter Realm website to get the featured headlines. But the web is always changing so we'd like to be able to get live data from the current version of a website. Luckily the [urllib module](https://docs.python.org/2/library/urllib.html) let's us open, read and then close a URL. 

## The Lab
Ok, now that we can read from a URL, get data out of the html (Just like in the headline lab), and write a page, we can finally get started on the lab itself. For today's lab

1. Choose a website that you frequent that has data (text) that could be scraped from it's HTML (this could be Facebook, CNN, Kitty Pictures, whatever)
2. Write some code that collects at least 10 pieces of information from the webiste (e.g. friends from Facebook, or headlines from CNN, comments on kitty pictures, etc)
3. Create a new web page that displays ONLY the information you collected in step 2

The page you create can be very simple. You only need to display the information in a readable format. No fancy formatting required ... we'll save that for next time :) To get checked off, be prepared to show:

1. The original website you got your data from
2. Your code
3. Your resulting html page that you created
