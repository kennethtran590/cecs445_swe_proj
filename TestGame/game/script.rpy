# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sylvie = Character("Sylvie")

define eileen = Character("Eileen")

define bosses = Character("Bosses")

define system = Character("")

define r = Character("Sylvie")
define m = Character("Mentor")

image mentor_happy = "KG110001.kg.png"
image mentor_slight_happy = "KG110002.kg.png"
image mentor_surprise = "KG110013.kg.png"
image mentor_smile_closeup = "KG110032.kg.png"
image mentor_smiling = "KG110042.kg.png"

image main_concerned = "eileen concerned.png"

# The game starts here.
# -------------------------------------------------------------- WEEK 1 ----------------------------------------------------------------
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg club

    #scene office_background

    show screen calendar(date_inf)

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
            "A week has advanced."
            $ calendar.focus(1) #Function that moves onto next week

        "Chill/Relax":
            show chill relax at center
            "Your stress level has decreased."
            "A week has advanced."
            $ calendar.focus(2) #Function that moves onto next week

        "Research":
            show research at center
            "Your technical skill has been boosted."
            "A week has advanced."
            $ calendar.focus(3) #Function that moves onto next week

        "Review own code/work":
            show review at center
            "Your productivity has been boosted."
            "A week has advanced."
            $ calendar.focus(4) #Function that moves onto next week

        "Socialize":
            show socialize at center
            "Your co-worker relationships have been boosted."
            "A week has advanced."
            $ calendar.focus(5) #Function that moves onto next week

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

    return

label training_with_mentor:
    scene office_background
    show mentor_happy at left

    m "Hey rookie! Welcome to the team, I'll be your mentor for this process. Here's where you're going to be working."

    show office_background

    show sylvie blue giggle at center
    with dissolve
    r "Thank you for the opportunity!"

    show mentor_slight_happy at left
    with dissolve
    m "So, I have a technical question to ask you- What do you know about computer architecture?"

    menu first_menu:
        "I know nothing.":
                jump ohno

        "I know lots!":
                show bg club
                with dissolve

                hide mentor_slight_happy
                with dissolve

                show mentor_smiling at left
                with dissolve

                jump first_quiz_question
#---------------------------------------------------------------------------------------------------------------------------------------
label ohno:
    show office_background
    with dissolve

    show mentor_surprise at left

    m "You must be kidding, right?"

    show sylvie blue surprised at center
    r "Ah..."

    scene office_background
    show mentor_smile_closeup at left
    with dissolve

    m "That's alright. There's lots of time to pick up information!"

    jump after_menu_1
#---------------------------------------------------------------------------------------------------------------------------------------
label first_quiz_question:
    show bg club
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

    "You have gained +5 Technical Skills Points"

    $ character_metrics.skills = character_metrics.skills + 5

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
    show sylvie blue giggle at center
    with dissolve
    "I'll continue to do my best for any other pop quizzes I may have!"

    "As you end your work week, you will be able to visit a store on the weekends!"

    "You can purchase"

    jump weekend_event_1

#---------------------------------------------------------------------------------------------------------------------------------------
# Weekend Event 1 / Week 1
label weekend_event_1:

    "Insert weekend event here"

    jump store_1

#---------------------------------------------------------------------------------------------------------------------------------------
# Store Event 1 / Week 1
label store_1:

    "Insert store event here"

    jump home_1

#---------------------------------------------------------------------------------------------------------------------------------------
# Store Event 1 / Week 1
label home_1:

    "Insert home event here"

    $ calendar.next() # Change to Week 2
    jump weekly_focus_2


# -------------------------------------------------------------- WEEK 2 ----------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
# Recurring weekly focus system / Week 2

label weekly_focus_2:
    scene office_background

    "You enter the new week ready to learn and work!"

    "'Focus on work' will boost your EXP point gain. 'Chill/Relax' will decrease your stress level. 'Research' will increase your technical skills.
    'Review own code/work' will increase your productivity gain. 'Socialize' will boost your co-worker relationships."

    "What will you focus on this week?"

    menu weekly_focus_choices_2:
        "Focus on work":
            show work hard at center
            "Your EXP points are boosted for the week."
            "A week has advanced."
            $ calendar.focus(1) #Function that moves onto next week

        "Chill/Relax":
            show chill relax at center
            "Your stress level has decreased."
            "A week has advanced."
            $ calendar.focus(2) #Function that moves onto next week

        "Research":
            show research at center
            "Your technical skill has been boosted."
            "A week has advanced."
            $ calendar.focus(3) #Function that moves onto next week

        "Review own code/work":
            show review at center
            "Your productivity has been boosted."
            "A week has advanced."
            $ calendar.focus(4) #Function that moves onto next week

        "Socialize":
            show socialize at center
            "Your co-worker relationships have been boosted."
            "A week has advanced."
            $ calendar.focus(5) #Function that moves onto next week

    jump meeting_with_higherups

#---------------------------------------------------------------------------------------------------------------------------------------
# Story event 2 / Week 2
label meeting_with_higherups:
    scene office_background
    with None

    show sylvie blue normal:
        xalign 0.0
        yalign 1.0
    with Dissolve(0.5)

    show software_team:
        xalign 0.75
        yalign 1.0
    with Dissolve(1.5)

    show sylvie surprised:
        xalign 0.0
        yalign 1.0


    sylvie "I wasn't expecting to see you guys here today."

    bosses "We just wanted to step by and check on your project."

    show sylvie blue smile

    sylvie "Awesome have you been checking in on the teams sprint report submissions?"

    bosses "Of course and we really like what we see. Do you mind if ask you a couple questions?"

    show sylvie blue smile

    sylvie "Go ahead I don't mind!"

    jump second_quiz_question

label second_quiz_question:
    show office_background
    with None

    show software_team at left
    with dissolve

    bosses "Relating to sprint backlog, how is estimated work remaining updated?"

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
    show software_team
    bosses "Relating to sprint backlog, how is estimated work remaining updated?"

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
    bosses "Good job! That's correct."

    "You have gained +5 Technical Skills Points"

    $ character_metrics.skills = character_metrics.skills + 5

    #needs jump statement from where you left off
    jump week2_check

label not_correct2:
    show software_team at left
    with dissolve

    bosses "Not quite!"

    jump AGAIN_second_quiz_question

#---------------------------------------------------------------------------------------------------------------------------------------
# Even Events have a checkpoint - Week 2 Check point
# GISSELLE INSERT A CHECKPOINT THAT CHECKS THE PLAYER'S CURRENT STATS IF THEY MEET A CERTAIN NUMBER

# pseudocode could be:
# if character specific metric doesn't meet a certain number:
#   trigger game over (might need to create a game over event/label)
# else:
#   continue

label week2_check:
    bosses "Let's check your progress in the project so far"

#---------------------------------------------------------------------------------------------------------------------------------------

label mentor_proud:
    scene bg club
    show mentor_smiling:
        xalign 0.75
        yalign 1.0
    with Dissolve(0.5)

    show sylvie blue normal:
        xalign 0.0
        yalign 1.0
    with Dissolve(0.7)

    m "I'm just so proud of you and all that you've accomplish"

    show mentor_surprise:
        xalign 0.75
        yalign 1.0

    m "I have nothing else to teach you I'm porud to announce you are no longer an entry-level developer"

    scene bg club
    show sylvie blue smile at center:

    sylvie "It's all thanks to you! This is only the beginning of my journey I'm sure their will be higher mountains in the future"
