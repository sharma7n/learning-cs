# Main Neopets

from shoyru import Shoyru
from kacheek import Kacheek
from starry import Starry
from flaming import Flaming

p1 = Shoyru("Persimmon Tao")
p2 = Kacheek("Lucky Roux")

p1 = Starry(p1)
print(p1.GetSpecies())

p2 = Flaming(p2)
p2 = Flaming(p2)
print(p2.GetSpecies())