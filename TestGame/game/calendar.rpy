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

    import random

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
            if (self.week <= 15):
                return 1
            if (15 < self.week <= 30):
                return 2
            if (30 < self.week <= 45):
                return 3

        def month(self):
            if (self.week < 4):
                return "January 2020"
            elif (self.week < 8):
                return "February 2020"
            elif (self.week < 12):
                return "March 2020"
            elif (self.week < 16):
                return "April 2020"
            elif (self.week < 20):
                return "May 2020"
            elif (self.week < 24):
                return "June 2020"
            elif (self.week < 28):
                return "July 2020"
            elif (self.week < 32):
                return "August 2020"
            elif (self.week < 36):
                return "September 2020"
            elif (self.week < 40):
                return "October 2020"
            elif (self.week < 44):
                return "November 2020"
            elif (self.week < 46):
                return "December 2020"
            else:
                return "None"

        def next(self, focus_choice):
            self.week += 1
            rangea, rangeb = character.getLevelRange() # Get range of randomly generated number depending on player level

            # Set up values to be added
            exp_add = 0
            stress_add = 0
            product_add = 0
            skills_add = 0

            # Get previous character metric values
            exp_old = character.exp
            stress_old = character.stressLvl
            product_old = character.product
            skills_old = character.skills

            # Add numbers to character metrics
            character.exp = character.exp + 300 # EXP
            exp_add = exp_add + 300

            random_stress = random.randint(1, 5) # Stress
            character.stressLvl = character.stressLvl + random_stress
            stress_add = stress_add + random_stress

            random_product = random.randint(rangea, rangeb) # Productivity
            character.product = character.product + random_product
            product_add = product_add + random_product

            random_skill = random.randint(rangea, rangeb) # Technical Skills
            character.product = character.product + random_skill
            skills_add = product_add + random_skill

            if((self.week % 2) == 0): # Money Generation Bi-weekly
                character.money= character.money + 0

            # Add weekly choice based on user choice
            if (focus_choice == 1):
                character.exp = character.exp + 200
                exp_add = exp_add + 200
            if (focus_choice == 2):
                character.stressLvl = character.stressLvl - 10
                stress_add = stress_add - 10
            if (focus_choice == 3):
                character.skills = character.skills + random_product
                skills_add = skills_add + random_skill
            if (focus_choice == 4):
                character.product = character.product + random_skill
                product_add = product_add + random_product
            #if (focus_choice == 5):


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
        xsize 210     # Pixel Size
        ysize 220     #
        xmargin .05   # Leave some transparent space around the box.
        ymargin .05   #
        xpadding .15  # Leave some unused space between the box and its contents.
        ypadding .09  #

        vbox:  # Arranges the things in it vertically.
            xalign 0.5
            text calendar.string() size 28 xalign 0.5    # Big text with the date in center of the box.
            hbox xalign 0.5:  # Arranges the things in it horizontically.
                text "Part " + str(calendar.part()) size 10 xalign 0.5
                text calendar.month() size 10  # Smallish texts with monthname and year in the center of the box.
                spacing 8 # Makes sure there's a space between the two text-items, so that it doesn't read 'august2014' but 'august 2014'.
            text "" size 10
            text "Level 1" size 16 xalign 0.5 #character.level
            text "Exp Points: " + str(character.exp) + " / 1,000" size 10 xalign 0.5 #character.exp.get()
            text "Technical Skills: " + str(character.skills) size 12 xalign 0.5 #character.skill
            text "Productivity: " + str(character.product) size 12 xalign 0.5 #character.product.get()
            text "Stress: " + str(character.stressLvl) size 12 xalign 0.5 #character.stressLvl.get()
            text "" size 4
            text "$" + str(character.money) size 14 xalign 0.5
            spacing 2
