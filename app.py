import app
import sys
import os
import settings

from tildagonos import tildagonos
from app_components import clear_background
from events.input import Buttons, BUTTON_TYPES
from system.patterndisplay.events import *
from system.eventbus import eventbus

ASSET_PATH = "/apps/mrpjevans_tildagon_hal/"

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