import sys
sys.path.append( '../ingredients' )

from Vegtables import *
from Spices import *

class BaseRecipe:
  ingredientList = None

  def totalCost( self ):
    acc = 0
    for items in self.ingredientList:
      acc += items.cost()

