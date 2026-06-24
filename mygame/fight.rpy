
label fight:
    stop music3 fadeout 5
    scene fight18 with dis
    t "You just signed your own death warrant, buddy." with dissolve
    t "Prepare to go back home in a wheelchair."
    window hide
    play music3 "sport.ogg"
    show tom 100
    with Dissolve (2)
    show you 100
    with Dissolve (2)

label fight00:
    show fight19  behind tom, you with dissolve
    t "I WILL END YOU!"
    window hide
    show fight1_0 behind tom, you
    with Dissolve (1)
    $ renpy.pause ()
    $ tom_points = 90
    $ you_points = 101

label fight0:
    menu:
        with dissolve 
        with dissolve
        "BLOCK":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight1_2 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
            jump fight3
        "DODGE{color=#00ff00} √√√{/color}":
            play sound "dodge.ogg"
            show fight1_1 behind tom, you with dissolve
            $ renpy.pause ()
            show fight20 behind tom, you with dissolve
            $ renpy.pause ()
            jump fight2
        "ATTACK":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight1_2 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
            jump fight3

label fight2:
    menu:
        with dissolve
        "REMAIN ON GUARD":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight32 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
        "ATTACK{color=#00ff00} √√√{/color}":
            $ tom_points -= 24
            play sound "punch.ogg"
            show fight21 behind tom, you with dissolve
            if tom_points >=80:
                show tom 80
            elif tom_points >=60:
                show tom 60
            elif tom_points >=40:
                show tom 40
            elif tom_points >=20:
                show tom 20
            elif tom_points >=1:
                show tom 1
            elif tom_points <=1:
                $ renpy.pause ()
                jump fightend
            $ renpy.pause ()

label fight3:
    show fight30 behind tom, you with dissolve
    t "TAKE THIS, MOTHERFUCKER!"
    window hide
    menu:
        with dissolve
        "BLOCK LEFT":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight32 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
        "BLOCK TOP":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight32 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
        "BLOCK DOWN":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight32 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
        "BLOCK RIGHT{color=#00ff00} √√√{/color}":
            play sound "parry.ogg"
            show fight31 behind tom, you with dissolve
            $ renpy.pause ()
    show fight40 behind tom, you with dissolve
    t "EAT THIS ONE, ASSHOLE!"
    window hide
    menu:
        with dissolve
        "BLOCK LEFT":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight322 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
        "BLOCK TOP{color=#00ff00} √√√{/color}":
            play sound "parry.ogg"
            show fight312 behind tom, you with dissolve
            $ renpy.pause ()
        "BLOCK DOWN":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight322 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
        "BLOCK RIGHT":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight322 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()

    show fight50 behind tom, you with dissolve
    t "I'LL KEEP KICKING YOUR ASS UNTIL YOU KNEEL BEFORE ME AND KISS MY BOOTS!"
    me "I'd rather be dead!"
    window hide
    menu:
        with dissolve
        "PARRY LEFT":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight323 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
            jump fight5
        "PARRY TOP{color=#00ff00} √√√{/color}":
            play sound "parry.ogg"
            show fight313 behind tom, you with dissolve
            $ renpy.pause ()
            jump fight4
        "PARRY DOWN":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight323 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
            jump fight5
        "PARRY RIGHT":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight323 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
            jump fight5

label fight4:
    menu:
        with dissolve
        "REMAIN ON GUARD":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight323 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
        "COUNTERATTACK{color=#00ff00} √√√{/color}":
            $ tom_points -= 24
            play sound "punch.ogg"
            show fight51 behind tom, you with dissolve
            if tom_points >=80:
                show tom 80
            elif tom_points >=60:
                show tom 60
            elif tom_points >=40:
                show tom 40
            elif tom_points >=20:
                show tom 20
            elif tom_points >=1:
                show tom 1
            elif tom_points <=1:
                $ renpy.pause ()
                jump fightend
            $ renpy.pause ()

label fight5:
    show fight60 behind tom, you with dissolve
    t "AFTER I'M FINISHED WITH YOU, EVEN YOUR OWN MOTHER WON'T RECOGNIZE YOU!"
    me "You do a lot of talking but not a lot of action."
    t "I'LL SHUT YOUR FUCKING MOUTH BY BEATING IT !!!"
    window hide
    menu:
        with dissolve
        "BLOCK LEFT UPPERCUT":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight62 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
        "BLOCK RIGHT UPPERCUT":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight62 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
        "DODGE{color=#00ff00} √√√{/color}":
            play sound "dodge.ogg"
            show fight61 behind tom, you with dissolve
            $ renpy.pause ()
        "COUNTERATTACK":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight62 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()

    show fight70 behind tom, you with dissolve
    t "IT'S TIME TO FINISH THIS!"
    me "Show me what you got scumbag!"
    window hide
    menu:
        with dissolve
        "PARRY LEFT{color=#00ff00} √√√{/color}":
            play sound "parry.ogg"
            show fight71 behind tom, you with dissolve
            $ renpy.pause ()
            jump fight6
        "PARRY RIGHT":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight72 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
            jump fight7
        "PARRY TOP":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight72 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
            jump fight7
        "PARRY DOWN":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight72 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
            jump fight7

label fight6:
    menu:
        with dissolve
        "REMAIN ON GUARD":
            $ you_points -= 20
            play sound "punch.ogg"
            show fight72 behind tom, you with dissolve
            if you_points >=80:
                show you 80
            elif you_points >=60:
                show you 60
            elif you_points >=40:
                show you 40
            elif you_points >=20:
                show you 20
            elif you_points >=1:
                show you 1
            elif you_points <=1:
                $ renpy.pause ()
                jump fightdefeat
            $ renpy.pause ()
        "COUNTERATTACK{color=#00ff00} √√√{/color}":
            $ tom_points -= 24
            play sound "punch.ogg"
            show fight80 behind tom, you with dissolve
            if tom_points >=80:
                show tom 80
            elif tom_points >=60:
                show tom 60
            elif tom_points >=40:
                show tom 40
            elif tom_points >=20:
                show tom 20
            elif tom_points >=1:
                show tom 1
            elif tom_points <=1:
                $ renpy.pause ()
                jump fightend
            $ renpy.pause ()
label fight7:
    show fight17 behind tom, you with dissolve
    me "What’s up, Tom? You’re looking a little sluggish. You tired?" with dissolve
    show fight192 behind tom, you with dissolve
    t "SHUT YOUR DAMN MOUTH!"
    scene fight19 behind tom, you
    if you_points >=100:
        show you 100
    elif you_points >=80:
        show you 80
    elif you_points >=60:
        show you 60
    elif you_points >=40:
        show you 40
    elif you_points >=20:
        show you 20
    elif you_points >=1:
        show you 1
    if tom_points >=100:
        show tom 100
    elif tom_points >=80:
        show tom 80
    elif tom_points >=60:
        show tom 60
    elif tom_points >=40:
        show tom 40
    elif tom_points >=20:
        show tom 20
    elif tom_points >=1:
        show tom 1
    me "Hah! You keep doing the same thing, like a brainless ape. I can predict all your movements."
    jump fight0


label fightdefeat:
    scene fight defeat with dissolve
    $ renpy.pause ()
    t "Hahahaha what's the problem, big guy?"
    t "You can't continue?"
    t "Pathetic."
    t "What a loser."
    t "Do yourself a favour and go home to cry."
    if inc is True:
        t "And tell the whore of your sister that I'm gonna fuck her in all her holes very soon."
    else:
        t "And tell that little whore you live with that I'm gonna fuck her in all her holes very soon."
    me "That's not gonna happen."
    t "Eh? What did you say?"
    scene fight defeat2 with dissolve
    me "I said I will continue to get off the ground until your face is fucking smashed."
    show tom 100
    show you 100
    jump fight00

label fightend:
    scene fightend0
    with Dissolve (1)
    me "Hey man, are you ok? You don't look so good." with dissolve
    scene fightend1
    t "YOU SON OF A BITCH!" with hpunch
    t "I’VE HAD ENOUGH OF YOU!"
    t "DO YOU WANNA PLAY? GOOD! LET'S DANCE!"
    me "Tom, you’ve lost it mate. What the fuck are you doing with that thing?"
    t "WHAT AM I DOING? I'M GONNA CUT THAT COCKY ATTITUDE RIGHT OUT OF YOU, THAT’S WHAT!"
    t "YOU ARE GONNA REGRET EVERYTHING YOU SAID WITH YOUR DAMNED MOUTH."
    me "If you’re not as stupid as you look, I suggest you put the knife down before one of us ends up in jail."
    t "DON’T YOU EVER SHUT UP?!"
    me "You're not thinking straight anymore, Tom."
    me "Put... {w}the knife... {w}down."
    scene fightend2
    t "DON'T TELL ME WHAT TO DOOOO !!!" with hpunch
    me "(Now.)"
    menu:
        with dissolve
        "FINISH HIM{color=#00ff00} √√√{/color}":
            play sound "punch.ogg"
            scene fightend3
            $ renpy.pause ()
            scene fightend4
            with Dissolve (1)
            $ renpy.pause ()
            play sound "fall.ogg"
            scene fightend5 with dissolve
            $ renpy.pause ()
            t ". . . ." with dissolve
            me "Now stay there till you clear your head."
            me "And if I ever see you bothering Lauren again, I will beat you up so much that everything will look blurred to you forever."
            me "Do you understand?"
            t ". . . ."
            me "Good."
    scene fightend6
    with Dissolve (1.2)
    stop music3 fadeout 6
    me "(Aww fuck, I've lost track of those men because of this garbage.)" with dis
    me "(Whoever they were, they're long gone by now.)"
    me "(However, on second thought, perhaps I was mistaken.)"
    me "(I was probably mistaken, actually.)"
    me "(I only saw them from a distance and it's true that at first that man looked a lot like my father, but it wouldn't be the first time I mistakenly thought I recognized someone.)"
    me "(He didn't even have the same haircut.)"
    me "(The man I saw seemed to have his head shaved.)"
    me "(There's no way my father changes his haircut, he has had the same one for over 20 years.)"
    me "(Maybe I should stop watching gangster movies. I see secret organizations wherever I look.)"
    me "(Anyway, I should get going, Lauren will be waiting for me.)"
    me "(I'll leave this idiot here. He'll wake up himself.)"
    $ renpy.pause ()

jump park
