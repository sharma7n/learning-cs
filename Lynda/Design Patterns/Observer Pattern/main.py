# Main Program

from twitter import Twitter
from web import Web
from mobile import Mobile

t = Twitter("Hello, world!")

w = Web(t)
m = Mobile(t)

w.Tweet("I just ate a taco! #tacos")
m.Tweet("I just pooped! #poop")