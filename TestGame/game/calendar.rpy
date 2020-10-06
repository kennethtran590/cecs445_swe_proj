######################################################
#  Section for initialization through Python
#
init python:

    # Import the date-module from the python package 'datetime'.
    # There's more things in the datetime package, but we're not using those so there's no need to import them.
    # The date-module contains functions for calculating with dates, and converting them to and from strings.
    from datetime import date

    # Import the locale package, which has data structures for keeping locale settings, i.e. which country this
    # computer is in and what language settings should be used.
    # Also, notably, the local names of the days and months.
    import locale

    # Find out what day it is.
    today = date.today()

    # Find out where we are and which language should be used.
    locale.setlocale(locale.LC_ALL, '')

    # Set a local data structure (here, a dictionary containing key-value pairs) to store
    # the strings we need to display the calendar.
    # Things like the date and year, and the name of the day and month.
    # More options available.. See strftime.org, or search for 'python strftime' if that site have disappeared since I wrote this.
    date_inf = {    "day": today.strftime("%A"),
                    "daynr": today.strftime("%d"),
                    "month": today.strftime("%B"),
                    "year": today.strftime("%Y")
                }


    class Calendar():
        '''Provides time-related information based on a sequence of day names.
        Most class methods take a daycount parameter, which is assumed to be a count
        of passed days, starting with 1 for the first day.
        newmoonday is the daycount of the first new moon, e.g. 1 for the first
        day.
        Provides date based on different logic (counter).
        '''
        def __init__(self, week=1):
            self.week = week

        def string(self):
            return ("Week " + str(self.week))

        def part(self):
            if (self.week < 15):
                return 1
            if (15 <= self.week <= 30):
                return 2
            if (30 < self.week <= 45):
                return 3

        def next(self):
            self.week += 1

    calendar = Calendar()


#  Define how the calendar should look, using Ren'Py's Screen Language.
#  This section would normally be placed in screens.rpy, but if you're
#  me, for the moment you'd rather have something to copy-paste, and test, and play around with.
screen calendar(date_inf):

    # Don't stop the user from interacting with other things - this screen is just showing stuff.
    modal False

    # The section of screen to which we'll place the rest.
    frame:
        xalign 1.0    # Place in the upper-right corner.
        yalign 0.0    #
        xsize 250     # Make it 100x100 pixels.
        ysize 100     #
        xmargin .05   # Leave some transparent space around the box.
        ymargin .05   #
        xpadding .15  # Leave some unused space between the box and its contents.
        ypadding .15  #

        vbox:  # Arranges the things in it vertically.
            text calendar.string() size 40 xalign 0.5    # Big text with the date in center of the box.
            hbox:  # Arranges the things in it horizontically.
                text "Part " + str(calendar.part()) size 12 xalign 0.5
                text date_inf["month"] size 12 xalign 0.5  # Smallish texts with monthname and year in the center of the box.
                text date_inf["year"] size 12 xalign 0.5   # ..and under the date because the hbox is the second item in the vbox.
                spacing 10 # Makes sure there's a space between the two text-items, so that it doesn't read 'august2014' but 'august 2014'.
