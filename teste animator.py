import Animator
import threading
from time import sleep

animation = Animator.load("anim2.txt")
animation.play(1)

while animation._state == "playing":
	pass

animation.reverse()
animation.play(1)