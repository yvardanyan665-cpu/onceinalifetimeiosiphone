
label hospital:
    default wwfirst = True
    default wwwindow = False
    default ewfirst = True
    default labfirst = True
    default codeh = False
    default codehh = False
    default stairsfirst = True
    default secondfirst = True
    default corpsefirst = True
    default bodyfirst = True
    default bodysecond = False
    default bodythird = False
    default roomsfirst = True
    default officefirst = True
    default cagefirst = True
    default recordsfirst = True
    default uv = False
    default uv2 = False
    default uv3 = False
    default officetwo = True
    default roomstwo = False
    default judiehospitalback = True
    stop music fadeout 2.5
    play music2 "wind.ogg" fadein 6
    scene hospital 1 
    with Dissolve (2.5)
    $ renpy.pause ()
    j "All right, here we are!" with dissolve
    me "Damn, this place is like a ghost town. Do you think anyone still lives here?" 
    scene hospital 4
    l "As far as I know, no, no one lives here."
    scene hospital 2
    j "I heard there used to be a coal factory here. They built houses for the workers, a church, shops, and a hospital for the ones injured in the mines, so it became an independent town."
    scene hospital 2b
    j "However, the factory shut down 15 years ago, and all the workers left this place." with dissolve
    j "It's been abandoned since then."
    me "That sounds like some kind of horror movie plot."    
    play sound "thunder2.ogg"
    scene hospital 3 
    with Dissolve (2)
    $ renpy.pause ()
    j "I think it's going to rain..." with dissolve
    me "See?! We were only lacking a storm. It's the perfect mix for getting murdered."
    me "It's that kind of situation where you say: \"Why are they going there? They're dumb, they're gonna be killed in there!\""
    scene hospital 5
    l "I don't know about the murdering but I don't want to get caught in a storm. Maybe we should walk around one last time and then head back home."
    scene hospital 2b 
    j "I agree."
    me "Okay, let's do that."
    scene hospital 6
    with Dissolve (1.5)
    me "Hmm..." with dissolve
    me "This place gives me the heebie-jeebies."
    scene hospital 7
    me "It's odd everybody left their homes like this..." with dissolve
    me "HELLO? ANYONE THERE?"
    me ". . ."
    scene hospital 6
    me "Nothing." with dissolve
    scene hospital 8 with dissolve
    play sound "piano.ogg"
    scene hospital 9 with dissolve
    $ renpy.pause ()
    me "What the fuck..." with dissolve
    me "Did you see that? There was someone there! Right?"
    j "I didn't see anything..."
    l "Are you trying to scare us?!"
    scene hospital 10
    me "No! I thought I saw..."
    me "Just wait for me here, I'll check that corner."
    scene hospital 9 with dissolve
    $ renpy.pause ()
    scene hospital 11
    with Dissolve (1.5)
    me "(There's no one here...)" with dissolve
    me "(But there was someone! I saw it... Did I imagine it?)"
    me "(I want to get out of here...)"
    j "[me]! Come here! Quick!"
    scene hospital 1 with dissolve
    $ renpy.pause ()
    scene hospital 12
    with Dissolve (1.5)
    me "Ok girls... I think we should turn around... What is it?" with dissolve
    scene hospital 13
    j "We found it! St. Augustine's Hospital!" with dissolve
    scene hospital 15
    me "This? It doesn't look like a hospital."
    scene hospital 13
    j "But it is! The plate was covered with moss but you can still read it!"
    scene hospital 14
    l "The door seems to be stuck, but it's not locked. It'd open with a big push."
    scene hospital 15 
    me "We should come another day, if it starts to rain, we'll have to wait until..."
    play sound "thunder2.ogg"
    scene hospital 16 
    with Dissolve (1)
    $ renpy.pause ()
    stop music2 fadeout 3
    play music "rain1.ogg" fadein 2.0
    scene hospital 17 
    with Dissolve (1.5)
    $ renpy.pause ()
    scene hospital 18
    me "Fuck." with dissolve
    j "I guess there's only one path forward."
    me "I guess so. We have to wait for the storm to stop anyway."
    l "We're going in!"
    me "All right, here we go..."
    play sound "doorslam.ogg" 
    scene hospital 19
    with Dissolve (3.5)
    pause 1.5
    play music "rain2.ogg" 
    $ renpy.pause ()
    me "(Whispering) Man, it is eerie in here. And I can't see shit." with dissolve
    scene hospital 20
    l "Here, take the flashlight."
    me "Thanks."
    scene hospital 19
    $ renpy.pause ()
    play sound "switch.ogg"
    scene hospital 21
    $ renpy.pause ()
    me "Okay... better." with dissolve
    scene hospital 25
    me "(Whispering) Ok, we get in, we find the Compound AAR, we get out." with dissolve
    me "Nobody dies, and by 10 pm the three of us will be watching a series eating some nachos. All right?"
    j "Mm-hm..."
    me "What's wrong, Judie?"
    scene hospital 24
    j "Nothing... it's just... this place. It gives me a bad feeling."
    scene hospital 25
    me "It'll soon be over. And don't worry, we came prepared! If we don’t split up everything will be fine. In a few years we’ll remember how we saved the world!"
    scene hospital 26
    j "Hahaha, if you say so, I believe it. Let's save the world!"
    if laurenmassage:
        scene hospital 22
        me "You ready, Lauren?" with dissolve
        l "Mm-hm."
        me "When we get back I can give you another massage... This is getting really stressful."
        scene hospital 23
        l "W-what the fuck are you talking about?! The massages are done! The favour you owed me has been paid, thank you so much!"
        me "Oh, okay, okay... Thank you for freeing me from that duty."
        me "(Dammit...)"
        me "(I wonder... if Judie hadn't shown up, would we have...?)"
        me "(Well, I guess it doesn’t matter now.)"
    scene hospital 27 
    with Dissolve (1)
    me "Ahem, as for the gun..." with dissolve
    default gunme = False
    default gunjudie = False
    default gunlauren = False
    menu:
        with dissolve
        "Carry it yourself{color=#00ff00} √√√{/color}":
            $ gunme = True
            me "I'll carry it."
            j "I think that's best."
            l "Ok."
        "Give it to Judie":
            $ gunjudie = True
            scene hospital 29 
            me "Judie, you'll carry the gun." with dissolve
            j "Whaaat?!"
            l "Are you sure?"
            j "I don't even know how to hold this thing!"
            me "If you have to use it just point it and say: You better not move an inch!"
            j "This can't end well..."
        "Give it to Lauren":
            $ gunlauren = True
            scene hospital 28
            me "Lauren, you'll carry the gun." with dissolve
            l "That's a smart decision!"
            j "You look hot with that, sis!"
            l "Haha, yeah, I think I do!"
    play sound "thunder2.ogg"
    scene hospital 21 
    with Dissolve (1.5)
    me "Ok, St. Augustine's... Time to find out what secrets you're hiding..." with dissolve
    scene hospital 30 with dissolve
    me "This place has a small entrance but it's much bigger from inside." with dissolve
    scene hospital 31
    me "There's even a second floor." with dissolve
    l "There's an echo, you hear?"
    scene hospital 30
    me "Yeah, this hall is half-empty." with dissolve
    scene hospital 32
    me "Is there something in there?" with dissolve
    l "Nah, it doesn't work. There is a power supply, though. Maybe there's some kind of power generator."
    me "Let's go through the building, see what we can find."
    
    default hos_step = 1

label hall:
    scene hospital 21 
    with Dissolve (1.5)
    $ renpy.pause ()
    menu:
        with dissolve
        "West wing{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 1 or hos_step == 18):
            $ hos_step += 1
            jump westwing
        "West wing"if (hos_step != 1 and hos_step != 18):
            jump westwing
        "East wing{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 12):
            $ hos_step += 1
            jump eastwing
        "East wing"if (hos_step != 12):
            jump eastwing
    
    
label westwing:
    if wwfirst:
        scene ww 0c
        me "Let's explore the west wing." with dissolve
    scene ww 0
    with Dissolve (1)
    $ renpy.pause ()
    if wwfirst:
        $ wwfirst = False
        scene ww 0b with dissolve
        $ renpy.pause ()
        me "Hmm..." with dissolve
        me "The sign above the door says \"Infectious diseases\". That doesn't sound very friendly."
        l "I heard many workers became infected with some strange disease and the village was isolated, just before the factory was closed down."
        j "Well, in any case, any viruses, bacteria or parasites couldn't have survived for so long without a host. There shouldn't be any danger."
        j "But... don't touch anything, just in case."
        me "Should we have a look?"
        l "Is there something at the end of the corridor?"
        scene ww 0 
        me "I think there are some stairs leading to the top floor." with dissolve
    menu:
        with dissolve
        "Infectious diseases{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 9 or hos_step == 31): #9 31
            $ hos_step += 1
            jump lab
        "Infectious diseases"if (hos_step != 9 and hos_step != 31):
            jump lab
        "Stairs{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 2 or hos_step == 19): #2 19
            $ hos_step += 1
            jump stairs
        "Stairs"if (hos_step != 2 and hos_step != 19):
            jump stairs
        "Reception{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 11): #11
            $ hos_step += 1
            pass
        "Reception"if (hos_step != 11):
            pass
    if wwwindow and laurenmassage:
        $ wwwindow = False
        scene ww 1 
        with Dissolve (1)
        l "It's really coming down out there..." with dissolve
        play sound "thunder2.ogg"
        l "It's so dark it feels like 2 am."
        scene ww 2
        if inc:
            me "I know... do you think Mom will worry?"
        else:
            me "I know... do you think Carla will worry?"
        scene ww 1 
        l "Nah, Judie and I told her we were going to be out late. I just hope we can walk out of this."
        scene ww 2 
        me "Of course we will!"
        menu:
            with dissolve
            "I've walked away from much worse, believe me.":
                scene ww 1
                l "I know... Thank you [me]." with dissolve
                scene ww 5
            "I won't let anything bad happen to you.{color=#00ff00} √√√{/color}":
                $ lauren_points += 1
                show screen lauren_points         
                scene ww 3
                show red
                l "Oh yeah... my knight in shining armour." with dissolve
                l "I'm not a princess who needs to be saved, you know?"
                me "Believe me, I know."
                scene ww 1
                hide screen lauren_points
                l "(Chuckles) You're going to laugh but... the truth is, I do feel safe by your side..." with dissolve
                l "So... Thank you, [me]. For everything."
                scene ww 5
            "I've seen you get out of many situations that seemed impossible. You can handle it.":
                scene ww 1
                l "I know... Thank you [me]." with dissolve
                scene ww 5
        l "And now let's find that bloody compound!" with dissolve
        me "That's my girl!"
    jump hall



label eastwing: 
    if ewfirst:
        scene ew 0c
        me "Let's explore the east wing." with dissolve
    scene ew 0
    with Dissolve (1)
    $ renpy.pause ()
    if ewfirst:
        $ ewfirst = False
        j "Look! There's a sign up ahead." with dissolve
        j "It says if we keep going in this direction we're headed to Trauma and burn unit, which seems to be blocked off, Psychiatry, and the Hospital's archive."
        me "Alright, let's take a look."
        play sound "thunder2.ogg"
    menu:
        with dissolve
        "Records room{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 13):
            $ hos_step += 1
            jump accounting
        "Records room"if (hos_step != 13):
            jump accounting
        "Psychiatry":
            jump cage
        "Go back to reception{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 17):
            $ hos_step += 1
            jump hall
        "Go back to reception"if (hos_step != 17):
            jump hall


label accounting:
    scene accounting 0
    with Dissolve (1)
    $ renpy.pause ()
    if recordsfirst:
        $ recordsfirst = False
        me "All of the hospital files were probably kept here. Maybe we’ll find something interesting." with dissolve
        scene accounting 5 
        me "But... It looks like they took it all." with dissolve
        j "Hey, here are some binders that look pretty new."
        scene accounting 1 with dissolve
        j "Hmm..." with dissolve
        scene accounting 2 
        j "What's this?..." with dissolve
        j "{i}August 31st: No subject has gone beyond stage 1 so far. The compound is too unstable. We need more test subjects."
        j "{i}October 10th: AAR-2v has been a success. Subjects in phase 3 can regenerate any part of their body, whether it has been cut, burned or mutilated in any way. The only problem is the many mutations which it still causes."
        j "{i}January 11th: Subject 93 looks promising. He seems immune to the negative effects of AAR. He has been isolated."
        play sound "thunder2.ogg"
        j "{i}January 20th: Today we tried to administer a much bigger dose to a new subject. The results were terrible. He developed analogous structures in his own body in a matter of seconds. He killed 3 guards before we could contain him."
        j "{i}January 21st: We've cut out his spine but he's still alive. It is a biological marvel. Even in a state of madness, the subject is still preserving his reasoning. He has painted some kind of symbols in the Psychiatry ward. Going in there with the ultraviolet lights is madness."
        j "{i}February 19th: Today my wife Mathilde died in another accident. I'm out of here. Ms. Swango will have to carry on alone. We've gone too far."
        scene accounting 3
        me "Wow..."
        me "It sounds like the plot of a Resident Evil game."
        me "I find it hard to believe, but... who knows."
        scene accounting 5
        me "Let's make sure we're not missing anything..." with dissolve
    if uv:
        $ uv = False
        $ uv2 = True
        scene accounting 0
        me "Hmmm... Do you see a code number anywhere?" with dissolve
        scene accounting 4
        l "I don't, but I saw some UV filters in that drawer." with dissolve
        scene accounting 5
        l "We could use them with our flashlights, go to the Psychiatric ward, and look for the drawings the files mentioned."
        me "Yeah... that sounds interesting."
    menu:
        with dissolve
        "Psychiatry{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 14):
            $ hos_step += 1
            jump cage
        "Psychiatry"if (hos_step != 14):
            jump cage
        "Go back to the East wing":
            jump eastwing


    
label cage:
    scene cage 0
    with Dissolve (1)
    $ renpy.pause ()
    if uv3:
        play sound "switch.ogg"
        scene cage 4 
        with Dissolve (1)
        me "A black four..." with dissolve
    if cagefirst:
        $ cagefirst = False
        me "Don't you find it odd that a rural hospital had a Psychiatry ward?" with dissolve
        j "Yes... maybe it was meant to assist relatives?"
        l "The question is: why is there a fucking cage in here? I don’t think it'd be a big help to the families..."
        scene cage 1
        j "There's a blackboard. Maybe they were teaching something or giving therapy." with dissolve
        l "...in a cage."
        j "Yeah... that's the weird part."
        me "Well, never mind, let's just keep going." with dissolve
label cagemenu:  
    menu:
        with dissolve
        "Use the UV filters{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 15) and uv2:
            $ hos_step += 1
            pass
        "Use the UV filters" if (hos_step != 15) and uv2:
            pass
        "Records room":
            jump accounting
        "Go back to the East wing{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 16):
            $ hos_step += 1
            jump eastwing
        "Go back to the East wing"if (hos_step != 16):
            jump eastwing
            
    $ uv2 = False
    $ uv3 = True
    scene cage 0
    me "Okay, if we use this we should be able to..." with dissolve 
    play sound "switch.ogg"
    scene cage 2
    with Dissolve (1)
    $ renpy.pause ()
    me "Hmmm... I don't see anything there at all. I guess they cleaned it." with dissolve
    scene cage 0
    me "Too bad." with dissolve
    j "Wait a second, I saw... Give me the flashlight!"
    scene cage 1 with dissolve
    $ renpy.pause ()
    play sound "switch.ogg"
    scene cage 3 with dissolve
    $ renpy.pause ()
    me "That's..." with dissolve
    scene cage 4 
    l "A black four..." with dissolve
    me "You son of a bitch... someone wants us to go crazy." 
    jump cagemenu
    
    
label lab:
    scene ww 0b with dissolve
    $ renpy.pause ()
    if labfirst:
        me "Let's have a look." with dissolve
        play sound "thunder2.ogg"
    scene lab 0
    with Dissolve (1)
    $ renpy.pause ()
    if labfirst:
        $ labfirst = False
        j "I don't like this place..." with dissolve
        me "Me neither..."
        scene lab 1 
        with Dissolve (1)
        me "The rooms look like cells..." with dissolve
        j "I'm guessing they were designed as a way of containing the diseases but... it seems really inhuman..."
        scene lab 2
        with Dissolve (1)
        me "It ends here." with dissolve
        l "That door can't be opened?"
        me "Nope, it doesn't even have a knob."
        me "We can't go any further..."
    else:
        scene lab 2
        with Dissolve (1)   
    if codeh:
        me "We can't go any further..." with dissolve
        l "Do you see anything we could use?"
        $ codehh = True
        $ codeh = False
        $ bodysecond = True
        $ wwwindow = True
        $ uv = True
        $ roomstwo = True
        j "Wait! Look at this!"
        scene lab 3 with dissolve
        me "What is it?" with dissolve
        j "There's some sort of keypad on the wall with numbers from 0 to 9. It's likely to be the control panel to open the doors. That one included."
        scene lab 6
        me "Oh, it's true, we didn't notice it before."
        scene lab 3
        me "But we don't know the code..."
        l "Of course! The numbers!"
        scene lab 4b
        me "What?"
        scene lab 4
        l "The note! In the director's office! Don't you remember?"
        l "\"Five numbers. One path. White, red, green, grey, black. That's the order. That's the way.\""
        l "And there was a white three!"
        scene lab 4b
        me "So... The first number is a 3?"
        scene lab 4
        l "That'd make sense."
        scene lab 4b 
        me "And the other 4 numbers?"
        scene lab 4
        l "I don't know... maybe... somewhere around the hospital?"
        play sound "thunder2.ogg"
        scene lab 5 
        with Dissolve (1)
        me "Hmm..." with dissolve
        me "Maybe you're right. Let's take a look around here and see if we find something."
        me "Although... Don't you think it looks like someone’s messing with us? I mean... this \"numbers and colors\" game..."
        j "I was wondering the same thing."
        scene lab 4b 
        me "Anyway, let's try it."
        scene lab 3
label codehospitale:   
    menu:
        with dissolve
        "Enter a code{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 32) and (codeh or codehh):
            $ hos_step += 1
            pass
        "Enter a code" if (hos_step != 32) and (codeh or codehh):
            pass
        "Go back to the west wing{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 10):
            $ hos_step += 1
            jump westwing
        "Go back to the west wing"if (hos_step != 10):
            jump westwing
            
    scene lab 6 
    $ codehospital = renpy.input("\"White, red, green, grey, black. That's the order. That's the way\"\n{color=#00ff00}(Tip: It's 32084){/color}",allow="0123456789",length=5)
    if codehospital == "32084":
        jump lilith
    else:
        play sound "error.ogg"
        me "Wrong code..."
        jump codehospitale


label stairs:  
    scene stairs 0
    with Dissolve (1.5)
    $ renpy.pause ()
    menu:
        with dissolve
        "Second floor{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 3 or hos_step == 20): #3 20
            $ hos_step += 1
            pass
        "Second floor"if (hos_step != 3 and hos_step != 20):
            pass
        "Go back to the west wing{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 8 or hos_step == 30): #8 30
            $ hos_step += 1
            jump westwing
        "Go back to the west wing"if (hos_step != 8 and hos_step != 30):
            jump westwing
    if stairsfirst:
        $ stairsfirst = False
        play sound "woodenstairs.ogg"
        scene stairs 1 
        with Dissolve (1.5)
        me "This building looks like it's going to fall apart at any moment." with dissolve
        j "And no wonder! Look at this picture! It's dated September 19th, 1819! This hospital is over two centuries old!"
        j "They probably redesigned the whole building a few times but it's still impressive."
    play sound "woodenstairs.ogg"
    jump secondfloor
    

label secondfloor:   
    if secondfirst:
        $ secondfirst = False
        scene 2f 20
        with Dissolve (2)
        me "You can see the first floor from up here." with dissolve
        scene 2f 21 with dissolve
        $ renpy.pause ()
        scene 2f 0
        with Dissolve (1)
        $ renpy.pause ()
        me "Ok... what do we have over here..." with dissolve
        scene 2f 1
        pause .1
        scene 2f 0
        pause .1
        scene 2f 1
        pause .2
        scene 2f 0
        me "Oh no... come on..." with dissolve
        scene 2f 1
        pause .1
        scene 2f 0
        pause .1
        scene 2f 1
        pause .1
        scene 2f 0
        pause .1
        scene 2f 1 with dissolve
        play sound "flashlight.ogg"
        me "Fuck, fuck, fuck, not now..." with dissolve
        me "Ok... my flashlight is dead. Do you have any extra batteries?"
        me "Girls?"
        scene 2f 2
        me "Erm... Lauren? Judie?" with dissolve
        me "Hello?!"
        me "You have to be kidding me..."
        me "(Searching the backpack) Please [me], tell me you're carrying some spare batteries in your backpack..."
        me "Come on..."
        play sound "woodenstairs.ogg"       
        $ renpy.pause ()
        menu: 
            with Dissolve (1)
            "Turn around{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 4): #4
                $ hos_step += 1
                pass
            "Turn around"if (hos_step != 4): #4
                pass
        scene 2f 1 with Dissolve (1.5)
        $ renpy.pause ()
        me "(Hyperventilating) W-who's there?!" with dissolve
        $ renpy.pause ()
        scene 2f 2 with dissolve
        me "(Motherfuckin' hell... What have I done to deserve this?!)" with dissolve
        me "(Fuuuuuck...)"
        me "(Yes! Spare batteries! Thank goodness!)"
        play sound "switch.ogg"
        scene 2f 3
        $ renpy.pause ()
        me "LAUREN! JUDIE!!" with hpunch
        l "Yes, yes! We're coming!"
        play sound "thunder2.ogg"
        scene 2f 4 
        me "God damn it, we said to stay together!" 
        l "Yes, we know! Sorry!"
        j "It was my fault, sorry bro!"
        scene 2f 5
        l "We got distracted looking at a map of the hospital that was on the stairs." with dissolve
        me "Don’t do this to me again! You almost gave me a heart attack."
        scene 2f 0 
        l "It won't happen again! Stick together!" with dissolve
        me "Well... what did the map say?"
        l "We have the nurses' break room to the left, the intensive care rooms to the right and the director's office down the hall."
        me "I see..."
    scene 2f 0
    with Dissolve (2)
    $ renpy.pause ()
    menu:
        with dissolve
        "Break room{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 21): #21
            $ hos_step += 1
            jump rooms
        "Break room"if (hos_step != 21): #21
            jump rooms
        "Intensive Care{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 23): #23
            $ hos_step += 1
            jump corpse
        "Intensive Care"if (hos_step != 23): #23
            jump corpse
        "Director's office{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 5 or hos_step == 27): #5 27
            $ hos_step += 1
            jump officeh
        "Director's office"if (hos_step != 5 and hos_step != 27):
            jump officeh
        "Go back to the first floor{color=#00ff00} (Step [hos_step] of 32){/color}"if (hos_step == 7 or hos_step == 29): #7 29
            $ hos_step += 1
            play sound "woodenstairs.ogg"
            jump stairs
        "Go back to the first floor"if (hos_step != 7 and hos_step != 29):
            play sound "woodenstairs.ogg"
            jump stairs
    
label rooms:
    scene rooms 0b
    with Dissolve (1)
    $ renpy.pause ()
    if roomsfirst:
        me "There're a few lockers and a bathroom. This area is pretty close to intensive care, isn't it?" with dissolve
        j "Probably so that nurses who were staying at night could respond to issues more quickly."
        j "This is a small village, so resources and staff were scarce."
        l "This hospital is too damn big for such a small village..."
        me "Let's check out that door."
    if roomstwo:
        l "You search that room, I'll check the bathroom." with dissolve
        me "Okay, call us if you find anything."
    play sound "door2.ogg" fadeout 0.4
    scene rooms 0 
    with Dissolve (1)
    $ renpy.pause ()
    if roomsfirst:
        $ roomsfirst = False
        me "Nothing of particular interest here. Empty and dusty, just like the rest of this forsaken place." with dissolve
    if roomstwo:
        $ roomstwo = False
        scene rooms 1 
        with Dissolve (1)
        me "It's still pouring out there..." with dissolve
        me "It seems that this part of the hospital faces the mountain. Or so I think, it's so dark I can hardly see." 
        play sound "thunder2.ogg"
        scene rooms 2 with dissolve
        scene rooms 1 
        with Dissolve (1.3)
        me "Will it never stop raining, for god's sake?" with dissolve
        scene rooms 5
        me "Anyway, there's nothing of interest in this room." with dissolve
        scene rooms 6
        me "Did you find anything?" with dissolve
        scene rooms 7
        j "Nope, just a pair of old socks. Let's meet Lauren in the bathroom."
        if judielove:
            scene rooms 8
            j "Look, the roof's leaking everywhere." with dissolve
            me "Be careful, you're going to fall." 
            scene rooms 9
            j "Oh, shit!"
            me "BE CAREFUL!"
            play sound "fall.ogg"
            scene rooms 11 with hpunch
            me "Ah... I told you..."  
            scene rooms 12
            j "Oh my god! I'm sorry! Lucky you were there! Are you okay?!" with dissolve
            me "Yeah, well, I think I broke my back... Promise me you'll get a wheelchair and push me around the park..."
            scene rooms 13
            j "Hahaha, I see you’re all right." with dissolve
            j "Thank goodness, I don't know what I'd do without my big brother!"
            me "Yeah, you'd be lost!"
            scene rooms 15
            me "(Oh my god, this position is quite... suggestive.)" with dissolve
            me "(Don't get hard, [me]. Don't embarrass yourself...)"
            scene rooms 16
            me "(Aaaaand yeah, you're getting hard, of course.)" with dissolve
            scene rooms 14
            $ renpy.pause ()
            scene rooms 17 with dissolve
            $ renpy.pause ()
            scene rooms 18 with dissolve
            $ renpy.pause ()
            me "(Why isn't she getting up?)" with dissolve
            me "(Why doesn't she say anything?)"
            me "(Hasn't she noticed it? Of course she has...)"
            scene rooms 19
            with Dissolve (1)
            me "(OK, I have such an erection right now.)"
            me "(I...)"
            scene rooms 20
            l "Judie! [me]! Come here! QUICK!" with dissolve
            j "Y-yeah sis, we're coming!"
        play sound "door2.ogg"
        scene rooms 21
        with Dissolve (1)
        me "What's wrong?" with dissolve
        if judielove:
            l "What were you guys doing? I called you like, 5 times."
            scene rooms 22
            j "Us? Nothing! Why? I fell and [me] helped me up and yeah, that's it. No numbers. The room's clean."
        scene rooms 23
        l "Well, I actually found something. Another piece of the puzzle. Take a look."
        scene rooms 24
        with Dissolve (1)
        me "Nice!" with dissolve
        me "Is it paint or... blood?"
        l "I'd rather not know..."
        me "Well, it's one of the numbers either way."
    if codehh:
        scene rooms 24
        me "A red 2..." with dissolve
        jump roomshh
label roomshh:    
    menu:
        with dissolve
        "Go back to the corridor{color=#00ff00} (Step [hos_step] of 32){/color}" if (hos_step == 22): #22
            $ hos_step += 1
            jump secondfloor
        "Go back to the corridor" if (hos_step != 22):
            jump secondfloor
    
    
label corpse:
    if corpsefirst:
        $ corpsefirst = False
        me "Intensive care, you said?"
        j "Yes! The ICU. Follow us, we have to turn right and right again."
        scene corpse 1
        with Dissolve (2)
        me "Jesus, it smells like rotten eggs in here." with dissolve
        l "Yeah... Something stinks."
        me "You don't smell that, Judie?"
        j "T-the..."
        me "Are you okay?"
        scene corpse 2
        j "T-there is a corpse in here..." with dissolve
        me "Oh fuck."
        j "Is she dead?"
        me "Well, judging by the smell... I think so. Maybe we should go."
        scene corpse 3
        l "Let me have a look..." with dissolve
        play sound "thunder2.ogg"
        scene corpse 4 
        with Dissolve (1)
        $ renpy.pause ()
        scene corpse 5 with dissolve
        $ renpy.pause ()
        scene corpse 4 with dissolve
        $ renpy.pause ()
        scene corpse 6 
        with Dissolve (1)
        l "Y-yeah, she's..." with dissolve
        scene corpse 7
        l "*Gagging*" with dissolve
        scene corpse 8
        l "Yeah, she's very dead. And it's not nice." with dissolve
        l "Judie, you shouldn't watch this."
        j "D-don't worry sis, I won't."
        scene corpse 9
        l "If you want to see it, go ahead. I've had enough."
        l "We'll wait outside."
    scene corpse 0
    with Dissolve (1)
    $ renpy.pause ()    
label bodyh:   
    if bodythird:
        scene corpse 14
        with Dissolve (1)
        me "A green zero..." with dissolve
    menu:
        with dissolve
        "Inspect the first body{color=#00ff00} (Step [hos_step] of 32){/color}" if (hos_step == 24): #24
            $ hos_step += 1
            pass
        "Inspect the first body" if (hos_step != 24) and bodyfirst: #24
            pass
        "Inspect the second body{color=#00ff00} (Step [hos_step] of 32){/color}" if (hos_step == 25): #25
            $ hos_step += 1
            pass
        "Inspect the second body" if (hos_step != 25) and bodyfirst == False: #25
            pass
        "Go back to the corridor{color=#00ff00} (Step [hos_step] of 32){/color}" if (hos_step == 26): #26
            $ hos_step += 1
            jump secondfloor
        "Go back to the corridor" if (hos_step != 26): #26
            jump secondfloor
            
    if bodyfirst == True:
        $ bodyfirst = False
        play sound "thunder2.ogg"
        scene corpse 11
        with Dissolve (1)
        $ renpy.pause ()
        me "(Oh Jesus Christ... She's been slashed open...)" with dissolve
        scene corpse 12
        me "(Oh my fucking god, who would do such a thing?)" with dissolve
        me "*Gagging*"
        me "(And this smell... It's horrendous.)"
        scene corpse 11
        me "(However... It doesn't look like she's been dead a long time...)" with dissolve
        me "(There's definitely someone in this hospital. Lilith has to be here... We're getting close.)"
        jump bodyh
    if bodysecond == True:
        $ bodysecond = False
        $ bodythird = True
        scene corpse 11
        me "I just hope she was already dead when they did this to her..." with dissolve
        l "Are you seeing anything over there? Any of those numbers?"
        scene corpse 15
        me "Erm..." with dissolve
        l "Any book? Any painting on the wall?"
        me "No, nothing."
        l "Well, then let's keep moving."
        me "Ok."
        play sound "piano.ogg"
        scene corpse 13 with dissolve
        $ renpy.pause ()
        me "W-w-w-what the..." with dissolve
        l "What happened?"
        me "S-she... the corpse... her eyes... S-she didn't have her eyes open..."
        l "What?!"
        me "I..."
        l "Hey! Look at her arm! What's that?"
        scene corpse 14
        l "She has a tattoo on her arm!" with dissolve
        me "What? Oh, It's true... a tattoo of a... zero?"
        l "A green zero!"
        scene corpse 13
        me "Oh my god... What kind of a psycho are we dealing with..." with dissolve
    jump bodyh


label officeh:
    if officefirst:
        scene office 0b
        with Dissolve (1)
        $ renpy.pause ()
        me "Ok, this is the office of the head of the hospital. If Lilith has ever been here, she must have been in this room." with dissolve
    play sound "door2.ogg" fadeout .4
    scene office 0
    with Dissolve (1.5)
    $ renpy.pause ()
    if officefirst:
        $ officefirst = False
        $ codeh = True
        me "Ok, there's got to be something in here. Look through the shelves, I'll go see if that computer is still working." with dissolve
        j "Ok!"
        l "Ok!"
        scene office 1 
        with Dissolve (1)
        play sound "thunder2.ogg"
        me "Hmmm..." with dissolve
        me "(This computer looks far too new... Lilith probably brought it with her.)"
        me "(What's this?... It looks like some kind of... diary?)"
        scene office 4 
        me "Hey, check this out:" with dissolve
        me "{i}August 24th: We've finished relocating the operations center. The place is such a wreck, but it's isolated from the population. According to my calculations, we should be done in less than a year."
        me "{i}December 7th: Subjects who survive phase 2 have been placed in the Infectious disease ward because of the risk of transmission."
        me "{i}January 10th: 3 guards were killed today by a subject in phase 4. Two more have fled. The organization will take care of them. We can't have loose ends. Not now."
        me "{i}March 1st: I've made it. The AAR is completed. The agent binds to DNA without causing chain mutations. Astaroth will be pleased. The final compound has been stored in a test tube in the basement under the Infectious disease ward."
        me "And... that's the last entry."
        me "I think we got it. What we're looking for is in that basement, under Infectious diseases."
        me "Did you find anything else?"
        scene office 5
        l "Only this weird note..."
        play sound "thunder2.ogg"
        l "{i}Five numbers. One path. White, red, green, grey, black. That's the order. That's the way."
        scene office 6
        l "Do you think this could mean something?"
        me "I don't think so, but... who knows."
        scene office 3 
        j "Hey, do you see that?"
        j "Someone painted a three in this book's cover..."
        j "This might mean something..."
        me "I don't know, maybe we're just over-thinking this. Let's go to infectious diseases."
        j "Yeah, that'll be best."
        scene office 0
        with Dissolve (1)
        $ renpy.pause ()
    if codehh and officetwo:
        $ officetwo = False
        scene office 3 
        j "Yeah, there's definitely a three on this book's cover." with dissolve
        scene office 4
        me "I'll see if there's something else on the computer... you search the room."
        l "I think I got it... Turn around and look."
        scene office 2
        me "What? The painting?" with dissolve
        me "Oh my fucking god. Good eye, Lauren!"
        me "We got an eight! A... grey eight? That's grey, isn't it?"
        j "It looks grey to me."
        me "Ok! We're nearly there..."  
        j "So..."
    if codehh:
        scene office 3
        j "A white three..." with dissolve
        scene office 2
        me "And a grey eight..." with dissolve
    menu:
        with dissolve
        "Go back to the corridor{color=#00ff00} (Step [hos_step] of 32){/color}" if (hos_step == 6 or hos_step == 28): #6 28
            $ hos_step += 1
            jump secondfloor
        "Go back to the corridor"if (hos_step != 6 and hos_step != 28):
            jump secondfloor             
 
 
 
label lilith:
    play sound "electroniclock.ogg"
    scene lab 2 
    with Dissolve (1)
    pause 2.2
    j "It works! We did it!" with dissolve
    if bodythird == False or uv3 == False:
        j "How did you figure out the full code?! We didn't find all the numbers!"
        me "I don't know, I had a vision... As if someone had told me..."
        j "WOW."
    ast "AHAHaHahAhAh YES!... y-you did it!"
    menu:
        with dissolve
        "Turn around{color=#00ff00} √√√{/color}":
            play sound "thunder2.ogg"
    scene lilith 1
    with Dissolve (1.5)
    me "(Oh fuck...)" with dissolve
    ast "Y-you solved the RIDDLE! The riddle of 93!"
    scene lilith 2
    me "Erm... W-who are you?"
    scene lilith 1
    nt "Whoo? Mee? I'm 93! Yes, I am. I just said it, yes..."
    scene lilith 2
    me "You painted all those numbers?"
    scene lilith 1
    nt "Yeees! 93 did it!"
    scene lilith 2
    me "You... you killed the woman with a tattoo on her arm?"
    scene lilith 3
    nt "NO. 93 did not do such a thing. No. 93 didn't kill her. No, no. The ashen lady did it. Yes..." 
    j "The... ashen lady?"
    scene lilith 5
    nt "YEES! The ashen lady, yes. She hurt us. Do you know her?"
    scene lilith 4
    j "N-no..."
    scene lilith 5
    nt "No? No. You don't. You shouldn't. She's bad. Yes. She'd hurt you. You're too small, yes."
    scene lilith 4
    j "I... Is the ashen lady here?"
    scene lilith 5
    nt "YES! She is. She's locked up. In her own basement, yes. 93 locked her up. She was bad. I changed the code, yes! Now she can't get out, no, no..."
    nt "I hid the code. I made a riddle! yes! You solved it! Did you like my riddle?"
    scene lilith 4
    j "...y-yes. A lot."
    scene lilith 5
    nt "YES! You did! You are good, little one, yes."
    scene lilith 7
    me "Okay 93... We... we have to go to the basement. There's... something there we need." with dissolve
    scene lilith 6
    nt "The basement? Yes! Sure. But be careful, the ashen lady will be angry! She's been there for a loooong time, yes..."
    scene lilith 2
    me "Okay... we will. Thank you, 93." with dissolve
    scene lilith 1
    nt "Yes, thank you, yes... You three have fun, yes! Goodbye!"
    scene lilith 8
    with Dissolve (1.5)
    me "Wow..." with dissolve
    l "The horrible things they must have done to that poor man for him to end up like that..."
    me "He was quite nice, though."
    me "I wonder if we’ll ever see him again."
    scene lilith 9
    me "Anyway, we have that last dare to complete. There's no going back." with dissolve
    menu:
        with dissolve
        "Get into the basement{color=#00ff00} √√√{/color}":
            play sound "heavydoor.ogg"
    scene lilith 10
    with Dissolve (3)
    pause 1
    play music "cave.ogg"
    $ renpy.pause ()
    me "(Whispering) Ok, Lilith is here, as is the compound AAR. We have to be very careful." with dissolve
    if gunme:
        me "I have the gun, just stay behind me."
        j "Ok!"
    if gunjudie:
        me "Judie, keep the gun close at hand."
        j "Erm... ok..."
    if gunlauren:
        me "Lauren, keep the gun close at hand."
        l "Ok!"
    me "Do you also have the amnesia spray ready?"
    j "Yes!"
    me "Ok..."
    scene lilith 11
    with Dissolve (1.5)
    $ renpy.pause ()
    scene lilith 12
    with Dissolve (1.5)
    $ renpy.pause ()
    me "I wonder what's in those containers?" with dissolve
    l "[me]! Come here! I think it's this way!"
    scene lilith 12b
    with Dissolve (1.5)
    me "Hmm... Restricted area. Interesting..." with dissolve
    scene lilith 13
    with Dissolve (1)
    j "Look, there's even an elevator!" with dissolve
    l "The door seems to be stuck."
    me "I think I can slip in."
    scene lilith 14 
    with Dissolve (1)
    $ renpy.pause ()
    scene lilith 15 
    me "Man, you have to be kidding me!" with dissolve
    l "What is it?"
    me "There're 6 floors! This place is fucking huge!"
    l "You should come out of there... the ground looks like it's about to crack..."
    scene lilith 16 
    me "Don't worry, I have..." with dissolve
    me "Oh shit..."
    play sound "creak.ogg"
    pause 1.5
    scene lilith 16b 
    pause .5
    scene lilith 16c 
    pause .5
    scene black 
    $ renpy.pause ()
    me "Ahhh..." with dissolve
    scene lilith 17
    with Dissolve (2)
    scene black 
    with Dissolve (2)
    scene lilith 17
    with Dissolve (2)
    j "[me]!! Oh my fucking god! HE'S DEAD!" with dissolve
    l "WHAT?!"
    j "(Crying) HE'S DEAAAAAD!"
    me "Hmmm...."
    scene lilith 20
    with Dissolve (1)
    $ renpy.pause ()
    scene lilith 18 with dissolve
    me "I'm not dead!" with dissolve
    j "HE'S ALIVE!"
    j "HE'S ALIVE, LAUREN!"
    l "It's a miracle!"
    me "Come on, this isn't such a big deal!"
    me "But I can't climb up... Is there a rope or something around there?"
    l "Yeah, I think I saw one somewhere."
    j "Ok! We'll go find it! Don't move from there!"
    me "Ok."
    scene lilith 19 with dissolve
    $ renpy.pause ()
    scene lilith 20 with dissolve
    me "(I hope the flashlight is still working...)" with dissolve 
    play sound "switch.ogg"
    scene lilith 21 
    me "(Nice.)"
    me "(Oh no... this place is a...)"
    li "6. . . 1. . . 7. . . 4. . ."
    li "Esse. . . Est. . . Deus. . ."
    me ". . ."
    scene lilith 22
    with Dissolve (1)
    li "Et finivit regnum dei." with dissolve
    me "Hello... Lilith? Is that you?"
    li "Esse est deus..."
    scene lilith 23
    with Dissolve (1)
    me "Lilith?" with dissolve
    li "*Muttering*"
    me "Ms. Swango?"
    scene lilith 24
    li "Hm?" with dissolve
    scene lilith 25
    li "Astaroth! Is that you, Astaroth? I knew you'd come!" with dissolve
    scene lilith 26
    me "Erm... yes."
    scene lilith 25
    li "I... I have it! I have the AAR. For you! But then... I was... locked in." 
    scene lilith 26
    me "Do you have it here?"
    scene lilith 27
    li "Yes! I always bring it with me!" with dissolve
    scene lilith 28
    me "I... I need it."
    scene lilith 29
    li "Of course... It's yours." with dissolve
    scene lilith 30
    li "Take it." with dissolve
    scene lilith 31 with dissolve
    menu:
        with dissolve
        "Take the Compound AAR{color=#00ff00} √√√{/color}":
            scene lilith 28 with dissolve
    me "Ok... thank you Lilith." with dissolve
    me "Now... come with me. We need to get out of here."
    scene lilith 27
    li "Oh no... I can't. I've been exposed for too long to the non-purified agents down here. And my genotype is not compatible so I'm already dead."
    scene lilith 28
    me "What?..."
    scene lilith 27
    li "But I'm happy because my work was completed. You should leave before I get transmuted in a hypermetabolic chain reaction."
    scene lilith 33
    li "*Coughing*" with dissolve
    scene lilith 34
    li "I don’t want you to see me like that." with dissolve
    me "What the fuck... Ok miss, you are clearly ill, so you need to get out of here NOW."
    me "I'll take you to a hospital."
    scene lilith 35 
    li "What?.... What are you saying, Astaroth? This was my mission..." with dissolve
    me "Look, I'm not Astaroth, and you have no mission to accomplish! LET'S GET OUT!"
    scene lilith 36
    li "You... you are not Astaroth? Who are you? Give me back the AAR, give me..." with dissolve
    scene lilith 37
    li "*Coughing violently*" with dissolve
    scene lilith 38
    me "Ms. Swango, ASTAROTH IS A CROOK, A LIAR. You don't have to die for him! LET'S GO!" with dissolve
    me "Do you really want to die here?!"
    li "*Still coughing*"
    scene lilith 39 with dissolve
    li "(Breathing heavily) Y-you... you don't understand... HE IS THE TRUTH." with dissolve
    li "You don't know anything..."
    me "Oh my fucking god..."
    scene lilith 40 with dissolve
    me "O-ok... If you don’t want to come, I'm going by myself." with dissolve
    scene lilith 41 with dissolve
    me "JUDIE! LAUREN! WHERE'S THE ROPE?!"
    j "Here! We're tying it to a pipe! Hold on!"
    stop music
    play sound "monster1.ogg" 
    $ renpy.pause ()
    scene lilith 42
    with Dissolve (1.5)
    me "What the fuck was that..." with dissolve
    me "And what the hell has come out of her back?!"
    scene lilith 43
    with Dissolve (1)
    me "...L-lilith?" with dissolve
    scene lilith 44
    with Dissolve (1.5)
    me "WHAT THE...." with dissolve
    play sound "monster1.ogg" 
    scene lilith 45 
    with Dissolve (1.5)
    play music "chase.ogg"
    me "WHAT THE FUCK?!" with hpunch
    scene lilith 46
    play sound "fall.ogg"
    me "What the hell is that thing?!"
    play sound "monster2.ogg"
    scene lilith 47
    me "AHHHH!" with hpunch
    me "FUCK THIS SHIT!"
    me "THE ROPE!!"
    l "There you go!"
    scene lilith 48 
    me "THANK GOD!"
    scene lilith 49 
    with Dissolve (2)
    j "Hey! Thank goodness you're all right! Is there something down there?" with dissolve
    scene lilith 50
    me "(Panting) The... the..."
    me "The AAR..."
    me "L-lilith..."
    scene lilith 49
    j "Lilith?! Did you talk to her?"
    scene lilith 50
    me "Yes! But she's... she has..."
    play sound "monsterscream.ogg"
    scene lilith 51
    with Dissolve (2)
    $ renpy.pause ()
    j "What was that?..." with dissolve
    me "WE NEED TO GET OUT OF HERE! NOW! RUN!"
    scene lilith 52 
    with Dissolve (1)
    $ renpy.pause ()
    scene lilith 53 
    with Dissolve (1)
    $ renpy.pause ()
    play sound "heavydoor.ogg"
    scene lilith 8 
    with Dissolve (1)
    $ renpy.pause ()
    scene lilith 54 
    with Dissolve (1)
    $ renpy.pause ()
    scene lilith 55 
    with Dissolve (1)
    l "Ok, the door's right here! Let's go!" with dissolve
    scene lilith 57
    l "OH MY GOD, WHERE'S JUDIE?!" with dissolve
    me "WHAT?!"
    scene ww 0c
    me "Judie?!" with hpunch
    scene lilith 56
    me "Okay, calm down..."
    $ flashfast = Fade(0.15, 0, 0.15, color="#FFFFFF")
    $ flashfaster = Fade(0.04, 0, 0.04, color="#FFFFFF")
    menu:
        with dissolve
        "Go back for her{color=#00ff00} √√√{/color}":
            me "We have to go back for her."
            scene lilith 57
            l "Of course we do!"
            scene ww 0c 
            me "Stay behind me..."
            scene ww 0
            with Dissolve (1)
            me "JUDIE! WHERE ARE YOU?!" with dissolve
            scene lilith 58
            j "I'm here!" with dissolve
            me "Dammit Judie! Where were you?"
            j "I'm sorry! You two run too fast! I got nervous and I took a wrong turn!"
            me "Ok, LET'S GO!"
            play sound "monsterscream.ogg"
            stop music fadeout 2.0
            play music "rain2.ogg" fadein 0.5
            scene lilith 59 with dissolve
            $ renpy.pause ()
            me "Don't move an inch..." with dissolve
            play sound "monster1.ogg"
            scene lilith 60
            with Dissolve (2.5)
            $ renpy.pause ()
            play sound "monster2.ogg"
            scene lilith 61
            with Dissolve (2.5)
            $ renpy.pause ()
            play sound "monster1.ogg"
            scene lilith 62
            with Dissolve (1)
            $ renpy.pause ()
            scene lilith 63
            with Dissolve (1)
            $ renpy.pause ()
            play sound "monster2.ogg"
            scene lilith 64
            with Dissolve (1.5)
            li ". . ." with dissolve
            if gunme:
                me "HEY!"
                scene lilith 65b        
                me "YOU! WHATEVER YOU ARE, STAY AWAY FROM MY LITTLE SISTER!" with dissolve
                play sound2 "monster2.ogg"
                scene lilith 65bb
                with Dissolve (1)
                li ". . ." with dissolve
                play sound "monster2.ogg"
                scene lilith 66b
                with Dissolve (1.5)
                menu:
                    with Dissolve (2)
                    "SHOOT{color=#00ff00} √√√{/color}":
                        play sound2 "gunshot3.mp3"                     
                scene lilith 67b with flashfaster
                scene lilith 67b with hpunch
                        
                play sound "monsterscream.ogg"
                scene lilith 68 
                with Dissolve (2)
                me "OK! NOW! MOVE, MOVE, MOVE! I'll distract her!" with dissolve
                l "But..."
                me "Just leave! Please!"
                l "O-ok... We'll be waiting outside!"
                play sound "monster2.ogg"
                scene lilith 69
                with Dissolve (3.5)
                play sound "monster1.ogg"
                me "Oh shit... Ok [me], this is how we die..." with dissolve
                me "Epic enough, to be honest." 
            if gunlauren:
                l "HEY!"
                scene lilith 65a
                l "YOU! WHATEVER YOU ARE, STAY AWAY FROM MY SISTER!" with dissolve
                play sound "monster2.ogg"
                scene lilith 66a 
                with Dissolve (1)
                li ". . ." with dissolve
                me "Shoot her!"
                play sound2 "gunshot3.mp3"
                scene lilith 67a with flashfaster
                scene lilith 67a with hpunch
                pause .4
                play sound "monsterscream.ogg"
                scene lilith 68 
                with Dissolve (2)
                me "OK! NOW! MOVE, MOVE, MOVE! I'll distract her!" with dissolve
                l "But..."
                me "Just leave! Please!"
                l "At least take the gun!"
                me "Ok! Go!"
                play sound "monster2.ogg"
                scene lilith 69
                with Dissolve (3.5)
                play sound "monster1.ogg"
                me "Oh shit... Ok [me], this is how we die... Epic enough, to be honest." with dissolve
            if gunjudie:
                me "J-judie... use the gun..."
                l "Judie..."
                j "I..."
                j "...c-can't m-m-move m-my arms..."
            scene lilith 70
            nt "aHahahHAHah, yes! The ashen lady is angry, yes! She tasted her own medicine! It doesn't taste good, no!"
            scene lilith 71
            play sound "monster2.ogg"
            pause 0.4
            scene lilith 72 
            with Dissolve (1.5)
            nt "She's doomed now, yes she is!" with dissolve
            scene lilith 73
            nt "93 beat the ashen lady, yes! hAahAhaHaHa..." with dissolve
            scene lilith 74 
            with Dissolve (.8)
            play sound "monsterscream.ogg"
            scene lilith 75 
            with Dissolve (1)
            scene lilith 76 
            with Dissolve (1)
            scene lilith 77 
            with Dissolve (1)
            $ renpy.pause ()
            me "(Oh Jesus Christ Almighty... That guy just saved my life...)" with dissolve
            scene lilith 54
            play sound2 "thunder2.ogg"
            me "(I'm getting the hell out of here!)" with dissolve
            scene lilith 78 
            with Dissolve (1)
            me "GOOD BYE ST.AUGUSTINE'S!" with dissolve
            me "SEE YOU NEVER!" 
            play sound "doorslam.ogg"
            stop music fadeout 3.5
            scene white 
            with Dissolve (3.5)
        "Abandon her":
            $ judiepath = False
            $ judiehospitalback = False
            me "We... we have to go..."
            scene lilith 57
            l "WHAT?!"
            scene lilith 56
            me "If we go back we'll all die!"
            scene lilith 78
            me "I'm getting the hell out!" with dissolve
            play sound "doorslam.ogg"
            stop music fadeout 3.5
            scene white 
            with Dissolve (3.5)

    jump rebeccasex