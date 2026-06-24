################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"






################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

style block1_multiple2_say_window:
    yalign 0.82

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    outlines [ (2, "#000000") ]
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    outlines [ (2, "#000000") ]
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.4
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            #textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.42
        if not main_menu:
            textbutton _("Paths") action ShowMenu("pointscreen")

    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.49
        if not main_menu:
            textbutton _("Gallery") action ShowMenu("gallery")


    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.85

        spacing 20

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("Save") action ShowMenu("save")


        textbutton _("Load") action ShowMenu("load")


        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        if main_menu:
            textbutton _("Credits") action ShowMenu("about")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    imagemap:
        ground "titleimage"
        hover "main_menu2.png"

        hotspot (403, 884, 846, 109) action OpenURL("https://www.patreon.com/user?u=24799077") hovered [ Play ("soundlow", "button2.mp3")]
        hotspot (73, 43, 133, 111) action OpenURL("https://www.patreon.com/user?u=24799077") hovered [ Play ("soundlow", "button2.mp3")]
        hotspot (71, 172, 133, 121) action OpenURL("https://subscribestar.adult/caribdis") hovered [ Play ("soundlow", "button2.mp3")]
        hotspot (68, 306, 136, 128) action OpenURL("https://discord.gg/g326cS4") hovered [ Play ("soundlow", "button2.mp3")]

    ## This empty frame darkens the main menu.


    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation



style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:

    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:

    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.game_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"
        action Return()





    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 0.3
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.
screen about4():
    tag menu
    use game_menu(_("Credits")):
        vbox:
            spacing 36
            xpos 70
            ypos -70
            label "{size=65}Special Thanks" xalign .5
        vbox:
            spacing 55
            xpos 70
            ypos 60
            text ("{size=40}{color=c0a545}Created by {color=BFBFBF} Caribdis")
            text ("{size=40}{color=c0a545}Proofread by{color=BFBFBF} Nebula {color=c0a545}&{color=BFBFBF} Dipper Pines")
            text ("{color=BFBFBF}A huge thanks to {color=c0a545}Frost{color=BFBFBF},{color=c0a545} Turska {color=BFBFBF}& {color=c0a545}Nebula {color=BFBFBF}for being the best moderators in all of Discord!")
            text ("{color=BFBFBF}Big thanks to {color=c0a545}Ixalon {color=BFBFBF}for his great Android ports!")
            text ("{color=BFBFBF}And thank you so much to every dev, modder, artist or user that has helped me \nin one way or another!")
            text ("{color=BFBFBF}This visual novel is free and always will be. \nIf you paid any money for it, you've been scammed. \nIf you'd like to support this project, you can go to my Patreon or Subscribestar pages!")
            text ("{size=40}{color=c0a545}Thank you for playing!")
screen about3():
    tag menu
    use game_menu(_("Credits")):
        vbox:
            spacing 36
            xpos 70
            ypos -120
            label "{size=65}Special Thanks" xalign .5
            label ("{size=40}I would like to thank the people who have made this game possible: \nMy most generous supporters. Without you, this would not exist. \nYou all are the best!")
        imagebutton:
            yalign .6
            xpos 1250
            idle "credits"
            hover "credits2"
            action ShowMenu("about4")
        add "sons.png" ypos 120
screen about2():
    tag menu
    use game_menu(_("Credits")):
        vbox:
            spacing 36
            xpos 70
            ypos -120
            label "{size=65}Special Thanks" xalign .5
            label ("{size=40}I would like to thank the people who have made this game possible: \nMy most generous supporters. Without you, this would not exist. \nYou all are the best!")
        imagebutton:
            yalign .6
            xpos 1250
            idle "credits"
            hover "credits2"
            action ShowMenu("about3")
        add "gods.png" ypos 110
screen about():
    tag menu
    use game_menu(_("Credits")):
        vbox:
            spacing 36
            xpos 70
            ypos -120
            label "{size=65}Special Thanks" xalign .5
            label ("{size=40}I would like to thank the people who have made this game possible: \nMy most generous supporters. Without you, this would not exist. \nYou all are the best!")
        imagebutton:
            yalign .6
            xpos 1250
            idle "credits"
            hover "credits2"
            action ShowMenu("about2")
        add "demons.png" ypos 110

## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
            #    vbox:
                #    style_prefix "radio"
                #    label "Language"

                #    textbutton "English" text_font "ade.ttf" action Language(None) ###idioma por defecto
                    #textbutton "Russian" text_font "SimSun.ttf" action Language("russian") #"INGLES" nombre visible, ("ingles") nombre de la carpeta del idioma
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    #if config.has_voice:
                     #   label _("Voice Volume")

                      #  hbox:
                       #     bar value Preference("voice volume")

                        #    if config.sample_voice:
                         #       textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900

################################################################################################ Gameshow
screen gameshowred:
    add "gameshow_red.png" xalign 0.97 yalign 0.02
    add "gameshow_blue.png" xalign 0.03 yalign 0.02
    frame xpos 145    ypos 65:
        text "{size=+15}{b}[game_blue]"
    frame xpos 1680    ypos 65:
        text "{size=+15}{b}[game_red]"

################################################################################################ Sex scenes buttons

screen fasteriris1:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("irisextwo")
            xalign 0.945
            yalign 0.9
screen fasterlauren1:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("laurensexI")
            xalign 0.945
            yalign 0.9
screen fasterlauren2:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("laurensexII")
            xalign 0.945
            yalign 0.9
screen fasterlauren3:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("laurensexIII")
            xalign 0.945
            yalign 0.9
screen fasterlauren4:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("laurensexIV")
            xalign 0.945
            yalign 0.9
screen fasterlauren5:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("laurensexV")
            xalign 0.945
            yalign 0.9
screen fasteriris2:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("irisexthree")
            xalign 0.945
            yalign 0.9
screen fasteriris3:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("irisexfour")
            xalign 0.945
            yalign 0.9
screen fasteriris4:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("irisexfive")
            xalign 0.945
            yalign 0.9
screen fasterjasmine1:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("jastrain1")
            xalign 0.945
            yalign 0.9
screen fasterjasmine2:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("jastrain2")
            xalign 0.945
            yalign 0.9
screen fasterjasmine3:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("jastrain3")
            xalign 0.945
            yalign 0.9
screen fasterjasmine4:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("jastrain4")
            xalign 0.945
            yalign 0.9


screen fastercarla1:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("carlafaster1")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("carlaview1b")
            xalign 0.07
            yalign 0.9

screen fastercarla1b:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("carlaview2b")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("carlaview1")
            xalign 0.07
            yalign 0.9

screen fastercarla2:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("carlafaster2")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("carlaview2b")
            xalign 0.07
            yalign 0.9

screen fastercarla2b:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("carlafaster2b")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("carlafaster1")
            xalign 0.07
            yalign 0.9

screen viewcarla3:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("carlafaster2b")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "position"
            hover "position1"
            action Jump ("positionc1")
            xalign 0.95
            yalign 0.9
screen viewcarla3b:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("carlafaster2")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "position"
            hover "position1"
            action Jump ("positionc1")
            xalign 0.95
            yalign 0.9

screen fastercarla4:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("carlafaster5")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("carlafaster4b")
            xalign 0.07
            yalign 0.9
screen fastercarla4b:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("carlafaster5b")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("carlafaster4")
            xalign 0.07
            yalign 0.9

screen fastercarla5:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("carlafaster6")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("carlafaster5b")
            xalign 0.07
            yalign 0.9
screen fastercarla5b:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("carlafaster6b")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("carlafaster5")
            xalign 0.07
            yalign 0.9

screen fastercarla6:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("carlafaster7")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("carlafaster6b")
            xalign 0.07
            yalign 0.9
screen fastercarla6b:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("carlafaster7b")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("carlafaster6")
            xalign 0.07
            yalign 0.9

#############################################################################


screen judiescreen1:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("judiefaster1_2")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("judiefaster1b")
            xalign 0.07
            yalign 0.9
screen judiescreen1b:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("judiefaster1_2b")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("judiefaster1")
            xalign 0.07
            yalign 0.9

screen judiescreen2:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("judiefaster1_3")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("judiefaster1_2b")
            xalign 0.07
            yalign 0.9
screen judiescreen2b:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("judiefaster1_3b")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("judiefaster1_2")
            xalign 0.07
            yalign 0.9

screen judiescreen3:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("judiefaster2_2")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("judiefaster2b")
            xalign 0.07
            yalign 0.9
screen judiescreen3b:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("judiefaster2_2b")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("judiefaster2")
            xalign 0.07
            yalign 0.9


screen judiescreen4:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("judiefaster2_2b")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "position"
            hover "position1"
            action Jump ("judiepc1")
            xalign 0.95
            yalign 0.9
screen judiescreen4b:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("judiefaster2_2")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "position"
            hover "position1"
            action Jump ("judiepc1")
            xalign 0.95
            yalign 0.9


screen judiescreen5:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("judiefaster3b")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("judiefaster3_2")
            xalign 0.95
            yalign 0.9
screen judiescreen5b:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("judiefaster3")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("judiefaster3_2b")
            xalign 0.95
            yalign 0.9

##########################################################################

screen slaurenbath1:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("llaurenbath1")
            xalign 0.95
            yalign 0.9
screen slaurenbath2:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("llaurenbath2")
            xalign 0.95
            yalign 0.9
screen slaurenbath3:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("laurenbatho1b")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("laurenbatho2")
            xalign 0.95
            yalign 0.9
screen slaurenbath3b:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("laurenbatho1")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("laurenbatho2b")
            xalign 0.95
            yalign 0.9
screen slaurenbath4:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("laurenbatho2b")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("laurenbathcum")
            xalign 0.95
            yalign 0.9
screen slaurenbath4b:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("laurenbatho2")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("laurenbathcum")
            xalign 0.95
            yalign 0.9

#################################################################

screen fasterbeach1:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("beachfaster1")
            xalign 0.95
            yalign 0.9

screen fasterbeach2:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("beachfaster2")
            xalign 0.95
            yalign 0.9

screen fasterbeach3:
    imagebutton:
            idle "view4"
            hover "view4b"
            action Jump ("beachfaster3c")
            xalign 0.06
            yalign 0.92
    imagebutton:
            idle "view3"
            hover "view3b"
            action Jump ("beachfaster3b")
            xalign 0.06
            yalign 0.81
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("beachfaster4")
            xalign 0.96
            yalign 0.9

screen fasterbeach3b:
    imagebutton:
            idle "view4"
            hover "view4b"
            action Jump ("beachfaster3c")
            xalign 0.06
            yalign 0.92
    imagebutton:
            idle "view2"
            hover "view2b"
            action Jump ("beachfaster3")
            xalign 0.06
            yalign 0.81
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("beachfaster4b")
            xalign 0.96
            yalign 0.9

screen fasterbeach3c:
    imagebutton:
            idle "view2"
            hover "view2b"
            action Jump ("beachfaster3")
            xalign 0.06
            yalign 0.81
    imagebutton:
            idle "view3"
            hover "view3b"
            action Jump ("beachfaster3b")
            xalign 0.06
            yalign 0.92
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("beachfaster4c")
            xalign 0.96
            yalign 0.9

screen fasterbeach4:
    imagebutton:
            idle "view4"
            hover "view4b"
            action Jump ("beachfaster4c")
            xalign 0.06
            yalign 0.92
    imagebutton:
            idle "view3"
            hover "view3b"
            action Jump ("beachfaster4b")
            xalign 0.06
            yalign 0.81
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("beachfaster5")
            xalign 0.96
            yalign 0.9

screen fasterbeach4b:
    imagebutton:
            idle "view4"
            hover "view4b"
            action Jump ("beachfaster4c")
            xalign 0.06
            yalign 0.92
    imagebutton:
            idle "view2"
            hover "view2b"
            action Jump ("beachfaster4")
            xalign 0.06
            yalign 0.81
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("beachfaster5b")
            xalign 0.96
            yalign 0.9

screen fasterbeach4c:
    imagebutton:
            idle "view2"
            hover "view2b"
            action Jump ("beachfaster4")
            xalign 0.06
            yalign 0.81
    imagebutton:
            idle "view3"
            hover "view3b"
            action Jump ("beachfaster4b")
            xalign 0.06
            yalign 0.92
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("beachfaster5c")
            xalign 0.96
            yalign 0.9

screen fasterbeach5:
    imagebutton:
            idle "view4"
            hover "view4b"
            action Jump ("beachfaster5c")
            xalign 0.06
            yalign 0.92
    imagebutton:
            idle "view3"
            hover "view3b"
            action Jump ("beachfaster5b")
            xalign 0.06
            yalign 0.81
    imagebutton:
            idle "position"
            hover "position1"
            action Jump ("beachfinish")
            xalign 0.96
            yalign 0.9

screen fasterbeach5b:
    imagebutton:
            idle "view4"
            hover "view4b"
            action Jump ("beachfaster5c")
            xalign 0.06
            yalign 0.92
    imagebutton:
            idle "view2"
            hover "view2b"
            action Jump ("beachfaster5")
            xalign 0.06
            yalign 0.81
    imagebutton:
            idle "position"
            hover "position1"
            action Jump ("beachfinish")
            xalign 0.96
            yalign 0.9
screen fasterbeach5c:
    imagebutton:
            idle "view2"
            hover "view2b"
            action Jump ("beachfaster5")
            xalign 0.06
            yalign 0.81
    imagebutton:
            idle "view3"
            hover "view3b"
            action Jump ("beachfaster5b")
            xalign 0.06
            yalign 0.92
    imagebutton:
            idle "position"
            hover "position1"
            action Jump ("beachfinish")
            xalign 0.96
            yalign 0.9
    #imagebutton:
            #idle "slower"
            #hover "slower1"
            #action Jump ("irisexone")
            #xalign 0.945
            #yalign 0.8

screen rspanks1:
    imagebutton:
            idle "spank"
            hover "spank1"
            action Jump ("rspankl1")
            xalign 0.96
            yalign 0.785
    imagebutton:
            idle "fuck"
            hover "fuck1"
            action Jump ("rfuckl1")
            xalign 0.96
            yalign 0.9

screen rspanks2:
    imagebutton:
            idle "spank"
            hover "spank1"
            action Jump ("rspankl2")
            xalign 0.96
            yalign 0.785
    imagebutton:
            idle "fuck"
            hover "fuck1"
            action Jump ("rfuckl1")
            xalign 0.96
            yalign 0.9

screen rsofas1:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("rsofal2")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("rsofall1")
            xalign 0.95
            yalign 0.9
screen rsofas2:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("rfuckl1")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("rsofall2")
            xalign 0.95
            yalign 0.9
#################################################

screen ivsf:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("ivml")
            xalign 0.96
            yalign 0.9
screen ivmf:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("ivfl")
            xalign 0.96
            yalign 0.9
screen jisf:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("jisl")
            xalign 0.96
            yalign 0.9

screen jisff:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("jissl")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("jifl")
            xalign 0.95
            yalign 0.9
screen jissf:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("jisll")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("jiffl")
            xalign 0.95
            yalign 0.9

screen jifs:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("jiffl")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("tsomecum")
            xalign 0.95
            yalign 0.9
screen jiffs:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("jifl")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("tsomecum")
            xalign 0.95
            yalign 0.9


screen fasterplug1:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("labelplug1")
        xalign 0.95
        yalign 0.9
screen fasterplug2:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("labelplug2")
        xalign 0.07
        yalign 0.9
screen fasterplug3:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("labelplug3")
        xalign 0.95
        yalign 0.9
screen fasterplug4:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("labelplug4")
        xalign 0.95
        yalign 0.9
screen fasterplug5:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("labelplug5")
        xalign 0.95
        yalign 0.9
screen fasterplug6:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("labelplug6")
        xalign 0.95
        yalign 0.9
screen fasterplug7:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("labelplug7")
        xalign 0.95
        yalign 0.9
screen fastercunni1:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("labelcunni1")
        xalign 0.07
        yalign 0.9
screen fasteranaly:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labelanaly2")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("labelanalyf")
            xalign 0.95
            yalign 0.9
screen fasteranaly2:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labelanaly3")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("labelanalyf")
            xalign 0.95
            yalign 0.9
screen fasteranaly3:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labelanaly")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("labelanalyf")
            xalign 0.95
            yalign 0.9

screen fasterplugplug:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labelplugplug2")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("labelplugplugcum")
            xalign 0.95
            yalign 0.9
screen fasterplugplug2:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labelplugplug")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("labelplugplugcum")
            xalign 0.95
            yalign 0.9



####################################

screen fasterpile1:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("labelpile1")
        xalign 0.95
        yalign 0.9
screen fasterpile2:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("labelpile2")
        xalign 0.95
        yalign 0.9
screen fasterstore1:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("labelstore1")
        xalign 0.95
        yalign 0.9

screen fasterstore2:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labelstore2b")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("labelstorecum")
            xalign 0.95
            yalign 0.9
screen fasterstore2b:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labelstore2c")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("labelstorecum")
            xalign 0.95
            yalign 0.9
screen fasterstore2c:
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labelstore2")
            xalign 0.07
            yalign 0.9
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("labelstorecum")
            xalign 0.95
            yalign 0.9

######################################################################## 0.10
screen fasterwed1:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("wedd1")
        xalign 0.95
        yalign 0.9
screen fasterwed2:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("wedd3")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("wedd2b")
            xalign 0.07
            yalign 0.9
screen fasterwed2b:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("wedd3")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("wedd2")
            xalign 0.07
            yalign 0.9
screen fasterwed3:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("wedd4")
            xalign 0.95
            yalign 0.9
screen fasterwed4:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("wedd5")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("wedd4b")
            xalign 0.07
            yalign 0.9
screen fasterwed4b:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("wedd5")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("wedd4c")
            xalign 0.07
            yalign 0.9
screen fasterwed5:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("wedd6")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("wedd5b")
            xalign 0.07
            yalign 0.9
screen fasterwed5b:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("wedd6")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("wedd5c")
            xalign 0.07
            yalign 0.9
screen fastertub:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("tubb1")
        xalign 0.95
        yalign 0.9
screen fastertub2:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("tubb3")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("tubb2b")
            xalign 0.07
            yalign 0.9
screen fastertub2b:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("tubb3")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("tubb2")
            xalign 0.07
            yalign 0.9
screen fastertub3:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("tubb5")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("tubb4b")
            xalign 0.07
            yalign 0.9
screen fastertub3b:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("tubb5")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("tubb4")
            xalign 0.07
            yalign 0.9
screen fastertub4:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("tubb6")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("tubb5b")
            xalign 0.07
            yalign 0.9
screen fastertub4b:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("tubb6")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("tubb5c")
            xalign 0.07
            yalign 0.9
screen fasterzxc:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("zxc1")
            xalign 0.95
            yalign 0.9
screen fasterzxc1:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("zxc2")
            xalign 0.95
            yalign 0.9
screen fasterzxc2:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("zxc3")
            xalign 0.95
            yalign 0.9
screen fasterzxc3:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("zxc5")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("zxc4")
            xalign 0.07
            yalign 0.9
screen fasterzxc4:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("zxc5")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("zxc4b")
            xalign 0.07
            yalign 0.9


screen fasterlast1:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("labellast1")
        xalign 0.95
        yalign 0.9
screen fasterlast2:
    imagebutton:
        idle "faster"
        hover "faster1"
        action Jump ("labellast2")
        xalign 0.95
        yalign 0.9
screen fasterlast3:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("labellast3")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labellastview3b")
            xalign 0.07
            yalign 0.9
screen fasterlast3b:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("labellast3")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labellastview3")
            xalign 0.07
            yalign 0.9
screen fasterlast4:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("labellastfinish1")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labellastview4")
            xalign 0.07
            yalign 0.9
screen fasterlast4b:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("labellastfinish1")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labellastview4b")
            xalign 0.07
            yalign 0.9
screen fasterlast5:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("labellast6pre")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labellast5b")
            xalign 0.07
            yalign 0.9
screen fasterlast5b:
    imagebutton:
            idle "faster"
            hover "faster1"
            action Jump ("labellast6pre")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labellast5")
            xalign 0.07
            yalign 0.9
screen fasterlast6:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("labellaurenlastcum")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labellast6b")
            xalign 0.07
            yalign 0.9
screen fasterlast6b:
    imagebutton:
            idle "finish"
            hover "finish1"
            action Jump ("labellaurenlastcum")
            xalign 0.95
            yalign 0.9
    imagebutton:
            idle "view"
            hover "view1"
            action Jump ("labellast6")
            xalign 0.07
            yalign 0.9

############################################################################################### Village map

screen villagemap:
        imagemap:
            ground "village1"
            hover "village3"
            idle "village2"

            hotspot (1045, 173, 153, 128) clicked Jump("vhotel")
            hotspot (483, 600, 153, 127) clicked Jump("vdocks")
            hotspot (1351, 316, 325, 127) clicked Jump("vcocaine")
            if uramen:
                hotspot (97, 382, 240, 128) clicked Jump("vramen")
            if udojo:
                hotspot (1040, 629, 153, 126) clicked Jump("vdojo")
            if utemple:
                hotspot (1434, 806, 163, 131) clicked Jump("vtemple")
            if uhotspring:
                hotspot (745, 0, 119, 204) clicked Jump("vhotspring")
            if ucity:
                hotspot (1687, 437, 208, 127) clicked Jump("vcity")
            if upublicbath:
                hotspot (111, 533, 214, 131) clicked Jump("vpublicbaths")
            if usquare:
                hotspot (438, 234, 163, 152) clicked Jump("vsquare")
            if ucemetery:
                hotspot (1660, 9, 192, 151) clicked Jump("vcemetery")



################################################################################################ Point screen

screen pointscreen:
    tag menu
    add "point_screen"
    frame xpos 625   ypos 140:
        text "{size=+18}{i}{color=#660000}[lauren_points]/40"
    frame xpos 696   ypos 388:
        text "{size=+18}{i}{color=#660000}[judie_points]/40"
    frame xpos 772   ypos 636:
        text "{size=+18}{i}{color=#660000}[carla_points]/25"
    frame xpos 843   ypos 884:
        text "{size=+18}{i}{color=#660000}[rebecca_points]/20"
    textbutton "Return":
        action Return()
        xalign 0.81
        yalign 0.91
    if jasminepath == False:
        add "jasminelost"
    if aikopath == False:
        add "aikolost"
    if irispath == False:
        add "irislost"
    if rebeccapath == False:
        add "rebeccalost"
    if carlapath == False:
        add "carlalost"
    if judiepath == False:
        add "judielost"
    if laurenpath == False:
        add "laurenlost"

################################################################################################ Gallery


screen gallery:
    tag menu
    add "gallerybackground"

    textbutton "Return":
        action Return()
        xalign 0.51
        yalign 0.97

    textbutton "NEXT":
        action ShowMenu("gallery2")
        xalign 0.76
        yalign 0.07

    
    imagebutton:
        idle "gjudie1"
        hover "gjudie1b"
        action ShowMenu('gjudierub')
        xalign 0.125
        yalign 0.255


    imagebutton:
        idle "grebecca1"
        hover "grebecca1b"
        action Jump('grebeccashower')
        xalign 0.514
        yalign 0.386


    imagebutton:
        idle "gjudie2"
        hover "gjudie2b"
        action Jump('gjudietemple')
        xalign 0.8935
        yalign 0.255


    imagebutton:
        idle "glauren1"
        hover "glauren1b"
        action Jump('glaurenspot')
        xalign 0.125
        yalign 0.715


    imagebutton:
        idle "gcarla1"
        hover "gcarla1b"
        action ShowMenu('gcarladildo')
        xalign 0.513
        yalign 0.842


    imagebutton:
        idle "grebecca2"
        hover "grebecca2b"
        action Jump('grebeccablind')
        xalign 0.894
        yalign 0.715


####################################################
screen gallery2:
    tag menu
    add "gallerybackground2"

    textbutton "Return":
        action Return()
        xalign 0.51
        yalign 0.97

    textbutton "BACK":
        action ShowMenu("gallery")
        xalign 0.25
        yalign 0.07

    textbutton "NEXT":
        action ShowMenu("gallery3")
        xalign 0.76
        yalign 0.07

    
    imagebutton:
        idle "gjudie3"
        hover "gjudie3b"
        action Jump('gjudiecloset')
        xalign 0.125
        yalign 0.255


    imagebutton:
        idle "gjasmine1"
        hover "gjasmine1b"
        action Jump('gjasmineparty')
        xalign 0.514
        yalign 0.386


    imagebutton:
        idle "gcarla2"
        hover "gcarla2b"
        action Jump('gcarlacunn')
        xalign 0.8935
        yalign 0.255


    imagebutton:
        idle "giris1"
        hover "giris1b"
        action Jump('girisjudie')
        xalign 0.125
        yalign 0.715


    imagebutton:
        idle "glauren2"
        hover "glauren2b"
        action Jump('glaurenmassage')
        xalign 0.513
        yalign 0.842


    imagebutton:
        idle "grebecca3"
        hover "grebecca3b"
        action Jump('grebeccasex1')
        xalign 0.894
        yalign 0.715

#############################################
screen gallery3:
    tag menu
    add "gallerybackground3"

    textbutton "Return":
        action Return()
        xalign 0.51
        yalign 0.97

    textbutton "BACK":
        action ShowMenu("gallery2")
        xalign 0.25
        yalign 0.07

    textbutton "NEXT":
        action ShowMenu("gallery4")
        xalign 0.76
        yalign 0.07

    
    imagebutton:
        idle "gjudie4"
        hover "gjudie4b"
        action Jump('gjudieshower')
        xalign 0.125
        yalign 0.255


    imagebutton:
        idle "giris2"
        hover "giris2b"
        action Jump('girislocker')
        xalign 0.514
        yalign 0.386


    imagebutton:
        idle "gcarlajudie1"
        hover "gcarlajudie1b"
        action Jump('gjudiecarlasofa')
        xalign 0.8935
        yalign 0.255


    imagebutton:
        idle "glauren3"
        hover "glauren3b"
        action Jump('glaurenspa')
        xalign 0.125
        yalign 0.715


    imagebutton:
        idle "gjasmine2"
        hover "gjasmine2b"
        action Jump('gjasminesextrain')
        xalign 0.513
        yalign 0.842


    imagebutton:
        idle "gaiko1"
        hover "gaiko1b"
        action Jump('gaikobath')
        xalign 0.894
        yalign 0.715

########################################
screen gallery4:
    tag menu
    add "gallerybackground4"

    textbutton "Return":
        action Return()
        xalign 0.51
        yalign 0.97

    textbutton "BACK":
        action ShowMenu("gallery3")
        xalign 0.25
        yalign 0.07

    textbutton "NEXT":
        action ShowMenu("gallery5")
        xalign 0.76
        yalign 0.07


    
    imagebutton:
        idle "gcarla3"
        hover "gcarla3b"
        action Jump('gcarlahots')
        xalign 0.125
        yalign 0.255


    imagebutton:
        idle "gjudie5"
        hover "gjudie5b"
        action Jump('gjudiesexjap')
        xalign 0.514
        yalign 0.386


    imagebutton:
        idle "glauren4"
        hover "glauren4b"
        action Jump('glaurenpublicbath')
        xalign 0.8935
        yalign 0.255


    imagebutton:
        idle "grebecca4"
        hover "grebecca4b"
        action Jump('grebeccabeach')
        xalign 0.125
        yalign 0.715


    imagebutton:
        idle "girisjudie"
        hover "girisjudieb"
        action Jump('girisjudieg')
        xalign 0.513
        yalign 0.842


    imagebutton:
        idle "gaiko2"
        hover "gaiko2b"
        action Jump('gaikomotel')
        xalign 0.894
        yalign 0.715

############################################

screen gallery5:
    tag menu
    add "gallerybackground5"

    textbutton "Return":
        action Return()
        xalign 0.51
        yalign 0.97

    textbutton "BACK":
        action ShowMenu("gallery4")
        xalign 0.25
        yalign 0.07

    
    imagebutton:
        idle "gcarla4"
        hover "gcarla4b"
        action Jump('gcarlastore')
        xalign 0.125
        yalign 0.255


    imagebutton:
        idle "gjasmine3"
        hover "gjasmine3b"
        action Jump('gjasminelauren')
        xalign 0.514
        yalign 0.386


    imagebutton:
        idle "grebecca5"
        hover "grebecca5b"
        action Jump('grebeccawedding')
        xalign 0.8935
        yalign 0.255


    imagebutton:
        idle "gaikolauren"
        hover "gaikolaurenb"
        action Jump('gaikodojo')
        xalign 0.125
        yalign 0.715


    imagebutton:
        idle "girisjudie2"
        hover "girisjudie2b"
        action Jump('girisanal')
        xalign 0.513
        yalign 0.842


    imagebutton:
        idle "gjudielauren"
        hover "gjudielaurenb"
        action Jump('gfinal')
        xalign 0.894
        yalign 0.715

############################################################################################## gallery1

label grebeccawedding:
    stop music fadeout 1
    stop music2 fadeout 1
    $ renpy.music.set_volume(0.35, channel='music3')
    play music3 "church2.mp3" fadein 1
    scene wed 47
    r "W-what the hell..." with dis
    r "Come on, [me], I don't have time for games."
    r "I think I've made myself very clear..."
    r "Stop!"
    scene wed 48 with Dissolve(1.4)
    me "*Gently kissing her neck*" with dissolve
    r "(Giggles) [me]!!"
    r "Enough!"
    r "Ahh..."
    me "(Whispering) Remember when I found you blindfolded in your apartment?"
    r "I remember discovering it was you a week later! I almost called the police!"
    me "But you didn't. Because you love this stuff, because David doesn't play these kind of games with you, and because you love me."
    r "I'm gonna get married today, [me]. I'm not running away with you! Stop!"
    me "I'm not asking you to run away anymore."
    me "I just wanted to feel your skin one last time..."
    r "Ahhmm..."
    play sound "clothes.ogg"
    scene wed 49 with Dissolve(1.2)
    r "Hey!" with dis
    me "Sorry, I didn't want this beautiful dress to get dirty."
    me "This corset is nice too..."
    r "Don't!"
    scene wed 50
    me "I bet you didn't have a bachelorette party." with dis
    r "Of course not. We agreed not to..."
    me "We? Or just David?"
    r "Um..."
    play sound "clothes.ogg"
    scene wed 51 with Dissolve(1.2)
    me "If you ask me, you deserve a bachelorette party." with dis
    r "[me], that's enough..."
    me "Before you go to live your \"stable and happy life\"..."
    me "You deserve a final 10 minutes of freedom..."
    r "(Chuckles) No..."
    me "5 minutes?"
    scene wed 52
    me "*Pressing your dick against her*" with dis
    r "Ahh... fuck..."
    scene wed 53
    r "That's as big as I remembered..." with dis
    r "*Chuckles*"
    r "Put it away..."
    scene wed 54
    me "*Sliding your dick between her thighs*"with dis
    r "[me]... I won't tell you again..."
    scene rw1 with Dissolve(1.5)
    r "[me]..." with dissolve
    r "Ah..."
    me "I miss your pussy so much, Rebecca..."
    r "I missed you too..."
    r "But we can't do it anymore. Especially not today..."
    me "You're already getting wet... You should take off your stockings before they get ruined."
    r "Ah..."
    me "How long has it been since David touched you?"
    r "I... don't even remember... Months."
    me "How long since he fucked you as well as I have?"
    r "Ah... He never has..."
    me "Don't you want to do it one last time?"
    r "Ah..."
    me "5 minutes?"
    r "I..."
    r "But he could come in..."
    r "And my family is behind that wall..."
    me "I'll lock the door."
    r ". . ."
    scene wed 53
    r "(Chuckles) O-okay... But hurry up..." with dis
    me "(Yes! Finally!)"
    play sound "clothes.ogg"
    scene wed 55 with Dissolve(1.7)
    me "Oh Rebecca..." with dissolve
    r "In 5 minutes I have to be at the altar getting married, so if you want to finish, you had better hurry..."
    scene wed 57
    me "Oh babe, I assure you, I'll give you my best." with dis
    me "Maybe I'll have to be a little rough, though... Are you ok with that?"
    r "Mm-hm..."
    r "(Whispering) I like it rough..."
    play sound "piston3.ogg"
    scene wed 56
    r "AAAAaaahhhh..." with hpunch
    r "FUCK!"
    $ renpy.music.set_volume(0.8, channel='music2')
    play music2 "reb1.ogg" fadein 2
    scene rw2 with Dissolve(1.5)
    r "OH MY GOD!" with dissolve
    r "Yeah! Yeah!"
    me "Oh yes... It feels so amazing to be back inside of you... You're so fucking wet..."
    r "Ahhhh..."
    r "Fuck me harder, [me]..."
    r "Give it all to me..."
    r "We don't have much time..."
    r "I want you to destroy my pussy..."
    play music2 "reb2.ogg"
    scene rw3 with Dissolve(2)
    r "AHHHH! YEAH! THAT'S IT!" with dissolve
    me "AAAAaaah... FUCK!"
    r "AAAAH... AHHH..."
    r "H-holy Mother of God, yeah!"
    me "N-not so loud, Becca..."
    r "AHHH..."
    me "If you keep screaming like that, David will hear us..."
    r "Maybe then he'll learn how a woman sounds when she’s properly satisfied..."
    r "Ahhh yeah..."
    scene rw4 with Dissolve(2)
    r "Ohh... ahh... y-yeah..." with dissolve
    r "Ahhh... Thank god the bells drown out the noise we're making..."
    me "Ahh... yes..."
    scene rw3 with Dissolve(2)
    r "Ahhh... Ahh..." with dissolve
    r "Fuck yeah, I don't think I can live without you..."
    r "I need this in my life... Every day..."
    me "Fuck... I'm about to cum..." with dissolve
    r "Yeah! I want you to cum inside me... please..."
    r "Creampie your teacher on the day of her wedding! Right now, inside this fucking church!"
    me "That's..."
    r "S-so wrong! And I love it!"
    me "Ahhh... I'm gonna..."
    r "YEAH! DO IT!"
    stop music2
    play sound "cum1.ogg"
    scene wed 58
    me "(Cumming inside her) Aaaaaah..." with hpunch
    play sound2 "cum1.ogg"
    me "Ahhh..." with hpunch
    r "Aaaargh... Yeah... Fill me up..."
    scene wed 59
    r "Oh my fucking god..." with dis
    me "Oh Jesus..."
    r "Why do I love feeling your cum inside of me so much..."
    r "What's wrong with me..."
    me "There's nothing wrong with you, it's only natural..."
    play sound "fall2.ogg"
    scene wed 60 with Dissolve(1.2)
    r "Yeah, if you say so..." with dissolve
    r "I'm pretty sure there's something wrong with my head. I'm a d-depraved person."
    r "I continue to cheat on my future husband with one of my students!"
    r "I’m no good for you, [me]... I'm a sexual deviant! Who knows, in a couple of weeks I could be asking you to have a threesome with Lauren and Judie or something like that! Haha!"
    me "Um..."
    me "Well, I don't think that sounds so ba--"
    play sound "forcing.mp3"
    pause 1.2
    play sound2 "knock2.mp3"
    scene wed 61
    d "Rebecca? Rebecca! Let me in!" with dissolve
    r "(Whispering) Oh, fuck!"
    scene wed 62
    d "REBECCA!" with dis
    r "(Removing the blindfold) Y-yeah, yeah, I'm here, what do you want now?"
    d "What's taking you so long?! It's going to be dark by the time we're done!"
    d "I have stuff to do, you know?"
    scene wed 63
    r "Yeah, yeah, tell them I just need 10 more minutes!" with dis
    d "10 MORE MINUTES?!"
    d "There's barely anyone here Rebecca, you don't need to dress up that much!"
    r "Y-you know I like to."
    play sound "forcing.mp3"
    scene wed 65
    d "Let me in, I'll help you. Why the fuck is the door locked?" with dissolve
    d "Open it!"
    scene wed 64
    r "I can't!" with dis
    r "Y-you aren't supposed to see the bride in her gown before you get married."
    r "It's a bad omen!"
    play sound "forcing.mp3"
    scene wed 65
    d "Spare me from your superstitious bullshit, Rebecca."
    scene wed 64
    r "I can't! You know how I believe in that stuff!"
    play sound "knock2.mp3"
    d "Open up, goddammit!{w=0.9}{nw}" with hpunch
    play sound2 "forcing.mp3"
    scene wed 66
    r "I TOLD YOU I JUST NEED 10 MORE FUCKING MINUTES!" with dis
    r "I'm already dressed! I just need to fix my hair!"
    me "(This is so hot...)"
    scene wed 65
    d "Grrrr... Fine, 10 minutes."
    scene wed 67
    me "(Whispering) Oh God Rebecca, you're getting me all wound up again..." with dis
    r "(Whispering) What's wrong with you now?"
    r "(Whispering) Come on, let me get dressed, I have to..."
    play sound "fall2.ogg"
    scene wed 68
    me "(Whispering) Come here..." with dis
    r "(Whispering) [me]!"
    d "Hmm? What happened?"
    scene wed 69
    r "N-nothing! I'm going as quick as I can!"
    d "Ok..."
    d "I'll be waiting on the altar with your tedious family..."
    r "O-okay! I'll be right there!"
    scene wed 70
    r "What the fuck, [me]? He almost caught us!" with dis
    me "Sorry, I couldn't resist..."
    r "How can you even be hard again? You just came a minute ago!"
    r "I still have all your juice inside me..."
    me "It's you, Rebecca. It's just... when you're with me, I could cum over and over again."
    r "Yeah, sure... that'll be the day."
    r "Anyway, let me go. I have to get married."
    me "Let me feel your pussy one more time, please..."
    r "What?"
    play sound "penetration1.ogg"
    play sound "piston3.ogg"
    scene wed 71
    r "AAAArghh..." with dissolve
    me "O-ohhh yeah..."
    play music2 "reb3.ogg" fadein 2
    scene rw5 with Dissolve(1.5)
    r "Ahhhh... Fuck..." with dissolve
    r "Y-you already creampied me... what more do you want..."
    me "Ahhh..."
    me "I want you to cum again... and I want to fill you up again... I can't get enough..."
    r "W-what? Where the hell do you get all that energy?"
    me "I don't know..."
    me "But I know you can go for another round..."
    me "What did you say to David? 10 minutes?"
    r "Ahhhh... Yeah..."
    me "Let's make it 5..."
    r "You’ve been saying \"5 minutes\" for 10 minutes already..."
    me "Best 5 minutes of my life..."
    r "Oh God..."
    r "Ahhh..."
    r "I... Oh fuck it. Just fuck me again [me]..."
    play music2 "reb4.ogg"
    scene rw6 with Dissolve(1.5)
    r "AHH! AHHH! AHHHH!" with dissolve
    r "Oh my fucking god!"
    r "Y-you're going too deep!"
    r "I still haven't gotten used to your size..."
    me "AAaaahh... Yeah, Becca..."
    me "Take it all..."
    scene rw7 with Dissolve(1.5)
    r "AAahh... ahhh... ahh..." with dissolve
    r "Are you trying to get me addicted to you?"
    r "Mmmmmm..."
    r "Is t-that your p-plan?"
    me "Aren't you already?"
    r "Haha..."
    r "M-maybe..."
    scene rw6 with Dissolve(1.5)
    r "A-a-ahhh..." with dissolve
    r "K-keep going..."
    r "Yes..."
    play music2 "reb6.ogg"
    scene rw8 with Dissolve(1.5)
    r "AAAaaaaAaargh..." with dissolve
    r "T-this is the best feeling I've ever f-f-felt..."
    scene rw8 with Dissolve(1.5)
    r "AAAaaaaAaargh..." with dissolve
    scene rw9 with Dissolve(1.5)
    r "A-a-a-ahh..." with dissolve
    r "I c-can't take it anymore...."
    stop music2
    play sound "cum1.ogg"
    scene wed 72
    me "AAAAAAH..." with hpunch
    play sound2 "cum1.ogg"
    r "AAAAAAAAAARH!" with hpunch
    play sound "clothes.ogg"
    scene wed 73
    r "J-jesus..." with Dissolve(1.5)
    r "You fuck like a wild bull..."
    me "Oh my god, Rebecca..."
    me "That was amazing..."
    me "Did we cum together?"
    r "Y-yeah..."
    scene wed 74
    r "(Panting) That was... the best... orgasm of my life..." with dis
    r "Now my mind is gonna associate orgasming with the sound of bells..."
    r "Bells of..."
    scene wed 75
    r "Bells! The wedding! Shit, I have to get married!" with dis
    scene gallerybackground
    call screen gallery5 with Dissolve(1)
label gaikodojo:
    stop music3 fadeout 1
    $ renpy.music.set_volume(0.4, channel='music2')
    play music "night.ogg" fadein 3
    play music2 "springwater.mp3" fadein 3
    scene aik 43
    ai "Ahhh... this feels nice. My feet were totally wasted."with dissolve
    scene aik 44
    ai "(Taking off her towel) It's too bad we can't come back here for a very long time, isn't it?" with dis
    scene aik 45
    l "A-Aiko? What are you doing?"
    ai "What?"
    scene aik 46
    ai "Oh, the towel? Come on Lauren, you can't expect me to bathe with a towel on..." with dis
    ai "I think we are comfortable enough with each other already."
    ai "For God's sake, I've even seen you two having sex!"
    scene aik 45
    l "Well, yeah I know, but..."
    l "[me]..."
    scene aik 47
    ai "Well, if it makes [me] uncomfortable we can call it a night, I guess..."
    me "N-no, it doesn't bother me at all..."
    ai "Nice! Then let's get in already!"
    me "Of course..."
    play sound "splash.ogg"
    scene aik 48
    me "*Getting in the hot tub*" with dis
    me "(Jesus Christ...)"
    ai "Is it warm enough?"
    me "Y-yeah, it's warm enough. I'd say it's the perfect temperature."
    ai "Nice..."
    scene aik 49
    ai "Come on, Lauren!" with dis
    ai "Don't just stand there, you're going to catch a cold."
    ai "Towel off!"
    scene aik 45
    l "Ok, ok! I'm coming."
    scene aik 50
    l "*Dropping her towel*" with Dissolve(1.3)
    ai "That's better!"
    me "(Oh, what a heavenly sight...)"
    ai "Let's enjoy the hot tub before Sensei turns the lights and the bubbles off."
    play sound "water.ogg"
    scene aik 51 with Dissolve(1.3)
    ai "Ahh..." with dissolve
    ai "You were right [me], the water's perfect..."
    scene aik 52
    l "*Sitting on the ledge*" with dis
    ai "With the workout we've been following all week, we deserved this so much. We earned it!"
    play sound "water.ogg"
    scene aik 53 with Dissolve(1.3)
    l "Ohhh..." with dis
    ai "And? Does it feel good or not?"
    l "It feels... marvelous. I can feel all my muscles relaxing."
    ai "Right?"
    play sound "water.ogg"
    scene aik 54
    l "Ahh..." with dis
    ai "Ahhhh..."
    me "Ahhh..."
    scene aik 55
    me "(Man, if I die this Sunday, this is what I hope heaven looks like.)" with dissolve
    me "(Just look at the two angels I have by my side.)"
    me "(Hmmm... is this the night?)"
    me "(Yeah, this must be the night. I'm not gonna get a better chance than this to have a threesome with Lauren and Aiko.)"
    me "(But I wonder how I should bring it up...)"
    l "Mmmm..."
    ai "Hmm..."
    me "(Maybe...)"
    scene aik 56
    play sound "slidingdoor2.ogg"
    dmr "Ahhh, it's getting kind of cold, isn't it?" with dis
    scene aik 57
    ai "W-w-what? Sensei! We're using the hot-tub!"
    scene aik 56
    dmr "Yeah, no shit, Sherlock! I granted you the permission myself!"
    dmr "I hope none of the other warriors will be pissed off seeing you using the hot tub after only one week!"
    dmr "Try not to annoy them tonight."
    scene aik 57
    ai "T-tonight? What do you mean?"
    play sound "slidingdoor2.ogg"
    scene aik 56b
    dmh "Oh, what a pleasant surprise! New people!" with dis
    scene aik 59
    ai "(Covering her boobs) W-WHAT THE FUCK?" with hpunch
    ai "I thought we were gonna be alone!"
    dmr "Haha! Really? Where did you get that idea? Friday night's bath is a sacred tradition in my dojo! We always gather in the sacred courtyard together!"
    ai "Everything is sacred in your dojo!"
    ai "And who the fuck is that old man?!"
    dmr "My lovely husband, of course!"
    play sound "splash.ogg"
    scene aik 60
    dmr "Ahhh... so relaxing..." with dis
    dmh "Hehe, don't worry young lady, I'll try not to get in the way."
    ai ". . ."
    play sound "water.ogg"
    scene aik 61
    dmh "Have you made any dinner for later, Hina?" with dis
    dmr "No, I haven't done anything, but we can order some food."
    dmh "Oh, sweet. Chinese or Indian?"
    dmr "You know, I'm in the mood for sushi. It'll be nice not having to prepare it myself."
    me "(What a great way to spoil the moment.)"
    play sound "slidingdoor2.ogg"
    scene aik 56c
    gsss "Oh, yeah! Glad you could join us, guys!" with dis
    me "(You have got to be kidding me...)"
    play sound "splash.ogg"
    scene aik 62 with dis
    gsss "Ahhhh... isn't it great?!" with dissolve
    ai "Um..."
    gsss "What a kick you gave me back there, Aiko! I blacked out for 10 whole minutes! Where did you learn to fight like that?"
    ai "Erm... I don't know. When I was in Japan."
    gsss "You look nervous..."
    gsss "Come on, don't be so shy, you two! This is a relaxation spot!"
    gsss "No need to cover yourselves! I'm not interested in such skinny chicks, anyway!"
    ai "Um... yeah, I prefer to stay like this, thanks."
    gsss "Haha! Ok, ok, suit yourself."
    play sound "slidingdoor2.ogg"
    scene aik 56d
    fit "Hello everyone." with dis
    fit "Sorry, I'm late today. I got caught up hauling some logs."
    dmr "No problem Jack! You're right on time!"
    play sound "splash.ogg"
    scene aik 63 with dis
    fit "Ahhh... this is the life." with dissolve
    gsss "You can say that again, brother."
    scene aik 64 with dis
    pause
    ai ". . ." with dissolve
    l ". . ."
    scene aik 65
    fit "Hmm?" with dis
    scene aik 66 with dis
    fit "Um..." with dissolve
    fit "Can I help you?"
    me "Jack! What the fuck?! It's me, [me]! Don't you recognize me?"
    scene aik 67
    fit "Ahhhh, [me]!" with Dissolve(.7)
    fit "And Lauren and Aiko! From school!"
    me "Of course!"
    fit "Yeah, sorry! Sometimes I have memory lapses... I don't know why."
    me "Do you train here?"
    fit "Yes, after my enlightenment, I joined all the fitness centers in town."
    fit "This one is my favorite."
    fit "Glad to see you're following the same path as well!"
    me "W-well, not exactly, but thanks."
    scene aik 68
    ai "Sorry about this, Lauren..." with dis
    ai "This isn't how I expected the night to be...."
    l "(Laughs) Don't worry! At least we’ll have a funny anecdote to tell."
    ai "That's true!"
    l "And well, I guess we can still relax for a bit before leaving!"
    ai "You're right!"
    scene fewminutes with Dissolve(2.5)
    pause
    scene aik 69 with Dissolve(3)
    pause
    show screen aikoeyes1 with dis
    ai "(This hot tub is incredible...)" with dis
    ai "(It's like I'm floating on a cloud.)"
    ai "(A month ago I was living in Japan, training all day, with no friends...)"
    show screen aikoeyes2
    ai "(And now here we are...)" with dissolve
    hide screen aikoeyes2
    ai "(Skinny-dipping in a hot tub with my new best friend...)"with dissolve
    show screen aikoeyes2
    ai "(And the man who saved me from that life.)" with dissolve
    ai "(Full moon, the sound of the crickets, the smell of incense...)"
    ai "(It's like I'm living in one of the romantic movies I used to watch when I was a kid and Azazel left town.)"
    scene aik 70
    hide screen aikoeyes1
    hide screen aikoeyes2
    ai "(Well... expect for all the other people who are here too!)" with hpunch
    ai "(Are they ever gonna leave?!)"
    ai "*Clears throat*"with hpunch
    ai "(They didn't budge... Dammit.)"
    ai "(I was hoping for some fun with [me]...)"
    scene aik 71
    ai "(He seems so relaxed too. He's not even hard, which is unusual for him.)"with dis
    ai "(Maybe...)"
    play sound "water.ogg"
    scene aik 72
    ai "(I wonder what he'd do if I started to fool around with him under the water...)" with dis
    scene aik 73
    me "(Ahhh...)" with dis
    me "(I've never felt so relaxed in my life.)"
    me "(Astaroth? The Grimoire? Who gives a fuck, these bubbles are taking away all my concerns...)"
    scene aik 74
    me "(Holy shit, these are some strong bubbles!)" with dissolve
    me "(It almost feels like...)"
    scene aik 75
    me "(Whispering) A-Aiko? What the fuck are you doing?"with dis
    ai "(Whispering) Isn't it obvious?"
    me "(Whipering) H-haven't you noticed that Lauren and 4 other people are here?"
    scene aik 70
    ai "(Whispering) Don't worry, they're not paying attention. I think most of them might even be sleeping."
    scene aik 75
    ai "(Whispering) Oh my god, you're hard already!"
    ai "(Whispering) This turns you on, doesn't it?"
    me "(Whispering) Um..."
    ai "(Whispering) And what if I start doing this?"
    scene aik 76
    me "(Whispering) O-ohhh god..." with dis
    ai "Hmm?"
    me "Ah..."
    $ renpy.music.set_volume(1, channel='music3')
    play music3 "water.ogg" fadein 2
    scene ad1 with Dissolve(1.5)
    me "(Whispering) Oh yeah..." with dissolve
    me "(Holy shit, she has a good technique...)"
    me "(This is hot...)"
    me "(Aiko rubbing my dick, plus the bubbles from the hot tub...)"
    me "(What a sensation...)"
    scene aik 70
    me "(Too bad all these other cockblocks are here!)" with dissolve
    me "(If any of them notices us, things could get pretty awkward...)"
    me "(I should ask her to stop.)"
    scene ad1
    me "(B-but I can't. It feels too good.)" with dis
    me "(Damnit...)"
    me "(Maybe I could try to ask Jack for help?)"
    me "(That'd be a risky move...)"
    me "(Aghh... god, yeah, don't stop...)"
    me "(I have to do something...)"
    scene aik 82
    me "Hmmm..." with dis
    scene aik 81
    me "*Pssst*"
    scene aik 82
    pause
    scene aik 81
    me "*Pssst*"
    scene aik 82
    pause
    scene aik 81
    me "*Pssst*"
    me "(Muttering) Jack!"
    scene aik 83
    fit "(Whispering) Huh? What? What's happening?" with dis
    me "(Whispering) Can I ask you for a favor, buddy?"
    fit "What is it? You want the secret to becoming stronger?"
    me "Um... no, could you come up with some excuse to clear these people out of here? They seem to respect you so they’ll probably listen."
    fit "Why?"
    me "W-well, I was thinking about having a little more of an intimate time, if you know what I mean."
    fit "With me?"
    me "What? No! With Aiko and Lauren! You have to leave too."
    scene aik 84
    fit "Ahh! You want to copulate with these two females!"
    me "Um... Well..."
    fit "Say no more, buddy. Performing the reproductive act is a great way to stimulate your muscles. It’s quite the full-body workout! I'm so proud of you."
    fit "Not as much as lifting cars or dragging tractor wheels, but good enough."
    fit "I got you covered."
    scene aik 85
    fit "Sensei!" with dis
    dmr "Yes?"
    dmr "What is it, Jack?"
    fit "I was thinking... Maybe it's time for me to break Izanagi's Stone."
    play sound "splash.mp3"
    scene aik 86
    dmr "WHAT?!" with hpunch
    dmh "Do you mean the sacred Stone of Izanagi?"
    fit "Yeah, yeah, that one."
    gsss "Are you sure, brother?"
    fit "Yeah, no problem. I effortlessly broke a similar stone in two earlier this morning."
    fit "Come on, let's go!"
    stop music3
    play sound "bubbles.mp3"
    play sound2 "drips.mp3"
    scene aik 87 with dis
    dmr "Oh my god, this is historic! Come on guys, let's go!" with dissolve
    ai "Don't worry about us Sensei, I think we’re going to stay here for a bit longer."
    dmr "Really?! You are going to miss it?!"
    me "Yeah, don't worry. We'll watch the video later."
    ai "Just make sure to record and upload it to YouTube."
    dmr "Of course! You should really see it with your own eyes, but oh well, your loss!"
    dmr "Remember to lock the door when you're done here!"
    ai "Sure! Bye!"
    play sound "slidingdoor2.ogg"
    scene aik 54 with Dissolve(1.5)
    ai "Ahhh... thank god they left! Now we can relax again." with dissolve
    l "Yeah, I was tired of having to cover myself up."
    me "Yeah..."
    play sound "water.ogg"
    scene aik 88
    ai "*Continues jacking you off underwater*" with dis
    me "O-ohh..."
    me "T-this is so relaxing..."
    l "*Starts massaging your balls*"
    l "(Wow, he's so hard.)"
    l "(Too bad Aiko's here...)"
    me "(Oh my god, if Lauren moved her hand just a little further up, she'd touch Aiko's hand.)"
    me "(I wonder how they'd react...)"
    me "(I guess there's only one way to find out.)"
    play sound "water.ogg"
    scene aik 89
    me "*Moves Lauren's hand up*" with dis
    scene aik 90
    l "Huh?" with dis
    ai "Oh my god."
    scene aik 91
    l "A-Aiko?" with dis
    scene aik 92
    ai "Were you giving [me] a handjob, Lauren? In front of me?!"
    scene aik 91
    l "W-what? No! I was just..."
    scene aik 92
    ai "I always believed the time I caught you two having sex was an accident, but... now I'm starting to think you guys enjoy being exhibitionists..."
    scene aik 91
    l "We don't! I... We... Um..."
    scene aik 92
    ai "Do you mind if I low the water level a little?"
    play sound "drain.mp3"
    scene aik 93
    ai "*Opening the drain*" with Dissolve(3)
    ai "What were you saying, that you weren't giving him a handjob?"
    scene aik 94
    l "Yeah, I..."
    scene aik 95
    l "Oh..." with dis
    scene aik 96
    l "(Chuckles) Ok, maybe I was giving him a handjob, but we're no exhibitionists."with dissolve
    scene aik 93
    ai "Ok fine, you're not. But you can finish the job if you want anyway, babe. Wouldn’t you like that?"
    scene aik 95
    l "What? Well... Yeah, I guess that'd be nice."
    l "And you're just gonna... stay there and watch us?"
    scene aik 93
    ai "Of course... Be my guests."
    scene aik 96
    l "Well, umm... Aiko... I was wondering..."
    l "Did you want to join us?"
    scene aik 93
    ai "Really?"
    scene aik 96
    l "Sure... it will be fun!"
    l "Come on, come over here..."
    play sound "water.ogg"
    scene aik 97 with Dissolve(1.5)
    l "Only if [me] is ok with it, of course." with dissolve
    me "Oh yeah, Lauren, I'm more than ok with that..."
    ai "You two are the best couple I've ever known!"
    l "I don't know how he bewitched me, but... it definitely worked."
    l "You want us to take care of you tonight, [me]?"
    me "Well, someone once told me... a little jerking doesn’t hurt anyone."
    l "Hey, I said that!"
    me "Yeah, and you were right after all..."
    l "(Chuckles) I guess so..."
    $ renpy.music.set_volume(0.8, channel='music3')
    play music3 "wank1.mp3"
    scene ad2 with Dissolve(1.5)
    me "O-o-ohh... fuck..." with dissolve
    l "Enjoying this?"
    if inc:
        l "Brother?"
    me "Y-yes..."
    ai "Oh my god... Grabbing this hard cock is making me horny as fuck..."
    l "Yeah, not gonna lie, I'm starting to feel really horny as well..."
    ai "I wanna taste it so bad..."
    l "Aiko says she wants to taste your cock, [me]. Should we let her?"
    me "Y-yeah... Please..."
    l "Alright..."
    play music3 "wank2.mp3"
    scene ad3 with Dissolve(1.5)
    me "Oh fuck yeah..." with dissolve
    ai "Mmmmm..."
    me "That's it... Right there..."
    me "Keep licking it..."
    scene ad4 with Dissolve(1.5)
    l "Mmmm...." with dissolve
    ai "Hhmmmm..."
    me "Oh yeah..."
    l "Mmmm... It's so juicy..."
    ai "And it smells so good..."
    me "Not sure this place is gonna stay so \"sacred\" after this..."
    me "Ahhh..."
    me "Fuck..."
    me "I need to be inside of your mouth... I want to feed it to you..."
    play music3 "blowjob2.mp3"
    scene ad5 with Dissolve(1.5)
    me "AAAH... yeah! That's what I'm talking about!" with dissolve
    ai "(Gagging) MMMmmh..."
    me "Fuck yes!"
    me "My two warrior girls..."
    me "Just for me..."
    me "Aiko..."
    me "Yeah..."
    me "Eat it all... every last bit of it..."
    stop music3 fadeout 1
    play sound "water.ogg"
    scene aik 98
    ai "(Gasping for air) AAAAH!" with dissolve
    ai "G-god! This is amazing!"
    l "I know..."
    l "Can I have a taste of it too?"
    ai "PLEASE! Don’t even ask such a question... I’ll always share [me] with you..."
    play music3 "blowjob3.mp3"
    scene ad6 with Dissolve(1.5)
    me "Ohhhh... my love..." with dissolve
    me "My Lauren..."
    ai "Yeah... Milk that big dick, girl!"
    me "T-this is incredible..."
    me "Ahhh..."
    if inc:
        ai "Who sucks your cock better, [me]? Me or your sister?"
    else:
        ai "Who sucks your cock better, [me]? Me or Lauren?"
    me "Y-you both are great..."
    ai "Always so proper..."
    me "Oh my god..."
    me "Don't stop Lauren..."
    l "Mmmmm..."
    stop music3
    play sound "splash.mp3"
    scene aik 99
    l "GOD!" with dis
    l "I c-can't go on anymore! I need air!"
    me "You used to be able to hold your breath for much longer than that, Lauren..."
    scene aik 100
    l "(Laughs) Hey, that's not fair! Aiko and I have been running and training all day!" with dis
    l "My lungs need air!"
    play sound "water.ogg"
    scene aik 101
    ai "Don't worry Lauren, I'll make you feel better..." with dis
    l "W-what?"
    ai "Your pussy is so wet you could fill this hot tub on your own..."
    l "Aren't we taking this a bit too far?"
    l "I mean... Don't get me wrong, I'm loving this, but..."
    l "I don’t know if we should..."
    play sound "water.ogg"
    scene aik 102
    ai "Mmmm..." with dis
    l "Should..."
    ai "Ahmmm..."
    l "O-o-oh my god..."
    l "A-A-Aiko...."
    scene aik 103
    l "Fuck..." with dis
    ai "*Eating Lauren's pussy*"
    me "Oh Jesus..."
    scene aik 104
    l "Enjoying the view back there, [me]?" with dissolve
    me "You have no idea..."
    play sound "water.ogg"
    scene aik 105
    me "I think you're ready for something a little more... intense, Aiko." with dis
    ai "Yes... Please... I've been waiting for you all day..."
    ai "Fuck me hard..."
    l "Be careful girl, he's... big."
    ai "I know... I don't care..."
    ai "Get inside of me already, [me]..."
    me "Your pussy is dripping wet..."
    ai "Only for you..."
    play sound "penetration3.ogg"
    scene aik 106
    ai "AAAArgh..." with dis
    ai "Y-YEAH!"
    ai "Fill me up, [me]..."
    play music3 "sexwater1.mp3" fadein 2
    scene ad7 with Dissolve(1.5)
    ai "MMMMM..." with dissolve
    me "Oh yeah, Aiko..."
    me "I love stretching your tight little pussy..."
    l "Ahh..."
    l "Oh my god..."
    l "Where did you learn to do this Aiko..."
    me "This feels amazing..."
    $ renpy.music.set_volume(1, channel='music3')
    play music3 "watersex2.mp3"
    scene ad8 with Dissolve(1.5)
    ai "Arghh!" with dissolve
    me "Oh f-fuck yeah!"
    ai "Oh Jesus Christ..."
    ai "*Continues eating Lauren's pussy* Mmmm..."
    l "Aaaah..."
    l "Seeing you sliding into Aiko is driving me insane, [me]..."
    l "Now I need you inside me..."
    me "I will be soon, don't worry..."
    l "Yeah..."
    scene ad9 with Dissolve(1.5)
    ai "AAAAH..." with dissolve
    me "My ninja girl..."
    me "I love how round and tight your ass is..."
    ai "Mmmmmmmm..."
    scene ad8 with Dissolve(1.5)
    ai "Mmmmmhh..." with dissolve
    me "Oh, yeah..."
    l "[me]..."
    stop music3
    play sound "cum2.ogg"
    scene aik 106
    ai "(Orgasming) AAAAAARGHhh..." with hpunch
    play sound2 "cum2.ogg"
    ai "Im c-c-cummming..."with hpunch
    me "O-oh god... I can feel your pussy contracting so much..."
    ai "AAaaaahh..."
    ai "T-this is... the b-best night ever..."
    l "Damn, girl..."
    play sound "water.ogg"
    scene aik 107
    ai "*French kisses Lauren*" with dis
    l "MMMm!"
    scene aik 108
    me "Yeah..." with dis
    play soundlow "splash.mp3"
    scene aik 109
    ai "Well, babe..."with dis
    ai "I think it's your turn..."
    l "Finally..."
    l "Lie down..."
    me "At your service..."
    play sound "water.ogg"
    scene aik 110
    me "Yeah, Lauren..." with Dissolve(1.4)
    me "Ride my cock like only you know how..."
    ai "Is that true, Lauren? You're a professional cowgirl?"
    l "Well, I'm gaining experience by practicing..."
    ai "Will you teach me?"
    l "Of course... It's not a secret..."
    l "I just sit on it and let myself go..."
    play sound "water.ogg"
    scene aik 111
    l "And right now..." with dis
    l "I need every..."
    play sound "penetration3.ogg"
    scene aik 112
    l "Inch of it..." with Dissolve(1.3)
    play sound2 "penetration3.ogg"
    scene aik 113
    l "Inside of m-me..." with Dissolve(1.4)
    l "J-just like t-that..."
    ai "Damn..."
    scene aik 114
    l "Aaaaahh..." with dis
    me "Oh god..."
    ai "Wow... I just came and I'm still jealous..."
    play soundlow "splash.mp3"
    scene aik 115
    me "Well come here, girl!" with dis
    me "I'm not done with you just yet..."
    ai "Oh y-yeah..."
    $ renpy.music.set_volume(0.8, channel='music3')
    scene ad10 with Dissolve(1.5)
    l "AAAaaahhh..." with dissolve
    ai "Oh yeah..."
    l "You have no idea... How much I needed this..."
    l "Aaaah..."
    scene ad11 with Dissolve(1.5)
    l "Aaahh..." with dissolve
    ai "Oh my..."
    me "(Eating Aiko's pussy) Mmmm..."
    me "Faster Lauren... Go faster..."
    l "Aaaah..."
    $ renpy.music.set_volume(1, channel='music3')
    play music3 "watersex4.mp3"
    scene ad12 with Dissolve(1.5)
    l "AAA-A-AHHHH..." with dissolve
    ai "Oh my god..."
    l "FUCK!"
    l "YEAH!"
    l "[me]! Shove it all inside me!"
    scene ad13 with Dissolve(1.5)
    l "Aaah... ahhh... ahhh..." with dis
    l "Y-you're going so deep..."
    l "You're h-hitting my cervix..."
    l "AHH!"
    l "Keep fucking me, [me]..."
    l "AAAaaargh..."
    l "I'm g-g-gonna come..." with dissolve
    l "I can't hold on any longer..."
    l "Jesus Christ..."
    me "Agh, I can't hold off anymore..."
    stop music3 fadeout 1
    play sound "splash.ogg"
    scene aik 116
    me "Come here, babe..." with dis
    l "(Panting) Ahh..."
    l "(Panting) But I'm about to cum..."
    ai "Well then, let me take care of you, my apprentice..."
    l "W-what?"
    play sound2 "splash.ogg"
    scene aik 117
    l "Oh my god..." with dis
    scene aik 118
    me "Oh fuck, I'm cumming too, Lauren..." with dis
    l "(Facesitting Aiko) MMmmm!"
    scene aik 119
    me "I'm almost there..." with dis
    l "Mmmmhmm!!"
    play sound "piston2b.ogg"
    scene aik 120
    me "Aaaaahhh... Yeah..." with hpunch
    play sound "cum1.ogg"
    play sound2 "cum2.ogg"
    scene aik 121
    me "AAAAAARGH..." with hpunch
    play sound2 "cum1.ogg"
    play sound4 "cum2.ogg"
    l "(Having an orgasm) MMMmmmmhh..." with hpunch
    me "Aaah..."
    play sound "cream2.mp3"
    scene aik 122
    me "(Panting) Oh my god..." with Dissolve(1.4)
    l ". . ."
    play sound "swallow.mp3"
    l "*Swallows*" with dissolve
    scene aik 123
    l "(Gasping) Argh..." with dissolve
    l "HOLY SHIT!"
    me "Oh my god, Lauren..."
    me "I'm sorry, I came a lot... Did you... swallow it all?"
    scene aik 124
    l "(Laughs) Yeah..." with dissolve
    l "I love tasting all of you..."
    me "That's my girl..."
    play sound "splash.ogg"
    scene aik 125
    me "AAah..." with Dissolve(1.4)
    ai "Jesus..."
    l "Oh my god..."
    scene aik 126
    ai "That was..." with dissolve
    l "Better than I could have ever imagined..."
    ai "Yeah..."
    scene aik 127
    l "You weren't wrong Aiko, this is a great dojo." with dissolve
    ai "(Laughs) Right?"
    stop music
    stop music2
    stop music3
    scene gallerybackground
    call screen gallery5 with Dissolve(1)
label girisanal:
    stop music fadeout 1
    stop music2 fadeout 1
    $ renpy.music.set_volume(0.4, channel='music3')
    play music3 "quirky.ogg" fadein 4
    scene iri 36
    i "(Where the hell did I hide it?)" with dis
    i "(It's been a while since I used it, but it should be here...)"
    i "(Did Mom take it?)"
    i "(No, that's impossible.)"
    scene iri 37
    i "(Ahh! BINGO! Here you are!)" with dissolve
    scene iri 38
    i "(Hello, old friend!)" with Dissolve(1.2)
    i "(Maybe it's not [me], but I need to satisfy this craving...)"
    i "(Yeah...)"
    i "(I'll lock myself in the bathroom.)"
    play sound "slam.ogg"
    scene iri 39
    j "HERE YOU ARE!" with dis
    j "Didn't you hear me?! I was calling you!"
    scene iri 40
    i "R-Really? Sorry babe, I didn't hear anything."
    scene iri 39
    j "What the hell are you doing here?"
    scene iri 40
    i "Nothing! I was just charging my phone. My battery was dead."
    scene iri 39
    j "Yeah... Um... Listen, do you wanna go for a run?"
    scene iri 40
    i "A... a run?"
    scene iri 39
    j "Y-Yeah, or do push-ups or something. I need... a distraction."
    scene iri 40
    i "Sounds good! Wait for me downstairs. I'll be right there in a minute! I just need to send an email really quick."
    scene iri 41
    j "Ok, ok, but hurry up!" with dis
    i "Sure!"
    play sound "doorclose.ogg"
    scene iri 38
    i "(That was close.)" with dis
    scene iri 42
    i "(Ok, I must hurry.)" with dis
    i "(As horny as I am, it shouldn't take more than a couple of minutes.)"
    scene iri 43
    i "(How should I do it?)" with Dissolve(1.8)
    i "(Lying on the bed? Or riding it?)"
    scene iri 44
    i "(Yeah... definitely riding it.)" with dis
    i "(I'll stick it to the floor.)"
    scene iri 45
    i "Hmm?" with dis
    j ". . ."
    i ". . ."
    scene iri 46
    j "I KNEW IT!" with hpunch
    i "SHIT! You scared me!"
    j "That’s strange, your phone looks awfully like a huge dildo!"
    play sound "couch.mp3"
    scene iri 48
    i "Um... I was gonna... Um..." with dis
    scene iri 47
    j "I know what you were gonna do."
    j "What the fuck is wrong with you?"
    scene iri 49
    i "It's not what it seems..."
    scene iri 47
    j "Yes it is. You invite me to your house just to leave me and go off masturbating in your room?"
    scene iri 49
    i "I'm sorry babe, it's just that... I couldn't help it."
    i "I began to feel some kind of sexual urge all of a sudden, and..."
    scene iri 50
    j "W-What? You too?"
    scene iri 51
    i "What do you mean? You too?!"
    scene iri 50
    j "Hell yes, I've never felt so horny in all my life. I feel like I need to have sex right now or else I'll die."
    scene iri 51
    i "I know! That's exactly what's happening to me!"
    scene iri 50
    j "D-Did you try to..."
    scene iri 49
    i "Finger myself? Yeah, and it did nothing."
    i "That's why I thought maybe the dildo would help..."
    scene iri 52
    i "Although... Maybe we can try to help each other." with dis
    scene iri 53
    j "W-What?"
    scene iri 52
    i "Maybe we need to have sex with someone else to solve this."
    i "And since [me] isn't here..."
    scene iri 53
    j "I d-don't think that will help."
    scene iri 54
    i "Come on, babe..." with dis
    i "If you're feeling the same thing I'm feeling right now, I know you can't resist."
    i "Let me help you. I'll touch you a bit... If it doesn't work, we'll stop."
    i "Come on, are we best friends or not?"
    scene iri 55
    j "I... o-okay, haha. I guess we can try it." with dis
    i "Yay!"
    i "Come on then! To the bed!"
    play sound "couch.mp3"
    scene iri 56 with Dissolve(1.5)
    i "*Giggles*" with dissolve
    i "This is hot! Do you think we're feeling like this because of something we ate? Or maybe it was that juice from [me]'s bag..."
    scene iri 57
    i "Sorry, I'm talking too much! Let's get those pants off!" with dissolve
    play sound "clothes.ogg"
    scene iri 58
    j "You're enjoying this too much. I'm starting to think it's you who drugged me or something." with dis
    i "I didn't, I swear! But if I discover what is causing this... we're gonna take it every day for breakfast!"
    play sound "clothes.ogg"
    scene iri 59
    j "B-Be careful!" with dis
    i "Damn, girl! You're dripping wet!"
    i "Is it because of whatever is making us feel like this?"
    $ renpy.music.set_volume(0.35, channel='music3')
    scene iri 60
    j "No... I'm always this wet... Well, at least when I'm with [me]..." with dis
    i "I see..."
    i "I totally understand that!"
    i "Let me help you, babe..."
    $ renpy.music.set_volume(0.3, channel='music3')
    scene ija1 with Dissolve(1.5)
    i "Oh yeah, you sure are wet!" with dissolve
    i "Did you know I always wanted to do this?"
    j "Why doesn't that surprise me?"
    j "Y-You're nuts..."
    $ renpy.music.set_volume(0.25, channel='music3')
    i "Is it helping? Are you feeling better?"
    j "Y-Yeah... A bit better..."
    $ renpy.music.set_volume(0.2, channel='music3')
    i "Good... now let's get these things out of the way..."
    $ renpy.music.set_volume(0.15, channel='music3')
    play music "judie1.ogg" fadein 2
    scene ija2 with Dissolve(1.5)
    j "Ahhh..." with dissolve
    j "Fuck..."
    i "Does that feel good? I've never done this before..."
    j "Y-Yes... It feels so fucking good..."
    j "Why didn't it feel like this when I tried to do it myself..."
    i "Damn babe, your pussy is tight as fuck!"
    i "How the hell does [me]'s cock fit in here?"
    j "I... I don't know..."
    j "Ahh... my god..."
    j "Go faster..."
    play music "judie2.mp3" fadein 2
    scene ija3 with Dissolve(1.5)
    j "AAAaah..."with dissolve
    j "Oh my g-god..."
    j "Shit, this feels intense..."
    j "Faster..."
    i "I can't go faster!"
    j "Fuck..."
    stop music fadeout 2
    play sound "couch.mp3"
    scene iri 61
    j "Ok, ok..." with dis
    j "S-stop..."
    i "Are you still feeling horny?"
    j "Even more than before..."
    j "I think it's time for something bigger..."
    scene iri 62
    j "This huge dildo will give me what I need..." with dis
    j "I should stop feeling this urge after..."
    play soundlow "punch2.mp3"
    play sound2 "couch.mp3"
    scene iri 63
    i "No way!" with hpunch
    i "It's my turn now!"
    i "I'm gonna use the dildo!"
    scene iri 64
    j "Whaaaat?" with dis
    i "I already fingered you! You had your fun! Now I want my turn!"
    j "But... now I'm even hornier than before because of you!"
    i "I said it's my turn! Don't be selfish!"
    scene iri 65
    j "Ok, ok... Use it yourself, but hurry up!" with dissolve
    i "Thanks babe! You're the best!"
    scene iri 66
    i "Hey, did your tits get bigger?" with dis
    j "H-Hey! Of course not!"
    j "They're the same size as always!"
    i "You sure? They look bigger to me."
    j "Stop groping me!"
    j "A-And they stopped growing years ago!"
    i "I don't know, I read in a magazine that..."
    play sound "slam.ogg"
    play sound2 "doorslam2.ogg"
    scene iri 67
    me "Fuck!" with hpunch
    play sound3 "fall2.ogg"
    scene iri 68
    me "Oh shit, what a fall..." with Dissolve(1.4)
    me "Uhh... h-hey girls!"
    me "I brought some wine!"
    scene iri 69
    j "[me]? What are you doing here?" with dis
    me "Well, I arrived here like we had planned and then I heard you two talking inside the room, so I put an ear to the door, but it burst open and I fell."
    j "W-what did you hear?"
    me "Something about you letting Iris use the dildo and your tits being bigger."
    scene iri 69
    j "O-Ok, t-this is not what it seems!"
    scene iri 70
    i "Actually, it is. We were masturbating each other."
    scene iri 69
    j "Iris!" with hpunch
    scene iri 70
    i "Did that bottle in your backpack contain something special?"
    me "Yeah... it's supposed to be an aphrodisiac."
    scene iri 69
    j "Really?! Of course!"
    scene iri 70
    if inc:
        i "That explains it. We were going crazy here, you know? Especially your sister."
    else:
        i "That explains it. We were going crazy here, you know? Especially Judie."
    me "I can imagine..."
    i "I guess we don't need the dildo anymore..."
    i "And since I’m such a generous person, I'll let you enjoy first, babe..."
    scene iri 69
    j "I... Really?"
    scene iri 70
    i "Yeah... come on, use my desk..."
    scene iri 71
    i "Oh yes..." with Dissolve(1.5)
    i "So hot..."
    i "I wanna see how that big cock stretches your tight pussy..."
    scene iri 72
    j "I still suspect that you already knew what that bottle contained..."with dis
    i "Did I know? No. Would I have poured you a glass anyway if I’d known? Hell yeah."
    j "You're a pervert."
    i "I can't help it."
    scene iri 73
    i "Come on, [me]! My parents are gonna arrive any minute! Satisfy Judie like she deserves!" with dissolve
    scene iri 74
    me "With pleasure..." with dis
    j "I've never needed you inside of me as much as I do right now..."
    scene iri 75
    me "Don't worry, my sweet girl... I'm here to help..." with dis
    me "(Oh boy, seems like I arrived just in time!)"
    play sound "penetration3.ogg"
    scene iri 76
    j "AAAaahh..." with Dissolve(1.3)
    me "Oh, Judie..."
    me "As tight as always..."
    i "I'd bet that feels a lot bigger than my fingers..."
    j "Y-You'd win t-that bet..."
    play sound "penetration3.ogg"
    scene iri 77
    j "AAAaAAAahh... YEAH..." with Dissolve(1.3)
    i "Wow..."
    j "Put it all the way in..."
    play music "judie4.mp3" fadein 2
    scene ija4 with Dissolve(1.5)
    j "MMmmmff..."with dissolve
    j "Y-You’re off to a pretty strong start, bro..."
    me "Y-You heard Iris..."
    if inc:
        me "Uncle Carl could be here any minute..."
    else:
        me "Her father could be here any minute..."
    me "I'm s-sure he wouldn't like to see this..."
    i "He wouldn't..."
    j "Aaahh..."
    j "Harder... Fuck me harder..."
    j "I wanna feel your body against mine..."
    me "Oh god..."
    play music "judie7.mp3"
    scene ija5 with Dissolve(1.5)
    j "Aaaaah yeah!"with dissolve
    j "O-O-OH MY GOD!!"
    j "This feels even better than usual!"
    j "Aaahhh..."
    i "Fuck..."
    i "Seeing you two fucking always drives me insane..."
    j "AAAAH..."
    i "You were meant to fuck each other..."
    scene ija6 with Dissolve(1.5)
    j "AhH... AHH... Ahhhh..." with dissolve
    i "Damn girl..."
    i "He's banging you like a drum..."
    j "F-f-fuck..."
    me "Oh Judie..."
    me "Your pussy is unrivalled..."
    i "Be careful not to break her, [me]..."
    me "She's a tough girl..."
    j "Aaaahh..."
    j "Let me lick your pussy..."
    j "I w-wanna know how it t-tastes..."
    i "Oh babe! That's the Judie I love!"
    scene ija7 with Dissolve(1.5)
    j "Mmmmm..." with dissolve
    i "Ohh... yeah..."
    i "Mmmm..."
    i "AAAAH!"
    i "Hot damn! Ahhh..."
    i "Y-You're better at this than I thought!"
    i "Ahh..."
    j "MMMmmmMmmff..."
    stop music
    play sound "cum1.ogg"
    scene iri 78
    j "AAAAAAARGH!" with hpunch
    $ judie_points += 1
    play sound "cum1.ogg"
    j "I'm cumming! I'm cumming..."with hpunch
    j "I h-have to stop..."
    j "Jesus fucking Christ..."
    i "(Chuckles) I've never heard you swear as much as I have today, Judie... That must have been good..."
    j "God, yes it was..."
    scene iri 79
    me "Oh, Judie..."with dis
    me "I..."
    scene iri 80
    i "*Kisses you*" with dis
    me "Hmm?!"
    scene iri 81
    me "Whoa, and that?"with dis
    i "Sorry."
    me "No! Don't say that, it was nice! It's just that I wasn't expecting it."
    i "I felt like kissing you."
    i "I... I couldn't be happier."
    i "I had a crush on you for years, you know?"
    i "I couldn't tell anyone because..."
    if inc:
        i "Well, you are my fucking cousin. I don't want people to think I'm a freak."
    else:
        i "Well, you're my best friend's step-brother. So that was kinda complicated."
    i "But now, here we are. Doing what I want. Being in a relationship with both the handsome love of my life and my best friend."
    i "(Laughs) If we can call ourselves that."
    me "Yeah, I think we can."
    i "And this Sunday we're taking a damn plane to god knows where, to live the life I've always dreamed about."
    scene iri 82
    i "I can't wait to have some fun with Lauren and the others..."
    scene iri 81
    i "I love you, [me]."
    me "I love you too, Iris."
    i "I know..."
    scene iri 82
    i "And now I want you to fuck me in the ass."
    play sound "slam.ogg"
    scene iri 83
    me "W-what?" (multiple=2) with hpunch
    j "WHAT?!" (multiple=2)
    j "D-did you say \“in the ass\”?! Did you mean you want to be fucked from behind? Like doggystyle??"
    i "I meant that as having anal sex."
    i "I've always wanted to try it. I won't have a better chance for my first time than this."
    i "I'm horny, I'm wet everywhere, and I have some lube in the drawer."
    j "B-But... isn't that supposed to hurt?"
    i "It doesn't have to. You don't know if you'll like it until you try it."
    i "But... only if [me] wants to try it too, of course..."
    me "Well..." with dissolve
    me "If you really wanna try it..."
    scene iri 84
    i "Yes, I do!" with dissolve
    j "Are you seriously gonna do it?"
    i "YES!"
    me "Where did you say you have that lube?"
    i "In the drawer!"
    play sound "couch.mp3"
    scene iri 85 with Dissolve(1.5)
    me "You sure about this, Iris?" with dissolve
    i "Yes..."
    i "It'll be like you took my virginity again..."
    me "Alright..."
    play sound "penetration3.ogg"
    scene iri 86
    i "Aaaarghh..." with Dissolve(1.5)
    scene iri 90
    j "Oh my god..."
    j "There's no way that will fit in there, don't you see?!"
    scene iri 86
    i "(Panting) Y-yeah, it will. I can take it. Go deeper, [me]..."
    play sound2 "penetration3.ogg"
    scene iri 87
    i "Aaaarghh... FUCK!" with Dissolve(1.5)
    me "Oh my fucking god... This sensation is unbelievable..."
    me "Y-You alright? Am I hurting you?"
    i "J-Just a bit... b-but don't worry..."
    i "Keep going..."
    play sound3 "penetration3.ogg"
    scene iri 86
    i "Aaaarghh..."with dis
    play sound4 "penetration3.ogg"
    scene iri 88
    i "Mmmmmmmfff..."with Dissolve(1.3)
    me "Better?"
    i "Mm-hm..."
    play sound "penetration3.ogg"
    scene iri 86
    i "Ahhh..." with dis
    play sound2 "penetration3.ogg"
    scene iri 89
    i "Aaaahhhhh..."with dis
    i "Holy fuck..."
    i "I think it's starting to feel good..."
    play music "anal1.ogg"
    scene ija8 with Dissolve(1.5)
    i "AHHH... FUCK..." with dissolve
    me "AHHHH GOD!"
    me "T-This is incredible..."
    i "This feels different..."
    i "B-but I like it..."
    me "Let me know if I'm going too fast..."
    i "You're n-not. Fuck my little asshole..."
    play music "anal2.ogg"
    scene ija9 with Dissolve(1.5)
    i "AAAAH!" with dissolve
    me "O-o-oh... Iris..."
    i "Oh Jesus..."
    scene iri 90
    j "D-does that feel good?" with dis
    i "AHHH... It's so amazing!"
    j "Really?"
    scene ija9
    i "Yeah!" with dis
    i "(Panting) It hurt a bit at first, but now..."
    i "Damn babe, I think I'm s-seeing stars..."
    i "I don't know if it's because of that aphrodisiac, but..."
    i "AAHHH..."
    i "Oh my god, I think I'm gonna cum!"
    i "I'm cumming!!"
    stop music
    play sound "cum1.ogg"
    scene iri 91
    i "AAAAAAARGH!" with hpunch
    play sound "cum1.ogg"
    i "FUUUCK!" with hpunch
    play sound2 "couch.mp3"
    scene iri 92
    i "Ahhh..." with dis
    i "Oh my god..."
    i "I just had an anal orgasm!"
    i "And it was spectacular... Better than a vaginal orgasm!"
    i "We have to get more of that aphrodisiac..."
    scene iri 90
    j "B-Better than a vaginal orgasm?"
    scene iri 92
    i "Yeah..."
    i "Wow..."
    scene iri 90
    j "Um..."
    j "Can I..."
    j "Can I try it?"
    scene iri 92
    i "You HAVE to try it."
    i "Bend over..."
    i "Just give me... a few seconds..."
    scene iri 93 with Dissolve(1.5)
    i "Believe me babe, you'll thank me later." with dissolve
    scene iri 94
    me "Are you sure about this, Judie?" with Dissolve(1.2)
    me "I mean, we can try it, but... I'm not sure it's gonna work."
    me "Your pussy is already tight as fuck, I can't even imagine your other hole..."
    i "I think she'll surprise us. She always does."
    i "What's the biggest thing you ever put in there?"
    scene iri 95
    j "W-what? Um... nothing?" with dissolve
    j "A-Am I supposed to put things in there?"
    scene iri 96
    me "Fuck... I can’t wait to squeeze into this tight little ass of yours..." with dis
    me "Are you ready, Judie?"
    me "I promise to be gentle."
    scene iri 97
    j "I'm nervous, but... yes, I'm ready, bro." with dis
    play sound4 "penetration3.ogg"
    scene iri 98
    j "Mmmmmmff..."with Dissolve(1.5)
    me "Oh my fucking god, you have to be kidding me..."
    me "I can’t fit... it won’t go in any further..."
    scene iri 100
    i "All good, babe?" with dis
    j "Y-yeah... but it's too big..."
    me "Yeah... I can't go in..."
    scene iri 98
    i "You have to relax, Judie!" with dis
    i "Stop thinking it's gonna hurt!"
    i "Just let yourself go and allow him to slip inside of you..."
    play sound4 "penetration3.ogg"
    scene iri 99
    j "AAARGH..."with Dissolve(1.2)
    me "Oh, Judie... I'm inside..."
    scene iri 100
    j "It... hurts a bit, Iris..."
    i " I know, don't worry! Just let the lube spread..."
    play music "anal3.ogg"
    scene ija10 with Dissolve(1.5)
    play music "anal3.ogg"
    j "Ahhh... ahhh... ahhh..." with dissolve
    me "Oh Judie..."
    me "I feel like my dick is gonna explode already..."
    j "Oh my god!"
    j "I'm... I'm being fucked in the ass!"
    j "Ahh..."
    j "And it feels so good..."
    j "I wanna feel you in every hole of my body..."
    j "Ahhh..."
    j "Fuck my ass harder, [me]..."
    play music "anal2.ogg"
    scene ija11 with Dissolve(1.5)
    j "AHHH... AHHH... AHHHH..." with dissolve
    i "Wow..."
    j "YEAH! OH JESUS!"
    j "Y-YOU WERE RIGHT, IRIS! T-THIS IS..."
    j "AMAZING..."
    j "IT'S SO INTENSE..."
    i "Told you..."
    j "AAaaaahhh..."
    scene ija12 with Dissolve(1.5)
    j "Arrrghhh..." with dissolve
    j "Oh god..."
    me "Oh baby..."
    scene ija11 with Dissolve(1.5)
    j "AHHH... AHHH... AHHHH..." with dissolve
    j "It feels so different... So good..."
    j "ARGH...." with dissolve
    j "I'm gonna cum again..."
    me "Ahhh... me too..."
    j "Let's cum together, bro..."
    j "Unload your seed deep inside my asshole..."
    me "Ahh..."
    stop music fadeout 1.5
    scene iri 101 with dis
    play sound "cum2.ogg"
    me "(Cumming inside) AAAAAAH..." with hpunch
    play sound2 "cum2.ogg"
    j "(Orgasming) AAAAAARRRRRRRGHHHH..." with hpunch
    j "OH GOD..."
    scene iri 102
    play sound "cum2.ogg"
    me "(Cumming inside) AAAAAAH..." with hpunch
    play sound3 "cream.mp3"
    scene iri 103
    me "Jesus..." with Dissolve(1.5)
    me "Oh Judie..."
    scene iri 101
    i "I love when you make that face, babe..." with dis
    i "Your face can't lie... I know it was good..."
    j "It was... Gggff..."
    me "Oh, fuck..."
    me "I’ve emptied every last drop of cum left in my body..."
    j "I c-can't get up..."
    stop music3
    scene gallerybackground
    call screen gallery5 with Dissolve(1)
label gfinal:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene last 3
    me "(Turning around) Ah, thank god, for a moment I thought that..." with dis
    $ renpy.music.set_volume(0.2, channel='music3')
    play music3 "4ever.ogg" fadein 8
    me "L-Lauren?"
    scene last 4
    me "W-Why are you naked?" with dis
    me "You should get dressed before Judie comes back!"
    me "If she sees you like this, she'll think that..."
    j "(Laughs) I'll think what?"
    scene last 5
    me "W-What?!" with dis
    me "Judie this is not what it looks... Uhh..."
    scene last 6
    me "J-Judie? W-Why are you naked too? " with dis
    me "What the hell is going on?"
    me "Um... Are you guys drunk?"
    me "Are you okay?!"
    scene last 7
    l "Oh yeah, we're better than okay! " with dis
    l "Why don’t you make yourself more comfortable? I think you’re wearing too many clothes..."
    me "My c-clothes? Um... Are we playing some kind of game?"
    l "Hmm... maybe..."
    l "Just do it. You won't regret it..."
    play sound "takeoff.ogg"
    scene last 8
    l "Judie and I had a little conversation while you were in the lobby, and we discovered we have even more in common than we thought..." with dissolve
    me "Um..."
    l "Not gonna lie, we needed a few minutes to process things, but after that... I came to the understanding that my little sister deserves to be as happy as I am."
    scene last 7
    l "You taught us that we're a team, [me], that we need each other." with dissolve
    l "How could we ever be apart after everything we've been through?"
    l "I love you and Judie more than anything else."
    scene last 8
    l "So when I found out that Judie can share our love too... I was relieved." with dissolve
    scene last 7
    l "(Chuckles) And also kinda excited. I mean, who am I kidding?" with dissolve
    l "We all deserve to be with each other."
    me "Am... am I dreaming?"
    scene last 9
    l "No, you're not dreaming, [me]." with dis
    l "It's just that..."
    l "I know that tomorrow we'll defeat Astaroth... that we'll win once and for all..."
    l "But from a certain view, I think we're saying goodbye to our \"normal\" life tonight."
    l "So... in any case, this is a special night that deserves to be remembered."
    l "And we thought that, together, we could make it even more special..."
    me "(Oh my god...)"
    scene last 10
    l "Judie! Come on, don't be shy now! Come down here!" with dis
    l "This was your idea!"
    scene last 11
    if inc:
        l "Judie suggested that we could give a little \"thank you\" to our beloved brother... together..." with dis
    else:
        l "Judie suggested that we could give a little \"thank you\" to our beloved step-brother... together..." with dis
    l "And show just how much we both appreciate you..."
    l "Didn't you, babe?"
    j "Yes... yes I did..."
    l "Well... it seems like he's ready to go..."
    l "And you look pretty eager, sis..."
    j "I am..."
    scene last 12
    l "I bet you’ve fantasized about this moment before..." with dis
    me "You don't know how many times..."
    l "Haha, I can imagine..."
    scene last 13
    j "Mmmm..." with dis
    me "Oh yeah, Judie..."
    l "Damn sis... are you sure his cock isn't too big for you?"
    l "You think you can take it all?"
    j "Mm-hmm..."
    l "Really? Well..."
    l "(Whispering) Show me..."
    stop music3 fadeout 5
    $ renpy.music.set_volume(0.05, channel='music2')
    play music2 "4ever.ogg" fadein 3
    play music "blow1_3.ogg" fadein 1.5
    scene judielauren1 with Dissolve(1.5)
    me "Ahhh... yeah..." with dissolve
    l "Does it feel good?"
    me "Ahh... it does..."
    l "I've always been afraid of Judie discovering what we were doing..."
    l "And it turns out that she's more of a nympho than I am..."
    me "Ahh... yeah she is..."
    l "Come on, Judie... Let's show [me] what we can do..."
    j "Mmmm..."
    play music "blow1.ogg"
    scene judielauren2 with dis
    me "Ooooh my fucking god, Judie..." with dissolve
    l "Wow, sis..."
    l "You're setting the bar very high..."
    j "(Gagging) Mmmm..."
    l "Holy shit, you deepthroat like a pro..."
    l "I love watching you swallow every inch of his hard cock..."
    l "This must feel incredible for you, hmm [me]?"
    me "My god..."
    me "I can feel the back of her throat with each thrust..."
    me "She’s slobbering all over my dick..."
    j "Mmmhmmm..."
    l "This is making me horny as fuck..."
    l "Are you gonna let your sister have some fun too?"
    j "Mmmm-"
    stop music fadeout 0.5
    scene last 13b
    j "(Gasping for air) AAAAAaaah...!!" with Dissolve(.8)
    j "Ahhhh... Oh my god..."
    l "Will you let me taste it now...?"
    me "Yeah..."
    l "I'm gonna pick up the slack, if you don't mind, sis..."
    j "Yeah... I need a minute to catch my breath..."
    j "It's all yours... I want to watch you..."
    scene last 13d
    me "(Getting up) Ahh... Come here Lauren..." with dis
    l "Mmm..."
    me "Ahh..."
    me "Do you taste Judie's saliva all over my cock?"
    l "Mm-hm..."
    scene last 13c
    l "Mmm... I do... it tastes so good..." with dis
    me "Do you wanna make a mess of my dick too?"
    l "Yeah... I'm so hungry for it..."
    l "Fuck my mouth, baby..."
    l "Hard..."
    me "Oh, I will..."
    me "Come here..."
    scene last 14
    l "(Gagging) Mmm!" with dis
    me "Oh yeah..."
    play music "blowjob2.mp3" fadein 2
    scene judielauren3 with Dissolve(1.5)
    me "Aaaahhh..." with dissolve
    me "My fucking god Lauren..."
    me "This feels too good..."
    j "Oh my god, sis..."
    j "Seeing you deepthroat that cock is driving me crazy..."
    me "(Oh Jesus, if the receptionist saw what I'm doing to my \"cute little sisters\" right now...)"
    stop music fadeout .5
    scene last 14
    l "MMMmm..." with dis
    scene last 15
    l "(Gasping for air) Arghh..." with dis
    l "Fuck..."
    scene last 16
    l "!!!" with hpunch
    scene last 17
    l "J-Judie?!"
    l "Ahh... What are you d-doing..."
    j "(Fingering Lauren) Nothing! Just giving you a little extra attention while you work that cock..."
    scene last 18
    l "A l-little e-ext... Aaaaahh..."
    j "Does it feel good?"
    l "Ahh... Y-yes..."
    j "(Fingering her sister) Damn, you're soaking wet... I think we're gonna leave a puddle on this carpet..."
    l "A-a-ahhhhh...."
    me "This is too fucking hot girls..."
    scene last 15
    me "Come back here, Lauren..." with dissolve
    l "Oohh..."
    me "I need to feel your mouth again..."
    play music "blowjob2.mp3" fadein 2
    scene judielauren4 with Dissolve(1.5)
    me "AAAH... Yes..." with dissolve
    me "That's it baby..."
    l "*Gagging*"
    j "(Fingering her sister) Wow..."
    me "Oh Lauren..."
    l "(Gagging) Mmmmm..."
    pause
    me "Oh, fuck... I think I'm gonna cum..." with dissolve
    me "(I can't cum now... Not yet...)"
    stop music fadeout .5
    scene last 15
    l "(Gasping for air) AHHHHH!!" with dis
    l "(Catching her breath) I n-need... ahhh... j-just give me a second..."
    scene last 19
    j "See, this wasn’t such a bad idea, now was it?" with dis
    l "Ahh..."
    l "I said it was a crazy idea... not a bad one..."
    j "I have to admit, sis... Doing this with you was fun. I enjoyed sharing this moment together..."
    scene last 19b
    l "*Kisses Judie*" with Dissolve(.8)
    j "Hmm?!"
    scene last 20
    l "(Getting up) Now come to bed!" with dis
    j "W-what?"
    scene last 21
    l "You're right, this was fun. And now we’re gonna have an even better time."
    l "I don't know about you, Judie, but I need to feel [me]'s cock deep inside me..."
    l "Would you like that too?"
    scene last 20
    j "I, well... yes. I would love that..."
    scene last 21
    l "Mm, I like the sound of that..."with dissolve
    l "Let's jump right to it, then..."
    scene last 22
    l "Well... Only if [me] wants it too, of course..."
    me "Do I even need to answer that?"
    l "Haha..."
    scene last 21
    l "What do you say, sis? I think we also deserve to get some more pleasure tonight..." with dissolve
    j "You're right..."
    play sound "couch.mp3"
    scene last 23
    j "Although..." with dis
    j "I don't know if [me] will be able to satisfy us both..."
    j "He mentioned that he was really tired before... do you think he has what it takes?"
    scene last 24
    me "My precious angels..." with dissolve
    me "Believe me, with this beautiful sight before my eyes, they'd have to kill me to stop me..."
    me "I'm gonna make you both cum so hard..."
    scene last 23
    j "(Giggles) We'll see about that..." with dissolve
    scene last 24
    me "Come here, Judie..." with dissolve
    me "Get on top of me..."
    scene last 25
    j "(Getting on top of you) Ah... my whole body is trembling like a leaf..." with Dissolve(1.3)
    scene last 26
    me "Why? It's not like it's our first time..."
    me "Are you nervous about something?"
    scene last 27
    l "Is it because I'm here?" with dis
    j "N-No! It's just... I’ve been looking forward to this moment ever since we started..."
    j "I can't stand it any longer..."
    me "Well, in that case... let's not waste any more time."
    j "*Giggles*"
    scene last 28
    j "I won't..." with dis
    scene last 29
    j "Ahh..." with dis
    me "Oh yes..."
    me "Just a little lower..."
    scene last 30
    j "AAaah..." with dis
    l ". . ."
    scene last 31
    j "Oh god..."
    j "You feel so big inside of me..."
    me "And you feel so good..."
    j "Will it always be this tight?"
    me "Jesus, I hope so..."
    scene last 32
    l "Oh my god, this is even hotter than I thought it would be..." with dis
    l "I bet Judie's pussy feels tight as fuck..."
    me "It does..."
    l "God, you're making me hornier than ever..."
    l "You should start riding him, sister... let your juices lubricate [me]'s big cock..."
    j "Yeah..."
    $ renpy.music.set_volume(0.4, channel='music3')
    play music3 "jl5.ogg" fadein 2
    scene judielauren5 with dis
    j "Ahhhhhh..." with dissolve
    j "Yeah... YEAH..."
    l "*French-kissing you*"
    l "Mmmm..."
    me "(Oh my god, this is...)"
    j "Incredible..."
    scene judielauren6 with dis
    j "Oh god..." with dissolve
    j "Mmmmmm... YEAH..."
    scene judielauren5 with dis
    j "Ahhh..." with dissolve
    j "Oh Jesus, I could ride your cock forever..."
    j "AaAaaaaahhh..." with dissolve
    j "You’re sooo big... sooo hard..."
    j "I need... I need more of you..."
    j "I'm gonna go faster..."
    l "Mmmmm..."
    play music3 "jl1.ogg"
    scene judielauren7 with dis
    j "AAAAaahh..." with dissolve
    me "AAAhh... Oh fuck, Judie..."
    l "(Fingering herself) Oh my god, Judie..."
    l "My little sister's all grown up..."
    j "Ahh.. ahh... ahhhh..."
    scene judielauren8 with dis
    j "Aaaahhh..." with dissolve
    me "Oooooh god..."
    me "Keep riding me like that, baby..."
    l "(Fingering herself) Oh damn, Judie... That thing is gonna tear you apart..."
    l "Aaah..."
    scene judielauren7 with dis
    j "AHH... AHHH.... AHHH..." with dissolve
    me "OH GOD...."
    me "Oh god... I'm gonna cum..." with dissolve
    l "Oh no you won't, mister!"
    l "Not until I’m done with you! I'm not going anywhere until you fuck me!"
    me "But... ahhhh.... I can't... hold...."
    j "AHH... AAAHHH... AAhhh..."
    j "I'm almost there..."
    j "I'm about to..."
    j "To..."
    stop music3
    play sound "gsv.mp3"
    scene last 33
    j "AAAAAAARGHHH..." with hpunch
    play sound "gsv.mp3"
    j "AAAaahhh..." with hpunch
    play sound "gsv.mp3"
    j "Aaaah..." with hpunch
    scene judielauren9
    with Dissolve(2)
    j "(Panting) Ah... ahh... ah..." with dissolve
    me "Oh my god, Judie..."
    j "(Panting) I have never had an orgasm like that before..."
    me "It sure was intense..."
    j "(Recovering her breath) You're... amazing..."
    l "(Chuckles) So... do you think I can have my turn with you now?" with dissolve
    me "Oh yeah you can, babe..."
    j "It's all yours, sis..."
    me "Come here, Lauren..." with dissolve
    scene last 34
    me "Are you ready?" with Dissolve(1.5)
    l "Yeah..."
    me "I can feel you're wet as fuck Lauren..."
    l "Ahh... I know..."
    l "I can't stand another minute..."
    l "I want you to fuck me harder than ever..."
    j "Oh my god, this is so hot..."
    scene last 35
    me "Oh, I'm gonna split you in half like a fucking piece of lumber..." with dis
    l "Oh really?"
    l "Well be sure not to cum too fast, mister..."
    me "Oh girl..."
    me "You'll see..."
    scene last 36
    l "AAAaahh..." with dis
    l "Yeah!"
    me "Oh yes..."
    scene last 37
    j "Oh my god, sis!! I can't believe we're finally doing this together!" with dis
    l "Haha, I know..."
    j "Can I kiss [me] while he's... inside you?"
    l "Huh? Of course you can... kiss him whenever you’d like! Plus, that’ll make me even hornier..."
    l "Now fuck me already..."
    l "Stretch my little pussy with your huge cock [me]..."
    me "With pleasure..."
    $ renpy.music.set_volume(0.5, channel='music3')
    play music3 "jl2.ogg" fadein 1.5
    scene judielauren10 with Dissolve(1.3)
    l "AAaaahhh... Yes... Yes..." with dissolve
    j "*French-kissing you*"
    j "Mmmmmm..."
    me "(Her lips are so soft...)"
    me "(God, and Lauren is dripping wet as always...)"
    l "Ahh... ahh... aahhh..."
    l "K-keep going... yeah..."
    scene judielauren10 with dis
    l "Mm.... Mmmm... Mmm..." with dissolve
    scene judielauren11 with dis
    l "AAAAahh..." with dissolve
    j "*Moaning*"
    l "Fuck me... fuck me harder..."
    play music3 "jl3.ogg"
    scene judielauren12 with dis
    l "F-FUCK!" with dissolve
    me "AAAargh..."
    l "(Crying out) A-a-a-aa-a-ahhhh..."
    l "Oh my f-fucking g-g-god-d-d..."
    me "Argh... yeah... this feels too good Lauren..."
    l "Don't you dare stop... please, I’m begging you..."
    scene judielauren12 with dis
    l "AHHH... AHHH..." with dissolve
    l "GOD..."
    scene judielauren13 with dis
    l "(Groaning) Ahhh... ahh..." with dissolve
    me "Oh Lauren..."
    j "Ahhh... He..."
    j "He's making that pussy his, sis..."
    l "Y-yeah..."
    me "You can take it, right Lauren?"
    l "Yeah... I love it..."
    l "Ahh.... Keep pounding me like that..."
    me "Oh my fucking god..." with dissolve
    me "This time I'm gonna cum for sure..."
    me "I'm at my limit..."
    l "AHH... AAAHHH... AAhhh..."
    l "OH GOD!!!"
    me "Ahh..."
    l "YEAH! YEAH! I'M GONNA..."
    l "I'M..."
    stop music3
    play sound "gsv.mp3"
    scene last 38
    l "AAAAAAARHHH..." with hpunch
    play sound "gsv.mp3"
    l "AAAaahhh..." with hpunch
    play sound "gsv.mp3"
    l "Aaaah..." with hpunch
    scene judielauren14
    with Dissolve(2.2)
    l "(Panting) Ah... ahh... ah..." with dissolve
    me "Jesus Christ..."
    me "Are you ok?"
    l "(Panting) I c-can't feel my arms... o-or my legs..."
    me "Baby... did you cum?"
    l "(Recovering her breath) I... I'm still cumming..."
    l "G-Give me.... a minute..."
    l "Jesus..."
    menu:
        with dis
        "Finish inside one of them":
            menu:
                with dis
                "Judie":
                    play sound "fall2.ogg"
                    scene last 44 with dis
                    me "Oh, Judie..." with dissolve
                    me "I'm about to burst..."
                    j "Well what are you waiting for?"
                    j "Just get back inside of me..."
                    scene last 45
                    me "Aah...." with dis
                    j "Yeah..."
                    me "Ohhh... yes..."
                    j "Fill me up with your cum..."
                    me "Do you want that, baby?"
                    j "Yes... I want you to shoot your load deep inside me..."
                    me "Oh yeah?"
                    j "I want you balls deep, filling my little pussy with all of your hot cum..."
                    j "Give it to me..."
                    me "Oh baby, I'm going to..."
                    play sound "piston3.ogg"
                    scene last 46
                    j "AAAAAAAHHH..." with hpunch
                    j "Y-YEAH!"
                    me "Arghh... I'm cumming..."
                    play sound "cum1.ogg"
                    me "AHH..." with hpunch
                    play sound "cum1.ogg"
                    me "Ahhhhh...."with hpunch
                    play sound "cum1.ogg"
                    me "Aaahh..."with hpunch
                    play sound "cream2.mp3" fadein 1
                    scene last 47
                    me "Fuck..." with Dissolve(1.2)
                    me "I have never cum so much in my life..."
                    j "Oh my god... I feel... so full..."
                    if inc:
                        me "Well, I filled you all the way up, sis..."
                    else:
                        me "Well, I filled you all the way up..."
                    scene last 48
                    me "You were begging for it..." with dis
                    j "(Panting) Haha, I know... and I loved it..."
                    if pregnancy:
                        j "Besides, it doesn't matter much anymore..."
                        me "What do you mean? Are you on the pill now?"
                        j "More or less... I'll tell you about it when we get on that plane and leave this place..."
                    j "Now if you’ll excuse me, I think I’m going to get cleaned up a little. You made such a mess of me..."
                    me "Of course..."
                    j "Thank you..."
                "Lauren":
                    play sound "fall2.ogg"
                    scene last 39 with dis
                    me "Oh, Lauren..." with dissolve
                    me "I'm about to burst..."
                    l "Well what are you waiting for?"
                    l "Just get back inside of me..."
                    scene last 40
                    me "Aah...." with dis
                    l "Yeahh..."
                    me "Ohhh... yes..."
                    l "Fill me up with your cum..."
                    me "Do you want that, baby?"
                    l "Yes... I want you to shoot your load deep inside me..."
                    me "Oh yeah?"
                    l "I want you balls deep, filling my little pussy with all of your hot cum..."
                    l "Give it to me..."
                    me "Oh baby, I'm going to..."
                    play sound "piston3.ogg"
                    scene last 41
                    l "AAAAAAAHHH..." with hpunch
                    l "YEAH!"
                    me "Arghh... I'm cumming..."
                    play sound "cum1.ogg"
                    me "AHH..." with hpunch
                    play sound "cum1.ogg"
                    me "Ahhhhh...."with hpunch
                    play sound "cum1.ogg"
                    me "Aaahh..."with hpunch
                    play sound "cream2.mp3" fadein 1
                    scene last 42
                    me "Fuck..." with Dissolve(1.2)
                    me "I have never cum so much in my life..."
                    l "Oh my god... I feel... so full..."
                    if inc:
                        me "Well, I filled you all the way up, sis..."
                    else:
                        me "Well, I filled you all the way up..."
                    scene last 43
                    me "You were begging for it..." with dis
                    l "(Panting) Haha, I know... and I loved it..."
                    if pregnancy:
                        l "Besides, it doesn't matter much anymore..."
                        me "What do you mean? Are you on the pill now?"
                        l "More or less... I'll tell you about it when we get on the plane and leave this place..."
                    l "Now if you’ll excuse me, I think I’m going to get cleaned up a little. You made such a mess of me..."
                    me "Of course..."
                    l "Thank you..."
        "Facial":
            play sound "fall2.ogg"
            scene last 49 with dis
            me "Come here girls, get on your knees..." with dissolve
            me "My loves..."
            me "Do you want me to cum all over you? All over those beautiful faces?"
            l "Yeah..."
            j "I want it..."
            scene last 50
            me "My princesses..." with dis
            scene last 51 with dissolve
            scene last 50 with dissolve
            scene last 51 with dissolve
            scene last 50 with dissolve
            scene last 51 with dissolve
            scene last 52
            me "Ahhh... I'm cumming..." with dis
            play sound "cum1.ogg"
            scene last 53
            me "AAAAAAAHHH..." with hpunch
            play sound "cum1.ogg"
            scene last 54
            me "Aaaahhh..." with hpunch
            me "YEAH... TAKE IT ALL..."
            scene last 55
            me "Ahhh..." with dis
            me "Oh god..."
            me "I have never cum so much in my life..."
            j "My god, you made a mess of us..."
            l "It tastes so good..."
            j "I have your seed all over my body..."
            me "Well, you two were begging for it..."
            l "Yeah, we know..."
            j "And we loved it..."
            l "We love being naughty only for you..."
            j "Nobody else..."
            j "But maybe we should clean ourselves now, if you'll excuse us..."
            me "Of course..."
            l "Thank you..."
    play sound "fall2.ogg"
    scene last 56 with Dissolve(1.5)
    stop music2 fadeout 10
    play music "night.ogg" fadein 10
    me "DAMN!" with dissolve
    me "I'm exhausted!"
    me "You're insatiable, girls..."
    me "Tonight was..."
    scene last 57
    j "So. Very. Perfect." with dis
    scene last 58
    l "If someone had told me a few months ago that this was gonna happen, I'd have kicked them in the nuts." with dis
    l "And now... here we are."
    l "I wouldn't trade what we have... what we did... for anything in the world."
    l "I..."
    l "I love you, [me]..."
    scene last 57
    j "I love you [me]!" with dis
    scene last 58b
    l "*Kisses you*" (multiple=2) with Dissolve(1.3)
    j "*Kisses you*" (multiple=2)
    scene last 57
    j "And we always will!"with dis
    scene last 58
    l "Don't ever leave us..." with dissolve
    scene last 59
    me "Leave you?" with dis
    me "Never."
    stop music3
    scene gallerybackground
    call screen gallery5 with Dissolve(1)





label gjudierub:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene hide23
    j "(Whispering) Boy, that was close. Sounds like they're changing. They are no longer looking for us, thank goodness." with dissolve
    scene hide24 with dissolve
    $ renpy.pause ()
    me "(Oh my god...)" with dissolve
    me "(I won’t last much longer without...)"
    me "(Oh no...)"
    scene hide6
    me "(Whispering) Erm... Judie, you might notice something shortly that can become kind of awkward."
    scene hide7
    j "Shhh, tell me about it later."
    scene hide25
    with Dissolve (1)
    $ renpy.pause ()
    scene hide26 with dissolve
    $ renpy.pause ()
    scene hide27
    with Dissolve (1)
    $ renpy.pause ()
    scene hide28
    $ renpy.pause ()
    scene hide29
    j "Wh... what... what the hell do you think you’re doing???"
    scene hide28
    me "(Whispering) It's not my fault! I can't control it."
    scene hide29
    j "How can you get a hard-on in a situation like this?"
    scene hide28
    me "I don't know, we're very squashed in here... it's a physiological response, completely innocent and accidental."
    scene hide29
    j "No, you're a pervert!"
    scene hide22
    t "And then I was like: You want me to throw you off the bridge, bitch?"
    ja "Hahaha, and what did she say?"
    scene hide31
    with Dissolve (1)
    j "For God's sake, they have been talking for ages. They’re never gonna leave?" with dissolve
    j "And if this... situation... were not enough, all those beers are starting to make me feel dizzy..."
    scene hide32
    me "Yeah, I'm sorry about “this situation”."
    scene hide31
    j "What?"
    scene hide33
    j "Ah, that... don't worry, I'm not bothered any more."
    j "Actually... it's even starting to feel good."
    j "It's feels... warm..."
    scene hide31
    j "It feels...{w} ... good..." with dissolve
    scene tight2
    with Dissolve (2)
    $ renpy.pause ()
    me "(Oh. my. god.)" with dissolve
    me "(Am I dreaming?)"
    me "(She just started rubbing against my dick!)"
    me "(Ohh sweet heaven...)"
    $ renpy.pause ()
    scene hide22
    t "And then that guy at the gym comes to me and he says: dude you're doing it wrong."
    scene hide30
    t "And I say: You want me to throw the bar at your head?"
    scene tight
    with Dissolve (2)
    $ renpy.pause ()
    me "(Oh yes... she's gone mad...)" with dissolve
    j "Aaah...."
    $ renpy.pause ()
    scene hide34
    t "Ok, let's get going. Are you ready?"
    ja "Ready, let's go."
    scene hide35
    with Dissolve (1.5)
    play sound "doorclose.ogg"
    $ renpy.pause ()
    me "He's gone." with dissolve
    me "We're alone now... should we...?"
    j "We should... we..."
    scene hide36
    j "We should what?"
    scene hide37
    j "OH MY GOD WHAT ARE WE DOING?"
    play sound "dooropen.ogg"
    scene hide38 with dissolve
    j "What the heck did I do?!"
    j "Oh god, how embarrassing."
    j "Look, hey, [me], haha, erm... I'm so drunk and I’ve lost my mind, so..."
    me "Don't worry Judie, I..."
    scene hide39
    j "Yeah, ok, it's forgotten then, great."
    j "Cool."
    j "Cool, cool, cool, cool."
    j "Well, I'll get going, yes, I'm going with Lauren and Iris, they must be wondering where I am."
    j "I'll see you later... or tomorrow... or next week. Bye!"
    scene hide11 with dissolve
    $ renpy.pause ()
    me "Wow, I don’t know exactly what happened, but damn, that was incredible." with dissolve
    me "I should get dressed and get out of here."
    scene gallerybackground
    call screen gallery with Dissolve(1)



label grebeccashower:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene sp 13
    me "(I haven't looked behind that door, though.)" with dissolve
    play sound "dooropen.ogg"
    scene sp 14 with Dissolve(1)
    play music "shower.ogg"
    me "Oh, it's a bathroom." with dissolve
    scene sp 15 with dissolve
    me "(It can't be...)" with dissolve
    scene sp 16 with dissolve
    $ renpy.pause ()
    me "(What is this heavenly sight I see before me?)" with dissolve
    me "(I know I shouldn't but... I can’t control my body...)"
    me "(I need to see more..)"
    me "(Just a little bit more..)"
    play sound "slidingdoor2.ogg"
    scene sp 17 with dissolve
    $ renpy.pause ()
    r "Hello honey, I though you’d be gone by now." with dissolve
    scene sp 18
    r "I see you couldn’t leave without saying goodbye to your woman..."
    scene sp 17
    r "I’m afraid we can’t entertain ourselves. My first student will be here soon."
    scene sp 19 with dissolve
    $ renpy.pause ()
    scene sp 20 with dissolve
    $ renpy.pause ()
    r "I'm almost done here." with dissolve
    scene sp 19 with dissolve
    $ renpy.pause ()
    scene sp 17 with dissolve
    $ renpy.pause ()
    scene sp 18
    r "Are you still here?" with dissolve
    r "You sure are playful today... I thought you said you were too tired lately..."
    scene sp 17
    r "Are you gonna take advantage of me? Now that I can’t open my eyes? You know it turns me on when I can’t see..."
    r "Don't you dare..."
    $ renpy.pause ()
    scene sp 18
    r "Hello?" with dissolve
    scene sp 21
    r "Are you gonna say something or what?" with dissolve
    scene sp 22
    me "(Oh Jesus Christ.)" with dissolve
    $ renpy.pause ()
    scene sp 23
    with Dissolve (1)
    $ renpy.pause ()
    scene sp 24
    with Dissolve (1)
    $ renpy.pause ()
    scene sp 25
    with Dissolve (1)
    $ renpy.pause ()
    r "Erm... David, are you all right?" with dissolve
    r "Honey?"
    scene sp 26 with dissolve
    r "For God's sake..."
    $ renpy.pause ()
    scene sp 27 with dissolve
    $ renpy.pause ()
    scene sp 28
    r "(Wow, he left.)"
    r "(He actually left.)"
    scene sp 29
    r "(I feel foolish right now.)"
    r "(Forgive me for trying to put a little passion into our relationship, David.)"
    r "(Unbelievable....)"
    r "(Anyway, I should get ready, [me] will be here any minute.)"
    stop music fadeout 1
    scene gallerybackground
    call screen gallery with Dissolve(1)




label gjudietemple:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene temple 61
    me "Thank you Judie, I really like spending time with you too." with dissolve
    me "But what about the party? Why are you nervous?"
    scene temple 63
    j "Well, you know, I haven’t decided what costume to wear yet..."
    j "Also, the girls talk about what we’ll do there, and they want to play some silly kissing game..."
    scene temple 61
    me "And?"
    scene temple 62
    j "Well, I've never kissed a boy..."
    scene temple 63
    j "And well... erm... I'm kinda nervous about..."
    scene temple 61
    me "Come on Judie, you don't have to worry about that."
    me "It just comes naturally, I'm sure it'll be fine."
    scene temple 63
    j "I guess..."
    me "If it helps you out, I could teach you how to kiss..."
    scene temple 62
    j "What?!"
    j "And we have to kiss?"
    me "Yeah well, I see no other way..."
    scene temple 63
    j "I... I don't know..."
    me "Not if you don't want..."
    scene temple 62
    j "...okay! But just one kiss! ...and you tell me what I do wrong!"
    me "Of course. That's why we're doing it."
    scene temple 64 with dissolve
    j "Okay... here goes."
    j "Just one kiss."
    scene temple 65 with dissolve
    $ renpy.pause ()
    scene temple 66 with dissolve
    $ renpy.pause ()
    scene temple 67 with dissolve
    $ renpy.pause ()
    scene temple 68 with dissolve
    $ renpy.pause ()
    j ". . ." with dissolve
    scene temple 67 with dissolve
    $ renpy.pause ()
    scene temple 69 with dissolve
    $ renpy.pause ()
    scene temple 70
    with Dissolve (1)
    $ renpy.pause ()
    scene temple 71 with dissolve
    $ renpy.pause ()
    scene temple 72 with dissolve
    j "OK... that was fun! I liked it! Did you like it?"
    scene temple 73
    me "A lot."
    scene temple 72
    j "I mean, was I OK at kissing?"
    scene temple 73
    me "Definitely."
    me "However, in this kind of game, people usually get carried away, and go beyond kissing..."
    scene temple 74
    j "What are you trying to say?..."
    scene temple 75
    me "I'm just saying that, once you're at that party, if you want to take it further, you have to be prepared. At least not to panic."
    me "I'm not talking about sex, but maybe a bit of touching here and there."
    scene temple 74
    j "Yeah of course, and you want me to practice that with you too, don’t you?"
    scene temple 75
    me "Only if you want. We trust each other enough to talk about this openly."
    scene temple 74
    j "I don't know... don't you think it's weird?"
    scene temple 75
    me "Nah... and besides, it wouldn't be the first time we ended up in a heated up situation... remember the pool?"
    scene temple 76
    j "I told you that was because of the beer!"
    j "But... okay, you win."
    j "...teach me."
    scene temple 77 with dissolve
    me "Ok, get on the floor."
    scene temple 78 with dissolve
    $ renpy.pause ()
    scene temple 79 with dissolve
    $ renpy.pause ()
    j "Oh my god! It's huge!" with dissolve
    j "Do all the boys have one that size?"
    me "...I don't think so."
    me "Ok, now grab it with both hands and shake it up and down."
    scene temple 80
    j "So... a handjob? I might be inexperienced, but I'm not stupid."
    me "Sorry, I got carried away."
    scene temple 81 with dissolve
    j "Like this?"
    me "Yeah, perfect."
    scene hand
    with Dissolve (1)
    $ renpy.pause ()
    me "Y-yeah that's it." with dissolve
    $ renpy.pause ()
    scene temple 81
    j "Am I doing it right?"
    me "...perfect."
    scene hand2
    with Dissolve (1)
    $ renpy.pause ()
    me "Ahh..." with dissolve
    menu:
        with dissolve
        "Warn her before cumming":
            me "J-judie I'm gonna cum..."
            scene temple 83
            me "AHH..." with hpunch
            scene temple 84
            j "Wow, haha, that was unexpected." with dissolve
            me "I'm sorry Judie."
            j "Don't worry, I'll take this as a sign that I’ve done well. Thanks for the warning, though."
            j "I have to admit this has been fun."
            j "Maybe... we can do it again sometime."
            j "I'm going to sleep. Tomorrow we have to leave early. Good night!"
            me "Good night..."
        "Don't warn her":
            me "Ohh yess..."
            scene temple 83
            me "AHH..." with hpunch
            scene temple 86
            j "What the fuck! This is the grossest thing I ever saw!" with dissolve
            me "I'm sorry!"
            j "Yeah well, you’re lucky I brought spare clothes."
            j "Let's go to sleep! Tomorrow we have to leave early."
            me "Ok..."
    scene gallerybackground
    call screen gallery with Dissolve(1)



label glaurenspot:
    stop music2 fadeout 1
    stop music3 fadeout 1
    play music "forest.ogg" fadein 1
    scene spot 34
    l "We can take a dip, if you want." with dissolve
    scene spot 32
    me "That sounds great, but I didn't bring swimwear. Too bad."
    scene spot 36
    l "Well, I usually go skinny-dipping."
    scene spot 37
    me "S-skinny what?"
    scene spot 36
    if inc:
        l "Naked. If you don’t have a problem, neither do I. We're siblings, right?"
    else:
        l "Naked. If you don’t have a problem, neither do I. We're practically siblings, right?"
    scene spot 37
    me "R-right."
    scene spot 36
    l "If you feel embarrassed, we can forget it."
    scene spot 37
    me "No, no! This is a great idea. An excellent one."
    scene spot 38 with dissolve
    l "Cool! I’ll leave my clothes by the shore." with dissolve
    scene spot 39 with dissolve
    $ renpy.pause ()
    scene spot 41 with dissolve
    $ renpy.pause ()
    scene spot 42 with dissolve
    $ renpy.pause ()
    scene spot 43 with dissolve
    $ renpy.pause ()
    scene spot 44 with dissolve
    $ renpy.pause ()
    scene spot 45 with dissolve
    $ renpy.pause ()
    scene spot 46 with dissolve
    $ renpy.pause ()
    scene spot 47 with Dissolve(1)
    l "The water's perfect! Not too cold, not too hot." with dissolve
    $ renpy.pause()
    scene spot 48 with Dissolve(1)
    l "So... " with dissolve
    l "Are you gonna swim or not?"
    scene spot 49 with dissolve
    $ renpy.pause ()
    me "(Oh my god...)" with dissolve
    me "Ehh.. yeah!"
    scene spot 50
    me "Of course! My clothes! Right away!"
    play sound "splash.ogg"
    $ renpy.pause ()
    scene spot 51 with dissolve
    l "Come on already! We don't have all day!"
    me "Coming!"
    scene spot 52
    me "Hop!" with dissolve
    play sound "splash.ogg"
    play music "pool.ogg" fadein 1.0
    scene spot 53 with dissolve
    $ renpy.pause ()
    play music "forest.ogg" fadein 0.5
    play sound "bubbles.mp3"
    scene spot 54 with dissolve
    me "Ahhh... refreshing." with dissolve
    me "Lauren?"
    scene spot 55
    me "(Where the hell did she go?)"
    scene spot 54
    $ renpy.pause ()
    scene spot 56 with dissolve
    $ renpy.pause ()
    play sound "bubbles.mp3"
    scene spot 57
    l "BOO!" with hpunch
    me "AHHH!"
    scene spot 58 with dissolve
    l "Hahaha I love how easily you get scared."
    scene spot 59
    me "T-that's not true!"
    me "(Jesus Christ, her boobs are mesmerizing...)"
    me "Sooo... tell me, how was school today?"
    scene spot 60
    l "Meh, quite normal."
    l "Jack slipped in the yard and fell into a mud puddle."
    scene spot 61
    me "Shaved head Jack or fat Jack?"
    scene spot 58
    l "Fat Jack."
    me "Hahahaha then that must have been funny."
    $ jasminelauren = True
    scene spot 60
    l "Oh, and Jasmine gave out invitations for her party to all those who were invited."
    scene spot 61
    me "Jeez, this damn party. You don't have one for me, do you?"
    scene spot 60
    l "Nope, I'm sorry... she gave me one for Judie, though."
    scene spot 61
    me "Aww damn it... You have to convince her to invite me!"
    me "Please!"
    scene spot 60
    l "Ok, I'll try to talk to her tomorrow."
    scene spot 61
    me "Thanks! You're the best!"
    scene spot 58
    l "Of course I am!"
    scene spot 59
    me "(I should get an award for maintaining eye contact for so long...)"
    scene spot 62
    l "Well, I think we should get going, before the blood stops reaching your brain."
    scene spot 63
    me "What? Are you talking to me? Maybe you’re too full of yourself, but I'm relaxing as never before."
    scene spot 64
    l "Oh, really?"
    scene spot 65 with dissolve
    l "Because your friend down here seems anything but relaxed..."
    scene spot 66
    me "Whoa! Haha... well, I have to admit that you have quite a nice body, and well..."
    scene spot 65
    l "And that's why you're hard as a rock."
    scene spot 66
    me "Maybe with a little help it could..."
    scene spot 67
    l "HAH! You wish!"
    l "We should get going, or we'll be late."
    me "Are you going to leave me like this?"
    l "You bet I am!"
    play sound "bubbles.mp3"
    scene spot 68
    with Dissolve (1)
    l "Come on, hurry! Or I'll leave you behind!" with dissolve
    me "Yeah, I'm coming..."
    scene spot 69 with dissolve
    l "Take a good look because you may never see it again!" with dissolve
    me "I don't need it, thank you very much, I have plenty of women at my disposal."
    me "(Taking 30 pictures per second mentally)"
    stop music fadeout 1
    scene gallerybackground
    call screen gallery with Dissolve(1)



label gcarladildo:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene dildo 2
    c "(Upstairs) Mmmm..." with dissolve
    me "(What was that?)"
    me "(Is this what I think it is?)"
    with Dissolve (1)
    scene dildo 3
    with Dissolve (1.5)
    c "Ahh..." with dissolve
    me "(Those are definitely moans of pleasure.)"
    scene dildo 4 with dissolve
    me "(Oh merciful Lord...)"
    scene dildo 5
    me "(She is fingering herself!)"
    scene dildo 6 with dissolve
    $ renpy.pause ()
    scene dildo 7
    with Dissolve (1)
    c "Ahhh..." with dissolve
    scene dildo 6 with dissolve
    pause (.5)
    scene dildo 8
    with Dissolve (1)
    c "(Oh my god, lately I'm horny as hell...)" with dissolve
    c "(Not that surprising though, with all the travelling Charles is almost never here.)"
    c "(And the worst part is that I can’t even have an orgasm on my own.)"
    scene dildo 9
    c "(Maybe I could use that...)"
    c "(When Cora gave it to me I never thought I’d use it, but... I could give it a try...)"
    scene dildo 10 with dissolve
    c "(Now, where did I put it?)" with dissolve
    scene dildo 11
    c "(I think I hid it over here somewhere.)"
    scene dildo h
    if inc:
        me "(Oh my fucking god Mom, you don't deserve to receive so little affection...)"
    else:
        me "(Oh my fucking god Carla, you don't deserve to receive so little affection...)"
    me "(I'm hard as a rock...)"
    scene dildo 11
    c "(Aha! Here it is!)"
    scene dildo 12 with dissolve
    c "(Oh my god, this thing is bigger than I remembered...)" with dissolve
    scene dildo 13 with dissolve
    $ renpy.pause ()
    scene dildo 14 with dissolve
    c "(Ok, let's give it a try.)" with dissolve
    scene dildo 15 with dissolve
    c "(Just a little, to get rid of this... \"hunger\".)" with dissolve
    scene dildo 16 with dissolve
    c "(Ok, easy now...)" with dissolve
    scene dildo 17
    with Dissolve (1)
    c "Ahhhh...." with dissolve
    scene d
    with Dissolve (1.5)
    $ renpy.pause ()
    me "(Oh Jesus, didn't know you were this naughty...)" with dissolve
    scene dildo h
    me "(Fuck, I'm gonna cum...)"
    scene dd with dissolve
    $ renpy.pause ()
    c "Oh my g-god... Ah... AH...." with dissolve
    c "AHHH... [me]... yeah..."
    c "AHHHH!!"
    scene dildo 18 with dissolve
    c "(Panting) Ahh...."
    scene dildo h
    me "(Did she just say...?!)"
    scene dildo 18
    c "(Oh my god, did I just shout [me]'s name?... First the dream and now this... I think I haven't had sex for too long... I no longer think clearly.)"
    play sound "brokenwindow.ogg"
    pause (0.8)
    scene dildo 19 with dissolve
    c "(What was that?!)"
    c "Erm... hello? Is anybody home?!"
    scene dildo 21
    me "(What the fuck was that noise?! Did it come from my room?)"
    me "(Shit!)"
    scene dildo 20
    c "(Oh my god how embarrassing... I hope no one left school early!)"
    c "(Where's my robe?)"
    scene dildo 3
    $ renpy.pause ()
    scene dildo 22 with dissolve
    c "(Hmmm...)" with dissolve
    scene dildo 23
    c "Hello? Lauren? Judie? Erm... [me]?" with dissolve
    scene dildo 22
    c "(It doesn't look like there's anybody up here... something must have fallen in the kitchen.)" with dissolve
    scene dildo 3 with dissolve
    c "(Thank god there's no one here...)" with dissolve
    scene gallerybackground
    call screen gallery with Dissolve(1)



label grebeccablind:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene bf 49
    r "Oh no... I can't see anything... what am I gonna do..." with dissolve
    me "(This sounds hot but this is my chance to escape.)"
    scene bf 50
    me "(Quiet now.)" with dissolve
    r "Where are you going big boy?"
    scene bf 51 with dissolve
    me "(Oh my god...)" with dissolve
    scene bf 52
    r "You promised you'd treat me like a queen today, David."
    r "And I hope you stick to it..."
    scene bf 53 with dissolve
    me "(Oh Jesus.)" with dissolve
    scene bf 54 with dissolve
    r "You’re gonna have to work today..."
    me "(With pleasure...)"
    scene bf 55 with dissolve
    $ renpy.pause ()
    scene bf 56 with dissolve
    r "Ah..." with dissolve
    r "Y-yeah that's it... I can see you were looking forward to this..."
    scene bf 57 with dissolve
    $ renpy.pause ()
    scene bf 58
    with Dissolve (1)
    r "Oh my god! T-this is amazing!" with dissolve
    scene bf 59 with dissolve
    $ renpy.pause ()
    scene bf 60 with dissolve
    r "Mmmm, y-yeah, just like that..." with dissolve
    scene bf 61 with dissolve
    r "OH YES, YES! AHHH!" with dissolve
    scene bf 62 with dissolve
    r "(Panting) S-stop! Stop now!..." with dissolve
    scene bf 63 with dissolve
    r "(Panting) Oh my god my love... That was incredible..." with dissolve
    scene bf 64
    r "Now... fuck me." with dissolve
    scene bf 65
    me "(YES! I mean... NO! I can't! She will notice I'm not her boyfriend!)"
    me "(And... well, I think I’ve risked enough, haven't I?)"
    menu:
        with dissolve
        "Try to fuck her":
            scene bf 66 with dissolve
            $ renpy.pause ()
            scene bf b1 with dissolve
            me "Oh my god, her pussy is so wet..." with dissolve
            scene bf b2
            with Dissolve (1)
            me "Ohh..." with dissolve
            scene bf b3 with dissolve
            $ renpy.pause ()
            r "W-woah! What the...? S-stop!"
            scene bf b4 with dissolve
            r "Ok, ok, I’m not gonna say I wasn’t liking it but, what was going on in there?" with dissolve
            r "Did you buy a toy or have you taken something?"
            me "(Oh my god, that sensation lasted 0.5 seconds but it felt incredible...)"
            scene bf b5 with dissolve
            r "(The game is about not being able to see, but you know you can still talk, right?)"
            me "(Time to get my blue balls out of here!)"
            r "David?"
            scene bf b6 with dissolve
            play sound "doorclose.ogg"
            $ renpy.pause ()
            scene bf b7 with dissolve
            r "(I can’t believe he just left like that again.)" with dissolve
            r "(I hate it when he does that.)"
        "Jerk off and cum on top of her":
            scene bf 66 with dissolve
            scene bf a1 with dissolve
            scene bf 66 with dissolve
            scene bf a1 with dissolve
            scene bf 66 with dissolve
            scene bf a2 with dissolve
            me "Ahh..." with dissolve
            scene bf a3 with dissolve
            r "(Sticking her tongue out) You're selfish, you know that?"
            scene bf a4 with dissolve
            r "But well, I can’t complain." with dissolve
            r "This has been fun, don't you think?"
            scene bf a5 with dissolve
            r "The game is about not being able to see, but you know you can still talk, right?" with dissolve
            me "(Time to get my blue balls out of here!)"
            r "David?"
            scene bf a6 with dissolve
            play sound "doorclose.ogg"
            $ renpy.pause ()
            scene bf a7 with dissolve
            r "(I can’t believe he just left like that again.)" with dissolve
            r "(I hate it when he does that.)"
    scene gallerybackground
    call screen gallery with Dissolve(1)


############################################################################################## gallery2


label gjudiecloset:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene closet 4
    j "What?!" with dissolve
    scene closet 5
    j "[me]! What are you doing here?" with dissolve
    me "Well, I couldn’t miss the party!"
    scene closet 6 with dissolve
    me "Come, sit down! We're supposed to stay in here for a while anyway." with dissolve
    scene closet 7
    j "Sure." with dissolve
    scene closet 8
    me "So... tell me, are you having a good time?"
    scene closet 9 with  dissolve
    j "Well, it's alright, I guess. Maybe... not my kind of \"party\" but hey, no complaints." with dissolve
    scene closet 10
    me "I saw you staring at that guy James..."
    scene closet 11
    j "W-what? Me? I... well... maybe... Why? Did he look at me?" with dissolve
    scene closet 9
    j "You know what? I don't care. It's true that I was only playing this silly game to spend some time with him, but hey, it didn't end so badly."
    j "I may not have ended up taking off my costume but at least I'm having a good time talking to you."
    scene closet 10
    me "Well, you can take off your costume anyway..."
    scene closet 12
    j "Haha, you wish."
    scene closet 13
    me "I'm serious! You’ve seen me naked a couple of times in less than a week, that's not fair..."
    me "Since we're here, we could play this silly game of theirs."
    j "Hmm..."
    scene closet 14
    j "Ok, fine... Just for a laugh!" with dissolve
    j "But turn around while I take it off!"
    me "What? That takes the fun out of it!"
    j "Come on, please! It's embarrassing!"
    scene closet 15 with dissolve
    me "Ok, ok, I'll turn around, tell me when you're ready."
    play sound "takeoff.ogg"
    pause 3.5
    j "Hmm... OK! Ready!" with dissolve
    scene closet 16 with dissolve
    j "D-do you like my underwear? D-do you think it's cute?" with dissolve
    scene closet 18
    me "(She's so fucking adorable.)"
    me "It's lovely."
    scene closet 16
    j "Haha, thanks!"
    j "You have to take off your costume too!"
    scene closet 18
    me "Hmm... Ok, I will if you take off your bra..."
    scene closet 17
    j "My... bra?"
    j "Erm..."
    scene closet 19
    j "OK! Deal!"
    play sound "takeoff.ogg"
    scene closet 20 with dissolve
    pause 3.0
    j "You... you're not wearing any underpants..." with dissolve
    me "Yeah, I know, this costume is too tight for them."
    me "Your turn..."
    scene closet 19
    j "Yeah, a deal's a deal."
    scene closet 21 with dissolve
    $ renpy.pause ()
    scene closet 22 with dissolve
    $ renpy.pause ()
    j ". . ." with dissolve
    me "You’re the most beautiful thing I’ve ever seen."
    scene closet 23
    j "Don't make fun of me!" with dissolve
    me "I'm not! I really believe it!"
    j "Yeah, sure. You..."
    scene closet 24 with dissolve
    j "Oh my god, you got a boner." with dissolve
    me "Well... how could I not when you're naked in front of me?"
    scene closet 25 with dissolve
    $ renpy.pause ()
    scene closet 26
    j "It’s the first time I’ve seen it so well..." with dissolve
    j "Can... can I touch it?"
    me "Of course, you already did it in that basement."
    j "Oh, yeah, that's true..."
    j "Can... can I taste it then? What does it taste like?"
    scene closet 27
    j "Oh my god! Scratch that, how embarrassing! I get kind of wound up when I'm nervous, I'm sorry." with dissolve
    scene closet 28 with dissolve
    j "Well! That's 10 minutes, we should get dressed before someone comes in." with dissolve
    scene closet 29 with dissolve
    me "There’s no reason to be embarrassed Judie, it's perfectly normal to be curious." with dissolve
    me "You can ask or do anything you want. If you're curious about it, go ahead."
    scene closet 30
    j "A... are you sure?"
    scene closet 29
    if inc:
        me "Totally! I'm your brother, I'm here to help you."
    else:
        me "Totally! I'm your step-brother, I'm here to help you."
    scene closet 30
    j "O-ok..." with dissolve
    scene closet 31
    with Dissolve (1)
    $ renpy.pause ()
    scene closet 32
    j "Holy fuck! This thing is huge..." with dissolve
    scene closet 33
    j "And it's warm..." with dissolve
    scene closet 34 with dissolve
    $ renpy.pause ()
    scene closet 33
    j "Lie down..." with dissolve
    scene closet 35
    with Dissolve (1)
    $ renpy.pause ()
    scene closet 36 with dissolve
    $ renpy.pause ()
    scene closet 37 with dissolve
    $ renpy.pause ()
    scene closet 38 with dissolve
    me "(Oh my god...)"
    scene closet 39 with dissolve
    $ renpy.pause ()
    scene closet 37 with dissolve
    $ renpy.pause ()
    play music "blow1_2.ogg" fadein 3
    scene clo
    with Dissolve (1.5)
    $ renpy.pause ()
    me "(OH MY FUCKING GOD.)" with dissolve
    $ renpy.pause ()
    stop music
    scene closet 39 with dissolve
    scene closet 38 with dissolve
    scene closet 37 with dissolve
    $ renpy.pause ()
    scene closet 35 with dissolve
    j "Am I doing a good job, bro?" with dissolve
    me "Y-you couldn’t be doing better..."
    j "Alright... come here..."
    play music "blow1.ogg" fadein 3.0
    scene cloo
    with Dissolve (1.5)
    $ renpy.pause ()
    me "Oh, fuck yes, Judie..." with dissolve
    me "How do you do that with your tongue?..."
    me "Oh god, I'm gonna cum..."
    me "I'm gonna cum..."
    stop music
    scene closet 43
    me "Ahhh..." with hpunch
    scene closet 40
    j ". . ." with dissolve
    scene closet 41
    j "*swallows*" with dissolve
    j "Oh Jesus, that was intense..."
    j "And tiring..."
    me "This was incredible Judie..."
    me "Now we really have to get back to the party, though... You coming?"
    scene closet 42
    j "No, you go ahead, don't worry... I need a minute."
    me "Ok... I'll see you later."
    j "Mm-hm."
    scene gallerybackground2
    call screen gallery2 with Dissolve(1)



label gjasmineparty:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene jsex 22
    y "You're quite a negotiator, huh?" with dissolve
    me "I’m just helping you realize you want this, too."
    scene jsex 20
    me "I mean, we're at a party, everybody's drunk, but here you are, holding everything together, all night."
    me "What's the worst thing that could happen?"
    scene jsex 21
    me "Getting a lil' dirty on your dad's desk? Do you think he'd be upset?"
    y ". . ."
    scene jsex 22
    y "Yes... He'd get mad..."
    me "Well, if that bothers you then..."
    scene jsex 23
    y "Okay... shut your fat mouth already. You know what? You caught me in a good mood. Today’s gonna be your fucking lucky day." with dissolve
    y "I'm gonna give you those 5 minutes, stud. Use them..."
    me "I plan to..."
    scene jsex 24
    with Dissolve (1)
    y "You’re gonna have to start taking off that ridiculous armor." with dissolve
    me "I will, although I know you like it."
    y "Well, your ass looks good in these, I'll give you that."
    play sound "takeoff.ogg"
    scene jsex 25
    with Dissolve (2)
    pause 1.0
    me "I think it's your turn..." with dissolve
    y "My turn? I'm not stripping down, baby. This is just a bet, remember?"
    scene jsex 26
    y "Go ahead... your time starts now." with dissolve
    scene jsex 27
    me "Ok... as you like." with dissolve
    scene jsex 28
    with Dissolve (1)
    $ renpy.pause ()
    me "Very nice, a tight, firm ass." with dissolve
    scene jsex 29
    y "The clock is ticking, you know? I wouldn’t waste too much time."
    scene jsex 28
    me "Don't worry babe, I have more than enough."
    scene jsex 30 with dissolve
    $ renpy.pause ()
    scene jsex 31 with dissolve
    $ renpy.pause ()
    scene jsex 32 with dissolve
    $ renpy.pause ()
    me "Alright... are you ready?" with dissolve
    scene jsex 33
    y "Mm-hm..." with dissolve
    scene jsex 34 with dissolve
    $ renpy.pause ()
    scene jsex 35 with dissolve
    me "Ahh..." with dissolve
    y "Holy fuck! Don't be so rough..."
    me "I thought you liked it rough..."
    scene jasminedesk1
    with Dissolve (2)
    $ renpy.pause ()
    y "(Panting) Oh my fucking god..." with dissolve
    y "Ahh.. AHH..."
    y "Y-you'll break me in two... Slow down a bit..."
    me "You're trembling, Jasmine..."
    me "How long has it been since you were satisfied?"
    y "...ahh ...definitely too long."
    $ renpy.pause ()
    scene jsex 36
    y "AHHH..." with hpunch
    scene jsex 37
    y "Ahhhh...." with dissolve
    scene jsex 38
    y "Ahhh..." with dissolve
    scene jsex 39
    y "Jesus..." with dissolve
    me "That sounded like an orgasm to me."
    scene jsex 40
    with Dissolve (1)
    y "(Catching her breath)" with dissolve
    scene jsex 41
    y "Yes, I fucking cummed, all right?" with dissolve
    scene jsex 42
    y "You won your fucking bet, congratulations, now get lost." with dissolve
    y "You can go, I won’t say anything to my father."
    scene jsex 43
    me "Thank you Jasmine, I appreciate it. Did you have a good time?"
    y "Hm."
    scene jsex 42
    y "It wasn't bad."
    scene jsex 43
    me "Before I go, can I see what you're hiding under that dress? I’ve been fantasizing about it all night."
    y "Hmm..."
    scene jsex 44 with dissolve
    $ renpy.pause ()
    scene jsex 45 with dissolve
    $ renpy.pause ()
    scene jsex 46
    y "Are you happy?" with dissolve
    me "I can see you're all sweaty, you should take this precious dress off before it gets dirty."
    y "Ha. Yeah, yeah, keep it short. Do you want to see me naked? Okay, enjoy the view."
    scene jsex 47
    with Dissolve (1)
    y "Is this enough?" with dissolve
    me "You're spectacular."
    y "Thank you honey, I know."
    scene jsex 48
    me "You know, I haven't cummed yet, but I'm still hard as a rock."
    me "Are you going to leave me like this?"
    scene jsex 49
    y "Well, the bet is over... but... since you’re here, I could help you. I feel sorry for you."
    scene jsex 50 with dissolve
    me "Oh no, no, it's not about me, if you don't want to, I'll leave. Don’t do it as a favor." with dissolve
    y "Hm."
    scene jsex 51
    y "Ok..."
    scene jsex 50
    me "Ok what? I want to hear you say it. I want to hear how your desire is greater than your pride..."
    scene jsex 51
    y "You're a real prick, you know that?"
    scene jsex 50
    y ". . ."
    scene jsex 51
    y "OK... fuck me. I need you to fuck me again, [me]."
    scene jsex 52
    me "Yes... that's better."
    scene jsex 53
    me "That's it, baby..." with dissolve
    scene jsex 54 with dissolve
    $ renpy.pause ()
    scene jsex 55 with dissolve
    $ renpy.pause ()
    scene jsex 56 with dissolve
    y "Oh god...." with dissolve
    scene jasminedesk2
    with Dissolve (2)
    $ renpy.pause ()
    y "AHHH..." with dissolve
    y "I'm cumming again..."
    me "Y-yeah... me too..."
    y "Cum inside, I don't care."
    me "Are you sure?"
    y "(Panting) YES..."
    $ renpy.pause ()
    scene jsex 57
    y "Ahh.."
    scene jsex 58
    y "AHHHHHH...." with hpunch
    scene jsex 59
    with Dissolve (1)
    y "Oh my fucking god..." with dissolve
    scene jsex 60
    me "(Panting) Ok... " with dissolve
    me "I can see why everybody speaks so well of your parties, Jasmine..."
    me "But I gotta go now, we've been here a while."
    scene jsex 61
    y "Y-yeah, yeah, go... Let me catch my breath... You go ahead..."
    me "Okay... I'll see you Monday."
    y "Hm....."
    scene gallerybackground2
    call screen gallery2 with Dissolve(1)



label gcarlacunn:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene ch 19
    c "(Does that make any sense?)" with dissolve
    c "(Maybe he's right... I mean, it's not as if we're gonna fuck, just something to break the tension. This way I may be able to forget about this embarrassing obsession...)"
    c "(If Dr. Monroe says this is the only way, he can't be wrong...)"
    play sound "toctoc.ogg"
    pause 0.5
    scene ch 18
    c "(Oh my god, he's here...)" with dissolve
    if inc:
        me "Mom? May I come in?"
    else:
        me "Carla? May I come in?"
    c "Erm... y-yes!"
    play sound "dooropen.ogg"
    scene ch 20
    with Dissolve (1.5)
    if inc:
        me "Hi Mom!" with dissolve
    else:
        me "Hi Carla!" with dissolve
    scene ch 21
    c "H-hi [me]..." with dissolve
    c "Have you... talked to Dr. Monroe?"
    scene ch 22
    me "I did. And I have to tell you that you don’t have to be ashamed. He explained everything to me perfectly, and I want to help you in whatever way I can."
    me "He said... ahem, a handjob? He used the words: break the sexual tension."
    scene ch 21
    c "Yeah... he said that to me too."
    c "Ok, he's the expert. I just hope he's right and I can get over this soon."
    scene ch 23 with dissolve
    c "(Taking a deep breath) Ok, get undressed. Let's not drag this out." with dissolve
    play sound "takeoff.ogg"
    pause 2.8
    me "Done." with dissolve
    scene ch 24
    me "You can turn around."
    c "Okay..."
    scene ch 25
    with Dissolve (1)
    $ renpy.pause ()
    scene ch 26
    c "Oh my god [me]... You sure have grown up..."
    scene ch 27
    c "And you sure didn’t get that from your father..." with dissolve
    scene ch 28 with dissolve
    $ renpy.pause ()
    scene ch 29
    c "A-ahem! Erm... Ok, let's do this and be done with it, shall we?"  with dissolve
    me "Ok."
    scene ch 30 with dissolve
    $ renpy.pause ()
    scene ch 31 with dissolve
    $ renpy.pause ()
    scene ch 32
    with Dissolve (1)
    c "*Wanking*" with dissolve
    c "(This feels wrong...)"
    scene ch 33
    c "(But... at the same time... it feels... right?)" with dissolve
    c "(I guess this is what Dr. Monroe meant.)"
    c "(Holy fuck, he sure has a huge one...)"
    scene ch 34
    c "Erm... are you all right?"
    scene ch 35
    me "Yes..."
    scene ch 34
    c "Are you almost done?"
    scene ch 35
    me "Hmm... Not really... This may take a while."
    scene ch 36
    c "What?! A while?!" with dissolve
    scene ch 37
    me "It's just... well, I'm lacking some... visual stimulation."
    scene ch 36
    c "Visual stimulation."
    scene ch 37
    me "Yeah, I mean... you're all dressed up and..."
    scene ch 36
    c "And if I get undressed you'll be able to finish?"
    scene ch 37
    me "Totally. As soon as the dust settles."
    c "Hmmm..."
    scene ch 38
    c "Bah, fine. Just lie on the bed... Let’s get this over with already."
    me "Ok!"
    scene ch 39
    with Dissolve (1)
    $ renpy.pause ()
    scene ch 40
    c "I can’t believe I’m agreeing to this..." with dissolve
    c "Don’t you think this is getting out of hand?"
    scene ch 41
    me "I don't think so. This is the only way to get over this. Dr. Monroe said it himself, he can't be wrong."
    scene ch 42
    c "Hmm... Yes... I guess you're right." with dissolve
    scene ch 43 with dissolve
    $ renpy.pause ()
    scene ch 44 with dissolve
    $ renpy.pause ()
    scene ch 45 with dissolve
    $ renpy.pause ()
    scene ch 46 with dissolve
    $ renpy.pause ()
    scene ch 47b with dissolve
    c "I this enough visual stimulation?" with dissolve
    me "Yes... I think so..."
    scene ch 48 with dissolve
    $ renpy.pause ()
    scene ha
    with Dissolve (1)
    $ renpy.pause ()
    if inc:
        me "Oh.... fuck yes Mom..." with dissolve
    else:
        me "Oh.... fuck yes Carla..." with dissolve
    me "Now you got it..."
    $ renpy.pause ()
    me "Ah..." with dissolve
    scene ch 49 with hpunch
    me "Ahh..."
    scene ch 50
    with Dissolve (1)
    c "Well, I guess we're done. Thank you [me], you've been very understanding." with dissolve
    scene ch 51
    me "I'm the one who should be thanking you, but I'm happy to help, too."
    me "However, are you sure this will do you?"
    scene ch 52
    c "What do you mean?"
    scene ch 51
    me "Well, if you aren't satisfied yourself, how is this gonna help you? I should return the gesture, don't you think?"
    scene ch 52
    c "Erm..."
    scene ch 53 with dissolve
    me "Look, let me show it to you!" with dissolve
    c "What are you doing?! [me]! Get out from under there!"
    scene ch 54
    if inc:
        me "Oh my god Mom, you're soaking wet down here!"
    else:
        me "Oh my god Carla, you're soaking wet down here!"
    scene ch 55
    $ renpy.pause ()
    scene ch 56 with dissolve
    $ renpy.pause ()
    scene ch 57 with dissolve
    c "Oh Jesus Christ! What are you doing?!" with dissolve
    scene ch 58
    c "Stop it now!"
    c "[me]!"
    scene ch 59
    c "Stop it... s-sto..." with dissolve
    c "Oh my god..."
    scene ch 60 with dissolve
    c "Oh fuck... that feels good..." with dissolve
    scene ch 61
    c "Ahh..." with dissolve
    scene haa
    with Dissolve (1)
    $ renpy.pause ()
    c "Oh my god..." with dissolve
    c "Keep going..."
    c "Keep going [me]..."
    $ renpy.pause ()
    c "Ahhhh..." with dissolve
    scene ch 62 with hpunch
    c "FUCK!"
    $ carla_points += 2
    scene ch 63
    show red
    show screen carla_points
    with Dissolve (1)
    c "(Panting) Ah..." with dissolve
    c "You were right... I needed that..."
    hide screen carla_points
    scene ch 64
    $ renpy.pause ()
    scene ch 65 with dissolve
    $ renpy.pause ()
    scene ch 66 with dissolve
    $ renpy.pause ()
    c "(Oh my god, this has totally spiraled out of control.)" with dissolve
    scene ch 67 with dissolve
    c "WELL! Erm... thank you! That was... very... therapeutic!"
    c "It's time to go to sleep!"
    c "I’d appreciate it if you didn’t talk about this with anyone... not even me!"
    scene ch 68
    with Dissolve (1)
    me "Of course not." with dissolve
    c "Good! Good, good, good. Good night then! I'll see you tomorrow! Bye!"
    play sound "doorclose.ogg"
    scene ch 69 with dissolve
    $ renpy.pause ()
    scene ch 70
    c "(Oh sweet lord, Dr. Monroe sure has some extravagant methods.)" with dissolve
    c "(I hope that worked...)"
    scene ch 71
    c "(At least I can say that was a therapy I enjoyed...)"
    scene gallerybackground2
    call screen gallery2 with Dissolve(1)



label girisjudie:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene ib 30
    me "Hey, what is it?" with dissolve
    me "(Oh fuck, it's a trap.)"
    j "Heeey bro, sit on the bed, please! We have to show you something."
    me "(Ok, this is definitely a trap.)"
    me "Erm... ok..."
    scene ib 32
    with Dissolve (1)
    me "So... what do you want me to see?" with dissolve
    scene ib 33
    i "The thing is, Judie and I were talking..."
    me "(Here comes the trap...)"
    i "...and we can't agree on who has the best boobs."
    me "(Oh.)"
    scene ib 34
    i "So... we were hoping you could help us... Think of yourself as an impartial judge."
    me "(OH.)"
    scene ib 33
    i "We show you our tits and you decide."
    me "(Oh sweet and wonderful trap...)"
    me "O-ok, yeah, I can do that."
    scene ib 35
    i "Ok then... I'll go first..." with dissolve
    me "Mm-hm..."
    scene ib 36
    $ renpy.pause ()
    scene ib 37 with dissolve
    $ renpy.pause ()
    me "(Oh my fucking god...)" with dissolve
    me "All right, yep, very nice!"
    scene ib 38 with dissolve
    i "You can touch, if you want... as judge, you need to explore everything..." with dissolve
    j "Erm... Iris? Don't get too excited, there's no need for that!"
    scene ib 39
    i "Okay, then it's your turn, baby..." with dissolve
    j "Y-yeah, I know, thanks."
    scene ib 40 with dissolve
    $ renpy.pause ()
    scene ib 41 with dissolve
    $ renpy.pause ()
    scene ib 42 with dissolve
    j "Okay, I'm naked already, can we just get this over with?" with dissolve
    i "Wait! We still need your brother's opinion!"
    scene ib 43
    i "So... [me], tell us. Who do you like best?" with dissolve
    scene ib 44
    me "(Oh my god, my pants are gonna explode...)"
    me "Erm... you... you're equally perfect girls! Everything is in its place. Just... perfect."
    scene ib 43
    if inc:
        i "Yeah but, if you could only choose one, who would it be? I mean, I know Judie is your sister and I'm your cousin, but try to forget about that for a second."
    else:
        i "Yeah but, if you could only choose one, who would it be? I mean, I know Judie is your step-sister, but try to forget about that for a second."
    scene ib 44
    me "Erm..."
    me "Judie's."
    scene ib 45
    j "Trying to get on my good side, huh? Nice try. Can we leave now?" with dissolve
    scene ib 46
    i "I think it’s pretty obvious he’s telling the truth, Judie."
    scene ib 47
    i "You only have to see how hard he got when you took your shirt off..."
    j ". . ." with dissolve
    me "Well, yeah... I..."
    scene ib 50
    i "Girl, are you seeing that?" with dissolve
    i "You can take some clothes off, [me], you must be terribly uncomfortable right now."
    scene ib 48
    j "Iris! I think that's enough!"
    scene ib 50
    i "Come on! We're just having fun! We're almost naked and he hasn't even taken off his shoes. We should level the playing field."
    scene ib 51
    me "Yeah... that's an eloquent statement."
    play sound "takeoff.ogg"
    scene ib 52
    with Dissolve (2)
    $ renpy.pause ()
    i "Oh... my... god." with dissolve
    i "Your brother has a huge dick Judie! Did you know it?!"
    j "Erm... No! How would I know that? I mean... I... I don't care at all!"
    scene ib 53
    i "Wow... Haha, I'm a bit horny right know..." with dissolve
    j "Yeah, we noticed."
    scene ib 54
    i "Can I touch it?" with dissolve
    scene ib 55
    me "Sure, don't be shy..."
    i "Okay, I won't..."
    scene ib 54
    $ renpy.pause ()
    scene ib 56 with dissolve
    i "Mmmm..." with dissolve
    scene ib 57
    if inc:
        j "IRIS! WHAT THE FUCK ARE YOU DOING?! W-we're cousins, you know?!"
    else:
        j "IRIS! WHAT THE FUCK ARE YOU DOING?! I'm right here, you know?!"
    scene ib 56
    i "Yes, I know... That's even better..."
    j "You're sick in the head!"
    i "I am..."
    play music "blow1_2.ogg"
    scene irisblow
    with Dissolve (1.5)
    $ renpy.pause ()
    me "Oh my fucking god..." with dissolve
    scene ib 58
    j ". . ."
    scene ib 59 with dissolve
    $ renpy.pause ()
    stop music
    scene ib 60
    i "Oh, fuck! Judie, you gotta try this!" with dissolve
    scene ib 61
    if inc:
        j "A-are you out of your mind?! He's my own brother!"
    else:
        j "A-are you out of your mind?! He's my step-brother!"
    scene ib 60
    i "So what? It's just a blowjob, that's fine!"
    scene ib 66
    j "For your information I've already..."
    scene ib 67
    j "Erm... I've already seen enough for today!"
    scene ib 60
    i "Okay, okay... More for me."
    play music "blow1_2.ogg"
    scene irisblow with dissolve
    $ renpy.pause ()
    me "Oh yes... I'm gonna cum..." with dissolve
    stop music
    scene irisb 39
    me "Ahhhh..." with hpunch
    scene ib 62
    with Dissolve (1)
    i "*Swallows*" with dissolve
    me "Oh my god..."
    i "That was nice..."
    scene ib 63 with dissolve
    i "Wasn't that fun?!" with dissolve
    j "Super fun..."
    if inc:
        i "Babe, I don't even live here, but you... You're the luckiest girl in the world!"
    else:
        i "Babe, your step-brother is awesome! You're the luckiest girl in the world!"
    j "W-why do you say that?! I'd never do anything with him!"
    i "Come on, let's grab some snacks!"
    j "Yeah, let's do that..."
    scene ib 64 with dissolve
    $ renpy.pause ()
    me "(Oh my god, she sucked me dry...)" with dissolve
    scene ib 65
    me "Oof..." with dissolve
    me "(I have to get back to study...)"
    me "(Just... one minute.)"
    scene gallerybackground2
    call screen gallery2 with Dissolve(1)



label glaurenmassage:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene attic 18
    me "Okay, let's..." with dissolve
    me "(Wow.)"
    me "I see you made yourself comfortable."
    scene attic 19
    l "Yeah, I brought the clothes I want to wear too, but I'll get changed after the massage."
    me "Mm-hm... makes sense."
    scene attic 20
    with Dissolve (1)
    me "Well, you ready for the best massage your back will ever have?" with dissolve
    l "Haha, I'll be the judge of that."
    scene attic 21 with dissolve
    l "Hey, this mattress is quite comfortable." with dissolve
    scene attic 23
    l "For your information, if you don't do a good job you'll still owe me a favour." with dissolve
    scene attic 24 with dissolve
    me "That won't be a problem, I'm told I have magic hands." with dissolve
    l "Wow, I'd really like to see for myself..."
    scene attic 25
    with Dissolve (1)
    me "You will..." with dissolve
    scene attic 26
    with Dissolve (1)
    $ renpy.pause ()
    l "Mmmm... yeah, that's the spot, I'm getting rid of the knots in my muscles, I can feel it." with dissolve
    me "Of course, just relax and enjoy."
    scene attic 36
    with Dissolve (1)
    $ renpy.pause ()
    l "I thought this was a backrub." with dissolve
    me "Yeah, but it's a great opportunity to relax those tired legs too."
    l "Mm-hm... I won't complain."
    me "(I wonder if she's wearing panties under that towel...)"
    scene attic 28
    with Dissolve (1)
    me "(SHE'S NOT!)" with dissolve
    me "(Lauren, Lauren, you naughty girl...)"
    scene attic 36 with dissolve
    l "This feels good..." with dissolve
    scene attic 31 with dissolve
    me "Do you mind if I pull the towel down a bit? So I can massage the lower back too." with dissolve
    l "Erm... Ok."
    scene attic 32 with dissolve
    $ renpy.pause ()
    scene attic 33 with dissolve
    $ renpy.pause ()
    scene attic 34 with dissolve
    l "Mmm..." with dissolve
    me "Yeah, here's where fatigue has accumulated."
    scene attic 33
    l "I have to admit you're not bad at this..." with dissolve
    scene attic 34 with dissolve
    $ renpy.pause ()
    scene attic 35 with dissolve
    me "Do you want a butt massage?" with dissolve
    l "A butt massage?"
    scene attic 36
    me "Yeah, technically it's on your back, and it's the final step for a total relaxation. My technique is exquisite." with dissolve
    l "Haha, okay, go ahead Mr. Magic Hands. In for a penny, in for a pound..."
    scene attic 35 with dissolve
    $ renpy.pause ()
    scene attic 37 with dissolve
    $ renpy.pause ()
    scene attic 38
    me "(Damn, man...)" with dissolve
    scene attic 39 with dissolve
    $ renpy.pause ()
    me "(I wanna hit that ass so bad...)" with dissolve
    me "(Squeezing her butt) Does that feel good?"
    scene attic 40
    l "Yes..."
    scene attic 41 with dissolve
    $ renpy.pause ()
    scene attic 42 with dissolve
    $ renpy.pause ()
    scene attic 42 with dissolve
    $ renpy.pause ()
    scene attic 43 with dissolve
    $ renpy.pause ()
    scene attic 44
    l "H-hey!!"
    scene attic 45 with dissolve
    l "H-hey..." with dissolve
    scene attic 46
    hide screen path
    me "*Fingering her pussy*" with dissolve
    l "W-what do y-you t-think you aaare d-doing..."
    scene attic 47
    me "(Fingering) Just giving you a massage... I want you to relax completely." with dissolve
    l "Ahh..."
    me "If you want me to stop just say it."
    scene attic 45
    l "No... Don't stop..." with dissolve
    scene attic 47
    l "Ahhh... yes..." with dissolve
    l "Right there..."
    scene attic 48 with dissolve
    me "Well... I think we're done." with dissolve
    l "(Panting)"
    scene attic 49
    with Dissolve (1)
    l "So... you finger me and then you're leaving it half done? You're so mean..." with dissolve
    scene attic 50
    me "Oh... so you liked my special massage?"
    scene attic 49
    l "Well... it wasn't bad but if you're leaving..."
    scene attic 51
    l "Then I guess I'll have to finish by myself..." with dissolve
    scene attic 52
    l "Ahh..." with dissolve
    scene attic 53 with dissolve
    me "I could help you with that..." with dissolve
    l "Could you?"
    me "Yes..."
    scene attic 54 with dissolve
    l "Then what are you waiting for?" with dissolve
    me "No need to tell me twice..."
    scene attic 55 with dissolve
    $ renpy.pause ()
    scene attic 56 with dissolve
    me "Oh my fucking god Lauren..." with dissolve
    scene attic 57 with dissolve
    me "You're a goddess..." with dissolve
    me "I'm gonna eat the fuck out of you..."
    scene attic 58
    l "Woah, not so fast, cowboy. You'll have to undress yourself first, don't you think?" with dissolve
    play sound "takeoff.ogg"
    scene attic 55
    with Dissolve (2)
    me "Better?" with dissolve
    l "Mm-hm..."
    scene attic 57 with dissolve
    me "We can get down to business then..." with dissolve
    scene attic 59 with dissolve
    l "Ah..." with dissolve
    me "Do you like it?"
    l "Yes..."
    me "Up to second gear then."
    scene attic 60 with dissolve
    l "AHH..." with dissolve
    scene attic 61
    with Dissolve (1)
    l "(Panting) Ok, ok..." with dissolve
    l "Lie down now... I want to do something..."
    scene attic 62
    with Dissolve (1)
    me "Fuck... you're driving me mad, Lauren..." with dissolve
    scene attic 63
    l "I like this position... This way you can keep doing what you were doing..."
    scene attic 64 with dissolve
    l "While I can take care of you..." with dissolve
    scene attic 65 with dissolve
    $ renpy.pause ()
    scene attic 66 with dissolve
    l "You are getting me so horny right now, you know?" with dissolve
    l "Think of this as a thank you for your massage..."
    scene attic 67 with dissolve
    $ renpy.pause ()
    scene attic 68 with dissolve
    $ renpy.pause ()
    scene attic 69 with dissolve
    $ renpy.pause ()
    scene attic 67
    with Dissolve (1)
    $ renpy.pause ()
    play music "blow1.ogg" fadein 1
    scene lsn
    with Dissolve (1)
    $ renpy.pause ()
    stop music fadeout .5
    scene attic 70
    l "(Catching her breath) Ahh..." with dissolve
    l "Fuck... s-stop for a second!"
    scene attic 71
    with Dissolve (1)
    l "You're having a good time, huh?!" with dissolve
    scene attic 72
    me "And you're not?"
    l "Yeah, sure... this is quite..."
    scene attic 73
    l "...entertaining." with dissolve
    me "Do you know how we could make it even more entertaining?"
    scene attic 74
    l "I can imagine... but I'm afraid that's a line we can't cross." with dissolve
    if inc:
        l "You seem to have forgotten that I'm your sister."
    else:
        l "You seem to have forgotten that I'm your step-sister."
    me "So what? We're just having fun... and besides, that is known only to us and to the walls of this attic..."
    l "So only the walls would know, huh?"
    me "Only the walls..."
    l "I see..."
    l "Then..."
    l "Maybe..."
    l "We..."
    play sound "toctoc.ogg"
    scene attic 75
    j "Lauren! [me]? You there?" with dissolve
    me "(Whispering) Fuck."
    scene gallerybackground2
    call screen gallery2 with Dissolve(1)



label grebeccasex1:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene rebs 63
    r "(He's acting like a selfish prick...)" with dissolve
    scene rebs 64
    r "(Am I really gonna marry a man who doesn't even touch me? Who doesn't listen to me?)" with dissolve
    r "(I don't know anymore...)"
    play sound "slidingdoor2.ogg"
    scene rebs 65 with dissolve
    r "(That's the last straw! This fat fuck again!)" with dissolve
    scene rebs 66
    r "I SAID I HAD TO GET MY FUCKING THINGS!"
    scene rebs 67
    r "SO YOU CAN..." with dissolve
    r "...[me]?"
    scene rebs 68
    me "(Clears throat) Erm... I know you don't want to talk to me but..." with dissolve
    me "I saw this bouquet of sunflowers and I remembered you once said it's your favourite flower and..."
    me "I thought it would be a good way to apologize, so..."
    me "Erm... I'm sorry and... I won't bother you anymore!"
    scene rebs 69
    me "So... yeah, that's all I had to say." with dissolve
    r ". . ."
    me "Erm... I'm leaving now."
    me "See you tomorr-"
    scene rebs 70 with dissolve
    with Dissolve (1.5)
    $ renpy.pause ()
    scene rebs 71
    me "W-what... Rebecca? What was that?" with dissolve
    r "Do you find me attractive, [me]?"
    me "What?"
    r "Just answer."
    me "What man in his right mind wouldn’t find you attractive?"
    scene rebs 72
    r "So... do you want me?" with dissolve
    me "I do want you..."
    r "How much do you want me?"
    me "I want you more than anything in my life."
    scene rebs 73
    r "Do you want to see my body?" with dissolve
    me "I do..."
    scene rebs 74
    r "Do you want to feel my body? Because I want to feel yours..." with dissolve
    me "Oh yes I do..."
    scene rebs 75
    r "I'm sick of pretending. Sick of deluding myself. Sick of not doing what I want to do." with dissolve
    r "And I want you to fuck me. I want you to fuck me so bad. And I want it now..."
    scene rebs 76
    r "I want you to nail me to the fucking wall..." with dissolve
    r "Will you do as your teacher asks?"
    play sound "takeoff.ogg"
    me "(Oh my fucking god...)"
    scene rebs 77
    with Dissolve (1)
    me "I will have to do this... I must listen to my teacher..." with dissolve
    scene rebs 78
    r "Mm-hm... That's the spirit... I wouldn’t want to have to fail you..." with dissolve
    scene rebs 79 with dissolve
    $ renpy.pause ()
    scene rebs 80
    me "Oh my god, check out this ass... I bet every guy in this school wanks over you."
    r "You think so? I guess you're lucky then..."
    scene rebs 81
    me "You have no idea how much..." with dissolve
    scene rebs 82 with dissolve
    $ renpy.pause ()
    scene rebs 83 with dissolve
    $ renpy.pause ()
    scene rebs 84
    r "Ahhh..." with dissolve
    me "(Fingering) You're so wet..."
    r "I know... I haven’t stopped thinking about you since I found out it was you who ate my pussy that day on the couch..."
    r "Ahhh..."
    r "I tried to forget about that but I couldn't... I can't..."
    r "Ahh..."
    r "I need you... I need to feel you inside me... Now..."
    scene rebs 85 with dissolve
    me "Fuck... You don't know how long I’ve been waiting for this..." with dissolve
    $ renpy.pause ()
    scene rebs 86 with dissolve
    $ renpy.pause ()
    scene rebs 87
    with Dissolve (1)
    r "OH GOD..." with dissolve
    scene rebs 88
    me "Ah... this is amazing..."
    r "That feels big..."
    me "Do you want me to keep it slow?"
    r "No... I'm a big girl, I think I can handle it..."
    scene rebeccawall
    with Dissolve (1.5)
    $ renpy.pause ()
    r "Ahh... Oh my god... Y-yes... Don't stop!" with dissolve
    r "Keep going..."
    $ renpy.pause ()
    scene rebs 89 with dissolve
    r "(Gasping) Ahhh...."
    scene rebs 90
    r "Ah... My bun..." with dissolve
    me "Oh... sorry."
    scene rebs 91
    r "Now I don't look like a respectable teacher, do I?" with dissolve
    scene rebs 92
    me "No... but you look sexy... Ms. Wilson." with dissolve
    scene rebs 93
    r "Call me that again..." with dissolve
    me "Ms. Wilson..."
    r "Uh-huh...."
    r "You show potential, [me]... but you’re gonna have to work hard to pass this course..."
    scene rebs 95
    me "What should I do, Ms. Wilson?"
    r "Well... Let me think..."
    scene rebs 97
    r "You're gonna grab your cock and shove it inside me all the way in..." with dissolve
    scene rebs 98
    r "And then..." with dissolve
    scene rebs 99
    r "Ahhh... you're gonna make me cum..." with dissolve
    scene rebs 100
    r "Over... and over..." with dissolve
    scene rebs 101
    r "Ahh... and over again..." with dissolve
    scene rebs 102
    r "You think you can do that?"
    me "Yes... I think so..."
    r "Then show it to me..."
    scene rebeccasex2
    with Dissolve (1.5)
    $ renpy.pause ()
    r "(Panting) AH... AHH... AHHH..." with dissolve
    r "Oh my god, I'm cumming..."
    me "M-me too, I can't hold it..."
    r "Cum inside me..."
    me "You sure?"
    r "Yes... I'm taking the pill anyway..."
    scene rebs 104
    me "Ah..." with hpunch
    r "Ahhhh..."
    r "I can feel your cum inside me..."
    scene rebs 103 with dissolve
    r "Fuck..." with dissolve
    r "That was... like... the best lay I ever had..."
    scene rebs 105
    with Dissolve (1.5)
    r "Jesus..." with dissolve
    r "You... you have to go before the principal comes back..."
    r "Go... I'll lock the room..."
    me "Ok."
    me "So... should we schedule a private lesson on Sunday?"
    r "What?"
    r "Hahaha..."
    scene rebs 106
    r "You're persistent, aren't you?" with dissolve
    scene rebs 107
    me "Just want to improve my grades."
    scene rebs 106
    r "Haha, yes, young man. Sunday at 10 AM. You'd better be there."
    scene rebs 107
    me "YES! You won't regret it Rebecca! See you tomorrow!"
    scene rebs 106
    r "I'm sure I won't..."
    scene gallerybackground2
    call screen gallery2 with Dissolve(1)



############################################################################################## gallery3


label gjudieshower:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene sho 18
    me ". . ." with dissolve
    scene sho 19
    me "*Whistling*" with dissolve
    scene sho 20
    me "*Whistling*" with Dissolve (1)
    scene sho 21
    me "AHH! WHAT THE...!" with hpunch
    scene sho 22
    me "Judie!" with dissolve
    j "H-hey..."
    scene sho 22b
    me "What the hell? Why are you here?"
    scene sho 22
    j "Erm... I was about to take a shower."
    scene sho 22b
    me "Why didn't you lock the door? You always do! I thought it was empty."
    scene sho 22
    j "That's the thing... I forgot to lock the door, then you came in and I was too embarrassed to say anything."
    j "I didn't know you were gonna shower, I thought you'd leave without noticing me."
    scene sho 22b
    me "Sorry about that, I'll let you shower first."
    scene sho 22
    j "Don't worry! I'll wait outside, you can go first. You have to go to that prison, and I'm in no hurry."
    scene sho 22b
    me "(Hmm...)"
    me "I was thinking..."
    me "Maybe we could... take a shower together?"
    scene sho 22
    j "T-together?"
    scene sho 22b
    if inc:
        me "Yeah, like when we were little!"
    else:
        me "Yeah! Why not?"
    me "It’s not like we haven’t seen each other naked already..."
    scene sho 22
    j "Erm..."
    j "I guess... We can save time..."
    scene sho 22b
    me "That's right."
    scene sho 23
    j "Okay... erm... let me... turn on the water." with dissolve
    scene sho 24 with Dissolve(1)
    me "(Oh my god... my precious, pure Judie...)" with dissolve
    play music "shower.ogg" fadein 0.5
    scene sho 25 with Dissolve(1)
    me "(My precious, pure, wet Judie...)" with dissolve
    scene sho 26
    j ". . ." with Dissolve(1)
    scene sho 27
    j "(Giggles) It's coming out a little bit cold..." with dissolve
    scene sho 28 with Dissolve (.8)
    $ renpy.pause ()
    j "Ok! Now it's perfect!" with dissolve
    scene sho 29
    me "(Yes, you can say that again, that's fucking perfect.)" with dissolve
    me "(Oh my god... It's begging to be groped...)"
    j "You coming or not? You'll catch a cold."
    scene sho 30
    me "Y-yes! Of course." with dissolve
    scene sho 31
    me "(Oh, fuck, I'm rock hard already.)" with dissolve
    me "(I don't want to scare her off.)"
    scene sho 32
    me "Erm..." with Dissolve(1)
    me "I'm gonna stand back to back, all right? Can you pass me the sponge?"
    scene sho 33
    j "Back to back? Are you challenging me to a duel? Haha." with dissolve
    me "It's not that, it's just that I'm a gentleman."
    j "I'm not so sure a gentleman would ask a lady to shower with him."
    me "A modern gentleman would."
    scene sho 34
    j "Hahaha, of course... Come here, \"gentleman\". I'll soap your back." with dissolve
    scene sho 35
    me "That's very kind of you, thank you."
    scene sho 34
    j "You have to be clean to make a good impression on your cell mates..."
    scene sho 35
    me "Ha, ha, very funny."
    scene sho 34
    j "Hahaha, ok, there you go... Come on, turn around!"
    scene sho 35
    me "Erm... I'm fine like this, thank you!"
    scene sho 36
    j "(Turning you around) What do you mean by that?! Well, well, who’s ashamed now?" with Dissolve(1)
    j "You propose we shower together and now you're embarrassed?"
    me "I..."
    scene sho 37 with Dissolve(.8)
    $ renpy.pause()
    scene sho 38 with Dissolve(.8)
    $ renpy.pause ()
    scene sho 39
    j "Oh... Erm... Haha, I see..." with dissolve
    scene sho 40
    j "Well... I can finish showering alone... That was fun!" with dissolve
    me "Do you want me to soap your back?"
    j "...my back?"
    scene sho 41
    me "Yes! You did it for me, it would be rude if I didn’t do the same." with dissolve
    j "Hmm..."
    scene sho 43
    j "Ok..." with Dissolve (1)
    me "Good decision!"
    scene sho 42 with Dissolve (1)
    me "(Oh my god, look at that booty, perfectly rounded like a peach...)" with dissolve
    me "(Should I try to make a move? Would she like it?)"
    scene sho 43
    me "Erm..." with dissolve
    me "Do you want me to give you a little massage?"
    scene sho 44
    j "A massage?"
    me "Yeah! I give really good massages, as far as I know."
    me "(At least that’s what someone told me the other day...)"
    j "Really? Okay, go ahead."
    scene sho 43
    me "But I need you to turn around..."
    scene sho 44
    j "What?!"
    scene sho 43
    me "Come on! A moment ago it was you who was bragging about who was ashamed and who wasn’t..."
    scene sho 44
    j "I..."
    j "Hmmm... okay, as you like..."
    scene sho 45 with Dissolve(1)
    $ renpy.pause ()
    j ". . ." with dissolve
    scene sho 46
    $ renpy.pause ()
    me "Wow, Judie, you got a beautiful body, you know that?" with dissolve
    j "Hmm."
    me "I'm gonna kneel to massage your legs, may I?"
    j "Mm-hm."
    scene sho 47
    me "Thank you..." with Dissolve(1)
    scene sho 48
    j ". . ."
    scene sho 47
    me "Wow, your skin is so soft..."
    j "Erm... are you gonna massage something or..."
    scene sho 48
    me "Yeah, sorry, I got distracted."
    scene sho 47
    $ renpy.pause ()
    scene sho 49 with Dissolve(1)
    $ renpy.pause ()
    scene sho 50
    j "H-hey!! What are you doing?! That’s what you mean by a massage?!"
    me "Just relax for a second, if it doesn’t feel good, I'll stop."
    j "Relax?! How am I supposed to relax?"
    j "You're... you're..."
    scene sho 51
    $ renpy.pause ()
    scene sho 52 with Dissolve(1)
    $ renpy.pause ()
    scene sho 53
    j "Stop right n-"
    scene sho 54
    j "N-nooow..." with Dissolve (1)
    j "Oh my god..."
    j "What are you doing to me..."
    scene judieshower_1
    with Dissolve (1)
    $ renpy.pause()
    j "Oh my god..." with dissolve
    j "OH MY GOD..."
    j "P-please, s-slow down a bit... I can't..."
    j "AHHH...."
    $ renpy.pause()
    scene sho 55
    j "Ahhhh... Stop! PLEASE!" with dissolve
    scene sho 56
    j "Oh my gosh, that was crazy..." with Dissolve (1)
    j "My knees are all dizzy..."
    j "I've never felt something like this before..."
    me "So... did you like my quick massage?"
    scene sho 57
    j "Hmm... Yeah, I liked it... Very intense."
    j "Now go before you're late, or Asmodeus will be angry with you..."
    me "That's true! I better be leaving. See you tonight!"
    j "See you..."
    stop music fadeout 1
    scene gallerybackground3
    call screen gallery3 with Dissolve(1)


label girislocker:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene iriss 15
    i "Well, since we can't go back to class, do you want to hang out for a bit? I've really got nothing better to do until it's time to leave..." with dissolve
    me "Sure."
    scene iriss 18
    i "Cool!" with dissolve
    me "(Holy mother, that swimsuit is really tight... it shows every single curve of her body.)"
    me "(I'm getting excited already... I'd better sit down.)"
    scene fewminutes with Dissolve (1.5)
    $ renpy.pause ()
    scene iriss 19 with Dissolve (1.5)
    i "I mean, I'm not like that, it's just that Judie and I were trying on some bras and then you came and I got carried away, haha." with dissolve
    i "So... sorry about that."
    scene iriss 20
    me "Sorry?! If anyone had a good time that day, it was me, I assure you."
    scene iriss 19
    if inc:
        i "Haha, thank you, I guess... I meant... well, we're cousins after all, I'm sure it was a bit awkward for you."
    else:
        i "Haha, thank you, I guess... I meant... well, with Judie in front of us, I'm sure it was a bit awkward for you."
    scene iriss 21
    me "Erm... yeah, sure, of course, but... don't worry, I like going crazy! I'm just as impulsive as you."
    i "Hmmm..."
    scene iriss 22
    i "Do you know..." with dissolve
    i "What would be..."
    i "Absolutely crazy and impulsive right now?"
    me "You tell me..."
    me "(I like where this is going...)"
    scene iriss 23
    i "Well..." with dissolve
    i "Since last time was so fun..."
    i "I could give you another blowjob..."
    me "D-do you mean now? Here?"
    scene iriss 24
    i "Yes... there’s still 30 minutes of class left..."
    i "No one will come until 3:50 P.M."
    scene iriss 25
    i "And besides..." with dissolve
    i "Last time you got to see my boobs..."
    scene iriss 26 with Dissolve (.8)
    me "(Oh Jesus...)" with dissolve
    scene iriss 27
    i "But you couldn't touch them..." with dissolve
    i "So..."
    scene iriss 28
    i "If you wanna squeeze them... you can do it..."
    me "Oh my god... that is an interesting proposal, for sure..."
    scene iriss 29 with dissolve
    me "I think I won't be able to refuse it..." with dissolve
    me "Let me check..."
    scene iriss 30 with dissolve
    me "Hmm... very well, yes, very soft, really well-placed tits." with dissolve
    scene iriss 31 with dissolve
    i "Aah..." with dissolve
    me "Sensitive nipples I see, interesting..."
    scene iriss 32
    i "Are you enjoying yourself so far?" with dissolve
    me "Very much."
    i "Take off your pants and let's get on with it."
    i "I wanna see your cock again..."
    scene iriss 34 with Dissolve(1)
    i "You know? I’ve been thinking about you and your dick all week..." with dissolve
    me "You slutty girl..."
    scene iriss 35 with dissolve
    i "I couldn't wait to have it in my mouth again..." with dissolve
    scene iriss 36 with dissolve
    i "Your warm, big, throbbing cock..." with dissolve
    scene iriss 37 with dissolve
    me "Oh yes..." with dissolve
    scene iriss 38 with dissolve
    $ renpy.pause ()
    scene iriss 39 with dissolve
    $ renpy.pause ()
    scene iriss 40 with dissolve
    $ renpy.pause ()
    scene iriss 41 with dissolve
    i "*Gagging*" with dissolve
    scene iriss 39 with dissolve
    $ renpy.pause ()
    scene iriss 41 with dissolve
    $ renpy.pause ()
    scene iriss 42
    me "Oh my fucking god..." with dissolve
    scene iriss 43
    me "Oh god Iris... you sure got a deep throat..." with dissolve
    scene iriss 44
    i "*Gagging*"
    scene iriss 45
    i "(Catching her breath) Are you enjoying it?" with dissolve
    me "Like you didn't know..."
    scene iriss 46
    i "I wanna have a good time too..." with dissolve
    i "I need to feel this cock inside me..."
    me "W-what?"
    me "(OH YES.)"
    scene iriss 47
    if inc:
        i "I know we can't but..."
    i "I need it..." with dissolve
    i "I need to know how it feels..."
    scene iriss 48 with dissolve
    i "I've never been so wet..." with dissolve
    i "You have to fuck me, or I'll go mad... I can't take it anymore."
    scene iriss 49 with dissolve
    $ renpy.pause ()
    i "Can you do me this favor? It'll be our secret..." with dissolve
    me "I'd like to but... if someone comes in..."
    scene iriss 50
    i "It'll be very fast... please..." with dissolve
    i "I'm so horny that I'm gonna cum in 15 seconds..."
    scene iriss 53
    me "You're making me so hard, Iris..." with dissolve
    scene iriss 52 with dissolve
    $ renpy.pause ()
    scene iriss 53
    me "I'm putting it in..."
    i "Mm-hm..."
    scene iriss 54 with dissolve
    $ renpy.pause ()
    i "Aah..." with dissolve
    me "You're wet as fuck..."
    scene iriss 55 with dissolve
    i "Aaaahhh..." with dissolve
    scene iriss 56
    i "Oh my fucking god... That feels big..."
    scene irisex1_2 with Dissolve (1)
    $ renpy.pause ()
    i "Aaahh..." with dissolve
    i "O-oh my god...."
    i "Y-you have no idea... Aaah..."
    i "You have no idea how often I've wished for this moment to come..."
    i "Fuck me [me]... Fuck me harder..."
    scene irisex1_1 with dissolve
    i "Mmmmmhh... Y-yeah, that's it..." with dissolve
    i "K-keep going, don't stop..."
    scene irisex1_3 with dissolve
    i "A-a-a-a-ahh... Oh my fucking god! Yeah! Yeah!" with dissolve
    i "I'm gonna cum..."
    $ renpy.pause ()
    scene iriss 56
    i "O-okay.. S-stop..." with dissolve
    i "It's almost 3:40 P.M..."
    scene iriss 55
    i "I have to go back to the girls' locker room..." with dissolve
    scene iriss 52 with Dissolve(.8)
    i "(Puffing) Oof..." with dissolve
    me "3:40 P.M.?"
    i "Yeah..."
    scene iriss 57 with dissolve
    me "(Throwing her onto the bag) Then we’ll have to hurry..." with dissolve
    me "Take off your swimsuit..."
    scene iriss 58 with Dissolve(.8)
    $ renpy.pause ()
    me "Open your legs..." with dissolve
    scene iriss 59 with Dissolve(.8)
    me "Good girl..." with dissolve
    scene iriss 60 with Dissolve(1)
    me "Are you ready?" with dissolve
    i "Mm-hm..."
    scene iriss 61 with Dissolve (1)
    $ renpy.pause ()
    scene iriss 62 with dissolve
    i "Aaaahhhh..." with dissolve
    scene irisex2_1 with Dissolve (1)
    $ renpy.pause ()
    i "Oh god..." with dissolve
    i "[me]..."
    me "Ahh... your pussy feels so good Iris..."
    scene irisex2_2 with dissolve
    $ renpy.pause ()
    i "Aah, aah, AAH..." with dissolve
    i "O-o-oh m-my f-fucking god... [me]... S-slow down a bit..."
    i "S-slow down..."
    scene irisex2_3 with dissolve
    i "AAAHHH... AAHHHHHHHHHH..." with dissolve
    me "N-not so loud! They'll hear us!"
    i "I can't... help it..."
    i "I'm cumming... again..."
    me "Ahhh... me too..."
    i "AHHHHH..."
    i "D-do... do want you want..."
    $ renpy.pause ()
    scene iriss 63
    menu:
        with dissolve
        "Cum on her":
            scene iriss 64a with dissolve
            scene iriss 63 with dissolve
            scene iriss 64b with hpunch
            me "Aaahhh..." with dissolve
            scene iriss 65b with Dissolve (1)
            me "Oh god..." with dissolve
            i "Oh my god..."
            i "You broke me in two..."
            scene iriss 66b
        "Cum inside":
            scene iriss 64a with dissolve
            scene iriss 63 with dissolve
            scene iriss 64a with hpunch
            me "Aaahhh..." with dissolve
            scene iriss 65a with Dissolve(1)
            me "Oh god..." with dissolve
            scene iriss 66a with Dissolve (1)
            i "Oh my god..." with dissolve
            i "You broke me in two..."
            scene iriss 67a
            i "You filled me with cum..." with dissolve
            me "I'm sorry I..."
            i "It's all right..."
            scene iriss 68a
    i "Okay, erm... I gotta go to the girls' locker room and take a shower before someone comes in..." with dissolve
    i "I’ll see you around..."
    me "Sure..."
    scene iriss 69 with Dissolve (1)
    i "Oh, and don't even think about saying anything to anyone! Especially to Judie!" with dissolve
    if inc:
        i "Her friendship means more than anything else in the world to me! Losing her it'd be the worst thing that could happen to me."
    else:
        i "Her friendship means more than anything else in the world to me! I wouldn't want to risk things... You're her step-brother and... well, I prefer to tell her my way."
    i "This didn't happen!"
    me "Of course, don't worry."
    scene iriss 70 with Dissolve(1)
    $ renpy.pause ()
    me "(It did happen, though...)" with dissolve
    me "(And, boy, what a memory to take home...)"
    scene gallerybackground3
    call screen gallery3 with Dissolve(1)



label gjudiecarlasofa:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    
    scene bb 21
    if inc:
        me "Erm... Can I ask you a question, Mom?" with dissolve
    else:
        me "Erm... Can I ask you a question, Carla?" with dissolve
    scene bb 22
    c "Sure, honey."
    scene bb 21
    me "Ahem... it's about what we did, what the psychologist recommended..."
    scene bb 23
    c "Oh... What's the matter?"
    scene bb 24
    me "Well... I wanted to ask you how you were doing."
    scene bb 23
    c "I'm fine... I feel lonely sometimes, but I can manage."
    scene bb 24
    me "I think I have a similar problem, I..."
    me "I can’t stop thinking about what happened, and I'm horny all the time now."
    scene bb 23
    c "Oh..."
    scene bb 24
    me "And when I try to... \"relieve myself\", that just... doesn't work."
    scene bb 23
    c "Erm..."
    c "(Oh my god, I like that he talks so openly with me, but it's quite awkward, too.)"
    c "I'm sorry, I wish I could help."
    scene bb 24
    me "Well... maybe if we repeat the therapy, it'd help us both."
    scene bb 25
    c "Erm... t-the therapy? Do you mean... another handjob?"
    scene bb 24
    me "Yes. Only if you agree, of course. I don’t know who else to ask for help..."
    scene bb 23
    c "Erm..."
    scene bb 24
    c "(I feel bad for him, teenage hormones must be popping out everywhere hijacking his brain.)"
    c "(Would it be so bad if we repeated it? It might help him...)"
    c "(And... well... let's be honest, last time it was not bad at all... I could really use some... distraction...)"
    scene bb 23
    c "Erm... okay, if you think it will help..."
    scene bb 24
    me "Of course it will!"
    scene bb 23
    c "But turn off the TV... I want to hear if anyone comes."
    scene bb 28 with Dissolve(2)
    $ renpy.pause()
    scene bb 26
    c "Well... what are we waiting for?" with dissolve
    scene bb 27
    me "I don't think I'm going to get hard just like that..."
    me "Maybe if you take off that dress..."
    c "Hmm..."
    scene bb 26
    c "Okay, okay..."
    scene bb 29 with dissolve
    $ renpy.pause()
    scene bb 30 with dissolve
    me "Oh my god... spectacular." with dissolve
    scene bb 31 with Dissolve(1)
    if inc:
        me "You have an amazing body, Mom. Dad doesn't deserve you..." with dissolve
    else:
        me "You have an amazing body, Carla. Dad doesn't deserve you..." with dissolve
    scene bb 32 with dissolve
    c "Oh Jesus... You got hard so fast..." with dissolve
    me "Let me get a little more comfortable..."
    scene bb 33 with Dissolve(1)
    c "Okay... here we go..." with dissolve
    me "Would a... blowjob be too much to ask?"
    c "A b-blowjob?!"
    me "Only if you want, just once..."
    c "I... well... if you think it will help..."
    me "It will..."
    c "Okay..."
    scene bb 34 with dissolve
    $ renpy.pause()
    scene bb 35 with Dissolve(.8)
    $ renpy.pause()
    c "Mmmm..." with dissolve
    scene bb 36 with Dissolve(1)
    me "Oh god..." with dissolve
    scene bb 35
    c "(Mmm... I'm getting a little horny...)" with dissolve
    c "(I haven’t had sex for too long...)"
    scene bb 36 with Dissolve(1)
    $ renpy.pause()
    scene bb 38 with Dissolve(1)
    $ renpy.pause()
    scene bb 36 with Dissolve(1)
    $ renpy.pause()
    c "Mmmmm..." with dissolve
    scene bb 38 with Dissolve(1)
    $ renpy.pause()
    scene bb 39 with Dissolve(1)
    me "Oh my fucking god..." with dissolve
    scene bb 40 with Dissolve(1)
    c "*Gagging*" with dissolve
    if inc:
        me "H-holy shit Mom, you know how to deepthroat..."
    else:
        me "H-holy shit Carla, you know how to deepthroat..."
    play music "blow1_3.ogg" fadein 1
    scene blow_carla1 with Dissolve(1)
    me "Ohhh..." with dissolve
    me "That's it..."
    if inc:
        me "This is amazing, Mom..."
    else:
        me "This is amazing, Carla..."
    me "(She looks so fucking eager... I think she's enjoying this even more than I am...)"
    $ renpy.pause()
    stop music
    scene bb 41 with dissolve
    me "Oh my god, you're really good at this..." with dissolve
    me "I won't last much longer at this rate."
    c "Mmmmmm..."
    me "Do you want us to..."
    play sound "dooropen.ogg"
    pause 1
    scene bb 42
    c "Did you hear that?!" with dissolve
    c "That was Judie's door! C-cover yourself up!"
    me "What? How can you know..."
    c "Shut up and put your clothes on!"

    scene bb 43 with Dissolve(2)
    j "Hey!! Are you still here? I thought I was the only one who couldn’t sleep because of tomorrow’s contest jitters!" with dissolve
    scene bb 44
    me "H-hey Judie! Yeah, we can't sleep either!"
    scene bb 45
    me "We were just sitting here, watching..."
    scene bb 46
    tv "And coming up next: BIRDS OF PREY."
    scene bb 47
    me "Erm... actually... we were just zapping."
    scene bb 44
    me "You can sit with us for a while, if you want."
    scene bb 48
    j "Sure! Let's see if there's anything good on!" with dissolve
    me "Y-yeah."
    scene fewminutes with Dissolve(1.5)
    $ renpy.pause()
    scene bb 49 with Dissolve(1.5)
    c "*Sleeping*" with dissolve
    scene bb 50
    j "*Sleeping*" with Dissolve(1)
    me "(Great, everyone's asleep but me. And why the fuck am I still hard?! It's been 20 minutes!)"
    me "(I think I'll go to bed and have a wank...)"
    scene bb 51
    j "Hmmm..." with dissolve
    scene bb 52
    j "*Yawns*" with dissolve
    scene bb 53
    j "Oops, I fell asleep! Mom too, it seems." with dissolve
    scene bb 54
    me "Yep." with dissolve
    j "Hmm?"
    scene bb 55
    j "You really like that pillow, don't you?" with dissolve
    me "No, I..."
    scene bb 56 with dissolve
    $ renpy.pause()
    scene bb 57 with dissolve
    $ renpy.pause()
    scene bb 58
    j "Erm... so... you're liking the movie, aren't you?" with dissolve
    me "It's not that, I... got an erection 20 minutes ago and I can't... well... I'm still hard..."
    j "Aha..."
    scene bb 59
    j "Hmm..." with dissolve
    scene bb 60
    j "And... Do you need help with that?" with dissolve
    scene bb 62
    if inc:
        me "W-what? Really? But... Mom's right here..."
    else:
        me "W-what? Really? But... Carla's right here..."
    scene bb 61
    j "I know, but she's asleep."
    scene bb 63
    j "And besides, I want to pay you back for the shower the other day." with dissolve
    j "I won't make any noise..."
    scene bb 65
    me "O-okay then..."
    me "You can..."
    play music "blow1_2.ogg" fadein 1
    scene judiesofab1 with Dissolve(1)
    me "O-o-oh..." with dissolve
    me "Oh god..."
    j "Mmmmm..."
    me "Ohh..."
    if inc:
        me "If Mom wakes up we're fucking dead, you know that?"
    else:
        me "If Carla wakes up we're fucking dead, you know that?"
    j "Mm-hm..."
    me "(Oh my god, if someone had told me 3 weeks ago that Judie would be doing this to me, I wouldn't have believed it...)"
    me "Ohh Judie..."
    scene bb 65
    j "Mmmm..." with dissolve
    stop music fadeout 1
    scene bb 66 with Dissolve(1)
    j "(Catching her breath) Well, I think you're right, we've already risked enough! End of the show!" with dissolve
    j "Night, bro!"
    scene bb 67
    me "(Grabbing her) Oh no, no, you can't just leave like this..." with dissolve
    j ". . ."
    scene bb 68
    me "So... you like the risk, huh?" with dissolve
    scene bb 69 with dissolve
    $ renpy.pause()
    me "Does it make you horny?" with dissolve
    j ". . ."
    scene bb 70 with dissolve
    j "Ah..." with dissolve
    me "Yes, you're wet... And I thought you were the good girl..."
    scene bb 71
    j "Ahhhh..." with dissolve
    j "S-stop it... if Mom wakes up and sees us like this..."
    scene bb 72
    $ renpy.pause ()
    scene bb 73 with Dissolve(1)
    $ renpy.pause ()
    scene bb 74 with Dissolve(1)
    $ renpy.pause ()
    scene bb 75 with dissolve
    j "Ahh... ahh..." with dissolve
    j "Oh my god... [me]..."
    scene bb 76
    me "Shhh... Don't make noise..." with dissolve
    j "(chewing her lip) Mm-hm..."
    j "Let... let me feel you between my legs..."
    scene bb 78 with Dissolve(1)
    j "Haha... you're so warm..." with dissolve
    me "You too..."
    scene bb 77
    j "This reminds me of that day at the pool, when we hid from Tom in the bathroom..."
    me "Ah, yes..."
    j "We’ve been through a lot since that day, huh?"
    me "A lot..."
    j "You know... I've been thinking, and..."
    j "There’s no one I trust more, you know that?"
    j "And I..."
    scene bb 79
    j "I want you to be my first..." with dissolve
    me "The first what?"
    j "I want you to..."
    scene bb 80
    $ renpy.pause()
    scene bb 81
    c "Hmmm..." with dissolve
    scene bb 82
    c "*Yawns*" with dissolve
    scene bb 83
    c "Hmm... I'm in the living room? Oh, I fell asleep..." with dissolve
    c "It's pretty late..."
    scene bb 84
    c "Hmm..." with dissolve
    scene bb 85
    c "Hm?" with dissolve
    scene bb 86
    c "Hey, are you still awake?"
    scene bb 87
    j "M-mom! Yeah, I... Heavens, look at the time! I'm going to bed!"
    c "Yeah, me too, I'll go with you. Good night, [me]."
    me "Mm-hm."
    scene bb 88 with Dissolve(1)
    $ renpy.pause()
    scene bb 89 with Dissolve(1)
    pause
    scene gallerybackground3
    call screen gallery3 with Dissolve(1)


label glaurenspa:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene ls 26
    me "(Wow, this looks like a luxury spa.)" with dissolve
    scene ls 27
    me "(I'd have expected it to be a lot more austere. This town has some hidden gems, that's for sure.)" with dissolve
    play sound "dooropen.ogg"
    pause .7
    l "Wow." with dissolve
    scene ls 28
    l "It's not bad, actually." with dissolve
    l "Did you know this place was so close to home?"
    me "Nope, I was thinking the same thing."
    scene ls 29
    l "There's even a jacuzzi! The candles and incense make it feel very relaxing." with dissolve
    me "Do... you want to take a bath?"
    scene ls 30
    l "Erm... okay, I see you didn't get it yet, so I'll make it very clear to you." with dissolve
    l "We came here to see how this place looks, because they gave us a free pass."
    l "If you want a massage, I'm gonna give you a massage as a thank you for saving my ass at school the other day."
    l "BUT no, I'm not gonna suck your dick, no, you're not gonna eat my pussy, and no, nothing weird is gonna happen, so... if that's what you were thinking, you can forget about that."
    scene ls 31
    me "I wasn't thinking about anything, I don't know why you think these things."
    me "(Goddammit.)"
    scene ls 33 with Dissolve(.8)
    l "Good! Then we can just chill! See how easy that was?" with dissolve
    l "Come on! Hop, hop! We don't have all day!"
    scene ls 34 with dissolve
    me "You don't have to ask me twice!" with dissolve
    me "I'd like to see if your massages are as good as mine."
    scene ls 35 with Dissolve(.8)
    l "You like to take your clothes off, huh?" with dissolve
    scene ls 36
    me "Well, I'm not embarrassed, if that's what you mean, just like you." with dissolve
    l "Mm-hm."
    scene ls 37 with Dissolve(1.5)
    $ renpy.pause()
    l "(Fuck... When I saw him naked it kinda turned me on... And he wasn't even hard...)" with dissolve
    l "(We should finish this thing quickly and go.)"
    scene ls 38 with Dissolve(1.5)
    $ renpy.pause()
    l "Ahem, well... all good?" with dissolve
    me "Yeah, very relaxing..."
    l "Is it enough, then?"
    me "Already?"
    me "I haven’t even turned around yet!"
    scene ls 35 with Dissolve(1)
    l "Hmm... okay, okay, turn around if you want." with dissolve
    me "Sure!"
    scene ls 39 with Dissolve(1)
    l "(Oh my god.)" with dissolve
    scene ls 41 with Dissolve(1.5)
    $ renpy.pause()
    l "(He's totally hard! He's enjoying the rub, that's for sure...)" with dissolve
    scene ls 42 with Dissolve(1.5)
    $ renpy.pause()
    me "I'm getting seriously aroused here." with dissolve
    l "Oh really? I hadn't realized."
    scene ls 43 with Dissolve(1)
    me "Jeez, I'm fucking hot right now Lauren..." with dissolve
    me "I know you said no blowjobs, but just a little... more intimate... rubbing..."
    me "Compared to that this is nothing..."
    me "Just as a thank you..."
    l "(Hmm...)"
    l "(Bah, fuck it. I'm kinda horny too. I'm gonna give him a wank. Why not...)"
    scene ls 44
    l "So you want a more intimate rubbing, do you?" with dissolve
    me "Hell yes..."
    scene ls 45 with dissolve
    l "You're horny, aren't you?" with dissolve
    me "You don't know how much..."
    scene ls 46 with Dissolve(1)
    l "Okay, okay..." with dissolve
    l "I don’t want to make this a punishment for you either..."
    scene ls 47 with Dissolve(1)
    $ renpy.pause()
    scene ls 48 with dissolve
    l "You always have it your way, don't you?" with dissolve
    me "Come on, you're enjoying this too..."
    l "Well... a little jerk doesn't hurt anyone."
    scene ls 49 with dissolve
    $ renpy.pause()
    scene ls 52 with Dissolve(1.5)
    $ renpy.pause
    l "*Wanking*" with dissolve
    me "Oh... yes..."
    l "*Wanking*"
    scene ls 53 with Dissolve(1.5)
    l "Oof..." with dissolve
    me "Are you ok?"
    l "Yeah... I think I got a little overheated... Haha..."
    scene ls 54
    $ renpy.pause()
    scene ls 55 with dissolve
    $ renpy.pause ()
    me "Maybe you should take your top off..." with dissolve
    me "It's making you sweat..."
    scene ls 56
    l "My top? If you want to see my breasts again, you can say it." with dissolve
    me "Well, I wouldn't mind..."
    scene ls 57 with dissolve
    l "Is it better this way?" with dissolve
    me "Yeah... much better..."
    me "Could... you... continue your massage now?"
    scene ls 58 with dissolve
    l "You want some more, huh?" with dissolve
    me "Mm-hm..."
    scene ls 59
    l "All right..." with dissolve
    l "I'm gonna give you one last rubbing..."
    scene ls 60 with dissolve
    $ renpy.pause ()
    scene ls 61 with dissolve
    $ renpy.pause ()
    scene ls 62 with dissolve
    $ renpy.pause ()
    me "Oh Jesus... I can feel how wet you are..." with dissolve
    l "You better enjoy it, because it's the closest you’ll ever feel my pussy..."
    scene laurensex1_2 with Dissolve(1)
    $ renpy.pause()
    l "Ahh..." with dissolve
    l "This is a great massage oil, isn't it?..."
    me "Yes... I'd recommend this site..."
    $ renpy.pause()
    scene laurensex1 with Dissolve(1)
    $ renpy.pause()
    l "Ahhh... ahh..." with dissolve
    me "(Fuck... this teasing is driving me crazy...)"
    $ renpy.pause()
    scene ls 63
    l "Ahh... Hahaha..." with dissolve
    l "Did you like the massage?"
    scene ls 64
    me "Yes... I... I think my balls are gonna explode..."
    scene ls 63
    l "Ahaha, I'm so sorry for you... "
    l "If you want to finish alone, I'm gonna step away..."
    scene ls 66 with dissolve
    me "Well... I was thinking... that maybe..." with dissolve
    scene ls 67 with dissolve
    $ renpy.pause()
    me "We could..." with dissolve
    scene ls 68 with dissolve
    $ renpy.pause()
    scene ls 69
    l "W-what are you trying to do?!"
    scene ls 70
    l "What are you... ahhh..." with dissolve
    scene ls 71
    l "N-no! No, no! What are we doing?!"
    scene ls 72
    l "Enough! We can't do that!" with dissolve
    me "(That was so close...)"
    l "It's one thing to play a bit, but... it's quite another to have sex!"
    l "I told you I've never done this before and..."
    if inc:
        l "I'm your sister, and you're my fucking brother! This is wrong!"
    else:
        l "I'm your step-sister! This is wrong!"
    scene ls 73
    me "Well, for this very reason..."
    me "I don’t think there’s anyone we can trust more than each other."
    scene ls 72
    l "I..."
    scene ls 73
    l ". . ." with dissolve
    scene ls 74
    with Dissolve(1)
    me "Come on, Lauren... We’ve had a good time so far..." with dissolve
    me "And tell me you’re not curious... because I am..."
    me "Just to get rid of the urge..."
    scene ls 75
    me "Just the tip... for a few seconds..." with Dissolve(1)
    l "Just the tip?"
    me "Of course."
    l "But if anyone finds out..."
    me "Nobody will find out."
    scene ls 76 with Dissolve(1)
    l "O-okay... But... Just for a few seconds and just the tip." with dissolve
    me "Of course..."
    scene ls 77
    me "Oh my god, Lauren... I've dreamed of this moment..." with Dissolve(1)
    scene ls 78 with Dissolve(1)
    me "(She's so wet...)" with dissolve
    scene ls 79
    me "Are you ready?"
    l "Yes..."
    scene ls 81
    me "(I can't believe this is really happening...)" with Dissolve(1)
    scene ls 82 with Dissolve(1)
    l "Ah..." with dissolve
    scene ls 81 with dissolve
    $ renpy.pause()
    scene ls 82 with dissolve
    $ renpy.pause()
    scene ls 83 with Dissolve(.8)
    l "Aaahhhh..." with dissolve
    scene ls 81 with dissolve
    $ renpy.pause()
    scene ls 82 with dissolve
    $ renpy.pause()
    scene ls 83 with dissolve
    l "Mmmm..." with dissolve
    me "Oh god... you're so tight..."
    scene ls 81 with dissolve
    $ renpy.pause()
    scene ls 82 with dissolve
    $ renpy.pause()
    scene ls 83 with dissolve
    $ renpy.pause()
    scene ls 84 with Dissolve(1)
    l "AAAAaahhhhh..." with dissolve
    l "T-that... that is not the tip..."
    me "Do you want me to stop?"
    scene ls 80
    l "N-no... Keep going... but... k-keep it slow..."
    scene laurensex2_1 with Dissolve(1)
    l "Ahh... ahhh... oh my god... oh Jesus..." with dissolve
    me "Oh Lauren... you're so fucking tight... but also so wet..."
    me "This is amazing..."
    $ renpy.pause()
    scene laurensex2_2 with dissolve
    l "Ahhhh..." with dissolve
    l "You're going fast..."
    me "(Oh my god... I can't believe this... I'm fucking Lauren...)"
    if inc:
        me "(I'm finally fucking my sister...)"
    else:
        me "(I'm finally fucking my step-sister...)"
    scene laurensex2_3 with dissolve
    l "AHHHH... Y-yes... yes... don't stop, [me]... don't stop..." with dissolve
    $ renpy.pause ()
    scene ls 85
    l "(Panting) Ahh..." with dissolve
    l "I... I need you... I need to feel you deeper... I want you to fuck me harder..."
    me "Are you sure?"
    l "Yeah... fuck me..."
    me "Ok..."
    scene laurensex3_1 with Dissolve(1.5)
    l "(Screaming) AAAAHHHHHHH... YES... YES..." with dissolve
    me "Ahh... N-not so loud..."
    if inc:
        me "The receptionist knows we're siblings... She'll think I'm fucking my own sister..."
    else:
        me "The receptionist knows we're step-siblings... She'll think I'm fucking you..."
    l "Ahhh... Y-you... you're doing exactly that..."
    me "Well, yeah but..."
    l "(Panting) I don't give a shit what she thinks..."
    l "Ahhh..."
    scene laurensex3_2 with dissolve
    l "AAAHHHHHHHHH... OH M-M-MY GOD..." with dissolve
    me "Oh god..."
    me "I can feel your pussy spasm all around my dick..."
    l "I'M CUMMING... I'M CUMMING..."
    $ renpy.pause()
    scene lsnnnn 22
    l "Aahhh..." with hpunch
    scene ls 86 with Dissolve(1)
    l "Fuck... I never had an orgasm like that before..." with dissolve
    l "What the hell did you do to me? Jesus..."
    scene ls 87 with Dissolve(.8)
    l "I’m gonna have to shower before we go..." with dissolve
    scene ls 88 with dissolve
    l "I got my hair all sweaty..." with dissolve
    scene ls 98
    me "So... you can't keep up?"
    scene ls 88
    l "What?" with dissolve
    scene ls 89 with Dissolve(1)
    me "If that first orgasm felt good, imagine the second one..." with dissolve
    l ". . ."
    me "I'm sure someone as fit as you can handle one more round..."
    scene ls 90
    l "I don't th... Aaaaahhhh..." with Dissolve(1)
    scene laurensex4_1 with Dissolve(1)
    $ renpy.pause ()
    l "Ooohh my fucking god... I need to rest... I can't do it again..." with dissolve
    scene laurensex4_2 with dissolve
    l "(Panting) Aah aah aahhh..." with dissolve
    l "(Panting) I can feel... every inch of your dick... filling me..."
    l "Aaaahhh..."
    scene laurensex4_3 with dissolve
    l "AAAAHH... AAAAAHH... AHHH..." with dissolve
    l "OH GOD... I'M CUMMING AGAIN..."
    l "I'm cumming again... Ahhhhhhhh..."
    me "Fuck... me too... I'm gonna cum..."
    l "(Panting) D-don't even think about finishing inside... I'm gonna kill you if you do it..."
    me "(Panting) But..."
    l "I SAID N-N-NOO.... AHHHH..."
    scene ls 92 with Dissolve(1)
    l "I'M CUMMING AGAIN..." with dissolve
    l "AAAAaaAAaAhhhHHhh..." with hpunch
    me "Ahh... it's coming..."
    scene ls 93 with dissolve
    scene ls 94 with hpunch
    me "Ahhhh..." with dissolve
    scene ls 95 with Dissolve(2)
    l "Oh my fucking god..." with dissolve
    l "That was..."
    l "Oh my fucking god..."
    scene ls 96
    me "Oh Jesus..."
    me " I think this time it REALLY got out of hand."
    scene ls 95
    l "Y-yeah, I think so..."
    l "This can't happen ever again."
    scene ls 96
    me "Ever again..."
    me "(Please, let it happen again...)"
    scene ls 95
    l "A one-time thing, to take to our graves."
    play sound "toctoc.ogg"
    scene ls 96
    pause .5
    rec "Erm... hello? Mr. [me]? Is everything ok?" with dissolve
    rec "You've been in there over 40 minutes!"
    scene ls 97
    l "(Whispering) Oh, shit! 40 minutes?!" with dissolve
    me "(Whispering) Fuck! We have to hurry or we're gonna miss our flight!"
    l "(Whispering) Yeah! Let's go!!"
    scene gallerybackground3
    call screen gallery3 with Dissolve(1)



############################################################################################## 0.7

label gjudiesexjap:
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene judsex 1
    me "(If I remember correctly, Judie took this room...)" with dissolve
    play sound "slidingdoor2.ogg"
    scene judsex 2 with Dissolve(1.5)
    me "Hey Judie, I'm here." with dissolve
    me "Judie?"
    scene judsex 3 with Dissolve(.8)
    me "(Where is she?)" with dissolve
    j "Hey!! Sorry, I was in the bathroom."
    scene judsex 4 with dissolve
    me "No problem. So... what did you want to show me?" with dissolve
    j ". . ."
    me "Judie? Are you ok?"
    play sound "fall2.ogg"
    scene judsex 5
    j "*Throwing you to the ground*" with Dissolve(.8)
    me "Whoa!"
    j "Ok..."
    j "Erm..."
    j "I've been thinking..."
    me "Uh-huh..."
    j "And..."
    j "Um... I don't know how to put this..."
    j "I... I'm gonna take my clothes off, ok?"
    me "Ok..."
    me "(So far so good...)"
    scene judsex 6 with Dissolve(1)
    pause
    scene judsex 7 with dissolve
    pause
    play sound "takeoff.ogg"
    scene judsex 8 with Dissolve(1.5)
    me "(Oh Jesus...)" with dissolve
    scene judsex 9 with dissolve
    me "Ok, I don't know if that was your intention, but I'm getting seriously aroused here..." with dissolve
    scene judsex 10
    j "Do you remember last night before coming here, on the couch, at home?"
    scene judsex 9
    me "Of course I do..."
    me "Why? Do you want... to do it again?"
    me "You can tell me if you want. You can tell me anything..."
    scene judsex 10
    j "I... I want to go one step further."
    scene judsex 9
    me "(Is this going where I think it’s going?)"
    me "Do you want to..."
    scene judsex 10
    j "Yes. I... I want you to be my first. I want my first time to be with... you."
    scene judsex 9
    me "(Oh sweet Jesus...)"
    scene judsex 12 with Dissolve(1)
    me "(Getting up) Are you sure Judie?" with dissolve
    j "I am..."
    if inc:
        me "I mean... We're siblings, we..."
    else:
        me "I mean... We're half-siblings, we..."
    j "I know. I don't care. Just..."
    j "Fuck me bro..."
    me "Oh God Judie... I've been dreaming of hearing those words for a long time..."
    me "Lie down..."
    scene judsex 15 with Dissolve(1)
    me "Let's heat things up a bit..." with dissolve
    me "Just relax, we've done this before..."
    j "Mm-hm..."
    scene judsex 16
    j "Ahhh..." with Dissolve(.8)
    me "You're already wet..."
    scene judiesex1 with Dissolve(1)
    j "Ahhh..." with dissolve
    me "(She's dripping wet...)"
    scene judiesex1_2
    j "A-a-ahhhh..." with dissolve
    me "Is this feeling good?"
    j "Y-yes..."
    pause
    j "Ahhh... I... I think I'm ready..." with dissolve
    j "I need you inside me..."
    scene judsex 18 with Dissolve(1)
    me "I'm eager to..." with dissolve
    scene judsex 19 with Dissolve(.75)
    me "Are you ready?" with dissolve
    j "Mm-hm..."
    scene judsex 20 with dissolve
    pause
    j "I-it looks even bigger from here..." with dissolve
    j "A-are you sure it's going to fit?"
    scene judsex 21
    me "Well... You're small but... I think you can manage..."
    me "We could try with only the tip..."
    me "Or we could stop..."
    j "N-no! I can do it!"
    j "Put it in..."
    scene judsex 22
    me "Alright..." with Dissolve(.8)
    scene judsex 23 with Dissolve(1.2)
    j "(Chewing her lip) Mmmm..." with dissolve
    me "Ohh..."
    me "(I can't believe this is finally happening...)"
    scene judsex 24 with Dissolve(1)
    j "Ahhh..." with dissolve
    scene judsex 25 with dissolve
    j "AAHhhh..." with dissolve
    scene judsex 24 with dissolve
    pause
    scene judsex 25 with dissolve
    me "(God... it's the tightest pussy I've ever seen...)" with dissolve
    me "(My dick can barely fit...)"
    scene judsex 24 with dissolve
    pause
    scene judsex 25 with dissolve
    me "(But she's wet as fuck... This feels fucking amazing...)" with dissolve
    me "(Maybe I can try to go a bit deeper...)"
    scene judsex 24 with dissolve
    pause
    scene judsex 26 with Dissolve(.8)
    j "AAAH!" with dissolve
    me "Are you ok?"
    j "Yeah... I'm fine... It's just... it's so big..."
    scene judsex 24 with dissolve
    pause
    scene judsex 26 with dissolve
    j "Ahhhhh..." with dissolve
    me "Do you need to stop?"
    j "N-no..."
    scene judsex 27
    j "I'm warming up to it already..." with dissolve
    j "Keep going..."
    j "Put it all the way down my little pussy..."
    me "Oh Judie..."
    scene judsex 28 with Dissolve(1)
    j "AHHH... OH MY GOD..." with dissolve
    scene judsex 29 with dissolve
    j "Ahhh..." with dissolve
    j "I-it's all the way in..."
    me "It is..."
    j "Be gentle... Please..."
    scene judiesexx1 with Dissolve(1)
    pause
    j "Aahhh... ahhhh... aahhhh..." with dissolve
    j "I can feel your cock... filling every inch of me..."
    me "Ahhh... Fuck, you're so fucking tight Judie..."
    me "If you weren't so lubed it wouldn't even fit..."
    scene judiesexx1_2 with Dissolve(1)
    j "(Panting) T-this feels amazing..." with dissolve
    me "Yeah..."
    scene judiesex1_3 with Dissolve(1)
    j "Aaahhh..." with dissolve
    scene judiesex1b with Dissolve(1)
    pause
    scene judiesex1_2b with Dissolve(1)
    j "Aaahhh..." with dissolve
    me "(I'm finally fucking Judie... I'm fucking her unspoiled little pussy...)"
    me "(I thought this day would never come...)"
    scene judiesex1_3b with Dissolve(1)
    j "(Squeaking) AHHH... AAHHH......" with dissolve
    if inc:
        me "(Panting) D-don't scream Judie... L-lauren and Mom are next door..."
    else:
        me "(Panting) D-don't scream Judie... L-lauren and Carla are next door..."
    j "Ahhh... I... I c-can't help it..."
    j "I'm reaching my climax..."
    pause
    scene judsex 29 with Dissolve(1)
    j "A-Aaaahhh..." with hpunch
    scene judsex 26
    j "Oh God... that was incredible..." with dissolve
    me "Did you cum?"
    j "I did..."
    scene judsex 30 with Dissolve(1.1)
    j "I never felt anything like that before..." with dissolve
    j "We should have done this much sooner..."
    me "Well, we can do it other days from now on..."
    scene judsex 31
    j "Other days? I wanna do it again... now..." with dissolve
    me "Now? I thought you already came..."
    j "Yeah, is it supposed to end already? I want to feel that again..."
    me "(Ohhh God...)"
    j "Please..."
    scene judsex 32
    j "Just stand a little more..." with dissolve
    scene judsex 33
    j "AAAAaaahhh. YEAH..." with dissolve
    scene judiesex2 with Dissolve(1)
    pause
    j "*Kissing you*" with dissolve
    j "Mmmmm..."
    scene judiesex2_2 with Dissolve(1)
    j "MMMM... Mm-mmmh..." with dissolve
    scene judiesex2b with Dissolve(1)
    pause
    scene judiesex2_2b with Dissolve(1)
    j "Ahhhh....ahhh..." with dissolve
    me "D-don't stop Judie... keep going..."
    scene judsex 35
    j "AH! Ahhh..." with dissolve
    me "(Oh Jesus, her pussy tightens even more when she orgasms...)"
    j "(Catching her breath) Aahh..."
    scene judsex 36 with Dissolve(1.2)
    j "W-wow... we should do this everyday bro..." with dissolve
    j "At first it hurt a little, but not anymore..."
    scene judsex 37
    j "Fuck me from behind now..." with Dissolve(1)
    me "W-what? Again?"
    j "Yes... Please, please, please..."
    scene judsex 39 with Dissolve(1)
    j "That's it... Put it in, bro... All the way in..." with dissolve
    j "I wanna feel every inch of you inside me..."
    scene judsex 38
    me "(Oh my god, I turned her into a nympho...)"
    j "Fuck me..."
    me "You'll see..."
    scene judiesex3 with dissolve
    pause
    j "AAaargh..." with dissolve
    j "Y-YES! YES! Keep going bro..."
    me "Aaah..."
    scene judiesex3_2 with dissolve
    pause
    scene judiesex3b with dissolve
    j "Aaagghhhh..." with dissolve
    scene judiesex3_2b with dissolve
    j "(Screaming) AAAH! AAAH! Y-you're g-gonna break me in half bro!!" with dissolve
    j "AAAahh..."
    j "I'm c-cumming again..."
    me "AAAahhh... me too, Judie..."
    menu:
        with dissolve
        "Creampie":
            scene judsex 40 with hpunch
            me "Aaaaaaahhh...."
            me "Oh my god..."
            j "(Gasping) Ahhh... y-you're filling me up..."
            pause
            scene judsex 41 with Dissolve(1.2)
            pause
            play sound "cream.mp3"
            scene judsex 42 with Dissolve(1.3)
            me "Oohh..." with dissolve
            scene judsex 43
            j "It's so warm..." with dissolve
            me "Jesus..."
        "Facial":
            scene judsex 44 with Dissolve(1.1)
            me "(Jacking off) Aaahhh... come here babe..." with dissolve
            scene judsex 45 with hpunch
            me "Aaahhh..." with hpunch
            scene judsex 46 with Dissolve(1)
            me "Aaah..." with dissolve
            j "Wow..."
    j "That was a lot..."
    me "I know..."
    scene judsex 47 with Dissolve(1.5)
    j "(Wiping her face) W-wow..." with dissolve
    j "I..."
    scene judsex 48
    j "I can't believe we did it..." with Dissolve(1)
    scene judsex 49
    me "And in what way..."
    scene judsex 48
    j "I... If anyone finds out, I... Oh god, how embarrassing..."
    me "(She's back to being her usual self.)"
    me "(She completely loses her mind during sex...)"
    scene judsex 49
    me "Don't worry, Judie. We did nothing wrong. And it'll be our secret..."
    scene judsex 50
    j "Haha, okay, if you say so, I feel reassured." with dissolve
    j "I'm gonna take a bath before going to bed..."
    scene judsex 51 with Dissolve(1)
    j "(Approaching you) . . ." with dissolve
    scene judsex 52
    j "*Mwah*" with dissolve
    scene judsex 53
    j "(Chuckles) Tonight has been perfect, thank you bro..." with dissolve
    scene judsex 54 with Dissolve(1)
    j "Good night!! I'll see you tomorrow for breakfast!" with dissolve
    me "Good night, Judie..."
    scene gallerybackground4
    call screen gallery4 with Dissolve(1)


label gjasminesextrain:
    play music "train.ogg" fadein 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene yt 19
    y "Moron!" with dissolve
    me "Bitch!"
    y "Wanker!"
    me "Shrew!"
    scene yt 20 with dissolve
    me "(W-what the fuck??!)" with dissolve
    y "Mmm..."
    me "(What's going on?!)"
    scene yt 21
    me "Erm... are you okay?" with Dissolve(1)
    y "You fucking prick... I don't know why, but you really turn me on..."
    y "I don't know if it's the way you talk to me, that you’re the only one who doesn’t try to make me like them, or that my Dad would hate you but..."
    scene yt 22 with Dissolve(1)
    y "I can't stop thinking about your fucking face since the day I threw the party..." with dissolve
    scene yt 23
    y "And the sex... that was something, wasn't it?" with dissolve
    me "I guess..."
    y "So... Do you want to repeat? We still have a few minutes..."
    scene yt 24
    y "I don't usually give anyone a second chance..." with Dissolve(1)
    scene yt 25
    me "Well... that sounds interesting, but... I don't know if you deserve it..." with dissolve
    y "Oh... do I have to earn it?"
    scene yt 26
    y "Do I have to say: \"Please\"?" with Dissolve(1)
    me "Hmm, that would be nice, yes."
    scene yt 27
    y "Alright... can I put your cock in my mouth?" with Dissolve(1)
    y "...please?"
    me "Well, if you ask me that way..."
    scene yt 29
    y "Mmmh..." with Dissolve(1)
    scene yt 30 with Dissolve(1)
    $ renpy.pause()
    scene yt 31 with Dissolve(1)
    $ renpy.pause()
    y "*Gagging*" with dissolve
    me "Ooh..."
    scene yt 29
    y "It tastes good..." with Dissolve(.8)
    scene yt 30
    y "Mmm..." with Dissolve(.8)
    scene  yt 32 with Dissolve (1.5)
    mo "Jasmine, start getting ready, we're..." with dissolve
    scene train 44
    mo "(Hmm?)"
    mo "Jasmine?"
    mo "(Where the fuck did she go?)"
    scene yt 33
    mo "(What if... that bastard...)"
    scene  yt 28 with Dissolve (1.5)
    y "*Sucking*" with dissolve
    y "Mmmmmm..."
    scene yt 34
    me "O-ohh my god, this feels good..."
    scene yt 31
    $ renpy.pause()
    scene yt 30 with Dissolve(1)
    $ renpy.pause()
    scene yt 35 with Dissolve(1)
    y "(Catching her breath) Ahh..." with dissolve
    me "God..."
    scene yt 36
    y "Well... Now that we're all warmed up..." with Dissolve(1)
    y "Let's see if you can live up to expectations..."
    scene yt 37
    y "*Unhooking her bra*" with dissolve
    scene yt 38 with Dissolve(1)
    $ renpy.pause()
    scene yt 39 with Dissolve(1)
    $ renpy.pause()
    scene yt 40 with Dissolve(1)
    $ renpy.pause()
    scene yt 41 with Dissolve(1)
    y "So... Are we gonna fuck or not?..." with dissolve
    scene yt 42
    me "(Jesus Christ...)" with dissolve
    scene yt 43
    me "Come here... you slut..." with dissolve
    y "So you're gonna keep insulting me, huh?"
    scene yt 44
    me "You love it, don't lie." with dissolve
    me "It makes you horny, doesn't it?"
    me "BITCH?"
    scene yt 45
    y "Haha, perhaps..." with dissolve
    scene yt 46
    y "Come on... put it in already... I need it..." with dissolve
    me "At your service..."
    scene yt 47 with dissolve
    $ renpy.pause()
    scene yt 48 with Dissolve(.8)
    y "Ahhh..." with dissolve
    me "You're wet..."
    scene yt 49
    y "Hmmm..." with dissolve
    y "Put it all the way in..."
    scene yt 50
    y "Aaaaahh... That's it..." with dissolve
    scene yt 48 with dissolve
    $ renpy.pause()
    scene yt 50 with dissolve
    y "Ahhh..." with dissolve
    scene jasminetrain1 with Dissolve(1)
    $ renpy.pause()
    y "Ahhh... ahhh..." with dissolve
    y "You're a fucking piece of shit..."
    me "You're a crazy bitch..."
    scene jasminetrain2 with Dissolve(1)
    $ renpy.pause()
    y "Ahh... Is t-that... is that all you can do?" with dissolve
    scene jasminetrain3 with Dissolve(1)
    y "AHHH.... AHHH..." with dissolve
    y "Y-yeah! Fuck me [me]... Keep fucking me..."
    $ renpy.pause()
    play sound "toctoc.ogg"
    scene yt 51
    mo "Jasmine! Are you there? The door's locked!"
    y "D-dad? Y-yes! I'm... erm... trying on a new outfit! Don't come in!"
    scene yt 52
    y "(Whispering) G-get off me!"
    me "(Whispering) Oh shit..."
    y "(Whispering) Shut up!"
    scene yt 51
    mo "Really? Now? You had me worried for a moment..."
    scene yt 53
    y "S-sorry Dad!"
    mo "Okay... finish quickly. I'll wait for you at the end of the wagon."
    scene yt 54
    y "Erm... No! No need! Go to your seat! I'll be right back!"
    me "(Jesus, I'm so fucking horny...)"
    scene yt 55 with Dissolve(.8)
    mo "I'd rather not, Jasmine... There could be someone... dangerous around here." with dissolve
    scene yt 56
    y "D-dangerous?" with Dissolve(.7)
    y "(Whispering) What the fuck are you doing? My Dad's right there!"
    scene yt 51
    mo "Yes, dangerous. Come on, Jasmine, don't make me worry about you."
    scene yt 57
    y "(Whispering) Are you fucking crazy? Stop!"
    me "(Whispering) You got a great ass, Jas."
    y "(Whispering) Don't call me that! And I told you to stop!"
    scene yt 51
    mo "Jasmine. Are you listening to me? Speak louder, I can't hear you."
    scene yt 57
    y "I'm sorry Dad... Erm... I said that I'm a big girl, I can take care of myself."
    y "You don't need to..."
    scene yt 58 with Dissolve(1)
    y "(Holding in a moan) T-to..." with dissolve
    me "(Ahh... This feels amazing...)"
    scene yt 59
    y "T-to... worry..." with dissolve
    scene yt 51
    mo "I know sweetie, but let's go back to our wagon anyway, please."
    scene jasminetrain4 with Dissolve(1)
    $ renpy.pause()
    y ". . ." with dissolve
    mo "Jasmine?!"
    y "D-dad, please, don't be a p-pain!"
    y "W-who the fuck would want to hurt me? Mmmm... y-you’re the one with the business enemies..."
    y "N-not me..."
    scene jasminetrain5 with Dissolve(1)
    mo "I... guess you're right, honey." with dissolve
    mo "Okay, I'll wait for you there. Don't be long!"
    y "I won't, Dad..."
    $ renpy.pause()
    scene yt 58
    y "AHHHH... O-oh my fucking g-god..." with dissolve
    me "I think he left..."
    scene yt 59
    y "F-finally... I couldn't hold it anymore..."
    y "Now let's get this over with quickly. ... if I'm not back soon he’ll come back..."
    scene jasminetrain6 with Dissolve(1)
    y "Mmmmmhh... YES... keep going..." with dissolve
    y "Faster... faster..."
    scene jasminetrain7 with Dissolve(1)
    y "(Screaming) AAAH... AAAHHH..." with dissolve
    y "I'M CUMMING..."
    me "Ah... I'm just about to..."
    y "C-cum on my back! Outside!"
    $ renpy.pause()
    scene yt 60
    me "Ahhh..." with Dissolve(.3)
    y "Aaaah..."
    scene yt 61 with Dissolve(1)
    me "Jesus..." with dissolve
    y "(Panting) Fuck..."
    y "(Panting) Okay, erm... get out, go back to your family..."
    scene gallerybackground3
    call screen gallery3 with Dissolve(1)


label gaikobath:
    stop music2 fadeout 1
    stop music3 fadeout 1
    play music "night.ogg" fadein 1
    scene japn 13
    me "Zzzzz..." with dissolve
    play sound "water.ogg"
    pause (1)
    scene japn 14
    me "Hmm?" with Dissolve(1)
    play sound "water.ogg"
    scene japn 15
    me "(What's that noise?)" with dissolve
    scene japn 16 with Dissolve(1.5)
    me "(Oh... It's Aiko...)" with dissolve
    me "(What is she doing?)"
    scene japn 17
    ai "(Wow... The water looks so good... We've never had baths like this at home...)"
    ai "(Should I take a bath?)"
    scene japn 18
    ai "(Yeah, why not... They're all sleeping and [me] said I could come to the hotel... and it's not their home anyway.)" with dissolve
    scene japn 19
    ai "(I'm gonna put my hair up.)"
    scene japn 20 with Dissolve(1.5)
    ai "(I won't stay long...)" with dissolve
    scene japn 21 with Dissolve(.7)
    pause
    scene japn 22
    pause
    play sound "takeoff.ogg"
    scene japn 23 with Dissolve(2)
    pause
    scene japn 24 with Dissolve(1)
    ai "(Looks like it's the perfect temperature...)" with dissolve
    scene japn 25 with dissolve
    pause
    play sound "water.ogg"
    scene japn 26 with Dissolve(.8)
    pause
    play sound "water.ogg"
    scene japn 27 with Dissolve(1.2)
    ai "Ahhh..." with dissolve
    ai "(It's so warm...)"
    play sound "water.ogg"
    scene japn 28 with Dissolve(1)
    ai "(So relaxing...)" with dissolve
    ai "(I'm in heaven...)"
    scene japn 31
    me "(I'm in heaven...)"
    me "(She's not gonna take off her bra? Come on...)"
    scene japn 29
    ai "(Always training... or on a mission... It feels good to be able to rest for a few days...)"
    scene japn 30
    ai "(Hmm...)" with dissolve
    scene japn 31
    me "(Come on...)"
    scene japn 32 with dissolve
    pause
    play sound "water.ogg"
    scene japn 33 with Dissolve(.8)
    pause
    me "(Oh yes!)" with dissolve
    scene japn 34 with dissolve
    pause
    ai "(And I'm not disobeying Azazel's orders... He told me to keep an eye on [me] and that's what I'm doing.)" with dissolve
    ai "(Maybe, if he told me more, I could be more helpful...)"
    ai "(I don't know what his interest is in [me] but... he doesn't seem like a bad guy.)"
    play sound "water.ogg"
    scene japn 35 with Dissolve(1)
    pause
    play sound "water.ogg"
    scene japn 36 with Dissolve(.8)
    ai "(He's kind of funny, actually...)" with dissolve
    ai "(I've never had a chance to have many friends, but...)"
    ai "(I don't know...)"
    scene japn 38
    me "(God, I'm so fucking horny... Should I join her?)"
    me "(Better not... She'll think I'm some crazy stalker. And well, she'd be kind of right.)"
    scene japn 36
    ai "(I've never thought about it but... I guess I'm not that...)"
    "*Slight noise*"
    scene japn 37
    ai ". . ." with Dissolve(.3)
    scene japn 38
    me "(Maybe I should leave. After all, she's working for Azazel...)"
    play sound "water.ogg"
    scene japn 39 with Dissolve(1)
    me "(What the fuck? Is that a kunai?)" with dissolve
    scene japn 40
    me "(What is she...)"
    play sound "knife.ogg"
    pause (.4)
    scene japn 41
    me "AAAGH!" with hpunch
    me "What the f...!"
    play sound "water.ogg"
    scene japn 42
    me "Haha... Aiko... Hey there... I didn't see you..." with dissolve
    scene japn 43
    me "(Where the hell did she get that katana from?!)"
    me "Erm... Y-you're naked, you know that?"
    play sound "sword.ogg"
    scene japn 44
    ai "What are you doing here?! You were waiting for the perfect moment to attack me, weren't you?! I knew I couldn't trust you..." with hpunch
    me "W-what?"
    scene japn 44b
    me "No! I... I was just..."
    scene japn 47
    ai "You have 5 seconds to explain yourself before I cut your throat!"
    scene japn 46
    me "I... um... I just saw you were taking a bath and... well, you have such a nice body and... I was... mesmerized." with dissolve
    scene japn 47
    ai "What? You were... spying on me? To see me naked?"
    scene japn 46
    me "Erm... yes."
    ai "Are you for real? Is that all? Swear it on whatever you hold sacred!"
    me "YES! I swear!"
    ai "Hmmm..."
    scene japn 47
    ai "Ok, I believe you... for now. But I'm watching you!"
    ai "And you better give it your all the next day you come to the dojo!"
    scene japn 46
    me "I will! I'll train hard!"
    scene japn 47
    ai "Ok... I'm leaving then... And stop looking at my breasts!"
    me "Y-yes! Sorry!"
    play sound "takeoff.ogg"
    scene japn 48 with Dissolve(2.5)
    ai ". . ." with dissolve
    scene japn 49 with dissolve
    pause
    scene japn 50
    pause
    scene japn 51
    pause (.1)
    ai "*Chuckles*" with dissolve
    scene japn 52 with Dissolve(1)
    pause
    scene japn 53 with dissolve
    pause
    stop music fadeout 1
    scene gallerybackground3
    call screen gallery3 with Dissolve(1)


label gcarlahots:
    stop music2 fadeout 1
    stop music3 fadeout 1
    play music "springwater.mp3" fadein 1
    scene hots 20
    c "I'm ready!" with dissolve
    me "That was fast!"
    c "Yeah, I want to get into the water already!"
    scene hots 21 with dissolve
    pause
    scene hots 22 with Dissolve(.8)
    c "Oh... the water's so warm..." with dissolve
    play sound "water.ogg"
    scene hots 23 with Dissolve(.8)
    c "Ooohh... it's perfect..." with dissolve
    play sound "water.ogg"
    scene hots 24 with Dissolve(.8)
    c "The water's hot... and look at all this bubbling! Looks like it's boiling!" with dissolve
    me "Yeah, that's true! I think that's because of the gas and steam that rises from the Earth's crust."
    c "Ahh... I see you have studied! I'm so proud! How do they keep the water warm?"
    me "As far as I know, it is heated geothermally, but I guess someone passes through from time to time to clean and care for this place."
    c "Yeah... Good thing that this site is little known..."
    play sound "water.ogg"
    scene hots 25 with Dissolve(.8)
    c "Look! There're even some towels and some sort of beverage!" with dissolve
    me "Cool..."
    play sound "water.ogg"
    scene hots 26
    c "Well... Do I have to take a bath alone or..." with dissolve
    me "N-no! Sorry! I'm coming!"
    play sound "splash.ogg"
    scene hots 29 with Dissolve(2)
    me "(Man... This is so hot...)" with dissolve
    if inc:
        me "(Mom's right here almost naked... We're in a hot spring... Alone...)"
    else:
        me "(Carla's right here, almost naked... We're in a hot spring... Alone...)"
    play sound "water.ogg"
    scene hots 27
    me "I hope you don't mind me being naked..." with dissolve
    scene hots 28
    c "Haha, don't worry, we're past that."
    scene hots 29
    me "Exactly the way I feel. If..."
    play sound "water.ogg"
    scene hots 30
    me "You know, if you want... you can take off your towel too." with Dissolve(.8)
    me "No one's coming..."
    play sound "water.ogg"
    scene hots 31
    c "My towel? Oh... of course... I guess I’ll be much more comfortable." with dissolve
    scene hots 32
    c "I'm sorry, I know there's plenty of trust, it's just the custom."
    me "No problem! I..."
    play sound "water.ogg"
    scene hots 33 with Dissolve(1)
    pause
    play sound "water.ogg"
    scene hots 34 with Dissolve(1)
    pause
    play sound "water.ogg"
    scene hots 35 with Dissolve(1)
    pause
    play sound "water.ogg"
    scene hots 37 with Dissolve(1)
    c "Ahhh... Much better, don't you think?" with dissolve
    me "Y-yeah, much better..."
    play sound "water.ogg"
    scene hots 36
    c "Come! Let's sit here and relax a while!" with Dissolve(.8)
    scene fewminutes with Dissolve(1.5)
    pause
    scene hots 38 with Dissolve(1.5)
    c "Ohhh... the trip is already worth it..." with dissolve
    me "You can say that again..."
    play sound "water.ogg"
    scene hots 39
    c "I still can't believe it came for free!" with dissolve
    me "Yeah, we were lucky..."
    scene hots 41
    me "By the way..." with dissolve
    me "What did Midoriko tell you at the temple?"
    scene hots 40
    c "I can't tell you that! It's a secret..."
    scene hots 41
    me "Come on! Tell me! Please..."
    scene hots 40
    c "It's personal!"
    c "But... Let's do something: I’ll tell you if you tell me a secret."
    scene hots 41
    me "A secret, huh? Alright..."
    me "Um..."
    me "Don't tell anyone but... you know Hiromi, our guide?"
    scene hots 40
    c "Yes..."
    scene hots 41
    me "Well, he's... something like a drug lord around here."
    scene hots 40
    c "Haha, really? Hiromi? Our Hiromi?"
    scene hots 41
    me "The very same."
    scene hots 40
    c "Wow... haha, I knew he was hiding something... illegal, but I didn't think it could be something that big."
    scene hots 41
    me "It's your turn..."
    scene hots 40
    c "Well... she just told me that... I should be honest with myself... and that I should come to this hot spring!"
    scene hots 41
    me "Said and done!"
    scene hots 40
    c "Of course!"
    c "This is fun! Tell me another secret!"
    scene hots 41
    me "Ok... Is there anything you want to know?"
    scene hots 40
    c "Well... we've never talked about it but... have you... have you ever slept with a girl?"
    scene hots 41
    me "Well... Yes... I've already had sex with a couple of girls, if that's what you wanted to know..."
    scene hots 39
    c "Ohh... I see..." with dissolve
    c "I guess you’re not a kid anymore... You’ve grown up so fast..."
    scene hots 41
    me "It's your turn! Tell me a secret..." with dissolve
    scene hots 39
    c "Ok..." with dissolve
    c "Do you remember that... ahem... that blowjob I gave you on our couch?"
    me "How could I forget..."
    c "Well..."
    c "I... I don’t know if it’s because we were interrupted, but... I haven't been able to stop thinking about it since then..."
    scene hots 42
    c "Did that happen to you?" with dissolve
    me "Y-yes... Something like that..."
    me "(Jesus, I'm getting so fucking horny...)"
    c "Maybe this is because we didn't finish... It's like Dr. Monroe said, we must finish a chapter before we can move on..."
    scene hots 43 with Dissolve(1)
    pause
    me "I... I agree..." with dissolve
    c "Yes, I see you do..."
    play sound "water.ogg"
    scene hots 44
    c "So... What do you say? Do you want me to finish the blowjob?" with Dissolve(1)
    c "I don't think we'll have a better chance..."
    me "I do... More than anything in the world..."
    scene hots 45
    c "Alright..." with Dissolve(1)
    play sound "water.ogg"
    scene hots 46 with Dissolve(1)
    pause
    me "Ohh..." with dissolve
    scene hots 47 with Dissolve(.8)
    pause
    c "Mmmm...." with dissolve
    scene hots 48 with Dissolve(.8)
    pause
    scene hots 49
    play sound "water.ogg"
    me "Ohhh... yeah..." with Dissolve(1)
    if inc:
        me "You're the best at this, Mom..."
    else:
        me "You're the best at this, Carla..."
    scene hots 50 with Dissolve(1)
    c "(Deepthroating) Mmmmm...." with dissolve
    scene carlasex1 with Dissolve(1)
    pause
    me "Oh my fucking god... Don't stop..." with dissolve
    scene hots 51
    if inc:
        me "Faster Mom... Please..." with dissolve
    else:
        me "Faster Carla... Please..." with dissolve
    c "Mm-hmm...."
    scene carlasex2 with Dissolve(1)
    pause
    scene hots 52 with Dissolve(1)
    pause
    scene hots 53 with Dissolve(1)
    me "Ohh God..." with dissolve
    scene hots 54 with Dissolve(1)
    me "How can you be so fucking hot... I wish I was Dad..." with dissolve
    me "You're a goddess..."
    scene hots 55 with Dissolve(1)
    c "*Gagging*" with dissolve
    scene hots 56
    c "(Catching her breath) Your father?" with Dissolve(1)
    me "Well, what I meant is... Erm..."
    play sound "water.ogg"
    scene hots 57
    c "Before you... cum... and we leave..." with Dissolve(1)
    c "Can I tell you... one last secret?"
    me "O-of course..."
    play sound "water.ogg"
    scene hots 58
    c "(Sitting on your lap) Alright..."  with Dissolve(1)
    c "How long... do you think... I've been without having sex?"
    me "W-without sex? Well... Dad's been gone for almost two months now so..."
    me "Two months?"
    scene hots 59
    c "I wish..." with dissolve
    c "I think... it's been... six months? Seven? I don't know, maybe more..."
    me "But... why?"
    c "Well... you know your Dad... Always busy, always working..."
    play sound "water.ogg"
    scene hots 62
    c "Or maybe it's me..." with Dissolve(1)
    c "Maybe I'm not good enough..."
    c "I guess I'm not as young as I used to be..."
    me "Are you fucking kidding me?!"
    me "You have the best body I’ve ever seen in my life."
    scene hots 63
    c "You really think so?" with Dissolve(1)
    me "(Oh dear lord...)"
    me "Absolutely..."
    play sound "water.ogg"
    scene hots 58
    c "Haha... thank you, [me]..." with Dissolve(1)
    c "I'm so lucky to have you..."
    scene hots 59
    me "If Dad doesn't notice you, for the amazing person that you are, inside and out, it's his loss. That just confirms he's insane." with dissolve
    c "Thank you..."
    scene hots 60
    c "It's just that... I haven't been with a man for so long..." with dissolve
    c "And you've been so caring that I felt..."
    me "If you want we could..."
    scene hots 61
    c "Haha, I see where you're trying to go, but that can't happen. Everything has its limits." with dissolve
    if inc:
        me "(Kissing her neck) Come on, Mom..."
    else:
        me "(Kissing her neck) Come on, Carla..."
    me "Midoriko said you shouldn't deny yourself..."
    me "Don't you want to satisfy your needs?"
    scene hots 64
    c "Well..." with Dissolve(1)
    c "I..."
    c "I admit that I am horny... I'm horny as hell..."
    c "And... having your huge cock between my legs is driving me crazy..."
    c "Maybe... if we did it..."
    c "Just for a few seconds... it wouldn't be so wrong..."
    scene hots 61
    c "But... Are you sure you wanna do this?" with dissolve
    me "Yes..."
    c "We shouldn't..."
    me "We should..."
    scene hots 64
    c "O-ok..." with dissolve
    scene hots 65 with Dissolve(1)
    c "Um... it's going in and out a couple of times and it's over." with dissolve
    c "Something quick, all right?"
    me "Of course..."
    pause
    scene hots 66 with Dissolve(1)
    if inc:
        me "(Oh my God... I can feel Mom's pussy...)" with dissolve
    else:
        me "(Oh my God... I can feel Carla's pussy...)" with dissolve
    me "(I'm finally about to fuck her...)"
    pause
    scene hots 67 with Dissolve(1)
    c "O-oh god..." with dissolve
    c "I had almost forgotten what it was like..."
    pause
    scene hots 68 with Dissolve(1.2)
    c "O-OH GOD... You're so big, [me]..." with dissolve
    pause
    scene hots 69 with Dissolve(1.3)
    c "AAAHH..." with dissolve
    me "O-oh my god..."
    c "Oh Jesus... I can feel your cock... inside me."
    c "Y-you're completely filling me up..."
    c "I'm g-gonna start moving... a couple of times... all right?"
    me "Yes..."
    scene carlasex3 with Dissolve(1.5)
    pause
    c "Ahhh..." with dissolve
    c "Yes... Oh Jesus..."
    c "I... I can't stop..."
    c "J-just... just a couple more, all right?"
    scene carlasex4 with dissolve
    c "AHHH... OH MY GOD... I can't stop...." with dissolve
    pause
    scene carlasex5 with dissolve
    c "O-O-OH MY FUCKING GOD..." with dissolve
    c "I h-had never felt this way... How could I have been missing this all my life..."
    c "(Moaning) Aaah..." with dissolve
    pause
    scene carlasex3b with dissolve
    pause
    scene carlasex4b with dissolve
    c "J-just a few more... Please... please... don't stop [me]..." with dissolve
    pause
    scene carlasex5b with dissolve
    c "Aaaahhhh..." with dissolve
    c "This is amazing..."
    c "(Moaning) Aaah..." with dissolve
    pause
    scene hots 69
    c "(Panting) Oh god... I can't... I can't go on..." with Dissolve(1)
    c "My legs are shaking..."
    me "Ahh... Hop up on the stone... Let me take it from here..."
    scene hots 68
    c "T-the stone?" with dissolve
    scene hots 65
    c "Ok..." with dissolve
    play sound "water.ogg"
    scene hots 70 with Dissolve(1.5)
    c "(Panting) Where do you get all that vitality?..." with dissolve
    play sound "water.ogg"
    scene hots 71
    me "With you right before me, I could go on all day..." with Dissolve(.8)
    scene hots 72
    c "You're such a naughty boy... I'm going to have to punish you..." with dissolve
    c "Grounded for 2 weeks..."
    scene hots 73
    me "Well... as long as you stay home too and I can keep fucking you all day..." with dissolve
    c "Oh yeah?... Would you fuck me hard?"
    scene hots 74
    me "Do you want to be fucked hard?" with dissolve
    c "I do... Fuck me as hard as you can..."
    c "Please..."
    scene hots 75 with hpunch
    c "O-o-oohh g-god..." with dissolve
    scene carlasex6 with Dissolve(1)
    c "Ahhh... Aaah... [me]..." with dissolve
    if inc:
        me "Ahh.. Your pussy feels so fucking good Mom..."
    else:
        me "Ahh.. Your pussy feels so fucking good Carla..."
    scene carlasex7 with dissolve
    c "(Squealing with pleasure) AAAHH... YES, YES!" with dissolve
    c "D-don't stop baby, don't stop..."
    scene carlasex8 with dissolve
    c "Aaahhh..." with dissolve
    pause
    scene carlasex6b with dissolve
    c "Ahhh..." with dissolve
    c "Ahh... Yeah... K-keep going..."
    pause
    scene carlasex7b with dissolve
    c "Ahh... Yes..." with dissolve
    if inc:
        c "Keep fucking your mommy..."
    pause
    scene carlasex8b with dissolve
    c "Yes... YES...." with dissolve
    pause
    scene carlasex9b with dissolve
    pause
    c "(Squealing) AHHH... AH... AHHHH...." with dissolve
    me "I'm cumming... I'm cumming..."
    c "Ahh... I... I reached my climax..."
    menu:
        with dissolve
        "Creampie":
            me "I can't hold..."
            scene hots 75
            me "(Cumming) O-ohhhh... GOD..." with hpunch
            scene hots 76 with Dissolve(1)
            pause
            c "Ahh... You... filled me up..." with dissolve
            c "A lot..."
            play sound "cream.mp3"
            scene hots 77 with Dissolve(1.5)
        "Pull out":
            play sound "water.ogg"
            scene hots 78 with Dissolve(1.5)
            me "Ahhh... I can't hold it any longer..." with dissolve
            scene hots 79 with hpunch
            me "Ahh..." with hpunch
            scene hots 80 with Dissolve(1)
    pause
    if inc:
        me "I... I'm sorry Mom." with dissolve
    else:
        me "I... I'm sorry..." with dissolve
    c "Don't worry... that's fine..."
    c "We should get going... It's a long walk to the hotel..."
    play sound "water.ogg"
    scene hots 81 with Dissolve(1.5)
    c "(Drying herself with the towel) Ahem..." with dissolve
    c "Um..."
    c "That... was quite intense."
    c "We... we should have sushi for dinner tonight. Yeah, we'll do that."
    c "(Oh my god, what have we done...)"
    me "But... that was good, wasn't it?"
    scene hots 82
    c "Good? That was the best sex of my life..." with dissolve
    scene hots 81
    c "B-but... um... it's got to stay between us, ok? Now we can wrap this up once and for all!" with dissolve
    c "What was I saying? Ah, yes! Sushi! Let's have some sushi. Hurry up, [me]! It'll be dark soon!"
    if inc:
        me "Yes, Mom!"
    else:
        me "Yes!"
    stop music fadeout 1
    scene gallerybackground4
    call screen gallery4 with Dissolve(1)


label glaurenpublicbath:
    play music "springwater.mp3" fadein 2
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene pb 32
    me "Have I ever told you how beautiful you are?" with dis
    scene pb 33
    l "Hmmm... yeah, sometimes..."
    scene pb 32
    me "Well, you look especially hot today..."
    me "I'm getting seriously horny just looking at you..."
    scene pb 34
    l "Hmm..." with dissolve
    play sound "water.ogg"
    scene pb 35
    l "Yes... I can see your little friend is getting excited down there..." with dissolve
    l "Too bad you have to go now..."
    play sound "water.ogg"
    scene pb 36
    l "These are the ladies' baths, you shouldn't be here..." with dis
    me "(Oh my god...)"
    l "Some employee could get in..."
    l "Mom or Judie could come back at any moment..."
    scene pb 37
    l "They went to the outside baths but, how long before they get back?" with dis
    l "15 minutes? 10?"
    l "It'll be better if they don't find you here..."
    me "(Is... is she giving me hints?)"
    me "(Look at that delicious pussy...)"
    scene pb 38 with dissolve
    me "(She's really turning me on... I'm rock-hard...)" with dissolve
    scene pb 39
    l "Can you imagine being caught here? You should speed up..."
    play sound "water.ogg"
    scene pb 40
    me "So... 10 minutes, you said?" with dis
    me "Then I guess I'm not in that much of a hurry, am I?"
    l "Well, I guess not..."
    me "I could stay a while..."
    me "Can you think of anything we could do?"
    scene pb 41
    l "I don't know..." with dis
    l "Surprise me..."
    scene pb 42
    me "Hmm... There's one thing I can think of..." with dissolve
    me "But you’re gonna have to do your part too..."
    scene pb 43
    l "I'm fine with it..." with dis
    me "Good..."
    scene pb 44 with Dissolve(1.5)
    l "AAaahhh..." with dissolve
    scene pb 45
    l "Ahhh... yeah... Fuck me, [me]..."
    me "You're finally being clear..."
    scene pb 46 with dis
    l "AAah...." with dissolve
    scene pb 47
    me "Oh God... I've missed your juicy pussy, Lauren..." with dis
    scene pb 48
    l "Y-yeah... I've missed your big cock..." with dis
    scene pb 49
    if inc:
        l "Well, what are you waiting for, brother?" with dis
    else:
        l "Well, what are you waiting for?" with dis
    l "You’ve been begging to fuck me this entire trip. This is your chance..."
    me "Oh, and I'm going to take it..."
    scene laurenpb1 with Dissolve(1.5)
    pause
    l "Yeah... keep going... I love it..." with dissolve
    me "Oh Lauren..."
    me "After this you’re gonna forget about me, again?"
    l "No... never again..."
    l "I wanna do this... everyday..."
    l "I wanna be with you... forever..."
    scene laurenpb2 with dis
    l "Ahhh... YES..." with dissolve
    l "Fuck me, [me]..."
    l "Make me yours..."
    l "Faster... FASTER..."
    scene laurenpb3 with Dissolve(1.5)
    l "O-OH MY GOD..." with dissolve
    l "T-this is...."
    l "A-A-a-ahhh..."
    pause
    scene pb 50
    j "Yeah, sure, I'm gonna tell her." with dis
    j "Order me a coke!"
    scene pb 51
    l "W-what?! T-they are already here!"
    l "STOP! Hide!"
    me "Ahh... What?"
    play sound "splash.mp3"
    scene pb 52
    l "I said hide!!!" with hpunch
    scene pb 53 with dis
    j "Hey sis!" with dissolve
    scene pb 54
    l "H-hey Judie! Are you done?"
    scene pb 53
    j "Yeah, we're gonna change now."
    j "You should try the outside baths before leaving! There's no one there, either!"
    scene pb 54
    l "Okay, cool, I'm gonna do that!"
    scene pb 55
    j "Okie Dokie! We'll wait for you in the street! Don't take too long!"
    l "OK! See you later!"
    scene pb 56 with dis
    l ". . ." with dissolve
    play sound "bubbles.mp3"
    scene pb 57
    me "(Catching his breath) Aaah!" with dissolve
    scene pb 58
    me "What the hell, Lauren?! I almost drowned!" with dissolve
    l "Hehe, I'm sorry..."
    play sound "water.ogg"
    scene pb 59
    l "But don't be angry, please..." with dis
    l "Follow me, I'm going to make it up to you..."
    l "I promise..."
    me "Hmm... I can't be mad at you if you get like that..."
    me "Where are we going?"
    l "You'll see..."
    stop music fadeout 2.5
    play music2 "waterfall.mp3" fadein 2.5
    scene pb 60 with Dissolve(2.5)
    me "Wow, this place is so cool!" with dissolve
    me "Now I understand why it’s so fucking expensive..."
    scene pb 61 with Dissolve(1.5)
    me "Whoa... It's so steamy in here." with dissolve
    me "Lauren?"
    l "I'm here..."
    scene pb 61b with dis
    l "This humidity's ruining my hair..." with dissolve
    me "I fucking love it when you get your hair all messy..."
    l "Oh, do you?"
    play sound "fall2.ogg"
    scene pb 63 with dis
    me "You were saying something about compensating me..." with dissolve
    scene pb 64
    l "Ah... yes..."
    l "I'm gonna ride you so hard you’re gonna come in 30 seconds..."
    l "I..."
    scene pb 65
    l "I know it's wrong, but..." with Dissolve(.8)
    l "I wanna be with you..."
    l "I need you..."
    l "I..."
    me "I love you, Lauren"
    l "D-don't be silly..." with dissolve
    me "I mean it..."
    l "(Chuckles) Shut up!"
    me "Alright... Then you’re gonna have to shut me up..."
    l "I'm gonna teach you a lesson..."
    scene pb 67 with dis
    pause
    scene pb 68 with dis
    l "Aaah..." with dissolve
    scene pb 69 with dis
    l "AAAAaahh... Yes..." with dissolve
    scene laurenpb4 with Dissolve(1.5)
    pause
    l "(Moaning) Mmmmhh... Yes..." with dissolve
    me "Oh Lauren..."
    me "Keep going..."
    pause
    l "You're so fucking big..." with dissolve
    me "Can I go in a little deeper?"
    l "(Panting) I guess... Will you be able to handle it?"
    me "Of course..."
    l "We'll see about that..."
    scene laurenpb5 with Dissolve(1.5)
    pause
    l "(Panting) AAAAH... AAAAHHH..." with dissolve
    l "O-oh my fucking g-god..."
    scene pb 70 with Dissolve(1.5)
    ai "(I should tell Lauren that her Mom and sister are ready.)" with dissolve
    scene pb 71 with Dissolve(1.2)
    pause
    scene pb 72 with dis
    ai "(If we delay we're gonna...)" with dissolve
    scene pb 73
    ai "(What the...)" with dis
    scene pb 74 with dis
    ai "(T-they...)" with dissolve
    scene pb 75
    ai "(T-they're having sex!)"
    scene pb 74
    if inc:
        ai "(What the hell?! But... weren't they siblings?)"
    else:
        ai "(What the hell?! But... weren't they step-siblings?)"
    ai "(Is... is this something normal in Europe?)"
    ai "(I don't think so...)"
    scene pb 75 with dis
    pause
    scene pb 76 with dis
    ai "(Lauren seems to be enjoying herself, that's for sure...)" with dissolve
    scene pb 77
    j "Aiko? Is Lauren there or not?"
    scene pb 78
    j "Aiko?"
    scene pb 79
    ai "Y-YES!" with hpunch
    ai "She's there! She says she'll be right up!"
    j "Oh, ok, does she need..."
    scene pb 80
    ai "No! She doesn't need anything else! She has everything under control!" with dissolve
    ai "L-let's wait for her upstairs!"
    j "O-ok!"
    ai ". . ."
    scene laurenpb5 with Dissolve(1.5)
    l "AAaahh..." with dissolve
    scene laurenpb5b with Dissolve(1.5)
    l "Yes..." with dissolve
    scene laurenpb6b with Dissolve(1.5)
    l "(Panting heavily) AAAHHH..." with dissolve
    scene laurenpb6 with Dissolve(1.5)
    l "(Panting heavily) AAAAAAARGHHH...." with dissolve
    me "(Gasping) Fuck, Lauren..." with dissolve
    me "(Gasping) I'm gonna cum..."
    me "(Gasping) If you don’t want to be impregnated... y-you should get off..."
    pause
    me "(Gasping) Ahh... L-lauren?" with dissolve
    l "(Panting) Aaaahh... D-do... d-do... w-what you... w-want...."
    menu:
        with dissolve
        "Creampie her":
            scene pb 83
            me "AAAAHH..." with hpunch
            scene pb 81
            l "AAAAaaaaaahahhhhhhhhh...." with hpunch
            scene pb 83 with dis
            pause
            scene pb 84 with dis
            pause
            scene pb 82
            me "Oh, Lauren... That was amazing..."
            scene pb 84 with dis
            pause
            scene pb 86 with dis
            pause
            play sound "cream.mp3"
            scene pb 85 with dis
            me "O-oh my god..." with dissolve
            play sound2 "cream.mp3"
            scene pb 86 with dis
            pause
            play sound3 "cream.mp3"
            scene pb 85 with dis
            pause
            play sound4 "cream.mp3"
            scene pb 86 with dis
            pause
            play sound "cream.mp3"
            scene pb 85 with dis
            me "OH GOD... I'm going to explode..." with dissolve
            l "(Moaning) Ahh... I can feel your load... filling me up..."
            scene pb 87 with dis
            pause
            play sound "cream.mp3"
            scene pb 88 with Dissolve(1.5)
            l "Ahh..." with dissolve
            me "(She let me cum inside her... That was fucking amazing...)"
        "Pull out":
            scene pb 90
            me "AAAAH..." with hpunch
            scene pb 81 with Dissolve(1)
            l "Oh my fucking god..." with dissolve
            me "Wow..."
            l "I won't be able to walk for a week..."
            me "Did you cum?"
            l "Stronger than ever..."
    scene pb 89 with Dissolve(2)
    l "Wow... That was even better than the last time..." with dissolve
    me "You sure have energy..."
    l "Come on, let's leave before Mom and Judie start wondering what we've been doing for so long..."
    stop music fadeout 1
    stop music2 fadeout 1
    scene gallerybackground4
    call screen gallery4 with Dissolve(1)


label grebeccabeach:
    stop music2 fadeout 1
    stop music3 fadeout 1
    play music "seashore.ogg" fadein 1
    scene rbs 96
    me "(Hmm... I don't think anyone went this far.)" with dis
    me "I think there's nobody left Rebecca, we should turn back too."
    scene rbs 97
    r "Yes, just take a look around the corner to see if anyone's there."
    me "Right away."
    scene rbs 98 with Dissolve(2)
    me "Hmmm... Nope, there's no one left. I think everybody went to the bus." with dissolve
    r "Great..."
    scene rbs 99
    r "Then... We're alone..." with dis
    me "We are..."
    r "I know we should get going but... I'm sure we still have a couple of minutes..."
    scene rbs 100 with dis
    r "*Undoing her skirt*" with dissolve
    scene rbs 101 with dis
    me "Oh my god Rebecca..." with dissolve
    me "You're risking your job..."
    scene rbs 102
    r "And my marriage."
    scene rbs 103
    r "But I don't wanna risk what we have. You made me feel special. You..." with dis
    scene rbs 104
    r "You fucked me like no one had ever done..." with dissolve
    r "I haven't stopped thinking about you since then."
    r "Did you think about me?"
    scene rbs 105
    me "I did..." with dis
    r "Mm-hm..."
    scene rbs 106 with dis
    pause
    scene rbs 107 with dis
    me "Oh god..." with dissolve
    scene rbs 108
    me "You're perfect..."
    scene rbs 109 with dis
    pause
    scene rbs 111 with dis
    r "Well..." with dissolve
    scene rbs 113
    r "We don't have much time, 5 minutes at most." with dissolve
    scene rbs 112
    me "So..."
    scene rbs 113
    r "So... we can't get all dirty, but I'm gonna make you have a really good time."
    r "So that you remember me over the weekend..."
    scene rbs 112
    me "Sounds good..."
    scene rbs 114 with dis
    me "So... 5 minutes, huh? You'll have to do a really good job, Ms. Wilson..." with dissolve
    scene rbs 115 with dis
    r "(Taking your trunks off) Oh, that's what I plan to..." with dissolve
    scene rbs 116 with dis
    pause
    scene rbs 117
    r "You have no idea how much I've been longing for your big cock, [me]..." with dissolve
    me "You're driving me insane..."
    scene rbs 116 with dis
    pause
    scene rbs 118 with dis
    r "Mmmmm..." with dissolve
    scene rbs 119 with dis
    pause
    scene rbs 118 with dis
    pause
    scene rbs 119 with dis
    pause
    scene rbs 118 with dis
    pause
    scene rbs 116
    r "(Gasping for air) Ahh..." with dis
    scene rbs 119 with dis
    pause
    scene rbs 120 with dis
    r "*Gagging*" with dissolve
    scene bos1 with dis
    r "Mmm..." with dissolve
    me "Ohhh... yeah..."
    me "That's it, keep sucking Rebecca..."
    scene bos2 with dis
    pause
    me "Ahhh..." with dissolve
    me "You're enjoying this as much as I am, aren't you?"
    r "Mmmm...."
    scene bof1 with dis
    r "(Gagging) G-gak! Gak!" with dissolve
    me "AAAhhh..."
    me "YEAH..."
    me "Oh my fucking god Rebecca..."
    scene rbs 122 with dis
    r "*Choking on her saliva*" with dissolve
    scene rbs 121
    r "(Gasping for air) Ahhhhh.....!" with dis
    scene rbs 122
    r "Hmmmh..." with dissolve
    scene rbs 121
    r "Ahhhh.... Oh God..." with dis
    me "Wow, Rebecca... Are you ok?"
    scene rbs 117
    r "Yeah, I am..." with dis
    r "But I'm afraid we have to leave now, Principal Johnson must be mad looking for us..."
    scene rbs 116
    r "But..." with dis
    r "I'm too horny... I need you..."
    r "I need to feel your cock inside me again..."
    r "And I need it now..."
    scene rbs 117
    me "Maybe he can wait another couple of minutes..." with dissolve
    scene rbs 118
    r "Mmmm..." with dissolve
    scene rbs 116
    r "Maybe you're right... Just a couple more minutes..." with dissolve
    r "But you’re gonna have to behave yourself and do as I say."
    scene rbs 115
    me "At your service, Ms. Wilson." with dis
    scene rbs 113
    r "Good boy... Now get down on the floor." with dis
    play sound "fall2.ogg"
    scene rbs 123
    r "This time I will be the one to take the lead." with dis
    scene rbs 125
    me "Uh-huh..." with Dissolve(1.3)
    me "You're the best teacher I could have ever asked for, Rebecca..."
    scene rbs 124
    r "Haha, you have no idea..."
    r "You're gonna be ridden so hard you're gonna faint."
    scene rbs 125
    me "OH YEAH..."
    scene rbs 126 with dis
    pause
    me "I love you body..." with dissolve
    scene rbs 127
    r "Are you ready?"
    me "I am..."
    r "Put your hands on the ground and don’t move..."
    scene rbs 126
    me "As you say, Ms. Wilson..."
    scene rbs 128 with Dissolve(1.2)
    pause
    scene rbs 129 with dis
    r "Ahh..." with dissolve
    scene rbs 130
    r "AAARGH...." with dis
    scene rbs 131
    r "O-oh g-god... This is amazing..."
    r "Y-you fill me up completely..."
    scene bvs1 with dis
    me "O-ooooh god..." with dissolve
    r "Aaahhh... ahh... yeah..."
    scene bvss1 with dis
    r "Ahhh..." with dissolve
    scene bvsss1 with dis
    r "Aaahh... [me]..." with dissolve
    r "You're mine..."
    scene bvs2 with dis
    r "Aaahh... Yes babe..." with dissolve
    scene bvss2 with dis
    r "Ahhh... ahhhh...." with dissolve
    scene bvsss2 with dis
    me "Oh my god Rebecca..." with dissolve
    scene bvf1 with dis
    r "A-a-a-a-ahhhhh...." with dissolve
    scene bvff1 with dis
    r "AHHHH... FUCK... THIS IS..." with dissolve
    scene bvfff1 with dis
    me "O-o-ohh J-jesus Christ... Ahhh..." with dissolve
    me "I can't hold much longer..."
    scene rbs 144 with Dissolve(1.5)
    r "(Breathing heavily) Ahhh... [me]... I can't keep up this pace..." with dis
    scene rbs 145
    r "God..." with dis
    r "My behavior is unacceptable for a good teacher..."
    me "It is..."
    r "Such a disgrace to the profession..."
    r "You'll have to punish me..."
    me "Come here..."
    play sound "slap1.mp3"
    scene rspanka1 with Dissolve(.1)
    pause .4
    scene rbs 147 with Dissolve(1.5)
    r "AAAAaargghhh...." with dissolve
    r "F-fuck..."
    me "Less than 2 months away from your wedding, in your working hours, and you're doing this?"
    r "Ahhhh... I need to be punished..."
    play sound "slap1.mp3"
    scene rspanka2 with Dissolve(.1)
    pause .4
    scene rbs 147
    r "(Biting her lip) Hmmff...." with dis
    scene rsofaa1 with Dissolve(1.5)
    r "AAAaahhh... YESSS..." with dissolve
    scene rsofab1 with dis
    r "Ahhh... ahhh..." with dissolve
    pause
    scene rsofab1fast2b with dis
    pause
    scene rsofab1fast with dis
    r "AAAAHHH!" with dis
    r "A-a-a-a-ahhh...."
    me "Oh god, I can't... I'm gonna cum..."
    me "Rebecca..."
    r "(Panting) Y-yeah..."
    r "(Panting) Give me all of yourself..."
    r "(Panting) Come inside me..."
    me "Jesus..."
    menu:
        with dissolve
        "Cum inside":
            scene rbk 3
            me "Aaaahhh..." with hpunch
            r "Aaaaah..." with hpunch
            scene rbs 150
            play sound "fall2.ogg"
            r "God..." with dis
            r "(Panting) Jesus Christ... I can't... I can't walk... I can't get up..."
            scene rbs 152
            hide screen rebecca_points
            me "Fuck... I... unloaded inside of you..." with dis
            r "(Panting) Yeah... I... I can feel it filling my pussy..."
            scene rbs 151
            r "(Panting) It feels warm..."
            scene rbs 152
        "Pull out":
            scene rbs 149
            me "Aaaahhh..." with hpunch
            r "Aaaaah..." with dissolve
            scene rbs 150
            play sound "fall2.ogg"
            r "God..." with dis
            r "(Panting) Jesus Christ... I can't... I can't walk... I can't get up..."
            scene rbs 153
            me "Oof... Thank god I pulled out in time..." with dis
    r "(Catching her breath) Ok..." with dis
    r "Now we REALLY have to go, or I'm gonna get fired..."
    me "Y-yeah, let's go.."
    me "Can you walk?"
    r "Yeah, give me... give me 30 seconds..."
    stop music fadeout 1
    stop music2 fadeout 1
    scene gallerybackground4
    call screen gallery4 with Dissolve(1)


label girisjudieg:
    stop music3 fadeout 1
    stop music2 fadeout 1
    play music "fireplace.mp3" fadein 1
    scene jisex 11
    i ". . ." with dis
    scene jisex 12
    i ". . ." with dis
    i "(Huh? Where...)"
    i "(Oh, I'm in [me]'s room...)"
    i "(I fell asleep in seconds...)"
    scene jisex 13
    i "(It's so nice and warm in here...)" with dis
    scene jisex 14
    i "(Hmm?)" with dis
    scene jisex 15
    i ". . ." with dis
    scene jisex 16
    i "(We are certainly in quite a suggestive position...)" with dis
    scene jisex 17
    i "(But that was a one-time thing, Iris.)" with dis
    if inc:
        i "(First of all, he's your cousin, and second...)"
    i "(You promised Judie you wouldn't try anything else ever again.)"
    scene jisex 18
    pause
    scene jisex 19 with Dissolve(1.4)
    pause
    scene jisex 20
    i "(He feels so warm...)" with dis
    i "(A little cuddle won't hurt anyone...)"
    scene jisex 21
    i "(Hmm...)" with dis
    i "(Fuck, I'm getting so horny...)"
    scene jisex 22
    i "*Fingering herself*" with dis
    i "(God... I wish he could fuck me right here and now...)"
    scene jisex 19
    i "Mmmm..."
    scene jisex 18
    i "Hmm?" with dis
    scene jisex 16
    i "(He... he's getting hard?)"
    i "(But he's still sleeping...)"
    i "(Maybe I'm rubbing too hard...)"
    play sound "sheet.mp3"
    scene jisex 23
    me "*Turning around*" with Dissolve(1.5)
    scene jisex 24
    i "(Damn it, he turned around... I was having fun...)" with dis
    scene jisex 25
    i "*Touching his dick through the shorts*" with dis
    i "(Yup, he's hard!)"
    i "(I wonder if he's dreaming about someone...)"
    scene jisex 26
    i "(Maybe I could pull his pants down a bit...)" with dis
    i "(To help him be... more comfortable.)"
    i "(I'm sure he'd thank me if he was awake...)"
    scene jisex 27
    i "*Pulling down his shorts*" with dis
    scene jisex 28
    i "(Oh god...)" with dis
    i "(It is... fully erect.)"
    scene jisex 29
    i "(I can't believe we're not gonna fuck again...)" with dis
    i "(I want it so bad...)"
    scene jisex 30
    i "(Maybe I can suck his big cock one last time...)" with dis
    i "(Neither he or Judie will even know...)"
    scene jisex 31
    i "Mmm..." with dis
    i "(It's so hot...)"
    i "(God, I'm so fucking horny...)"
    scene jisex 32
    i "Mmmmmmm..." with dis
    scene jisex 33 with dis
    i "*Gagging*" with dissolve
    scene jisex 32 with dis
    pause
    scene jisex 33 with dis
    i "Mmmm..." with dissolve
    scene black with dis
    pause
    me "Mmmmm... yeah... that's it..." with dis
    me "Don't stop..."
    scene jisex 87 with dis
    me "(Huh?)" with dis
    me "(Oh... what a dream... I...)"
    me "O-o-oh god..."
    scene jisex 35
    me "W-what the..." with dis
    me "(Whispering) I-iris?!"
    i "Mmmm..."
    scene jisex 36
    i "Ahhh... Hi [me]..." with dis
    me "(Whispering) What the fuck?! Judie's right here!"
    i "(Whispering) I know... Sorry..."
    i "(Whispering) It's just..."
    i "(Whispering) I couldn't help myself..."
    i "(Whispering) Just let me suck it for a minute, please..."
    scene jisex 37
    i "(Whispering) I've nearly finished, I promise..." with dis
    me "(Whispering) But-"
    play music2 "blowjob3.mp3" fadein 1.5
    scene ioa with Dissolve(1.5)
    me "O-oh my god..." with dissolve
    i "Mmmm..."
    pause
    me "O-ok... We should stop..." with dissolve
    scene iooa with dis
    me "Ahhh... Iris..." with dissolve
    me "Oh my fucking god..."
    me "You sure are very convincing when you need to be..."
    i "Mm-hm..."
    me "(I hope Judie doesn't wake up...)"
    pause
    stop music2 fadeout 1
    scene jisex 37
    i "(Catching her breath) Ahhh..." with dis
    me "Jesus..."
    i "Your cock tastes too good..."
    i "It always makes me lose my mind..."
    scene jisex 38
    i "I'm so fucking horny right now, it hurts..." with dis
    me "Oh, yeah...?"
    scene jisex 39
    i "Yeah..." with dis
    me "Jesus..."
    scene jisex 40
    me "You're perfect..." with dis
    i "Do you wanna fuck me?"
    me "Yes I do..."
    i "I wanna feel your big cock inside my wet pussy again..."
    scene jisex 41
    me "Fuck it... me too..."
    me "Do you wanna go somewhere else?"
    scene jisex 42
    i "(Chuckles) No..." with dis
    scene jisex 43
    i "We can't leave Judie alone... What if something happens to her?" with dis
    i "I want you to fuck me right here..."
    me "R-right here?"
    i "Yeah..."
    i "But we have to be very, very quiet..."
    i "Because if not..."
    $ renpy.music.set_volume(0.35, channel='soundlow')
    play soundlow "sheet.mp3"
    $ hpunch2 = Move((10, 0), (-10, 0), .10, bounce=True, repeat=True, delay=1)
    scene jisex 44 with dis
    j "*Moves slightly*" with dis
    j "Hmm..."
    i "(Fuck, Judie almost woke up!)"
    i "(After the conversation we had, I'm sure she'd be mad...)"
    i "(What am I doing... I told her I wouldn't do this anymore and I won't.)"
    scene jisex 46
    me "(Whispering) That was close..." with dis
    i "(Whispering) Um..."
    i "(Whispering) I think I'm getting carried away by my impulses... again."
    scene jisex 45
    i "(Whispering) I'm sorry I dragged you into this."
    i "(Whispering) We'd better go to sleep..."
    me "Um..."
    scene jisex 46
    me "(Whispering) Hmmm... Yeah... I guess that'll be better..." with dis
    i "We're risking too much... aren't we?"
    scene jisex 47
    me "I agree..." with dis
    me "We're definitely risking too much..."
    scene jisex 48 with dis
    pause
    scene jisex 49 with dis
    me "Ahh..." with dis
    scene jisex 51
    i "(Whispering) W-what are you doing?! Am I the only one who came to my senses?!"
    i "(Whispering) We can't fuck next to Judie! She'll wake up!"
    me "(Whispering) I know... I just wanted to feel your pussy for a second... You turned me on too much..."
    scene jisex 49
    me "(Whispering) Just a bit..."
    scene jisex 50 with dis
    pause
    scene jisex 51
    i "D-don't..."
    scene jisex 52
    i "O-oh god..." with dis
    i "It's inside..."
    me "Ahh... it is..."
    scene ivsa with Dissolve(1.2)
    i "MMMmmmm..." with dissolve
    i "W-what are we doing..."
    i "We're gonna get caught..."
    me "I can't... I can't stop..."
    me "It just feels so fucking good..."
    me "Just a few more seconds... Please..."
    i "Mmmm..."
    i "Okay... Let's get this over quickly..."
    play music2 "bedcreak.ogg" fadein 1.5
    scene ivma with dis
    i "Ah.... ah.... ahhh...." with dissolve
    me "B-be quiet..."
    i "Ahh... I can't help it..."
    i "Ahhh..."
    i "The bed is squeaking anyway..."
    pause
    scene ivmma with dis
    i "Ahh..." with dissolve
    if inc:
        i "Does my pussy feel good, cousin?"
    else:
        i "Does my pussy feel good?"
    me "It feels fucking amazing..."
    i "Ahh... ah... Don't stop..."
    i "Keep going..."
    pause
    scene ivma with dis
    i "Ahhh... Yes... yes..." with dissolve
    i "Fuck me harder, [me]..."
    i "Harder..."
    me "Oh god..."
    me "Fuck it..."
    i "Harder..."
    $ renpy.music.set_volume(0.35, channel='music3')
    stop music2 fadeout 1.5
    play music3 "bedcreak2.ogg" fadein 1.5
    scene ivfa with dis
    i "(Biting her tongue) M-M-m-M-m-mmhhhh..." with dissolve
    me "O-oh my f-fucking god, Iris..."
    me "You're wet as fuck... This feels amazing..."
    me "Ahhh..."
    i "MMMmmmmm..."
    pause
    stop music3 fadeout 1.5
    scene jisex 53 with Dissolve(1.5)
    i "AAAAHHH... AAAHHH..." with dissolve
    i "YEAH..."
    me "D-don't scream..."
    i "Ahhhh... Y-you're fucking breaking me... I can't hold back anymore..."
    i "And besides, if this noisy bed hasn't woken Judie up, I don't think I..."
    scene jisex 54
    j "Hmmmm..." with dis
    i "(F-FUCK!)"
    scene jisex 55
    j "*YAWN*" with dis
    play sound "fall2.ogg"
    scene jisex 56
    j "Hmm?" with dissolve
    scene jisex 57
    j "[me]! Was your sleep disturbed, too? I..." with Dissolve(1.3)
    scene jisex 58
    j ". . ." with dis
    scene jisex 59
    j "Um... W-why are you naked? And boned?" with dis
    me "Erm..."
    j "Were you touching yourself?"
    me "Well, um... I... well..."
    j "I see..."
    j "And where's Iris?"
    me "She... went to her room, I think. There's not enough space for the three of us here."
    j "Her room?"
    scene jisex 60
    j "If that's so, I have a great idea, bro..." with dis
    me "Um..."
    j "Well, since you're hard already..." with dissolve
    scene jisex 61
    j "(Getting on top of you) And Iris isn't here..." with dis
    j "We could... have a little fun, don't you think?"
    me ". . ."
    scene jisex 62
    j "It's been too many days already since that night in Japan..." with dis
    me "Oh Judie..."
    scene jisex 63
    j "And I want to feel that again, bro..." with dis
    scene jisex 64
    j "I want you to fuck me, I want to feel your dick inside me again..." with dis
    scene jisex 65
    i "OH... {w} MY...{w} GOD." with dis
    j "W-WHAT?!"
    scene jisex 66
    j "I-i-iris! W-what are you doing h-here?!" with dis
    j "I... Erm... I... I thought... Um..."
    j "T-this is not what it seems! Haha..."
    scene jisex 67
    if inc:
        i "Oh, really? Because what it sounds like is that you fucked your brother in Japan and you were about to fuck him again right now."
    else:
        i "Oh, really? Because what it sounds like is that you fucked your step-brother in Japan and you were about to fuck him again right now."
    scene jisex 66
    j "What?! That's ridiculous! We were just kidding!"
    j "You know how much we like to fool around..."
    scene jisex 67
    i "Come on, babe! Don't be shy! This is fucking great!"
    scene jisex 68
    j "G-great? How is this great?" with dis
    j "This is a nightmare..."
    j "A-aren't you mad about this?"
    scene jisex 69
    i "Mad?! Are you kidding me?" with dis
    i "This is like... my wildest fantasy come true!"
    i "Do you know how many times I've dreamed of this moment?"
    scene jisex 70
    if inc:
        i "All I wanna see right now is my two cousins fuck each other..." with dis
    else:
        i "All I wanna see right now is my best friend getting pounded..." with dis
    j "W-what?"
    i "Your tight little pussy getting stretched..."
    j "Um... I don't feel comfortable with this, Iris..."
    i "Just relax..."
    i "You know as well as I do how good it feels..."
    me "(Oh my fucking god, this can't be happening...)"
    scene jisex 71
    i "That's it, babe..." with dis
    i "Are you ready?"
    j ". . ."
    scene jisex 72
    i "Well, it's your turn, [me]..." with dis
    if inc:
        i "Time to stick your big fat cock inside your sister's tight pussy..."
    else:
        i "Time to stick your big fat cock inside your step-sister's tight pussy..."
    scene jisex 73
    i "Mmmm..." with dis
    scene jisex 74
    i "Ahh... I’ll never get tired of sucking it..." with dis
    scene jisex 75
    i "Come on, Judie..." with dis
    i "I wanna see your peachy ass bouncing up and down..."
    i "You don't want that?"
    j "I..."
    j "I do..."
    i "That's my girl..."
    scene jisex 76 with dis
    pause
    scene jisex 77 with dis
    j "Ahhh..." with dis
    me "Yeah... Oh... Judie..."
    scene jisex 78 with Dissolve(1.3)
    j "AAaaaahhh..." with dis
    me "Oh Jesus..."
    me "It's as tight as the first time..."
    scene jisex 79
    i "Can you feel it, babe?" with dis
    j "Y-yes..."
    j "It's so big..."
    i "Yeah, it is... And it's all the way inside you..."
    j "Ahh..."
    i "And now... let yourself go..."
    i "I wanna see you screaming with pleasure..."
    scene jisa with Dissolve(1.5)
    i "Yeah..." with dis
    j "Ahh... ahhh..."
    me "Oh Judie... You're so fucking tight..."
    play music2 "bedcreak.ogg" fadein 1
    scene jisaa with dis
    pause
    i "Yeah... fuck her... fuck her harder..." with dissolve
    me "Ohh..."
    j "Ahhh... ahhh... ahhhh..." with dissolve
    j "Yes..."
    scene jissa with dis
    j "Aahh... ahhh..." with dissolve
    i "Mmmmm..."
    stop music2 fadeout 1.5
    play music3 "bedcreak2.ogg" fadein 1.5
    scene jifa with Dissolve(1.5)
    j "(Panting) AAAHH... AHHH... AHH... YEAH..." with dissolve
    i "*Sucking your balls*"
    me "O-oh god... My babes..."
    me "Oh my god..."
    scene jiffa with Dissolve(1.5)
    j "(Panting) AAAHH... Ahhh... YES..." with dissolve
    j "(Panting) I-iris! W-what are you doing... Ahh... I can feel your tongue..."
    me "O-oh god... My babes..."
    me "Ahh..."
    menu:
        with dissolve
        "Finish with Judie":
            stop music3 fadeout 2
            scene jisex a80 with Dissolve(2)
            pause
            j "(Panting) Ahhh... ahh... ahh..." with dis
            j "(Panting) Oh my god..."
            j "(Panting) T-that was intense..."
            j "(Panting) I'm sweating like crazy..."
            i "You're a pro, babe..."
            me "Can you hold on one last time, Judie?"
            j "(Panting) Yeah... Fuck me like there's no tomorrow, bro..."
            j "(Panting) I wanna come again... and again... and again..."
            if inc:
                me "You're the best little sister I could have ever asked for..."
            else:
                me "You're the best..."
            me "Get ready..."
            j "Fuck me..."
            play music3 "bedcreak3.ogg" fadein 2
            scene jica with Dissolve(2)
            j "(Squealing) ARGHHHH!" with dis
            j "(Squealing) A-a-A-A-a-A-a-a-a-a-ahhhh..."
            j "(Squealing) J-jes-sus c-christ..."
            me "FUCK, JUDIE..."
            j "Ahh... ah... ahhh..."
            j "I c-can't t-take i-it a-a-anymore..."
            pause
            menu:
                with dissolve
                "Cum inside":
                    $ vpunch2 = Move((0, 20), (0, -20), .10, bounce=True, repeat=True, delay=.875)
                    play sound "cream.mp3"
                    stop music3 fadeout 1.5
                    scene jisex a81
                    me "AAAaaaahhh..." with vpunch2
                    j "AaAaaahhh..."
                    j "(Breathing very heavily) Oh my god..."
                "Cum in her mouth":
                    stop music3 fadeout 1.5
                    scene jisex a82
                    me "Aaahhh... come here..." with dis
                    j "Mmmm..."
                    scene jisex a83
                    me "Yeah... take it all, Judie..."
                    j "Mmmm..."
                    scene jisex a84 with dis
                    scene jisex a83 with dis
                    scene jisex a84 with dis
                    scene jisex a85
                    me "AAAaaaahhh..." with hpunch
                    j "(Choking) MMm!" with hpunch
                    scene jisex a86
                    j "Mmmmmmm..." with dis
        "Finish with Iris":
            stop music3 fadeout 2
            scene jisex b80 with Dissolve(2)
            pause
            j "(Panting) Ahhh... Haha..." with dis
            j "(Panting) Damn, girl..."
            j "(Panting) T-that was intense..."
            j "(Panting) I'm sweating like crazy..."
            i "You're a pro, babe..."
            j "(Panting) I can't even last for one more second..."
            me "Can you hold on one last time, Iris?"
            i "Ahhh... Yeah... I think I can..."
            if inc:
                i "Fuck me like there's no tomorrow, cousin..."
            else:
                i "Fuck me like there's no tomorrow, [me]..."
            i "I wanna come again..."
            if inc:
                me "You're the best cousin we could have ever asked for..."
            else:
                me "You're the best..."
            j "Yeah, she is..."
            me "Get ready..."
            i "Fuck me..."
            play music3 "bedcreak3.ogg" fadein 2
            scene jicca with Dissolve(2)
            i "(Squealing) ARGHHHH!" with dis
            i "(Squealing) A-a-A-A-a-A-a-a-a-a-ahhhh..."
            i "(Squealing) J-jes-sus c-christ..."
            me "FUCK, IRIS..."
            i "Ahh... ah... ahhh..."
            i "I c-can't t-take i-it a-a-anymore..."
            pause
            menu:
                with dissolve
                "Cum inside":
                    $ vpunch2 = Move((0, 20), (0, -20), .10, bounce=True, repeat=True, delay=.875)
                    play sound "cream.mp3"
                    stop music3 fadeout 1.5
                    scene jisex b81
                    me "AAAaaaahhh..." with vpunch2
                    i "AaAaaahhh..."
                    i "(Breathing very heavily) Oh my god..."
                "Cum in her mouth":
                    stop music3 fadeout 1.5
                    scene jisex b82
                    me "Aaahhh... come here..." with dis
                    i "Mmmm..."
                    scene jisex b83
                    me "Yeah... take it all, Iris..."
                    i "Mmmm..."
                    scene jisex b84 with dis
                    scene jisex b83 with dis
                    scene jisex b84 with dis
                    scene jisex b85
                    me "AAAaaaahhh..." with hpunch
                    i "(Choking) MMm!" with hpunch
                    scene jisex b86
                    i "Mmmmmmm..." with dis
    scene jisex 87 with Dissolve(1.5)
    play sound "fall2.ogg"
    me "(Lying back on the bed) Oh my fucking god..." with dis
    me "That was..."
    me "Wow..."
    scene jisex 88
    me "You girls are insatiable..." with dis
    scene jisex 89
    i "That was fucking amazing..." with dis
    i "You and Judie just made my most forbidden fantasy come true..."
    i "God, I don't think I'll be able to walk tomorrow..."
    i "Good night, [me]..."
    me "Good night, Iris..."
    scene jisex 90
    j "That was even better than the first time, bro..." with dis
    j "My whole body is burning, inside and outside, but... it was worth it..."
    j "I love you, bro." with dissolve
    me "I love you too, Judie." with dissolve
    me "Good night..."
    scene jisex 91 with Dissolve(1.5)
    pause
    me "(Oh... my... god...)" with dis
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene gallerybackground4
    call screen gallery4 with Dissolve(1)



label gaikomotel:
    stop music
    stop music2
    $ renpy.music.set_volume(0.3, channel='music3')
    play music3 "motel.mp3" fadein 6
    scene motel 55
    ai "(Why is he still covering my mouth?)" with dissolve
    ai "(It's not like I was about to start screaming if he wasn't...)"
    ai "(If I wanted, I could get rid of him easily.)"
    ai "(Although... he's quite strong, not gonna lie.)"
    ai "(Maybe it wouldn't be so easy...)"
    ai "(He's got... strong arms.)"
    ai ". . ."
    ai "(W-why is this whole thing turning me on?)"
    ai "(What the fuck is wrong with you, Aiko?)"
    scene motel 58
    dea2 "Well, this is a closed deal!"
    dea2 "Do you want anything else?"
    dea "Nah, I'm good."
    dea2 "Then let's go get a beer! They don't have shit in this motel, but there's a bar a couple of miles up ahead."
    dea "Sweet! Let's go."
    play sound "door3.ogg"
    scene motel 59 with Dissolve(1.5)
    pause
    me "(Whispering) O-ok... They're gone." with dissolve
    me "They were just some small-time dealers..."
    me "No need to worry about them..."
    ai "Mm-hm..."
    scene motel 60b
    me "Oh shit, sorry Aiko. Are you ok?" with dissolve
    ai "(Catching a breath) Ahh..."
    ai "Yeah, I'm fine, thank you..."
    scene motel 62 with Dissolve(1.5)
    play sound "couch.mp3"
    me "(Sitting on the bed) Damn!" with dissolve
    me "We always end up in trouble, don't we?"
    scene motel 61
    ai "Haha, yeah, you do seem to have a bit of a knack at being in the wrong place at the wrong time."
    scene motel 62
    me "Good thing I was here to protect you."
    scene motel 61
    ai "Hahaha, what? Okay, that was funny!"
    ai "Protect me? From those wimps?!"
    ai "I could have handled this myself, thank you."
    me "Hmm... I don't know, you seemed pretty defenseless back there..."
    ai "Well, that's because I didn’t want to break your illusion of being the alpha male."
    me "Nah... You know I could beat you in a fight, you told me yourself I was a great fighter when we were in Japan, in the dojo!"
    ai "Haha, we both know I held myself back!"
    ai "In a real training, you wouldn't last a minute."
    me "Oh... you think so...?"
    me "You wanna bet on that?"
    scene motel 64
    ai "Haha, I know what kind of \"training\" you're thinking about..." with dis
    ai "...and let me assure you: you wouldn't last a minute."
    me "I get the feeling you keep underestimating me..."
    me "Either that or you're afraid of losing..."
    ai "Hahaha... So that's how it is, huh?"
    ai "You really want to prove you can stand an intense training session, don't you?"
    me "Oh yes... I’ve been looking forward to it since the first kick you gave me..."
    ai "Alright, tough guy..."
    ai "Lie on the bed and take off your clothes..."
    ai "Let's see what you got..."
    play sound "takeoff.ogg"
    scene motel 65 with Dissolve(2)
    ai "Are you sure you want to do this? It’s your last chance to back out." with dissolve
    me "Oh, I assure you, nothing in the world would make me change my mind..."
    ai "Okay then..."
    play sound "couch.mp3"
    scene motel 66 with Dissolve(1.5)
    me "So... you used to do this kind of training often back in Japan?" with dissolve
    scene motel 67
    ai "(Undoing her shirt) Oh, no, not really..." with dis
    ai "We were trained in various disciplines, 8 martial arts, 5 types of bladed weapons... and we were told that we should use all our resources in a life or death situation."
    me "Interesting..."
    scene motel 68
    ai "But well, both the academy and the dojo were exclusively for girls, so... we could never put it into practice..." with dis
    me "Very interesting..."
    scene motel 69
    ai "I've always been a very reserved person, but..." with dis
    ai "You came, opened my eyes, and helped me without expecting anything in return..."
    ai "I can't help being grateful..."
    scene motel 70
    me "Oh god, Aiko..." with dis
    me "You're perfect..."
    me "I need you to be mine..."
    scene motel 72 with dis
    ai "Ah, ah, ah... what do you mean \"mine\"?" with dissolve
    ai "I'm the one in charge here, haha."
    scene motel 71
    me "Oh, really?"
    scene motel 72
    ai "Of course!"
    ai "You're used to ruling the roost, aren't you?"
    scene motel 71
    me "Well, I wouldn't say that..."
    scene motel 72
    ai "Can I ask you a question?"
    scene motel 71
    me "As many as you want..."
    scene motel 72
    ai "But you have to tell me the truth!"
    scene motel 71
    me "Always."
    scene motel 72
    ai "Ok..."
    ai "Last night... Before we went to the mansion..."
    ai "You fucked Judie and Iris in your room, didn't you?"
    scene motel 71
    me "W-what?"
    me "Um..."
    me "Erm..." with dis
    me "Well, it wasn't planned, but..."
    scene motel 73
    ai "HAH! I knew it..."
    ai "I knew it the moment I saw their faces the next morning..."
    ai "The same face Lauren had after the public baths..."
    scene motel 71
    me "You're definitely a voyeur, Aiko..."
    me "You really enjoyed watching us that day, didn't you?"
    scene motel 73
    ai "Maybe..."
    ai "I'm not gonna lie, she... seemed to be having a great time."
    ai "And I was curious..."
    ai "You seemed so... vigorous, so... dominant..."
    scene motel 71
    me "Well, I can't help it..."
    play sound "couch.mp3"
    scene motel 74 with dis
    ai "(Getting up) Well, that won't happen this time, though..." with dissolve
    me "Oh my god..."
    ai "I'm gonna make you cum touching you only with my foot."
    ai "Maybe this way you’ll realize how weak you really are."
    me "Oh Jesus..."
    ai "You're hard as a rock, huh?"
    scene motel 75
    me "How could I not be..."
    me "You're driving me insane, Aiko..."
    ai "Huh..."
    ai "This will be a lesson you'll never forget..."
    $ renpy.music.set_volume(0.5, channel='music2')
    play music2 "foot7.ogg"
    scene foot1 with Dissolve(1.5)
    me "O-oh my god..." with dis
    ai "Is everything ok down there, [me]?"
    me "Yes..."
    me "You have very skilful feet..."
    ai "Of course I do..."
    me "Ahh..."
    me "Y-you're having fun, huh?"
    ai "Oh yes, you don't know how much..."
    ai "I've been waiting for this moment..."
    ai "Your cock feels... big... and warm..."
    me "Ah..."
    ai "Time to shift to second gear..."
    play music2 "foot2.ogg"
    scene foot2 with dis
    me "Ohhh yes..." with dissolve
    me "Keep going Aiko..."
    ai "Yeah, this is what you were saying to Lauren that day in those baths..."
    ai "Keep going..."
    ai "To be honest, I haven't stopped thinking about that since then..."
    me "You're a naughty girl, Aiko..."
    ai "Haha..."
    ai "Perhaps..."
    pause
    play music2 "foot4.ogg"
    scene foot3 with dis
    me "O-o-oh fuck..." with dissolve
    me "Aiko..."
    ai "All good?"
    ai "You need a break?"
    me "N-not at all..."
    me "I love seeing your tits bouncing from here..."
    me "They're perfect..."
    me "I could spend the whole day like this..."
    stop music2 fadeout 1
    play sound "couch.mp3"
    scene motel 76 with dis
    ai "You're talking too much, you know?" with dissolve
    me "Yeah, I usually do."
    ai "Well, then..."
    ai "Looks like I'm gonna have to try a bit harder..."
    me "Oh, I thought you were gonna give up already..."
    ai "Haha... oh not at all..."
    ai "The training just started..."
    scene motel 77 with Dissolve(1.5)
    pause
    ai "Good view?" with dissolve
    me "Oh god Aiko, show me that ass of yours..."
    ai "Do you want to see it?"
    me "Yes..."
    play sound "clothes.ogg"
    scene motel 78 with Dissolve(2)
    me "Oh my god..." with dissolve
    ai "...do you want to touch it?"
    me "Oh fuck yes, I do..."
    ai "...do you want to fuck me?"
    me "Oh my fucking god, I'm gonna fuck you so hard, I'm gonna split you in half..."
    play sound "couch.mp3"
    scene motel 79
    ai "Ah! That's where you're wrong!" with dis
    me "Whoa!"
    ai "You seem to have forgotten this is your training!"
    ai "If anything, I am the one who's gonna fuck you..."
    ai "So..."
    scene motel 80
    ai "Bring that big cock of yours, tough boy..." with dis
    ai "And show me what you're capable of..."
    scene motel 81
    me "(Oh my god, I'm finally gonna fuck Aiko...)" with dis
    ai "Ah..."
    play soundlow "cream.mp3"
    scene motel 82 with Dissolve(1.4)
    ai "AaaAaahh..." with dissolve
    me "O-o-oooh god..."
    $ renpy.music.set_volume(0.6, channel='music2')
    play music2 "pile1.ogg" fadein 1.5
    scene pile1 with Dissolve(1.5)
    ai "Aaaaaahhh..." with dissolve
    ai "Oh Jesus..."
    me "O-oh god, Aiko..."
    me "You're wet as fuck..."
    me "For just a training session, I can tell you were looking forward to this..."
    ai "AAAhh..."
    ai "Oh my god..."
    ai "This feels even better than I thought..."
    ai "N-not even close to w-when I touch myself..."
    ai "(Squealing) Aaahh..."
    me "Y-you ok, Aiko? If you want we can stop..."
    ai "S-shut up!"
    ai "Y-you'll see now..."
    play music2 "pile2.ogg"
    scene pile2 with dis
    ai "AAAaaaaahhhh..." with dissolve
    me "O-ohhh yeah..."
    ai "(Panting) I..."
    ai "(Panting) I d-don't need to stop..."
    ai "(Panting) I c-can... continue..."
    ai "(Panting) A-as long as I w-want..."
    ai "(Panting) I..."
    ai "(Squealing) Aaaaaaahhh..."
    ai "YEAH..."
    ai "O-OH MY GOD!"
    stop music2 fadeout .7
    scene motel 82
    ai "AAAAHH..." with hpunch
    ai "Aaaaahh..." with hpunch
    play sound "couch.mp3"
    scene motel 83
    ai "(Falling over you) O-oh god..." with dis
    me "Oh damn..."
    scene motel 84
    ai "Jesus..." with dis
    ai "That was..."
    ai "Wow..."
    me "Did you come already?"
    ai ". . ."
    me "Aiko?"
    ai "Y-yeah... I did..."
    me "Haha, that's good, don't be ashamed!"
    ai "I know..."
    ai "It's just..."
    ai "Holy shit, I couldn't resist any longer..."
    ai "I've been waiting for this moment to come for so long that..."
    ai "Fuck, I'm exhausted..."
    me "Don't worry, baby girl..."
    scene motel 85
    me "(Picking her up) I guess it's my turn to take the lead..." with dis
    ai "W-what?!"
    me "I have a lot of energy left..."
    me "Just relax and enjoy..."
    scene motel 86
    ai "O-ok..." with dis
    me "You wanna come again?"
    ai "Y..."
    ai "Yes..."
    me "So... you wanna be fucked now?"
    ai ". . ."
    ai "Yes..."
    me "What? I didn't hear you..."
    ai ". . ."
    ai "I wanna be fucked..."
    ai "I want you to fuck me..."
    scene motel 87
    me "Good girl..." with dis
    scene motel 88 with dis
    pause
    scene motel 89
    ai "Ahh..." with dis
    scene motel 90
    ai "Aaaaaahhh..." with dis
    scene motel 91
    ai "AAAAAAAAAAaaaahh..." with dis
    ai "Oh fuck, [me]..."
    ai "It's huge..."
    $ renpy.music.set_volume(0.35, channel='music2')
    play music2 "pile3.ogg" fadein 1.5
    scene pile3 with Dissolve(1.5)
    ai "Ahhh..." with dissolve
    ai "Aaaahhh..."
    ai "Oh my god [me]..."
    me "Oh Aiko..."
    ai "T-this is incredible..."
    me "Your pussy feels amazing..."
    ai "Ahhh..."
    ai "Fuck me..."
    ai "Fuck me, [me]..."
    ai "Fuck me harder..."
    ai "Break me..."
    me "Alright, ninja girl..."
    play music2 "pile4.ogg"
    scene pile4 with dis
    ai "Ahhhh..." with dissolve
    ai "Y-yeah..."
    ai "Don't stop..."
    ai "Keep fucking me..."
    scene pile5 with dis
    me "(Oh my fucking god...)" with dissolve
    me "(I can't believe how good her pussy feels...)"
    me "(She's so wet, but also so tight...)"
    ai "Ahhh..."
    ai "O-oh my god [me], your dick is too big..."
    ai "Y-you're going to tear me apart..."
    ai "Ahhh... ahh..."
    me "Wasn't this what you wanted?"
    ai "(Biting her lip) MMMMmm..."
    ai "Y-yes..."
    scene pile6 with dis
    ai "Ahhh..." with dissolve
    ai "AAaaahh..."
    ai "Y-you're so deep inside me..."
    me "I know..."
    ai "Ahhh... fuck..."
    ai "We should have done this long ago..."
    ai "T-the first day we met..."
    me "We still have plenty of time..."
    ai "Ahhh..."
    scene pile4 with dis
    ai "Ahhhh..." with dissolve
    ai "Faster..."
    me "Ahhh... F-faster?"
    ai "Y-yeah...."
    play music2 "pile5.ogg"
    scene pile7 with dis
    ai "A-AHH... AHH... AHH... AH..." with dissolve
    me "A-a-ahhh..."
    me "O-oh my god Aiko..."
    ai "AAAHH..."
    ai "AHHHHHHH..."
    ai "I... I'm c-c-coming a-again..."
    me "Ahhh... mee too, babe..."
    me "Y-you've taken me to the limit..."
    ai "AHHHH..."
    pause
    menu:
        with dissolve
        "Cum inside":
            stop music2
            scene motel 92
            play sound "cum1.ogg"
            me "(Pulling her hair) Ahhh..." with hpunch
            play sound2 "cum2.ogg"
            play sound3 "cum1.ogg"
            scene motel 92b
            me "AAAH..." with hpunch
            play sound2 "cum1.ogg"
            scene motel 92c
            me "Aaaaahhh..." with hpunch
            scene motel 92d
            ai "Ahhh..." with Dissolve(1.3)
            me "Oh my fucking god..."
            ai "Ahh... ah.... ah..."
            ai "Jesus, you filled me up..."
            me "S-sorry..."
            ai "No..."
            ai "That's... okay..."
            ai "I love how it feels..."
        "Cum outside":
            stop music2
            scene motel 93
            play sound "cum1.ogg"
            me "(Pulling her hair) Ahhh..." with hpunch
            play sound2 "cum1.ogg"
            me "Ahhh..." with hpunch
            ai "Mmmmm..."
            scene motel 93b
            ai "Ahhh..." with Dissolve(1.3)
            me "Oh my fucking god..."
            ai "Ahh... ah.... ah..."
            ai "Jesus, you covered me in cum..."
            me "S-sorry..."
            ai "No..."
            ai "That's... okay... I can clean it..."
            ai "And I like how it feels..."
    play sound "fall2.ogg"
    scene motel 94 with Dissolve(1.5)
    ai "Wow..." with dissolve
    me "Jesus Christ!"
    me "I can't feel my arms..."
    me "I wasn't expecting you to last that long the second time..."
    ai "That was..."
    ai "The best feeling I've ever felt in my entire life..."
    me "Yeah, it was crazy..."
    ai "It was amazing..."
    ai "(God, we have to repeat this again another day...)"
    scene motel 95
    ai "(Maybe I could try to get Lauren to join us...)" with dissolve
    ai "(I'm sure they'd both love it...)"
    ai "(If this was good, imagine that...)"
    me "We should go back to the van..."
    me "We're late..."
    me "Don't even think about telling anything to Lauren or Judie..."
    ai "Yeah, of course..."
    ai "Let's go..."
    $ renpy.music.set_volume(0.99, channel='music2')
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene gallerybackground4
    call screen gallery4 with dis


label gcarlastore:
    stop music
    stop music2
    stop music3
    play sound "curtain.mp3"
    $ renpy.music.set_volume(0.02, channel='music3')
    play music3 "store.ogg" fadein 6
    scene store 58b
    me "And besides, if someone found me here, why would it be weird?" with dis
    me "They'd just think I'm your boyfriend, and I'm helping you picking clothes."
    scene store 59
    c "Haha, thank you for the compliment, but I'm too old for them to think that."
    scene store 58b
    if inc:
        me "Come on Mom!"
    else:
        me "Come on Carla!"
    me "Don't you see yourself?!"
    me "You have the best body I've ever seen! Women your age would kill to have this."
    me "I still wonder if you made a deal with the devil..."
    scene store 59
    c "Haha, no, not that I recall."
    c "Only working out regularly and eating healthy!"
    scene store 58b
    me "And... well, if you were looking for my opinion, yeah, that lingerie is so fucking hot..."
    scene store 60
    c "Thanks!" with dis
    c "The whole set was on sale!"
    c "Wait, there's one last piece. I'll show you."
    scene store 61
    c "What do you think?" with dis
    me "Whoa... Very nice. You look too hot..."
    scene store 62
    c "Thank you sweetie, I think I'm gonna buy it." with dis
    me "Yeah, you should!"
    scene store 63 with dis
    me "(Jeez, she's making me too damn horny...)" with dissolve
    me "(I wonder if I should try to make a move...)"
    me "(We haven't talked much about what happened in Japan since we came back.)"
    if pregnancy:
        me "(And she's been kinda evasive since she went to that check-up at the hospital...)"
    else:
        me "(I mean, not that she said she regrets it... she just avoided talking about it.)"
    scene store 64
    c "Okay then, I'll take it!" with dis
    c "I'm gonna go pay for it."
    scene store 65
    me "*Grabbing her waist*" with dis
    scene store 66
    c "[me]! What are you doing?"
    me "I don't know!"
    me "I can't control my hands!"
    me "I was watching you looking in the mirror, and suddenly my body started moving by itself! I can't control it anymore!"
    c "Hahaha, very funny."
    c "Come on, don't be silly!"
    if inc:
        me "Seriously though, I've missed you so much, Mom..."
    else:
        me "Seriously though, I've missed you so much, Carla..."
    scene store 67
    c "(Pushing you away) Okay, okay, I..." with dis
    c "I've missed you too, but let's not get crazy..."
    scene store 68
    me "Really? Have you missed me? I thought you were avoiding me..."
    me "Then... you don't regret what happened in the hot springs?"
    scene store 67
    c "Of course not... That was..."
    c "Incredible..."
    c "I haven't stopped thinking about that moment since that day..."
    scene store 68
    me "Well, we could have that moment again..."
    scene store 67
    c "Um..."
    c "Maybe someday."
    scene store 68
    me "And why not now?"
    me "I need it now..."
    scene store 67
    c "Are you nuts?"
    c "This is a public place! Don't talk nonsense..."
    scene store 68
    me "Well, the music is quite loud out there, and no one knows we're here..."
    scene store 67
    c "Another client could come in any minute..."
    scene store 68
    me "Well, that only makes it more exciting..."
    scene store 67
    c "Haha, stop it! We're not gonna fuck in a dressing room! We're not animals!"
    scene store 69
    me "Well..." with dis
    if inc:
        me "At least let me pleasure you as you deserve, Mom..."
    else:
        me "At least let me pleasure you as you deserve, Carla..."
    scene store 70
    me "I've missed the taste of your pussy so much..." with dis
    c "Um... S-sweetie... We shouldn't..."
    scene store 71 with dis
    pause
    scene store 72
    c "Ahh..." with dis
    scene store1 with Dissolve(1.5)
    c "Ohhh..." with dissolve
    c "Oh my god [me]..."
    c "I had forgotten how good you are at this..."
    if inc:
        me "(God, Mom's pussy tastes amazing...)"
    else:
        me "(God, Carla's pussy tastes amazing...)"
    me "(She's always so wet...)"
    c "Ahh..."
    c "Ohh yeah..."
    scene store 73
    c "(Undoing her bra) Oh, fuck..." with dis
    c "(Undoing her bra) Keep going baby..."
    scene store 74
    c "Ahh..." with dis
    scene store2 with dis
    c "Ahhh..." with dissolve
    c "O-oh my god!"
    c "Y-yeah!!"
    me "(God, she's spasming!)"
    me "(I knew she only needed a little warm up...)"
    me "(Once she's in the mood, she's always so eager...)"
    c "Oh my fucking god, baby..."
    c "How can you do that..."
    c "You sure know how to use your tongue..."
    c "Jesus..."
    pause
    c "Ahh..." with dis
    c "I..."
    c "I'm so horny..."
    c "Ahh..."
    c "I need you to fuck me..."
    c "I need to feel your big cock in my insides once more..."
    play sound "fall2.ogg"
    scene store 75
    me "*Putting her on top of the bench*" with dis
    me "Thank god you said that..."
    me "I couldn't hold it anymore..."
    me "We should get a little more comfortable..."
    play sound "clothes.ogg"
    scene store 77 with Dissolve(1.5)
    me "That's better..." with dissolve
    me "What were you saying?"
    c "That I need you to fuck me..."
    me "I thought you said we weren't animals..."
    c "Well... Maybe we are..."
    c "Maybe we should behave like animals..."
    me "Oh yeah..."
    scene store 78
    if inc:
        me "God, I love these juicy breasts of yours, Mom..." with dis
    else:
        me "God, I love these juicy breasts of yours, Carla..." with dis
    c "Ahh..."
    me "So big, so soft..."
    c "Mmmm..."
    scene store 77
    c "The're all yours..." with dis
    c "Only yours..."
    me "Oh yeah..."
    me "Come here..."
    $ renpy.music.set_volume(0.5, channel='music2')
    play music2 "carla1.mp3" fadein 1.5
    scene store3 with Dissolve(1.5)
    me "Ohh... yeah..." with dissolve
    c "Aahhh..."
    me "Oh my god..."
    me "You have no idea how much I've missed this..."
    c "Me too, my baby..."
    c "Mmmmmm..."
    c "I can't continue deluding myself anymore..."
    c "You complete me..."
    me "You too..."
    c "Now fuck your mommy hard..."
    c "Harder than ever..."
    me "Oh yes..."
    play music2 "carla2.mp3"
    scene store4 with dis
    c "AAAaahh... Y-yeah..." with dis
    me "Oh my god..."
    c "AHHH... AHHH..."
    me "If you s-scream so much we're gonna get caught..."
    c "I c-can't help it..."
    c "Ahhh..."
    stop music2
    scene cssss 13
    c "Aaaaahhhhh...." with hpunch
    play sound "cream2.mp3"
    scene store 79
    c "Oh Jesus Christ..." with dis
    me "You ok?"
    c "Y-yeah..."
    c "I just need a second..."
    c "God, I'm all sweaty..."
    c "I'm gonna have to buy all these clothes..."
    scene store 80
    me "Well, you were gonna do it anyway, weren't you?" with dis
    c "(Undoing her hair) Yeah, I guess..."
    c "(Undoing her hair) Maybe not the stockings..."
    c "(Undoing her hair) Well, it doesn't matter..."
    scene store 81
    c "(Pulling her hair back) Ahh..." with dis
    c "Much better..."
    scene store 82
    c "I have to get a haircut soon..." with dis
    c "My hair's too long..."
    me "Really? I think you're even hotter with your hair down like that."
    scene store 83
    c "Haha... Thank you honey..." with dissolve
    c "You always know what to say..."
    c "Would you still love me with messy hair and no makeup?"
    me "I'd love you more, if that's even possible."
    c "Haha..."
    c "Come here, big boy..."
    if inc:
        c "Show your mommy what you can do..."
    else:
        c "Show me what you can do..."
    play sound "fall2.ogg"
    scene store 84 with dis
    c "Ahh..." with dissolve
    me "Are you ready for a second round?"
    c "Yeah..."
    c "Don't hold back..."
    me "I won't..."
    play music2 "carla3.mp3" fadein 1.5
    scene store5 with Dissolve(1.5)
    c "Aaaaahh..." with dissolve
    c "Ahhh..."
    c "O-oh my god..."
    c "H-how is it possible..."
    c "Your father never could please me like this..."
    c "Neither he nor anyone else..."
    c "Aaah..."
    scene store6 with dis
    me "Aah..." with dissolve
    me "A woman like you deserves to be pleased properly..."
    c "Aaaaah..."
    c "Jesus Christ..."
    c "You're huge..."
    c "Where did you even get that from..."
    c "Ahhh..."
    c "This is just too good..."
    c "Oh god..."
    pause
    scene store5 with dis
    c "Ahhh..." with dissolve
    c "Oh Jesus, you're insatiable..."
    me "Ahh... You like it?"
    c "Yeah..."
    c "Keep fucking me with that big cock of yours baby..."
    c "Ahhh..."
    stop music2
    $ renpy.music.set_volume(0.4, channel='music3')
    play sound "toctoc.ogg"
    scene store 84b
    sg "Hello?"
    sg "You still there, ma'am?"
    $ renpy.music.set_volume(0.02, channel='music3')
    scene cssssssss 11
    c "(Whispering) O-oh my god! It's the shop girl!"
    c "(Whispering) Oh god, how embarrassing..."
    $ renpy.music.set_volume(0.4, channel='music3')
    scene store 84b
    sg "Ma'am?"
    $ renpy.music.set_volume(0.02, channel='music3')
    scene cssssssss 11
    c "Um... Y-yeah! I'm here!"
    c "It's just that... I was trying on everything a couple of times!"
    sg "Oh, I see, no problem!"
    $ renpy.music.set_volume(0.99, channel='music2')
    play music2 "carla6.ogg" fadein 2
    scene store7 with Dissolve(2)
    c "(Holding a squeak) [me]!" with dissolve
    me "Oh god..."
    c "W-what are you d-ddoing..."
    c "S-stop!!"
    stop music2
    $ renpy.music.set_volume(0.4, channel='music3')
    scene store 84b
    sg "Ma'am?"
    play music2 "carla6.ogg"
    $ renpy.music.set_volume(0.02, channel='music3')
    scene store9
    c "W-WHAT?"
    stop music2
    $ renpy.music.set_volume(0.4, channel='music3')
    scene store 84b
    sg "Do you need help with anything? I can come in to help you, if you want. I know those buttons can be tricky."
    play music2 "carla6.ogg"
    $ renpy.music.set_volume(0.02, channel='music3')
    scene store9
    c "WHAT? NO! I..."
    c "Ahh..."
    c "I CAN HANDLE IT, THANK YOU."
    stop music2
    $ renpy.music.set_volume(0.4, channel='music3')
    scene store 84b
    sg "Alright, then I'll go. Do you need any other size? I could bring it to you."
    play music2 "carla6.ogg"
    $ renpy.music.set_volume(0.02, channel='music3')
    scene store8
    c "Ahhh..."
    c "Oh god..."
    c "N-no, thank you!"
    c "Everything fits right in..."
    stop music2
    $ renpy.music.set_volume(0.4, channel='music3')
    scene store 84b
    sg "What? I'm sorry, I can't hear you very well."
    play music2 "carla6.ogg"
    $ renpy.music.set_volume(0.02, channel='music3')
    scene store9
    c "I S-SAID NO, T-THANK YOU!"
    c "Ahh... I'M GOOD!"
    sg "Alright! I'll be right out here if you need anything!"
    c "O-okay..."
    scene store7 with dis
    c "AAAAAaaaahh..." with dissolve
    c "Oh my f-fucking god, I thought she'd never leave..."
    if inc:
        me "Ahhh... Oh my fucking god Mom..."
    else:
        me "Ahhh... Oh my fucking god Carla..."
    scene store8 with dis
    c "AAahh... ahhh... ahh..." with dissolve
    scene store9 with dis
    c "Aaaahhh... O-oh my god..." with dissolve
    me "O-oh my fucking god..." with dissolve
    me "I'm about to cum..."
    c "Aaaaghghh..."
    c "I d-don't feel my legs..."
    menu:
        with dissolve
        "Cum inside":
            stop music2
            play sound "cum1.ogg"
            scene store 85
            me "(Unloading inside her) AAAARGH..." with hpunch
            play sound2 "cum1.ogg"
            me "(Unloading inside her) Ahhhhhhhh..." with hpunch
            play sound3 "cum1.ogg"
            c "AAAahhhhhhhhhh..." with hpunch
            play soundlow "cream2.mp3"
            scene store 86 with Dissolve(1.2)
            me "Oh Jesus..." with dis
            c "(Panting)"
            if inc:
                me "(I just came inside Mom...)"
            else:
                me "(I just came inside Carla...)"
            me "(Again...)"
            me "That was..."
            c "...amazing..."
        "Cum over her":
            stop music2
            play sound "cum1.ogg"
            scene store 87
            me "AAAARGH..." with hpunch
            play sound2 "cum1.ogg"
            me "Ahhhhhhhh..." with hpunch
            play sound3 "cum1.ogg"
            c "AAAahhhhhhhhhh..." with hpunch
            me "Oh Jesus..."
            if inc:
                me "(I just covered Mom in cum...)"
            else:
                me "(I just covered Carla in cum...)"
            c "(Panting)"
            me "That was..."
            c "...amazing..."
    scene store 88 with Dissolve(1.7)
    c "Oh my fucking god..." with dis
    c "You're... a beast..."
    if inc:
        me "You're no less, Mom..."
    else:
        me "You're no less, Mom..."
        c "Haha, don't call me that!"
        me "When we met, you told me I could..."
        c "Yeah, but... I wasn't expecting we would be fucking when you did it..."
    scene store 89 with Dissolve(1.6)
    c "Oh, damn..." with dis
    $ renpy.music.set_volume(0.3, channel='music3')
    $ renpy.music.set_volume(0.99, channel='music2')
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene gallerybackground5
    call screen gallery5 with dis


label gjasminelauren:
    stop music
    stop music2
    stop music3
    $ renpy.music.set_volume(0.12, channel='music3')
    play sound "dooropen.ogg"
    play music3 "bath2.ogg" fadein 1
    scene plug 37
    me "(I hear a running tap...)" with dis
    play sound "doorclose.ogg"
    scene plug 38 with Dissolve(1.5)
    me "(Hm?)" with dissolve
    y "I thought you weren't coming..."
    scene plu 1 with dis
    pause
    me "Oh mama..." with dis
    y "All that truth-or-dare stuff was such a turn-on, don't you think?"
    me "Yeah..."
    y "Is there something you wanted? There's another bathroom across the hall, you know..."
    me "I want you..."
    scene plu 2
    y "Well, you better get out of those wet clothes then, because you're dripping on the floor."
    me "Gladly..."
    play sound "takeoff.ogg"
    scene plu 3 with Dissolve(2)
    y "Oh yes, come here..." with dis
    y "You have no idea how much I've missed your big cock..."
    scene plu 4 with dis
    y "*Touching herself*" with Dissolve(1.5)
    y "Mmm..."
    me "You know Jas, I feel like you threw this \"party\" just so you could be with me..."
    scene plu 5
    y "Haha, don't flatter yourself, honey." with dis
    y "I wasn't even sure whether to invite you or not..."
    me "Really?"
    scene plu 6
    y "Oh, yes... " with dis
    y "I was only going to invite Lauren, but I felt sorry for you..."
    me "Sure..."
    scene plu 7
    y "Mmmm..." with dis
    me "Oh my god..."
    scene plu 8 with dis
    pause
    scene plu 7
    y "Mmmmmm..." with dis
    scene plu 8
    y "*Gagging*" with dis
    scene plu 7 with dis
    pause
    scene plu 6
    y "(Breathing) Ahhh..." with dis
    scene plu 9 with dis
    y "(Getting up) Come..." with dissolve
    y "I want you to fuck me... I can't stand it any longer..."
    scene cunni 1 with Dissolve(1.5)
    me "You know, I've always wondered how a rich girl's pussy tastes..." with dissolve
    y "Haha..."
    y "Well... why don't you check it out for yourself?"
    scene cunni 2
    me "Oh... with pleasure..." with dis
    scene jascunni1 with Dissolve(1.6)
    y "Aaahh..." with dis
    y "Fuck..."
    y "D-did you know that I never let anyone do this to me before?"
    y "Ahhh..."
    y "I don't like... to feel... v-vulnerable..."
    me "(What an honor...)"
    y "Ahh..."
    scene jascunni2 with Dissolve(1.5)
    y "AAAAaahhh..." with dissolve
    y "F-FUCK!"
    y "Oh my god, [me]..."
    y "Yeah..."
    y "Ahhhh..."
    me "(I still remember when the most popular girl in school didn't even know who I was...)"
    me "(And now I'm eating her pussy...)"
    me "(Fuck yes...)"
    y "AAaaahhh..."
    pause
    scene jascun 0
    y "Ahhh... S-stop..." with dis
    y "Enough foreplay..."
    y "L-let me get up..."
    scene plu 10 with Dissolve(1.5)
    y "I need you inside me now..." with dis
    me "You have a killer body, Jas..."
    me "I guess I'm a lucky man..."
    y "Oh yeah, you are..."
    me "Bend over..."
    y "Oh... how overbearing..."
    scene plu 11
    y "I like it..." with dis
    scene plu 12 with dis
    pause
    me "(Hmm...)" with dissolve
    me "(Let's play...)"
    scene plu 11 with dis
    pause
    scene plu 13
    me "Bring that butt here, you bitch..." with dis
    y "*Chuckles*"
    y "You moron..."
    scene plu 14 with dis
    pause
    scene plu 13 with dis
    pause
    scene plu 14 with dis
    pause
    scene plu 15 with Dissolve(1.5)
    pause
    me "You're wet as fuck down here, Jasmine..." with dissolve
    y "Come on... Fuck me already... I'm going crazy..."
    me "(Let's see how she reacts...)"
    scene plu 16 with Dissolve(1.5)
    pause
    scene plu 21
    y "W-WHAT??" with hpunch
    scene plu 22
    y "Um.... What do you think you're doing?!" with dissolve
    me "Playing with some toys that I found right here."
    y "Yeah, I can see that. That's not even mine, so leave it where it was."
    scene plu 16
    me "Not yours? Whose are they?"
    y "My Mom's, I guess."
    me "So... your Mom can stand these kind of games, and you can't?"
    me "I thought you were a tough girl..."
    scene plu 22
    y "I'm tougher than she'll ever be."
    me "Then... Can you take this?"
    y "Of course I can!"
    y "Idiot..."
    scene plu 16
    me "Good girl..."
    me "I've even lubricated it so it won't hurt."
    scene plu 17 with dis
    pause
    scene plu 16 with dis
    pause
    scene plu 17 with dis
    y "Uugh..." with dissolve
    scene plu 23
    me "Did I hear a moan?"
    scene plu 22
    y "N-no! I d-didn't say anything!" with dis
    scene plu 16
    me "Ok, ok..."
    scene plu 17 with dis
    pause
    scene plu 16 with dis
    pause
    scene plu 17 with dis
    pause
    scene plu 23
    y ". . ."
    scene plu 16
    pause
    scene plu 17 with dis
    pause
    scene plu 18 with dis
    me "*Pushing the plug*" with dis
    play sound "penetration2.ogg"
    scene plu 19 with dis
    pause
    scene plu 23
    pause .5
    scene plu 24
    y "O-oh m-my g-goddd..." with dis
    me "That was a moan!"
    play sound "fall2.ogg"
    scene plu 25 with dis
    y "Holy shit..." with dis
    y "I can't stand up..."
    me "Does it feel good, though?"
    scene plu 27
    y "Ahh... It feels..." with dis
    y "Weird..."
    me "You're still getting used to it."
    y "Ahh..."
    y "I guess I can see myself getting used to it, yes..."
    scene plu 28 with dis
    me "That's my girl..." with dissolve
    me "And you haven't seen anything yet..."
    scene plu 29
    me "Are you ready?"
    y "Ahh..."
    y "Yes... I've been getting ready all night..."
    y "I can't wait anymore..."
    scene plu 30
    me "Me neither..." with dis
    scene plu 31
    y "AAAArgh..." with dis
    $ renpy.music.set_volume(0.50, channel='music2')
    play music2 "piston1.ogg" fadein 1.5
    scene jplug1 with Dissolve(1.5)
    y "O-oh my god..." with dissolve
    me "Jesus... This feels amazing..."
    me "I can feel the plug pressing my dick..."
    me "It feels so much tighter..."
    y "Y-yeah..."
    y "I c-can feel it too..."
    y "Ahh... ahhh..."
    play music2 "piston1b.ogg"
    scene jplug2 with Dissolve(1.5)
    y "AAAaARgh..." with dissolve
    y "OH MY GOD..."
    y "Y-YES!"
    y "T-this sensation...."
    y "It's as if I was being double-penetrated..."
    y "O-oh my fucking god..."
    me "Oh, Jas..."
    y "Ahhh..."
    y "Ahhhhhhh..."
    y "D-don't stop!"
    y "Keep going... Just keep going..."
    y "P-please..."
    play music2 "piston1c.ogg"
    scene jplug3 with Dissolve(1.5)
    y "Arrrgh...." with dissolve
    me "Oh y-yeah..."
    y "(Panting) A-a-a-a-a-ahh..."
    y "(Panting) I've never f-felt so filled..."
    y "(Panting) Ahh... ahh... ahhh..."
    me "Aaahh..."
    me "S-see how using the plug wasn't a bad idea?"
    y "(Panting) Ahh... ahh... Argh..."
    me "(She's beside herself...)"
    pause
    stop music2 fadeout 1.3
    scene plu 31
    y "AAaahhh..." with Dissolve(1.3)
    y "Aahhh..."
    y "I'm coming..."
    y "O-oh my god..."
    play soundlow "fall2.ogg"
    scene plu 25
    y "(Moving away) Oh god..." with dis
    y "I'm shaking like a leaf..."
    scene plu 32
    y "Now I can see why people use these things..." with dis
    y "Jesus Christ..."
    y "Can you remove it?"
    scene plu 33
    me "Of course, m'lady..." with dis
    scene plu 34
    y "Ahhh..." with dis
    y "Thanks..."
    scene plu 35
    y "Holy shit, that was incredible..." with dis
    me "It was..."
    y "I never thought I'd enjoy anal play..."
    me "I bet you'll love it even more now..."
    me "Now that you’ve already warmed up..."
    y "What?"
    play soundlow "penetration1.ogg"
    scene plu 36 with dis
    y "Grr!" with hpunch
    me "Oh.... YES..."
    scene plu 37 with dis
    pause
    y "Ahh... Fuck..." with dissolve
    y "G-goddammit, [me]..."
    y "That's way too big..."
    me "Jesus Christ... that's tight as fuck..."
    y "Arghhhhh... Do you hear me?! Y-your dick is too big!"
    y "It hurts!"
    me "You need to relax your muscles..."
    me "You're so tense..."
    scene plu 40
    y "Yeah, of course, that's easy for you to say!"
    me "If you relax, you’ll see how incredible it feels..."
    y "(Grinding her teeth) Hmmm..."
    scene plu 38 with dis
    pause
    scene plu 39 with Dissolve(1.8)
    y "AAAAAH..." with dissolve
    me "Ohhh... That's it, babe..."
    scene plu 38 with Dissolve(1.4)
    pause .07
    scene plu 39
    y "Aaahhh..." with dis
    scene plu 38 with dis
    pause .05
    scene plu 39
    y "Aaaahh...." with Dissolve(.75)
    y "O-oh my god..."
    play music2 "sex1.ogg" fadein 2
    scene jplug4 with Dissolve(2)
    y "AHH!" with dissolve
    y "OH MY GOD!"
    me "That feels tighter than any pussy..."
    y "AHH... AHH..."
    y "You fucker..."
    y "G-go easy, please..."
    me "Oh Jas... Your butt feels fucking amazing..."
    y "Aaah..."
    me "You ok?"
    y "Mmmm... Y-yes..."
    y "Aaagh..."
    y "This is... starting to feel... ahh..."
    y "Bearable..."
    me "I told you..."
    play music2 "sex2.ogg"
    scene jplug5b with dis
    y "(Screaming) ARGHHHH!" with dissolve
    y "OH MY GOD!!!"
    me "Oh Jasmine..."
    me "(I'm destroying Jasmine's butthole...)"
    me "(This is unbelievable...)"
    y "(Panting) Ahhh... ah.... ahhh..."
    y "(Panting) S-SLOW DOWN! YOU'RE GONNA BREAK ME!"
    play music2 "sex1.ogg"
    scene jplug4 with dis
    me "*Slowing down*" with dissolve
    y "Oh god..."
    y "Yeah..."
    me "Better?"
    y "Yeah..."
    y "This feels good now..."
    y "Mmmm..."
    me "Do you like being fucked in the ass, Jas?"
    y ". . ."
    y "Y-yes..."
    me "Yes?"
    y "Yeah..."
    y "Fuck me, [me]..."
    y "Keep pounding my little ass..."
    play music2 "sex2.ogg"
    scene jplug5b with Dissolve(1.5)
    y "AAHHHH..." with dissolve
    y "Aa-a-a-ahhh..."
    y "Oh my god..."
    scene analy3 with dis
    y "Oh my f-fucking god..." with dissolve
    scene jplug6b with dis
    y "AAaaahh..." with dissolve
    y "I c-can't stand t-this any l-l-longer..." with dissolve
    me "Ahh... Me neither..."
    me "I'm about to finish..."
    y "AAaahh..."
    y "C-cum inside me..."
    y "Fill me up..."
    me "Oh god..."
    stop music2 fadeout 1
    play soundlow "cum1.ogg"
    scene jppppp 2
    me "(Cumming inside her) AAH..." with hpunch
    play soundlow "cum1.ogg"
    y "AAAaahhh..." with hpunch
    play soundlow "cream.mp3"
    scene plu 41 with dis
    y "(Panting) Oh my fucking god..." with dis
    y "(Panting) I'm melting..."
    me "Oh god, Jas..."
    scene plu 42 with Dissolve(1.8)
    y "(Recovering her breath) W-what... What the fuck just happened?" with dis
    me "That was incredible..."
    y "I won't be able to sit for a week..."
    me "You seemed to enjoy it, though..."
    scene plu 43
    y "Haha... Not gonna lie." with dissolve
    y "That was... Damn, that was good..."
    me "I know, right?"
    y "I never thought I'd enjoy anal..."
    y "I guess I had to meet a perv like you."
    me "I knew you'd like it..."
    y "This is definitely not the last time we're doing this..."
    me "Oh yes... fucking yes... It won't be the last, you dirty girl..."
    y "Nice..."
    play sound "dooropen.ogg"
    scene plu 44 with Dissolve(1.5)
    l "Finally!" with hpunch
    l "There you are!"
    me "(Oh, I'd forgotten about Lauren!)"
    l "For fuck's sake, how many bathrooms does this place have?"
    l "I've been looking for..."
    scene plu 45
    y ". . ."
    scene plu 44
    l "For..."
    scene plu 46
    l "Oh my god... you really did it!" with dis
    l "I can't believe it!!"
    l "Wow, Jas... I thought you wouldn't do it..."
    me "Well, you know myself and baths are an irresistible combination..."
    scene plu 47
    l "Haha, yeah, of course..." with dissolve
    l "Maybe alcohol helped too."
    me "Oh, so you're telling me that you didn't have fun in those public baths?"
    l "I didn't say that..."
    l "You know I did..."
    l "I wish we could go back to Japan..."
    scene plu 48
    y "Alright, hold your horses, you two!"
    y "Having fun?"
    y "Japan?"
    y "Baths?"
    y "You're the girl [me] talked about when we were playing truth or dare?!! The bathhouse one?"
    y "You two have fucked?!"
    scene plu 46
    l "W-what?! W-what are you talking about?"
    l "Of course not!"
    if inc:
        l "H-he's my brother!"
    else:
        l "H-he's my step-brother!"
    scene plu 49 with Dissolve(1.5)
    y "Oh my god..." with dissolve
    y "You two had sex!"
    y "I knew it!"
    scene plu 50
    l "N-no! That's not true!"
    scene plu 49
    y "I had my suspicions, but when I saw you kissing, it became clear!"
    scene plu 50
    l "I told you that's not true!"
    l "[me]! Tell her it's not true!"
    scene plu 49
    me "Um..." with dissolve
    me "Yeah, we had sex. Twice, actually..."
    scene plu 50
    l "[me]!!!" with hpunch
    y "I knew it..."
    scene plu 51
    y "Don't be shy, Lauren!" with dis
    y "This is awesome!"
    y "You're precious and you're smokin' hot. This had to happen sooner or later..."
    scene plu 52
    y "I bet you’ve been getting horny all night..." with dis
    y "The teasing, the kisses, the pool..."
    if inc:
        y "Your brother in front of you this whole time... You must have been going crazy!"
    else:
        y "Your step-brother in front of you this whole time... You must have been going crazy!"
    y "Am I right or not?"
    scene plu 53
    l "Um... Maybe... A bit..." with dis
    y "Of course..."
    y "I bet that all you’d like to do now is take off this wet dress and have [me] fuck you right here..."
    y "Isn't it?"
    l "Um..."
    scene plu 54
    y "(Taking off Lauren's dress) Feeling his big fat cock inside of you..." with Dissolve(1.3)
    y "While you moan with pleasure..."
    me "(Oh god... )"
    y "While you beg him not to stop..."
    y "Wouldn't you like that?"
    l "Yes..."
    l "I want that..."
    scene plu 55
    y "That's normal..." with Dissolve(1.3)
    l "Ahh..."
    y "She wants you to fuck her, [me]..."
    y "What about you?"
    me "I want it so bad..."
    y "So I thought..."
    scene plu 56
    y "What do you say, honey?" with dis
    y "Should we make this one a night to remember?"
    l "Haha... Yeah, I think we should..."
    y "I'll have to stand aside, because... well, let's just say that [me] really took it out of me."
    y "Can you handle this on your own?"
    l "Yes, I think I can..."
    me "Oh yeah, my babes..."
    scene plu 57
    y "(Pushing you) Ah, ah, ah! You can't talk, [me]! It's Lauren's time to take the lead here!" with dis
    me "Whoa!"
    play sound "fall2.ogg"
    scene plu 58 with dis
    me "Ouch!" with dissolve
    y "Are you ready to screw your brother into the ground, babe?"
    l "Oh yes..."
    scene plu 59 with Dissolve(1.2)
    me "Oh Lauren..." with dissolve
    l "I'm soaked down there..."
    me "Oh, I can tell..."
    if inc:
        l "I want you to be the only one to fuck me for the rest of my life, brother..."
    else:
        l "I want you to be the only one to fuck me for the rest of my life, [me]..."
    l "Nobody’s gonna fill me up like you do..."
    me "You're mine..."
    l "I'm yours..."
    me "Bring that tight pussy of yours over here..."
    scene plu 60 with dis
    pause
    play sound "cream.mp3"
    scene plu 61 with Dissolve(1.5)
    l "AaAaaahhh..." with dis
    me "Ohhh god..."
    play music2 "piston2.ogg" fadein 1.5
    scene jplug5 with Dissolve(1.5)
    l "Ahhhhh..." with dis
    l "Yes..."
    l "Oh my god..."
    me "(Squeezing her boobs) Oh fuck yes, Lauren..."
    me "I love your boobs..."
    me "So big... So squishy..."
    me "I spent years thinking what it would be like to touch them..."
    l "Ahhh..."
    l "Y-you're doing much more than that now, aren't you?"
    me "Oh yes..."
    scene jplug6 with dis
    l "AHHH..." with dissolve
    l "Yeah... keep going..."
    l "Fuck me deeper..."
    l "Aaahh... ahh..."
    play music2 "piston2b.ogg"
    scene jplug7 with dis
    l "AAAaaaaAaahhh..." with dis
    l "Yeah..."
    l "This is amazing..."
    l "Each t-time feels better than the last..."
    pause
    scene jplug8 with dis
    me "Oh yeah..." with dissolve
    l "Ahhh..."
    l "[me]..."
    me "Ahhh... Lauren..."
    if inc:
        me "(Why does my sister's pussy always feel so good...)"
    else:
        me "(Why does her pussy always feel so good...)"
    me "(It's like we were meant to be together...)"
    play music2 "piston2c.ogg"
    scene jplug9 with Dissolve(1.5)
    pause
    y "Oh my god..." with dis
    if inc:
        y "(Looking at him nailing his sister is so fucking hot...)"
    else:
        y "(Looking at him nailing his step-sister is so fucking hot...)"
    l "*Kissing you*"
    l "Mmmmm..."
    l "MMMMmmmmhhh..."
    me "(Oh Jesus...)"
    me "(The way her tight pussy wraps around my cock...)"
    me "(It's like a drug...)"
    me "(Keep bouncing babe...)"
    l "*Frenching you*"
    l "(Moaning) Mmmmmmmm..."
    play music2 "piston2d.mp3"
    scene jplug10 with Dissolve(1.5)
    l "AAAAAAAAARGGHHHHHH..." with dissolve
    me "Oh god, Lauren..."
    me "Your pussy is fucking magic..."
    me "I can't last any longer..."
    l "(Panting) D-don't stop y-yet, please..."
    l "(Panting) J-just a few more seconds..."
    l "(Panting) Just a little more..."
    scene jplug11 with dis
    l "AAAAaaahhh..." with dissolve
    l "YEAHHH..."
    me "Aaahh... I'm gonna cum Lauren..."
    l "(Panting) Ahhh... ah.... Yes... Me too..."
    l "(Panting) Cum inside me... Give it to me..."
    me "W-what? But I..."
    l "(Panting) I w-want it..."
    l "(Panting) Give me your load..."
    me "Oh god..."
    l "(Panting) Yes... yes..."
    l "(Panting) I'm coming too..."
    stop music2 fadeout 1.5
    scene plu 62b with Dissolve(1.5)
    play sound2 "cum2.ogg"
    play sound "cum1.ogg"
    scene plu 62 with hpunch
    scene plu 62 with hpunch
    pause .1
    play sound3 "cum2.ogg"
    scene plu 62 with hpunch
    me "Ahhhhhhhh..." with dis
    l "AAaAaahhh..."
    l "Yeah..."
    if inc:
        l "Fill me up with your seed, bro..."
    else:
        l "Fill me up with your seed..."
    me "Ahh..."
    play sound "fall2.ogg"
    scene plu 63 with Dissolve(1.5)
    me "JESUS!" with dis
    l "Oh my god..."
    l "That was..."
    l "I can't even describe it..."
    l "Is it me or does it get better every time?"
    me "It does..."
    l "When I'm with you I forget about everything..."
    l "It's as if the rest of the world didn't exist..."
    me "I feel the same way, Lauren."
    l "I love you..."
    y "Awww... you're so cute!"
    scene plu 64
    l "J-jasmine!" with dissolve
    l "Oh my god, I forgot you were there!"
    y "Don't worry, I already had enough action for tonight... I was just enjoying the view."
    if inc:
        y "That was hot as fuck. The forbidden love... The Romeo and Juliet of the 21st century."
    l "Oh god, how embarrassing..."
    y "Haha, don't be ashamed honey! Come, let me get you a towel."
    l "T-thanks..."
    stop music fadeout 1
    stop music2 fadeout 1
    stop music3 fadeout 1
    scene gallerybackground5
    call screen gallery5 with dis

screen aikoeyes2:
    add "aik 69b"
screen aikoeyes1:
    add "aik 69c"
screen movie1:
    imagemap:
        ground "filmmovie1"
        hover "filmmovie1b"
        hotspot (464, 532, 200, 178) action Jump('labelmovie5') hovered [ Play ("soundlow", "button1.mp3")]
        hotspot (682, 493, 196, 189) action Jump('labelmovie2') hovered [ Play ("soundlow", "button1.mp3")]
        hotspot (880, 156, 431, 579) action Jump('labelmoviedb') hovered [ Play ("soundlow", "button1.mp3")]
screen movie2:
    imagemap:
        ground "filmmovie2"
        hover "filmmovie2b"
        hotspot (464, 532, 200, 178) action Jump('labelmovie1') hovered [ Play ("soundlow", "button1.mp3")]
        hotspot (682, 493, 196, 189) action Jump('labelmovie3') hovered [ Play ("soundlow", "button1.mp3")]
        hotspot (880, 156, 431, 579) action Jump('labelmoviejl') hovered [ Play ("soundlow", "button1.mp3")]
screen movie3:
    imagemap:
        ground "filmmovie3"
        hover "filmmovie3b"
        hotspot (464, 532, 200, 178) action Jump('labelmovie2') hovered [ Play ("soundlow", "button1.mp3")]
        hotspot (682, 493, 196, 189) action Jump('labelmovie4') hovered [ Play ("soundlow", "button1.mp3")]
        hotspot (880, 156, 431, 579) action Jump('labelmoviezs') hovered [ Play ("soundlow", "button1.mp3")]
screen movie4:
    imagemap:
        ground "filmmovie4"
        hover "filmmovie4b"
        hotspot (464, 532, 200, 178) action Jump('labelmovie3') hovered [ Play ("soundlow", "button1.mp3")]
        hotspot (682, 493, 196, 189) action Jump('labelmovie5') hovered [ Play ("soundlow", "button1.mp3")]
        hotspot (880, 156, 431, 579) action Jump('labelmoviehc') hovered [ Play ("soundlow", "button1.mp3")]
screen movie5:
    imagemap:
        ground "filmmovie5"
        hover "filmmovie5b"
        hotspot (464, 532, 200, 178) action Jump('labelmovie4') hovered [ Play ("soundlow", "button1.mp3")]
        hotspot (682, 493, 196, 189) action Jump('labelmovie1') hovered [ Play ("soundlow", "button1.mp3")]
        hotspot (880, 156, 431, 579) action Jump('labelmovies') hovered [ Play ("soundlow", "button1.mp3")]
