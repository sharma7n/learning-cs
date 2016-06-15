from weapon import Weapon
from sfx_slash import Slash
from sfx_bonk import Bonk
from damage_cut import Cut
from damage_bludgeon import Bludgeon

Sword = Weapon(Slash(), Cut())
Hammer = Weapon(Bonk(), Bludgeon())

for w in [Sword, Hammer]:
	w.play_sfx()
	w.deal_damage()