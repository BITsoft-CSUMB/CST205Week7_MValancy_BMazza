"""
School: CSU, Monterey Bay
Course: CST 205 Multimedia Design and Programming
Instructor: Allie Xiong
Assignment: Lab #15: Python Standard Library
Authors: Matthew Valancy (Crenshaw) & Brittany Mazza
Date: December 9-15, 2015
Filename: lab15.py
Python Version: 2.2.1 (JES 4.3)
Version: 1
"""


from random import randint
import datetime
import calendar
random.seed()


def playCraps():
  """
  Play a simple craps game. User can either "roll" or "quit". The rolled
  values determine how the game is played out.
  """
  playing = True
  win = False
  firstRoll = True
  point = 0
  while playing:
    instruction = raw_input('Would you like to roll or quit? ').lower()
    if 'q' in instruction or 'quit' in instruction:
      printNow('Thanks for playing!')
      return
    if 'roll' not in instruction:
      printNow('Invalid entry. Specify \"roll\" or \"quit\".')
      continue
    dice = randint(2, 12)
    if firstRoll:
      firstRoll = False
      if dice in [7, 11]:
        win = True
        playing = False
        printNow("You rolled a " + str(dice) + ". You win!")
        continue # Automatically won.
      elif dice in [2, 3, 12]:
        playing = False
        printNow("You rolled a " + str(dice) + ". You lose.")
        continue # Automatically lost. boo :(
      else:
        point = dice
        printNow("You rolled a " + str(dice) + ". Keep going.")
    else:
      if dice == 7:
        playing = False
        printNow("You rolled a " + str(dice) + ". You lose.")
        continue # Player lost
      if dice == point:
        playing = False
        win = True
        printNow("You rolled a " + str(dice) + ". You win!")
        continue
      else:
        printNow("You rolled a " + str(dice) + ". Keep going.")
        continue


# problem 2a - Print out a calendar of the month you were born
def showBdayInfo():
  """
  Show the calendar of the month the user was born in, as well as the
  countdown until their next birthday.
  """
  year = int(raw_input("What year were you born (YYYY format)? "))
  month = int(raw_input("What month were you born (MM format)? "))
  day = int(raw_input("What day were you born (DD format)? "))
  birthdate = datetime.date(year, month, day)
  bdayCalendar(birthdate)
  bdayCountdown(birthdate)


def bdayCalendar(birthday):
  """
  Show the calendar for the month of the year the user was born.
  """
  print "__Your Birthday Month:__"
  calendar.prmonth(birthday.year, birthday.month)


# problem 2b - Tell you how many days it is until your next birthday
def bdayCountdown(birthday):
  """
  Display number of days until the next birthdate.
  """
  printNow("Birthday countdown.")
  today = datetime.datetime.now()
  nextBirthdayYr = birthday.year # initialize bday in the past

  if birthday.month < today.month:
    nextBirthdayYr = today.year + 1
  elif birthday.month == today.month:
    if birthday.day > today.day:
      nextBirthdayYr = today.year
    else:
      nextBirthdayYr = today.year + 1
  else:
    nextBirthdayYr = today.year

  nextBirthday = datetime.date(nextBirthdayYr, birthday.month, birthday.day)
  daysTilNextBday = (nextBirthday - today).days
  print "There are %s days until your next birthdate." % daysTilNextBday


# problem 2C - What day of the week was the Declaration of Independence
# ratified by the Continental Congress?
def independenceDayOfWeek():
  """
  Display what day of the week the Declaration of Independence was signed on.
  """
  dayName = calendar.day_name[calendar.weekday(1776,7,4)]
  print "The Declaration of Independence was signed on a %s." % dayName
