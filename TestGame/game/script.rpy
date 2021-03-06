# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# CHARACTERS
define sylvie = Character("Sylvie")
define eileen = Character("Eileen")
define bosses = Character("Bosses")
define system = Character("")
define r = Character("Sylvie")
define m = Character("Mentor")
define a = Character("Adrian")

# IMAGES

image mentor_happy = "KG110001.kg.png"
image mentor_slight_happy = "KG110002.kg.png"
image mentor_surprise = "KG110013.kg.png"
image mentor_smile_closeup = "KG110032.kg.png"
image mentor_smiling = "KG110042.kg.png"
image mentor_shock = "mentor shocked.png"

image main_concerned = "eileen concerned.png"
image main_happy = "eileen happy.png"
image main_v_happy = "eileen vhappy.png"

image presentation_2 = "cropped_presentation.jpg"
image list = "bg_notepad.jpg"

image coworker_happy = "coworker happy.png"
image coworker_cheeky = "coworker cheeky.png"
image coworker_thumbs = "coworker thumbs up.png"
image coworker_sigh = "coworker sigh.png"
image coworker_shirtless = "coworker shirtless.png"

image beach_day = "bg_beach_day.jpg"
image beach_night = "bg_beach_night.jpg"

# INVENTORY
default shop = []
default inventory = []
default equipped = []
default selected_item = None
default selected_shop_item = None
default player = Player(0,0,100,0,0,0)

#Equipment
default keyboard1 = Keyboard("keyboard", 'Razer Ornata', 'Combining a soft touch with a crisp tactile click, the Razer Ornata Chroma presents a mecha-membrane typing experience that’s swift and exact. Plus, it’s incredibly comfortable to use.', 75, 37, 5, 0, 0)
default keyboard2 = Keyboard("keyboard", 'Anne Pro 2', ' This 60% compact keyboard feels very well-built and looks sleek in most computer setups. Every key on it can be fully programmed, and it has fully customizable RGB lighting behind each key.', 125, 62, 10, 0, 0)
default keyboard3 = Keyboard("keyboard", 'Ducky One 2 Mini', 'The bezel design shares a similar sleek frame as its predecessor. They use USB HID with the highest frequency of 1000 Hz polling rate, meaning the keyboard is sending its input signal(s) to your PC 1000 times per second.', 200, 100, 20, 0, 0)
default keyboard4 = Keyboard("keyboard", 'Happy Hacking Keyboard', 'The Happy Hacking Keyboard is a small computer keyboard produced by PFU Limited of Japan, codeveloped with Japanese computer scientist and pioneer Eiiti Wada. Its reduction of keys from the common 104-key layout down to 60 keys in the professional series is the basis for its smaller size while retaining full key size.', 300, 150, 50, 0, 0)

default mouse1 = Mouse("mouse", 'Gaming Mouse V1', 'A mouse with additional functions to make it suited to computer gaming and high intensity programming. Functions include programmable buttons.', 20, 10, 5, 0, 0)
default mouse2 = Mouse("mouse", 'Gaming Mouse V2', 'A mouse with additional functions to make it suited to computer gaming and high intensity programming. Functions include programmable buttons, higher sensitivity.', 35, 17, 10, 0, 0)
default mouse3 = Mouse("mouse", 'Gaming Mouse V3', 'A mouse with additional functions to make it suited to computer gaming and high intensity programming. Functions include programmable buttons, higher sensitivity, adjustable weight and faster response times.', 60, 30, 20, 0, 0)

default chair1 = Chair("chair", 'Wooden Chair', 'A basic plastic lawn chair.', 40, 20, 5, 0, 0)
default chair2 = Chair("chair", 'Office Chair', 'A black leather chair with adequate padding for comfort.', 70, 35, 10, 0, 0)
default chair3 = Chair("chair", 'Gaming Chair', 'A chair designed for the comfort of video game players, having high backrest designed to support the upper back and shoulders.', 130, 65, 15, 0, 0)

default monitor1 = Monitor("monitor", '1080p Monitor', 'A high-definition PC monitor that delivers a visually clear and exciting multimedia experience.', 35, 17, 10, 0, 0)
default monitor2 = Monitor("monitor", '4k Monitor', 'A high-definition PC monitor delivers a visually clear and exciting multimedia experience at a higher resolution for better code viewing.', 60, 30, 30, 0, 0)
default monitor3 = Monitor("monitor", '8k Monitor', 'A high-definition PC monitor delivers a visually clear and exciting multimedia experience at even higher resolution to view even more code.', 110, 55, 75, 0, 0)

#Consumable Items
default coffee = Consumable("coffee", 'Coffee', 'A brewed drink prepared from roasted coffee beans that is a good source of caffeine.', 10, 5, 1.5, 0, 0)
default energy = Consumable("energy", 'Energy Drink', 'A drink containing stimulating compounds, such as caffeine, to heavily restore stamina and improve productivity.', 15, 7, 3, 0, 0)
default rubik = Consumable("rubik", "Rubik's Cube", 'A common puzzle in the form of a plastic cube covered with multicolored squares, which the player attempts to twist and turn so that all the squares on each face are of the same color.', 25, 12, 0, 5, 5)
default fidget = Consumable("fidget", 'Fidget Spinner', 'A toy that consists of a ball bearing in the center of a multi-lobed (typically two or three) flat structure made from metal or plastic designed to spin along its axis with very little effort.', 50, 25, 0, 10, 0)
default candle = Consumable("candle", 'Eucalyptus Candle', 'A candle with a a minty and uplifting smell, eucalyptus helps decongest the nose and provide relief from colds, sinusitis, and allergies. It is emanated also to build energy.', 120, 60, 5, 15, 0)
default intro_code = Book("book", 'Intro to Coding Textbook', 'A textbook providing the fundamental teachings for coding. Can only be purchased once.', 50, 25, 0, 0, 5)
default adv_code = Book("book", 'Intro to Algorithms', 'A textbook providing the fundamental teachings for algorithms. Can only be purchased once.', 100, 50, 0, 0, 10)
default intro_algr = Book("book", 'Advance Coding Textbook', 'A textbook providing advanced techniques and teachings for coding. Can only be purchased once.', 175, 87, 0, 0, 20)
default adv_algr = Book("book", 'Advance Algorithms', 'A textbook providing advanced techniques and teachings for algorithms. Can only be purchased once.', 250, 125, 0, 0, 50)


# The game starts here.
# -------------------------------------------------------------- WEEK 1 ----------------------------------------------------------------
label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg club

    #scene office_background

    # ADD SHOP ITEMS
    $shop.append(keyboard1)
    $shop.append(keyboard2)
    $shop.append(keyboard3)
    $shop.append(keyboard4)

    $shop.append(mouse1)
    $shop.append(mouse2)
    $shop.append(mouse3)

    $shop.append(monitor1)
    $shop.append(monitor2)
    $shop.append(monitor3)

    $shop.append(chair1)
    $shop.append(chair2)
    $shop.append(chair3)
    $shop.append(coffee)
    $shop.append(energy)
    $shop.append(rubik)
    $shop.append(fidget)
    $shop.append(candle)
    $shop.append(intro_code)
    $shop.append(adv_code)
    $shop.append(intro_algr)
    $shop.append(adv_algr)

    show screen calendar(date_inf)
    show screen show_inventory

#---------------------------------------------------------------------------------------------------------------------------------------
# Introduction of the game / Week 1

    scene bg club

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sylvie blue normal:
        xalign 0.0
        yalign 1.0


    # Start by playing some music.
    play music "illurock.opus"

    # Define slow disolve
    define slowDissolve = Dissolve(1.0)

    # These display lines of dialogue.

    sylvie "First day at the new job! I’m so excited to get started."

    show eileen happy:
        xalign 0.75
        yalign 1.0
    with Dissolve(0.5)

    eileen "I’m glad we were able to get hired at the same company Sylvie. I can't wait for our next project"

    sylvie "Did you hear Eileen? The company is looking for a new young developer to launch the new project."

    show eileen concerned
    eileen "Oh no! Here you go again"

    show sylvie blue giggle
    sylvie "That’s right here I go again, I’m taking on “The Big One”"

    sylvie "It's time to get cracking! Let's go ahead and see which developers are being assigned to the big one that way we can go ahead and put our team together and get started working."

    scene office_background

    show sylvie blue normal:
        xalign 0.75
        yalign 1.0
    with Dissolve(0.5)

    show eileen vhappy:
        xalign 0.0
        yalign 1.0
    with Dissolve(0.7)

    eileen "So how are we going to do this?"

    show sylvie blue giggle
    sylvie "Using scrum and agile methodology."

    eileen "What's that?"

    show eileen happy
    show sylvie blue normal
    sylvie "In short, scrum refers to a framework that makes for effective collaborations among teams that are working on complex products.
    Although it is most often used by software development teams, scrum is beneficial to any team that is working toward a common goal."

    sylvie "In particular, scrum is a collection of meetings, roles, and tools
    that work together to help teams to better structure and manage their workload."


    scene team_meeting_room
    show sylvie blue smile
    with slowDissolve

    sylvie "So for our project, I'll be the Scrum master. The scrum master is the facilitator of the scrum development process.
    In addition to holding daily meetings with the scrum team,"

    sylvie "The scrum master makes certain that scrum rules are being enforced and
    applied as intended."


    scene team_meeting_room
    show eileen happy
    with slowDissolve

    sylvie "Eileen you'll be the Product owner, representing
    stakeholders, which are typically customers."

    sylvie "To ensure the scrum team is
    always delivering value to stakeholders and the business, the product owner
    determines product expectations, records changes to the product and administers
    a scrum backlog, a detailed and constantly updated to-do list for the scrum project."

    scene team_meeting_room
    show software_team:
        xalign 0.5
        yalign 0.5
    with slowDissolve

    sylvie "The rest of the developers will be the scrum team. A scrum team
    is a self-organized group of three to nine individuals who have the business,
    design, analytical, and development skills to carry out the actual work, solve
    problems, and produce deliverable products."

    scene office_background
    show sylvie blue normal:
        xalign 0.75
        yalign 1.0

    show eileen happy:
        xalign 0.0
        yalign 1.0
    with slowDissolve

    eileen "So what will you be doing on a week to week basis?"

    #Start tutorial for weekly calendar events

    jump tutorial

#---------------------------------------------------------------------------------------------------------------------------------------
# Tutorial / Week 1

label tutorial:

    scene office_background

    system "Throughout the game, you will advance week by week."

    system "Each week, you will generate a number and it will be added to your character attributes
    that you can see on the top right hand corner."

    "At the start of each week, you will choose a specific area of work to focus in for the week."

    "Your character stats that are generated during the week while you work on the project will be affected by your focus choice."

    system "The player attributes that you will have in this game are: Level (Exp Points), Technical Skills, Productivity, Stress, and Money."

    system "Throughout the game, there will be checkpoints that will determine if you have the necessary amount of attribute points to advance."

    system "You will have to make sure you are actively gaining and balancing the points in all categories throughout the game."

    system "Your Level acts as your completion progress to your team's software engineering project.
    As you advance through the game and complete the project, you will gain experience points (Exp Points) and level up."

    system "Your Technical Skill is your knowledge of programming languages and computer science principles needed for software engineering.
    As you advance through the game, you will gain Technical Skill points by researching and correctly answering game questions."

    system "Your Productivity Points are how well you are progressing and managing the project as a scrum leader.
    As you advance through the game, you will gain Productivity Points by performing code reviews and supporting your team."

    system "As every person knows, stress accumulates over the time that you work.
    As you advance through the game, you will generate stress. You will have to manage developing your project and skills while managing your stress as well."

    system "Lastly, every 2 weeks, it is payday! You will recieve money for your work that you will be able to use to pay your bills and purchase items."

    system "Here's a tip: The best software engineers are not the ones that are the smartest or busiest.
    Be sure to try to get the perfect balance between all of your skills!"

    # Add relationships after

    jump weekly_focus_1

#---------------------------------------------------------------------------------------------------------------------------------------
# Recurring weekly focus system / Week 1

label weekly_focus_1:
    scene office_background

    "You enter the new week ready to learn and work!"

    "'Focus on work' will boost your EXP point gain. 'Chill/Relax' will decrease your stress level. 'Research' will increase your technical skills.
    'Review own code/work' will increase your productivity gain. 'Socialize' will boost your co-worker relationships."

    "What will you focus on this week?"

    menu weekly_focus_choices:
        "Focus on work":
            show work hard at center
            "Your EXP points are boosted for the week."

            $ calendar.focus(1) #Function that moves onto next week

        "Chill/Relax":
            show chill relax at center
            "Your stress level has decreased."

            $ calendar.focus(2) #Function that moves onto next week

        "Research":
            show research at center
            "Your technical skill has been boosted."

            $ calendar.focus(3) #Function that moves onto next week

        "Review own code/work":
            show review at center
            "Your productivity has been boosted."

            $ calendar.focus(4) #Function that moves onto next week

        #"Socialize":
            #show socialize at center
            #"Your co-worker relationships have been boosted."
            #
            #$ calendar.focus(5) #Function that moves onto next week

    system "Next, your mentor will walk you through how to answer questions in the game!"

    #jump weekly_focus_1

    jump part1_training

#---------------------------------------------------------------------------------------------------------------------------------------
# Random Event 1 / Week 1
# Rachel's Events for Sprint 2

label part1_training:

    scene office_background

    show sylvie blue giggle

    # These display lines of dialogue.

    "This is exciting. I'm going to be working on a team with other programmers!"

    jump training_with_mentor

label training_with_mentor:
    scene office_background
    show mentor_happy at left

    m "Hey rookie! Welcome to the team, I'll be your mentor for this process. Here's where you're going to be working."

    show office_background

    show main_v_happy at center
    with dissolve
    r "Thank you for the opportunity!"

    show mentor_slight_happy at left
    with dissolve
    m "So, I have a technical question to ask you- What do you know about computer architecture?"

    menu first_menu:
        "I know nothing.":
                jump ohno

        "I know lots!":
                #show bg club
                #with dissolve

                #hide mentor_slight_happy
                #with dissolve

                #show mentor_smiling at left
                #with dissolve

                jump first_quiz_question
#---------------------------------------------------------------------------------------------------------------------------------------
label ohno:
    show office_background
    with dissolve

    show mentor_surprise at left

    m "You must be kidding, right?"

    show main_happy at center
    r "Ah..."

    scene office_background
    show mentor_smile_closeup at left
    with dissolve

    m "That's alright. There's lots of time to pick up information!"

    jump after_menu_1
#---------------------------------------------------------------------------------------------------------------------------------------
label first_quiz_question:
    scene office_background
    with None

    show mentor_smiling at left
    with dissolve

    m "So - The _______ takes care of the concurrency and the synchoronization issues between sub-systems in the system is what?"

    menu first_quiz_questions:
        "Logical view":
            "Is this correct?"
            jump not_correct

        "Development view":
            "Is this correct?"
            jump not_correct

        "Process view":
            "Is this correct?"
            jump not_correct

        "Physical view":
            "Is this correct?"
            jump correct_answer

label AGAIN_first_quiz_question:
    show mentor_smiling
    m "Let's try again. The _______ takes care of the concurrency and the synchoronization issues between sub-systems in the system is what?"

    menu first_quiz_questionsv2:
        "Logical view":
            "Is this correct?"
            jump not_correct

        "Development view":
            "Is this correct?"
            jump not_correct

        "Process view":
            "Is this correct?"
            jump not_correct

        "Physical view":
            "Is this correct?"
            jump correct_answer

label correct_answer:
    m "Good job! That's correct."

    jump after_menu_1

label not_correct:
    show mentor_surprise at left
    with dissolve

    m "Not quite!"

    jump AGAIN_first_quiz_question

#---------------------------------------------------------------------------------------------------------------------------------------
# Where the script left off
label after_menu_1:
    scene office_background
    show main_v_happy at center
    with dissolve
    "I'll continue to do my best for any other pop quizzes I may have!"

    scene office_background

    "As you end your work week, you will be able to visit a store on the weekends!"

    "You will gain $150 for your work on the project every week."

    "At the end of the weekend, you can be able to go to a store to purchase items that will help you boost your skills."

    "You can be able to equip items such as a better keyboard, mouse, desk chair and more!"

    "You can also be able to consume some items for a boost in skills."

    "That wraps it up for the work week. You pack up your things and get ready to head home."

    jump weekend_event_1

#---------------------------------------------------------------------------------------------------------------------------------------
# Weekend Event 1 / Week 1
label weekend_event_1:

    scene bg club

    "As you head home you wonder if you should stop by the store to buy more items..."

    "Do you want to head to the store?"

    menu ask_store_1:
        "Yes, head to the store.":
            "You ready your wallet and head to the store!"
            window hide
            show screen shop_screen
            pause
            jump home_1

        "No, head home.":
            "You decide to save money and head home."
            jump home_1

#---------------------------------------------------------------------------------------------------------------------------------------
# Home Event 1 / Week 1
label home_1:
    hide screen shop_screen

    scene home
    with dissolve

    "After a busy week, you head home to rest up."

    "You learned a lot about software engineering this week and are eager for what's to come in the future!"

    $ calendar.next() # Change to Week 2

    $ renpy.notify("A week has advanced.")

    jump weekly_focus_2


# -------------------------------------------------------------- WEEK 2 ----------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
# Recurring weekly focus system / Week 2

label weekly_focus_2:
    scene bg club
    with dissolve

    "You enter the new week ready to learn and work!"

    scene office_background

    "What will you focus on this week?"

    "Reminder!"

    "'Focus on work' will boost your EXP point gain. 'Chill/Relax' will decrease your stress level. 'Research' will increase your technical skills.
    'Review own code/work' will increase your productivity gain. 'Socialize' will boost your co-worker relationships."

    menu weekly_focus_choices_2:
        "Focus on work":
            show work hard at center
            "Your EXP points are boosted for the week."

            $ calendar.focus(1) #Function that moves onto next week

        "Chill/Relax":
            show chill relax at center
            "Your stress level has decreased."

            $ calendar.focus(2) #Function that moves onto next week

        "Research":
            show research at center
            "Your technical skill has been boosted."

            $ calendar.focus(3) #Function that moves onto next week

        "Review own code/work":
            show review at center
            "Your productivity has been boosted."

            $ calendar.focus(4) #Function that moves onto next week

        #"Socialize":
        #    show socialize at center
        #    "Your co-worker relationships have been boosted."
        #
        #    $ calendar.focus(5) #Function that moves onto next week

    jump meeting_with_higherups

#---------------------------------------------------------------------------------------------------------------------------------------
# Story event 2 / Week 2
label meeting_with_higherups:
    scene office_background
    with None

    show main_v_happy:
        xalign 0.0
        yalign 1.0
    with Dissolve(0.5)

    show mentor_happy:
        xalign 0.75
        yalign 1.0
    with Dissolve(1.5)




    r "I wasn't expecting to see you guys here today."

    m "I just wanted to stop by and check on your project."

    r "Awesome have you been checking in on the teams sprint report submissions?"

    m "Of course and I really like what I see. Do you mind if ask you a couple questions?"

    r "Go ahead I don't mind!"

    jump second_quiz_question

label second_quiz_question:
    show office_background
    with None


    m "Relating to sprint backlog, how is estimated work remaining updated?"

    menu second_quiz_questions:
        "Monthly":
            "Is this correct?"
            jump not_correct2

        "Weekly":
            "Is this correct?"
            jump not_correct2

        "Bi-weekly":
            "Is this correct?"
            jump not_correct2

        "Daily":
            "Is this correct?"
            jump correct_answer2

label AGAIN_second_quiz_question:

    m "Relating to sprint backlog, how is estimated work remaining updated?"

    menu second_quiz_questionsv2:
        "Monthly":
            "Is this correct?"
            jump not_correct2

        "Weekly":
            "Is this correct?"
            jump not_correct2

        "Bi-weekly":
            "Is this correct?"
            jump not_correct2

        "Daily":
            "Is this correct?"
            jump correct_answer2

label correct_answer2:
    m "Good job! That's correct."

    #needs jump statement from where you left off
    jump week2_check

label not_correct2:

    m "Not quite!"

    jump AGAIN_second_quiz_question

#---------------------------------------------------------------------------------------------------------------------------------------
# Even Events have a checkpoint - Week 2 Check point

label week2_check:

    # After event is done
    "That wraps it up for the work week. You pack up your things and get ready to head home."
    jump weekend_event_2

#---------------------------------------------------------------------------------------------------------------------------------------
# Weekend Event 2 / Week 2
label weekend_event_2:

    scene bg club

    "As you head home you wonder if you should stop by the store to buy more items..."

    "Do you want to head to the store?"

    menu ask_store_2:
        "Yes, head to the store.":
            "You ready your wallet and head to the store!"
            window hide
            show screen shop_screen
            pause
            jump home_2

        "No, head home.":
            "You decide to save money and head home."
            jump home_2

#---------------------------------------------------------------------------------------------------------------------------------------
# Home Event 2 / Week 2
label home_2:
    hide screen shop_screen

    scene home
    with dissolve

    "After a busy week, you head home to rest up."

    "You learned a lot about software engineering this week and are eager for what's to come in the future!"

    $ calendar.next() # Change to Week 3

    $ renpy.notify("A week has advanced.")

    jump weekly_focus_3

# -------------------------------------------------------------- WEEK 3 ----------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
# Recurring weekly focus system / Week 3

label weekly_focus_3:
    scene bg club
    with dissolve

    "You enter the new week ready to learn and work!"

    scene office_background

    "What will you focus on this week?"

    "Reminder!"

    "'Focus on work' will boost your EXP point gain. 'Chill/Relax' will decrease your stress level. 'Research' will increase your technical skills.
    'Review own code/work' will increase your productivity gain. 'Socialize' will boost your co-worker relationships."

    menu weekly_focus_choices_3:
        "Focus on work":
            show work hard at center
            "Your EXP points are boosted for the week."

            $ calendar.focus(1) #Function that moves onto next week

        "Chill/Relax":
            show chill relax at center
            "Your stress level has decreased."

            $ calendar.focus(2) #Function that moves onto next week

        "Research":
            show research at center
            "Your technical skill has been boosted."

            $ calendar.focus(3) #Function that moves onto next week

        "Review own code/work":
            show review at center
            "Your productivity has been boosted."

            $ calendar.focus(4) #Function that moves onto next week

        #"Socialize":
        #    show socialize at center
        #    "Your co-worker relationships have been boosted."
        #
        #    $ calendar.focus(5) #Function that moves onto next week

    jump lead_lunch_and_learn

#---------------------------------------------------------------------------------------------------------------------------------------
# Week 3 Event
#Random Event 2: Mentor gives you the opportunity to lead the lunch and learn
label lead_lunch_and_learn:

    show bg club
    with None

    show mentor_smiling at left
    with dissolve

    m "Hey Sylvie, you've been here for a couple months now. How would you like to lead the next lunch and learn?"

    show main_happy at center
    with dissolve

    r "What do I need to lead?"

    show bg club
    with None
    show mentor_smiling at left
    m "Well, this quarter, we'll be teaching about how connectors work within computer architecture to other folks within the company. What do you say?"


    scene bg club
    show main_concerned
    with dissolve
    "What do I do...?"

    menu lunch_decision:
        "Yes, I would love to!":
            scene presentation_2
            show main_happy
            "Let's do it!"
            jump lets_do_it

        "Um, maybe not...":
            "I don't think I'm ready to do that yet... I'd like to decline, please."
            jump im_not_ready

label lets_do_it:
    scene presentation_2
    show mentor_happy
    m "Okay, sounds good! You're on for the next one. Here's a list of the topics."

    show list
    pause
    jump after_lets_do_it

label after_lets_do_it:
    scene office_background
    with None

    show mentor_smiling
    m "Well, today's the big day! Good luck!"

    scene presentation_2
    show main_concerned
    "I'm nervous. I hope I do well!"

    scene presentation_2
    show eileen happy at center
    r "Alright, thank you everyone for coming. I will now begin the presentation."

    scene presentation_2
    "Here I present-"

    scene office_background
    show mentor_smile_closeup at left
    hide mentor_smile_closeup
    m "Wow, you did a great job! I'm sure I'll hear great responses from the higher ups."

    scene office_background
    show main_v_happy
    r "Wow, I'm so glad. Thank you!"

    jump weekend_event_3

#this is for declining the lunch and learn
label im_not_ready:
    scene office_background
    show mentor_slight_happy at left

    m "That's fine! We can just take it slow."

    show main_happy at center
    r "Okay, thank you!"

    "That wraps it up for the work week. You pack up your things and get ready to head home."

    jump weekend_event_3

#---------------------------------------------------------------------------------------------------------------------------------------
# Weekend Event 3 / Week 3
label weekend_event_3:

    scene bg club

    "As you head home you wonder if you should stop by the store to buy more items..."

    "Do you want to head to the store?"

    menu ask_store_3:
        "Yes, head to the store.":
            "You ready your wallet and head to the store!"
            window hide
            show screen shop_screen
            pause
            jump home_3

        "No, head home.":
            "You decide to save money and head home."
            jump home_3

#---------------------------------------------------------------------------------------------------------------------------------------
# Home Event 3 / Week 3
label home_3:
    hide screen shop_screen

    scene home
    with dissolve

    "After a busy week, you head home to rest up."

    "You learned a lot about software engineering this week and are eager for what's to come in the future!"

    $ calendar.next() # Change to Week 4

    $ renpy.notify("A week has advanced.")

    jump weekly_focus_4

# -------------------------------------------------------------- WEEK 4 ----------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
# Recurring weekly focus system / Week 4

label weekly_focus_4:
    scene bg club
    with dissolve

    "You enter the new week ready to learn and work!"

    scene office_background

    "What will you focus on this week?"

    "Reminder!"

    "'Focus on work' will boost your EXP point gain. 'Chill/Relax' will decrease your stress level. 'Research' will increase your technical skills.
    'Review own code/work' will increase your productivity gain. 'Socialize' will boost your co-worker relationships."

    menu weekly_focus_choices_4:
        "Focus on work":
            show work hard at center
            "Your EXP points are boosted for the week."

            $ calendar.focus(1) #Function that moves onto next week

        "Chill/Relax":
            show chill relax at center
            "Your stress level has decreased."

            $ calendar.focus(2) #Function that moves onto next week

        "Research":
            show research at center
            "Your technical skill has been boosted."

            $ calendar.focus(3) #Function that moves onto next week

        "Review own code/work":
            show review at center
            "Your productivity has been boosted."

            $ calendar.focus(4) #Function that moves onto next week

        #"Socialize":
        #    show socialize at center
        #    "Your co-worker relationships have been boosted."
        #
        #    $ calendar.focus(5) #Function that moves onto next week

    jump sick_day

#---------------------------------------------------------------------------------------------------------------------------------------
# Week 4 Event
#Story Event 4: sick day
label sick_day:
    scene office_background
    with None

    show main_concerned:
        xalign 0.0
        yalign 1.0
    with Dissolve(0.5)

    show mentor_shock:
        xalign 0.75
        yalign 1.0
    with Dissolve(1.5)


    m "Oh no! You look terrible did you come into work sick?"

    r "I don't want to let my team down I can still work."

    m "You can't work if you're sick! It's terrible for your health and you could infect someone else. "

    m "What did I tell you?"

    jump third_quiz_question

label third_quiz_question:
    show office_background
    with None


    m "Should you come into the office if you're sick?"

    menu third_quiz_questions:
        "Working sick is fine because you can save sick days.":
            "Is this correct?"
            jump not_correct3

        "Never be a quitter.":
            "Is this correct?"
            jump not_correct3

        "The project is more important than my health.":
            "Is this correct?"
            jump not_correct3

        "If I'm sick I should take care of myself and be considerate to my coworkers.":
            "Is this correct?"
            jump correct_answer3

label AGAIN_third_quiz_question:

    m "Should you come into the office if you're sick?"

    menu third_quiz_questionsv2:
        "Working sick is fine because you can save sick days.":
            "Is this correct?"
            jump not_correct3

        "Never be a quitter.":
            "Is this correct?"
            jump not_correct3

        "The project is more important than my health.":
            "Is this correct?"
            jump not_correct3

        "If I'm sick I should take care of myself and be considerate to my coworkers.":
            "Is this correct?"
            jump correct_answer3

label correct_answer3:
    m "Good job! That's correct. Now go home and get some sleep"

    jump weekend_event_4


label not_correct3:
    scene office_background
    show mentor_shock
    m "That is totally wrong!"

    jump AGAIN_third_quiz_question

#---------------------------------------------------------------------------------------------------------------------------------------
# Weekend Event 4 / Week 4
label weekend_event_4:

    scene bg club

    "As you head home you wonder if you should stop by the store to buy more items..."

    "Do you want to head to the store?"

    menu ask_store_4:
        "Yes, head to the store.":
            "You ready your wallet and head to the store!"
            window hide
            show screen shop_screen
            pause
            jump home_4

        "No, head home.":
            "You decide to save money and head home."
            jump home_4

#---------------------------------------------------------------------------------------------------------------------------------------
# Home Event 4 / Week 4
label home_4:
    hide screen shop_screen

    scene home
    with dissolve

    "After a busy week, you head home to rest up."

    "You learned a lot about software engineering this week and are eager for what's to come in the future!"

    $ calendar.next() # Change to Week 5

    $ renpy.notify("A week has advanced.")

    jump weekly_focus_5


# -------------------------------------------------------------- WEEK 5 ----------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
# Recurring weekly focus system / Week 5

label weekly_focus_5:
    scene bg club
    with dissolve

    "You enter the new week ready to learn and work!"

    scene office_background

    "What will you focus on this week?"

    "Reminder!"

    "'Focus on work' will boost your EXP point gain. 'Chill/Relax' will decrease your stress level. 'Research' will increase your technical skills.
    'Review own code/work' will increase your productivity gain. 'Socialize' will boost your co-worker relationships."

    menu weekly_focus_choices_5:
        "Focus on work":
            show work hard at center
            "Your EXP points are boosted for the week."

            $ calendar.focus(1) #Function that moves onto next week

        "Chill/Relax":
            show chill relax at center
            "Your stress level has decreased."

            $ calendar.focus(2) #Function that moves onto next week

        "Research":
            show research at center
            "Your technical skill has been boosted."

            $ calendar.focus(3) #Function that moves onto next week

        "Review own code/work":
            show review at center
            "Your productivity has been boosted."

            $ calendar.focus(4) #Function that moves onto next week

        #"Socialize":
        #    show socialize at center
        #    "Your co-worker relationships have been boosted."
        #
        #    $ calendar.focus(5) #Function that moves onto next week

    jump coworker_needs_help

#---------------------------------------------------------------------------------------------------------------------------------------
# Week 5 Event
#Random Event 3: Coworker asks you for help on their project

label coworker_needs_help:

    scene office_background
    show coworker_happy at center
    a "Hi! My name is Adrian. I don't think we've met before."

    scene office_background
    show main_happy at center
    r "Hi! My name is Sylvie. It's nice to meet you. Which department are you from?"

    a "I'm from the digital design department. I was actually wondering..."
    hide coworker_happy
    show coworker_cheeky at left

    r "Yeah?"

    scene office_background
    show coworker_thumbs

    a "Would you be able to help me do a design that incorporates architecture and aesthetics? We could team up for this!"

    scene office_background
    show main_happy at center
    r "When should I let you know?"

    scene office_background
    show coworker_thumbs
    a "Right now would be great! But please let me know by the end of the day."

    menu decide_help_coworker:
        "Yes, help Adrian!":
            scene office_background
            show main_happy "Yeah, just email me the information and we can schedule a meeting!"
            jump yes_coworker

        "No, don't help Adrian.":
            scene office_background
            show main_concerned
            r "I think at the moment, I have too many tasks on my plate. I would love to help you at a later time though."
            jump no_coworker

label yes_coworker:
    scene office_background
    show coworker_happy
    a "Great! I'll send you the details soon. Thanks!"

    scene office_background
    show main_happy
    r " This is great. I can meet more coworkers and collaborate on different projects!"
    jump end_ask_coworker

label no_coworker:
    scene office_background
    show coworker_sigh
    a "It's okay. It was worth a shot! I'll definitely keep in touch with you to see when you're next available."
    jump end_ask_coworker

label end_ask_coworker:
    scene office_background
    show main_happy
    r "I'm glad I can see others in the company."

    "That wraps it up for the work week. You pack up your things and get ready to head home."
    jump weekend_event_5

#---------------------------------------------------------------------------------------------------------------------------------------
# Weekend Event 5 / Week 5
label weekend_event_5:

    scene bg club

    "As you head home you wonder if you should stop by the store to buy more items..."

    "Do you want to head to the store?"

    menu ask_store_5:
        "Yes, head to the store.":
            "You ready your wallet and head to the store!"
            window hide
            show screen shop_screen
            pause
            jump home_5

        "No, head home.":
            "You decide to save money and head home."
            jump home_5

#---------------------------------------------------------------------------------------------------------------------------------------
# Home Event 5 / Week 5
label home_5:
    hide screen shop_screen

    scene home
    with dissolve

    "After a busy week, you head home to rest up."

    "You learned a lot about software engineering this week and are eager for what's to come in the future!"

    $ calendar.next() # Change to Week 6

    $ renpy.notify("A week has advanced.")

    jump end_check

# Midpoint checkpoint
label end_check:
    $ ending = character.checkForEnd()
    if ending == True:
        jump gameOver
    else:
        jump weekly_focus_6

# -------------------------------------------------------------- WEEK 6 ----------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
# Recurring weekly focus system / Week 6

label weekly_focus_6:
    scene bg club
    with dissolve

    "You enter the new week ready to learn and work!"

    scene office_background

    "What will you focus on this week?"

    "Reminder!"

    "'Focus on work' will boost your EXP point gain. 'Chill/Relax' will decrease your stress level. 'Research' will increase your technical skills.
    'Review own code/work' will increase your productivity gain. 'Socialize' will boost your co-worker relationships."

    menu weekly_focus_choices_6:
        "Focus on work":
            show work hard at center
            "Your EXP points are boosted for the week."

            $ calendar.focus(1) #Function that moves onto next week

        "Chill/Relax":
            show chill relax at center
            "Your stress level has decreased."

            $ calendar.focus(2) #Function that moves onto next week

        "Research":
            show research at center
            "Your technical skill has been boosted."

            $ calendar.focus(3) #Function that moves onto next week

        "Review own code/work":
            show review at center
            "Your productivity has been boosted."

            $ calendar.focus(4) #Function that moves onto next week

        #"Socialize":
        #    show socialize at center
        #    "Your co-worker relationships have been boosted."
        #
        #    $ calendar.focus(5) #Function that moves onto next week

    jump ransomware

# Week 6 Event
#Story event event 3: Ransomware

label ransomware:
    scene presentation
    show mentor_happy
    m "Hey Sylvie, the reason why I scheduled this meeting today is to go over ransomware attacks."

    scene presentation
    show main_v_happy
    r "Ransomware? Could you remind me what that is again?"

    scene presentation
    show mentor_smile_closeup
    m "No problem! That's why I'm here."

    scene presentation
    show mentor_surprise
    m "Ransomware is malicious software that infects your computer and displays messages demanding a fee to be paid in order for your system to work again."

    scene presentation
    show mentor_surprise
    m "Follow these three basic rules to avoid ransomware"

    "1. Never click on unverified links"

    "2. Do not open untrusted email attachments"

    "3. Only download from sites you trust"

    scene presentation
    show main_v_happy
    r "Okay, sounds good!"

    "I'll make sure to be careful."

    scene presentation
    show main_v_happy at left
    show mentor_smiling at center

    m "All right now get back to work and be safe!"

    jump weekend_event_6

#---------------------------------------------------------------------------------------------------------------------------------------
# Weekend Event 6 / Week 6
label weekend_event_6:

    scene bg club

    "As you head home you wonder if you should stop by the store to buy more items..."

    "Do you want to head to the store?"

    menu ask_store_6:
        "Yes, head to the store.":
            "You ready your wallet and head to the store!"
            window hide
            show screen shop_screen
            pause
            jump home_6

        "No, head home.":
            "You decide to save money and head home."
            jump home_6

#---------------------------------------------------------------------------------------------------------------------------------------
# Home Event 6 / Week 6
label home_6:
    hide screen shop_screen

    scene home
    with dissolve

    "After a busy week, you head home to rest up."

    "You learned a lot about software engineering this week and are eager for what's to come in the future!"

    $ calendar.next() # Change to Week 7

    $ renpy.notify("A week has advanced.")

    jump weekly_focus_7

# -------------------------------------------------------------- WEEK 7 ----------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
# Recurring weekly focus system / Week 7

label weekly_focus_7:
    scene bg club
    with dissolve

    "You enter the new week ready to learn and work!"

    scene office_background

    "What will you focus on this week?"

    "Reminder!"

    "'Focus on work' will boost your EXP point gain. 'Chill/Relax' will decrease your stress level. 'Research' will increase your technical skills.
    'Review own code/work' will increase your productivity gain. 'Socialize' will boost your co-worker relationships."

    menu weekly_focus_choices_7:
        "Focus on work":
            show work hard at center
            "Your EXP points are boosted for the week."

            $ calendar.focus(1) #Function that moves onto next week

        "Chill/Relax":
            show chill relax at center
            "Your stress level has decreased."

            $ calendar.focus(2) #Function that moves onto next week

        "Research":
            show research at center
            "Your technical skill has been boosted."

            $ calendar.focus(3) #Function that moves onto next week

        "Review own code/work":
            show review at center
            "Your productivity has been boosted."

            $ calendar.focus(4) #Function that moves onto next week

        #"Socialize":
        #    show socialize at center
        #    "Your co-worker relationships have been boosted."
        #
        #    $ calendar.focus(5) #Function that moves onto next week

    jump earthquake

#---------------------------------------------------------------------------------------------------------------------------------------
# Week 7 Event
#Random event 4: EARTHQUAKE

label earthquake:
    scene office_background
    with vpunch

    scene office_background
    with vpunch

    show main_concerned
    with vpunch
    "OH NO AN EARTHQUAKE!!"

    scene office_background
    with vpunch
    show mentor_shock
    with vpunch
    m "Just hang on! It'll be over in a second."

    scene office_background
    show main_concerned
    with vpunch
    "Okay, I'll try!"

    scene office_background
    with vpunch

    scene office_background
    show mentor_smiling at left
    m "Okay, grab your stuff and we'll evacuate outside."

    show main_concerned at center
    r "Got it!"

    scene bg club
    with vpunch
    show mentor_shock
    m "Okay, once this dies down - everyone should go home for the day and stay safe at home!"

    scene bg club
    with vpunch
    show main_concerned
    r "Okay! Will do!"

    jump weekend_event_7

#---------------------------------------------------------------------------------------------------------------------------------------
# Weekend Event 7 / Week 7
label weekend_event_7:

    scene bg club

    "As you head home you wonder if you should stop by the store to buy more items..."

    "Do you want to head to the store?"

    menu ask_store_7:
        "Yes, head to the store.":
            "You ready your wallet and head to the store!"
            window hide
            show screen shop_screen
            pause
            jump home_7

        "No, head home.":
            "You decide to save money and head home."
            jump home_7

#---------------------------------------------------------------------------------------------------------------------------------------
# Home Event 7 / Week 7
label home_7:
    hide screen shop_screen

    scene home
    with dissolve

    "After a busy week, you head home to rest up."

    "You learned a lot about software engineering this week and are eager for what's to come in the future!"

    $ calendar.next() # Change to Week 8

    $ renpy.notify("A week has advanced.")

    jump weekly_focus_8

# -------------------------------------------------------------- WEEK 8 ----------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
# Recurring weekly focus system / Week 8

label weekly_focus_8:
    scene bg club
    with dissolve

    "You enter the new week ready to learn and work!"

    scene office_background

    "What will you focus on this week?"

    "Reminder!"

    "'Focus on work' will boost your EXP point gain. 'Chill/Relax' will decrease your stress level. 'Research' will increase your technical skills.
    'Review own code/work' will increase your productivity gain. 'Socialize' will boost your co-worker relationships."

    menu weekly_focus_choices_8:
        "Focus on work":
            show work hard at center
            "Your EXP points are boosted for the week."

            $ calendar.focus(1) #Function that moves onto next week

        "Chill/Relax":
            show chill relax at center
            "Your stress level has decreased."

            $ calendar.focus(2) #Function that moves onto next week

        "Research":
            show research at center
            "Your technical skill has been boosted."

            $ calendar.focus(3) #Function that moves onto next week

        "Review own code/work":
            show review at center
            "Your productivity has been boosted."

            $ calendar.focus(4) #Function that moves onto next week

        #"Socialize":
        #    show socialize at center
        #    "Your co-worker relationships have been boosted."
        #
        #    $ calendar.focus(5) #Function that moves onto next week

    jump turn_in

#---------------------------------------------------------------------------------------------------------------------------------------
# Week 8 Event
#Story event: Turn in day
label turn_in:
    scene bg club
    show mentor_smiling:
        xalign 0.75
        yalign 1.0
    with Dissolve(0.5)

    show main_v_happy:
        xalign 0.0
        yalign 1.0
    with Dissolve(0.7)

    m "Well after your final review next week you will be turning in your project"

    show mentor_surprise:
        xalign 0.75
        yalign 1.0

    m "Now that I'm thinking about it you are practically done how do you feel?"

    r "Like a senior developer. It's all thanks to you!"

    scene bg club
    show mentor_smiling at center:

    m "Maybe we will have a little suprise next week"

    "That wraps it up for the work week. You pack up your things and get ready to head home."
    jump weekend_event_8

#---------------------------------------------------------------------------------------------------------------------------------------
# Weekend Event 8 / Week 8
label weekend_event_8:

    scene bg club

    "As you head home you wonder if you should stop by the store to buy more items..."

    "Do you want to head to the store?"

    menu ask_store_8:
        "Yes, head to the store.":
            "You ready your wallet and head to the store!"
            window hide
            show screen shop_screen
            pause
            jump home_8

        "No, head home.":
            "You decide to save money and head home."
            jump home_8

#---------------------------------------------------------------------------------------------------------------------------------------
# Home Event 8 / Week 8
label home_8:
    hide screen shop_screen

    scene home
    with dissolve

    "After a busy week, you head home to rest up."

    "You learned a lot about software engineering this week and are eager for what's to come in the future!"

    $ calendar.next() # Change to Week 9

    $ renpy.notify("A week has advanced.")

    jump weekly_focus_9

# -------------------------------------------------------------- WEEK 9 ----------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
# Recurring weekly focus system / Week 9

label weekly_focus_9:
    scene bg club
    with dissolve

    "You enter the new week ready to learn and work!"

    scene office_background

    "What will you focus on this week?"

    "Reminder!"

    "'Focus on work' will boost your EXP point gain. 'Chill/Relax' will decrease your stress level. 'Research' will increase your technical skills.
    'Review own code/work' will increase your productivity gain. 'Socialize' will boost your co-worker relationships."

    menu weekly_focus_choices_9:
        "Focus on work":
            show work hard at center
            "Your EXP points are boosted for the week."

            $ calendar.focus(1) #Function that moves onto next week

        "Chill/Relax":
            show chill relax at center
            "Your stress level has decreased."

            $ calendar.focus(2) #Function that moves onto next week

        "Research":
            show research at center
            "Your technical skill has been boosted."

            $ calendar.focus(3) #Function that moves onto next week

        "Review own code/work":
            show review at center
            "Your productivity has been boosted."

            $ calendar.focus(4) #Function that moves onto next week

        #"Socialize":
        #    show socialize at center
        #    "Your co-worker relationships have been boosted."
        #
        #    $ calendar.focus(5) #Function that moves onto next week

    jump beach_episode

#---------------------------------------------------------------------------------------------------------------------------------------
# Week 9 Event
#Random event 5: BEACH EPISODE

label beach_episode:
    scene office_background
    show coworker_cheeky
    a "Hey Sylviel! I'm back again. I was wondering..."

    scene office_background
    show main_happy at center
    r "Hey Adrian! What's up?"

    show coworker_happy at left
    a "A couple of us from the office want to go to the beach this weekend. Are you interested?"

    hide main_happy at center
    show main_v_happy at center
    r "Wow, thanks for the invite!! I would love to go. Send me the details when you can!"

    jump beach_day

label beach_day:
    scene beach_day
    show main_v_happy
    r "Wow, it's so nice to be out here!"

    scene beach_day
    show coworker_shirtless
    a "Hey, Sylvie!! Glad you could make it out!!"

    scene beach_day
    show main_v_happy
    r "Thanks for inviting me!!"

    scene beach_day
    show mentor_smiling
    m "Ey, Sylvie! You made it out! Don't worry about formalities while we're out here. All of us are just relaxing from the week."

    scene beach_day
    show main_v_happy
    r "Okay, sounds good!"

    "It's hard to do that though."

    scene beach_night
    with dissolve

    show main_v_happy at left
    show mentor_smiling:
        xalign 0.80
        yalign 1.0
    show coworker_shirtless:
        xalign 0.4
        yalign 1.0

    "This was a great day with everyone."

    jump weekend_event_9

#---------------------------------------------------------------------------------------------------------------------------------------
# Weekend Event 9 / Week 9
label weekend_event_9:

    scene bg club

    "As you head home you wonder if you should stop by the store to buy more items..."

    "Do you want to head to the store?"

    menu ask_store_9:
        "Yes, head to the store.":
            "You ready your wallet and head to the store!"
            window hide
            show screen shop_screen
            pause
            jump home_9

        "No, head home.":
            "You decide to save money and head home."
            jump home_9

#---------------------------------------------------------------------------------------------------------------------------------------
# Home Event 9 / Week 9
label home_9:
    hide screen shop_screen

    scene home
    with dissolve

    "After a busy week, you head home to rest up."

    "The project is finishing up and you are excited for what your mentor thinks of the final project!"

    $ calendar.next() # Change to Week 10

    $ renpy.notify("A week has advanced.")

    jump check_for_Winning

# -------------------------------------------------------------- WEEK 10 ----------------------------------------------------------------

#check to see if game has been won
label check_for_Winning:
    $ ending = character.checkForWin()
    if ending == True:
       jump mentor_proud
    else:
       jump gameOver

label mentor_proud:
    scene bg club
    show mentor_smiling:
        xalign 0.75
        yalign 1.0
    with Dissolve(0.5)

    show main_v_happy:
        xalign 0.0
        yalign 1.0
    with Dissolve(0.7)

    m "The higher ups loved your project! I'm just so proud of you and all that you've accomplish"

    show mentor_surprise:
        xalign 0.75
        yalign 1.0

    m "I have nothing else to teach you I'm proud to announce you are no longer an entry-level developer"

    scene bg club
    show main_v_happy at center:

    r "It's all thanks to you! This is only the beginning of my journey I'm sure their will be higher mountains in the future"

    scene winning
    pause

    return

    #GAME IS COMPLETE


label gameOver:
    # At game over, the game returns to the main menu
    scene bg club
    "You enter the office and feel the tension in the air."

    scene office_background
    bosses "We need to talk..."
    bosses "You did not meet the required progress at this point of the project."
    bosses "YOU ARE FIRED!"

    scene gameover
    pause

    return
