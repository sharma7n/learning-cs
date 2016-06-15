from treasure_chest import TreasureChest

t = TreasureChest()

# t is initially Locked and Empty.

t.unlock() # success
t.lock() # success
t.open() # failure
t.close() # failure
t.empty() # failure
t.fill("Cookies") # failure

t.unlock()
t.fill("Cookies")
t.close()
t.lock()
t.unlock()
c = t.empty()
print(c)