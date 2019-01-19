#!/usr/bin/python3




from jk_rawhtml import *


"""
cs = ColorSpectrum(Color.RED)
cs.append(Color.GREEN)
cs.append(Color.BLUE)
cs.append(Color.YELLOW)
cs.append(Color.PINK)
cs.append(Color.CYAN)
"""


BAR_LENGTH = 60


for cs in ColorSpectrum.ALL:
	print(cs.name)
	print("\n\t", end="")
	for i in range(0, BAR_LENGTH + 1):
		f = i / BAR_LENGTH
		c = cs.getColor(f)
		print(c.toConsoleBackGround() + "  ", end="")
	print(Color.CONSOLE_RESET_BG + "\n")



