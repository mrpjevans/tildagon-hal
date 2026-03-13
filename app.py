import app
import sys
import os
import settings

from tildagonos import tildagonos
from app_components import clear_background
from events.input import Buttons, BUTTON_TYPES
from system.patterndisplay.events import *
from system.eventbus import eventbus

if sys.implementation.name == "micropython":
    apps = os.listdir("/apps")
    path = ""
    for a in apps:
        # This is important for apps deployed to the appstore
        # The Snake app from naomi stored at
        # https://github.com/npentrel/tildagon-snake/
        # has all its files in the folder
        # npentrel_tildagon_snake
        if a == "github_user_github_repo_name":
            path = "/apps/" + a
    ASSET_PATH = path + "/assets/"
else:
    # while testing, put your files in the folder you are developing in,
    # for example: example/streak.jpg
    ASSET_PATH = "apps/2001/"

ASSET_PATH = "apps/2001/"

class ExampleApp(app.App):
    def __init__(self):
        self.button_states = Buttons(self)
        eventbus.emit(PatternDisable())

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()

    def draw(self, ctx):
        tildagonos.set_led_power(True)
        for n in range(0, 13):
            tildagonos.leds[n] = (64, 0, 0)
            tildagonos.leds.write()
        clear_background(ctx)
        ctx.save()
        ctx.image(ASSET_PATH + "hal240.jpg", -120, -120, 240, 240)
        ctx.restore()


__app_export__ = ExampleApp