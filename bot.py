###
# use 'python_auto_gui' to interact with the 3rd party GUI
import pyautogui
###
# Coord class will provide the co-ordinates for the planned click.


class Coord():

    chromeBtn = (242, 755)

###
# Function to execute the coord class.
# Uses python_auto_gui's click along with the
# given coordinates to click on screen


def start():
    pyautogui.click(Coord.chromeBtn)


def jump():
    pyautogui.keyDown('space')
    print('jump')

    pyautogui.keyUp('space')


start()
