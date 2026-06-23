
label dream:
    play sound "toctoc.ogg"
    scene dream 1
    with Dissolve (1.5)
    me "Hello? Judie? Comin' in."
    me "Judie?"
    scene dream 2 with dissolve
    me "May I ask what you're doing?"
    j "Hiding something."
    me "For what?"
    j "For protection."
    me "And what are you hiding?"
    j "Tools of self-defense."
    me "What kind of tools?"
    scene dream 3
    j "Very inquisitive today, aren't you?"
    scene dream 2
    j "Ok, I'll show you, just don't freak out."
    me "After so many years living with you and Lauren I've gotten used to your weird stuff. It's quite difficult to shock me."
    scene dream 4 with dissolve
    j "It's a kunai knife. I've been practicing, I can hit an apple from 6 meters."
    scene dream 5
    me "Wow, forget what I said. You never cease to amaze me."
    me "Ok, first of all: What the fuck?"
    me "And secondly: where did you get that from and what do you need it for?"
    scene dream 4
    j "I already had them, from when I cosplayed Naruto."
    j "And I just told you they're for self-defense."
    scene dream 5 
    me "Could you put that down while you explain this to me?"
    scene dream 6
    j "Fiiine."
    scene dream 7
    me "And self-defense? Someone's trying to kill you?"
    scene dreamj
    j "I don't know, maybe. Do I need to remind you what we saw in the basement? They might know we know."
    j "They could be watching us right now."
    scene dream 7
    me "They? Who are \"they\"?"
    scene dream 10
    j "Aha! That's the big question. I hope to find the answer tomorrow when we go to those coordinates."
    scene dream 12
    me "Do you still want to go? I think this thing is getting to you too much."
    scene dream 10
    j "Of course I want to! We have to solve this mystery!"
    scene dream 12
    me "Ok... well, it's decided, then."
    scene dream 9
    j "Cool! I’ll carry the kunai in my backpack."
    scene dream 13
    me "Oh god, at least don’t let anyone see them. You wouldn't want to get arrested."
    scene dream 9
    j "Don't worry about that! I'm undetectable."
    scene dream 7
    if inc is True:
        me "By the way, before mom gets here, I wanted to ask you..."
    else:
        me "By the way, before Carla gets here, I wanted to ask you..."
    me "About what happened yesterday at the pool..."
    scene dream 8
    j "Oh, yeah, I thought that was a dead issue."
    j "I was drunk, and I can barely remember what happened, but if something happened, it's just a mere anecdote, and I don’t think we need to talk about it anymore."
    j "(Holding the knives tightly) Don't you think?"
    me "Y-yes."
    scene dream 9
    j "Excellent."
    play sound "doorbell.ogg"
    scene dream 14 with dissolve
    j "Oh! That's Mom! Let's go!"
    scene dream 15
    with Dissolve (1.5)
    j "Hiii Mom!!!" with dissolve
    scene dream 16 with dissolve
    c "Hello sweetie! How have you been?"
    j "Better than good!"
    if inc is True:
        me "Welcome back Mom!"
    else:
        me "Welcome back Carla!"
    menu: 
        with dissolve
        "You look even more beautiful than before!{color=#00ff00} √√√{/color}":
            $ carla_points += 1
            show red
            show screen carla_points
            c "Aww, thank you [me]!" with dissolve
            hide screen carla_points 
            hide red 
            
            scene dream 15
            c "Do you want me to tell you how the trip went? We can order something to eat." with dissolve
            l "Sounds good to me."
            j "Super!"
            me "Nice."
        "Thank god you're back, we don’t know how the washing machine works.":
            scene dream 15
            $ carla_points -= 1
            show blue
            show screen carla_points
            
            c "Do you want me to tell you how the trip went while [me] makes dinner for us?" with dissolve
            hide screen carla_points 
            hide blue 
            
            l "Sounds good to me." with dissolve
            j "Super!"
            me "(That's what I get for being silly.)"
        "What's the big deal? Were you gone?":
            scene dream 15
            $ carla_points -= 1
            show blue
            show screen carla_points
            
            c "Do you want me to tell you how the trip went while [me] makes dinner for us?" with dissolve
            hide screen carla_points 
            hide blue 
            
            l "Sounds good to me." with dissolve
            j "Super!"
            me "(That's what I get for being silly.)"
        "So... what's for dinner?":
            scene dream 15
            $ carla_points -= 1
            show blue
            show screen carla_points
            
            c "Do you want me to tell you how the trip went while [me] makes dinner for us?" with dissolve
            hide screen carla_points 
            hide blue 
            
            l "Sounds good to me." with dissolve
            j "Super!"
            me "(That's what I get for being silly.)"
    scene dream 17
    with Dissolve (2)
    c "*Yawn*" with dissolve
    scene dream 18
    c "I'm sorry kids, I'm exhausted. But, well, I think I’ve already told you all my stories."
    c "I’m gonna take a shower and go straight to bed. I’m gonna fall asleep in a second."
    scene dream 19
    j "Of course! Go get some rest!"
    l "Yeah, sleep well!"
    me "Good night!"
    scene dream 18
    c "Good night, everyone."
    scene dream 20
    with Dissolve (2.5)
    c "(Ahh, after 5 hours in a train, I appreciated that shower.)" with dissolve
    scene dream 21
    c "(And now, off to bed. I have to work tomorrow.)"
    scene dream 22 with Dissolve (1)
    c "(There's nothing like sleeping in your own bed after being away.)" with dissolve
    c "(I don't know how Charles can handle it so often.)"
    play sound "toctoc.ogg"
    $ renpy.pause ()
    scene dream 23 with dissolve
    c "(Hmm? Who is it now?)" with dissolve
    scene dream 24 with dissolve
    c "Lauren, is that you?"
    c "If this is about the last piece of cheesecake, [me] ate it, I'm sorry."
    play sound "dooropen.ogg"
    scene dream 25 with dissolve
    c "Oh, [me], it's you. Do you need something?"
    me "Yes, but I think you need it more than I do."
    c "What?"
    scene dream 26 with dissolve
    c "Ah!"
    c "What are you doing? What's gotten into you?"
    scene dream 27
    me "I know you want this."
    me "I know you haven't been satisfied for a long time."
    me "And considering all you do for us, you deserve a good fuck."
    scene dream 28 with dissolve
    $ renpy.pause ()
    me "So I'm gonna fuck you so hard that I'm gonna split you in half." with dissolve
    c "W-what are you saying??... You're out of your mind!"
    me "Stop restraining yourself."
    scene dream 29 with dissolve
    $ renpy.pause ()
    me "Just let yourself go." with dissolve
    c "Oh my god... I didn't know you were so big..."
    scene dream 30 with dissolve
    me "That's it. Just relax."
    c "But I shouldn't..."
    c "It's wrong..."
    c "But..."
    scene dream 31 with dissolve
    $ renpy.pause ()
    scene dream 32 with dissolve
    c "Ah!"
    me "Take off your panties."
    scene dream 33 with dissolve
    $ renpy.pause ()
    scene dream 34 with dissolve
    $ renpy.pause ()
    c "Oh my god..." with dissolve
    me "Your pussy is soaking wet."
    me "I can tell you were looking forward to this."
    c "I..."
    me "Say it."
    c "I want you to fuck me."
    me "Good."
    scene dream 35 with dissolve
    $ renpy.pause ()
    c "Oh god!" with dissolve
    scene dream 36 with dissolve
    c "Please, be car.." 
    scene dream 37 
    c "Ahhhhh... " 
    scene dream 38 with hpunch 
    c "AHHHHHH!"
    scene dream 39 with dissolve
    c "(Oh my god...)" with dissolve
    c "(I just had a sex dream about [me]...)"
    c "(And... that was kind of a turn on...)"
    c "(I haven't had an orgasm for too long, I guess that's affecting me.)"
    c "(That damn man and his damn business trips...)"
    c "(Anyway, I’d better go back to sleep.)"
    c "(If I can...)"
    scene dream 40
    with Dissolve (2)
    me "(Ok, time for bed.)" with dissolve
    scene dream 41
    me "(I have school tomorrow, and anyway, I'm feeling sleepy.)"
    scene dream 42 with dissolve
    me "(Hmm.. I should set the alarm.)"
    me "(I have to be there at 09:00 AM, and I have to shower, change, eat breakfast, and go all the way there.)"
    me "(Hmm.. I'm setting it for 08:45 AM.)"
    play sound "toctoc.ogg"
    $ renpy.pause ()
    scene dream 43 with dissolve
    me "(Hmm? Who is it now?)" with dissolve
    scene dream 44 with dissolve
    me "Lauren, is that you?"
    me "If this is about the last piece of cheesecake, yes, I ate it, I'm sorry."
    play sound "door2.ogg"
    scene dream 45 
    with Dissolve (1)
    $ renpy.pause ()
    me "What..." with dissolve
    me "What the fuck..."
    scene dream 46 
    with Dissolve (1)
    play music "musicbox.ogg" fadein 4.0
    me "What the fuck is going on?" with dissolve
    me "Where am I?"
    me "Am I dreaming?"
    me "Yes, of course... I'm dreaming."
    scene dream 45
    with Dissolve (1)
    me "Either that, or I’ve completely lost my mind..." with dissolve
    me "I’ve never had such a realistic dream."
    play sound "cry.ogg"
    $ renpy.pause ()
    scene dream 47 with dissolve
    me "You've got to be kidding me..." with dissolve
    me "Erm... hello?"
    me "Are you ok, miss?"
    scene dream 48 
    with Dissolve (1.2)
    play sound "cry.ogg"
    me "Hello?" with dissolve
    me "Do you need help, ma'am?"
    me ". . ."
    stop sound
    scene dream 49 
    me "Hey, can you hear me?" with dissolve
    hide screens
    scene dream 50 
    with Dissolve (1)
    $ renpy.pause ()
    scene dream 51
    with Dissolve (2)
    $ renpy.pause ()
    me "What the hell..." with dissolve
    scene dream 52 with dissolve
    me "(What the hell is going on here...)" with dissolve
    scene dream 53 with dissolve
    me "(Oh shit, oh shit, oh shit.)"
    ast "{i}Esse est deus.{/i}"
    ast "{i}Et finivit regnum dei.{/i}"
    ast "{i}Astaroth incipit imperare.{/i}"
    me "What??!"
    ast "{i}Esse {w}est {w}deus.{/i}"
    scene dream 54 with hpunch
    $ renpy.pause ()
    scene dream 46
    me "HOLY CRAP, FUCK THIS SHIT."
    me "I just... I need to get out of here."
    scene dream m1
    me "What?!"
    me "Why are there three doors now?"
    me "Okay, calm down, I need to think fast."
    me "Erm..."
    default n1 = False
    default o1 = False
    default p1 = False
    default q1 = False
    menu:
        with dissolve
        "Door 1":
            scene dream m2
            me "This one."
            jump n1
        "Door 2":
            scene dream m3
            me "This one."
            jump o1
        "Door 3{color=#00ff00} √√√{/color}":
            scene dream m4
            me "This one."
            jump p1
label n1:
    $ n1 = True
    play sound "door2.ogg"
    scene dream n2
    with Dissolve (1)
    $ renpy.pause ()
    scene dream n1 with dissolve
    me "And now, where am I?"
    me "There are four more doors..."
    scene dream n3 with hpunch
    me "Oh holly shit, not that thing again!"
    scene dream n4 
    me "Which way should I go? I don't know what to do..."
    scene dream n5 with hpunch
    me "Fuck! Get away from me!"
    scene dream n9 
    me "Fuck, fuck, fuck!"
    menu:
        with dissolve
        "Blue door":
            scene dream n8
            me "This one."
            if o1:
                jump o2
            else:
                jump o1
        "Green door":
            scene dream n7
            me "This one."
            if p1:
                jump p2
            else:
                jump p1
        "Red door":
            scene dream n6
            me "This one."
            if q1:
                jump q2
            else:
                jump m2
        "White door":
            scene dream n4
            me "This one."
            jump m2
label o1:
    $ o1 = True
    play sound "door2.ogg"
    scene dream o1
    with Dissolve (1)
    $ renpy.pause ()
    me "Is this... the park?"
    me "Yes, this is the park where Lauren and I went for a run."
    me "What am I doing here?..."
    me "Four more doors..."
    scene dream o3 with hpunch
    me "Bloody hell!"
    me "What's that thing and why is it haunting me?..."
    me "Leave me be!"
    scene dream o2
    me "Fuck this shit."
    menu:
        with dissolve
        "Green door":
            scene dream o5
            me "This one."
            if n1:
                jump n2
            else:
                jump n1
        "Red door":
            scene dream o7
            me "This one."
            if q1:
                jump q2
            else:
                jump m2
        "Blue door":
            scene dream o6
            me "This one."
            if p1:
                jump p2
            else:
                jump p1
        "White door":
            scene dream o4
            me "This one."
            jump m2
label p1:
    $ p1 = True
    play sound "door2.ogg"
    scene dream p6
    with Dissolve (1)
    $ renpy.pause ()
    me "(Shivering) God, it's s-so cold in h-here..."
    scene dream p1
    me "That creature again..."
    me "WHAT DO YOU WANT?!"
    ast ". . . "
    scene dream p6 
    me "I have to get out of here..."
    me "I have to..."
    me "One of these doors has to be the good one..."
    menu:
        with dissolve
        "Green door":
            scene dream p5
            me "This one."
            if o1:
                jump o2
            else:
                jump o1
        "Red door{color=#00ff00} √√√{/color}":
            scene dream p4
            me "This one."
            if q1:
                jump m2
            else:
                jump q1
        "Blue door":
            scene dream p3
            me "This one."
            jump m2
        "White door":
            scene dream p2
            me "This one."
            if n1:
                jump n2
            else:
                jump n1
label q1:
    play sound "door2.ogg"
    $ q1 = True
    scene dream q1
    with Dissolve (1)
    me "Fuck!"
    me "I can’t go this way!"
    scene dream q2
    me "It will kill me!"
    menu:
        with dissolve
        "Go back through the white door{color=#00ff00} √√√{/color}":
            jump p2
label m2:    
    play sound "door2.ogg"
    scene dream 45
    with Dissolve (1)
    me "Fuck, I'm back where I started. This makes no sense..."
    me "I can’t be stuck here forever... It can't be!"
    scene dream m1
    me "There has to be a way out..."
    menu:
        with dissolve
        "Door 1":
            scene dream m2
            me "This one."
            if n1:
                jump n2
            else:
                jump n1
        "Door 2":
            scene dream m3
            me "This one."
            if o1:
                jump o2
            else:
                jump o1
        "Door 3":
            scene dream m4
            me "This one."
            if p1:
                jump p2
            else:
                jump p1
label n2:
    play sound "door2.ogg"
    scene dream n2
    with Dissolve (1)
    $ renpy.pause ()
    scene dream n1 
    me "Great, I'm here once again."
    scene dream n2
    me "I hope this is the last time..."
    menu:
        with dissolve
        "Blue door":
            scene dream n8
            me "This one."
            if o1:
                jump o2
            else:
                jump o1
        "Green door":
            scene dream n7
            me "This one."
            if p1:
                jump p2
            else:
                jump p1
        "Red door":
            scene dream n6
            me "This one."
            if q1:
                jump q2
            else:
                jump m2
        "White door":
            scene dream n4
            me "This one."
            jump m2
label o2:
    play sound "door2.ogg"
    scene dream o1
    with Dissolve (1)
    $ renpy.pause ()
    me "The park again."
    me "When will this nightmare end?"
    menu:
        with dissolve
        "Green door":
            scene dream o5
            me "This one."
            if n1:
                jump n2
            else:
                jump n1
        "Red door":
            scene dream o7
            me "This one."
            if q1:
                jump q2
            else:
                jump m2
        "Blue door":
            scene dream o6
            me "This one."
            if p1:
                jump p2
            else:
                jump p1
        "White door":
            scene dream o4
            me "This one."
            jump m2
label p2:
    play sound "door2.ogg"
    scene dream p6
    with Dissolve (1)
    me "(Shivering) T-this f-fucking iceberg again..."
    me "Am I doomed to wander this place forever?"
    menu:
        with dissolve
        "Green door":
            scene dream p5
            me "This one."
            if o1:
                jump o2
            else:
                jump o1
        "Red door{color=#00ff00} √√√{/color}":
            scene dream p4
            me "This one."
            if q1:
                jump q2
            else:
                jump q1
        "Blue door":
            scene dream p3
            me "This one."
            jump m2
        "White door":
            scene dream p2
            me "This one."
            if n1:
                jump n2
            else:
                jump n1
label q2:
    play sound "door2.ogg"
    scene dream q3
    with Dissolve (1)
    me "Here again..."
    me "At least it's clear now." 
    menu:
        with dissolve
        "Green door":
            scene dream q6
            me "This one."
            jump o2
        "Red door{color=#00ff00} √√√{/color}":
            scene dream q4
            me "This one."
            jump dream_end  
        "Blue door":
            scene dream q5
            me "This one."
            jump p2
        "White door":
            jump m2
label dream_end:
    play sound "door2.ogg"
    stop music fadeout 4.0
    scene dream r1
    with Dissolve (1)
    me "Oh thank goodness!"
    me "My room!"
    me "I was starting to think that nightmare would never end."
    me "I'm glad I c..."
    $ renpy.pause ()
    scene dream r2
    with Dissolve (2.5)
    $ renpy.pause ()
    scene dream r3
    with Dissolve (2.5)
    $ renpy.pause ()
    scene dream r4
    play sound "jumpscare.ogg"
    $ renpy.pause (0.3)
    scene black 
    $ renpy.pause (1.5)
    scene dream r5
    me "AHHHHHHHHHHHHHH" with hpunch
    me "FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCK"
    scene dream r6 
    with Dissolve (1)
    me "Oh man... that was a terrible dream." with dissolve
    me "I’ve never had a worse time in my entire life."
    me "I have a headache."
    me "Jeez, why can’t I just dream about busty women?"
    me "I think all those stories of secret cults and demons are just, like, getting in my head, I guess."
    scene dream r7 with dissolve
    me "I'll sleep with the light on."
    me "Hopefully I won’t have another nightmare..."
    me "I'd settle for d..."
    me "For..."
    play music "musicbox.ogg" fadein 4.0
    me "Zzzzzzzz..."
    $ renpy.pause ()
    scene dream r8 
    with Dissolve (2.2)
    $ renpy.pause ()
    scene dream r9
    with Dissolve (2.2)
    $ renpy.pause ()
    scene dream r10
    with Dissolve (2.2)
    $ renpy.pause ()
    scene dream r11
    with Dissolve (2.2)
    $ renpy.pause ()

    jump temple
    
    
    
    
    