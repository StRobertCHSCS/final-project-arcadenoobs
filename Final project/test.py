import Resource.Mage.Attack as M_A
import Resource.Mage.Movement as M_M
import Resource.Mage.Main as MMain
import arcade
import os

class test(MMain.Mage):
    def __init__(self):
        super().on_key_press(1)

t = test()