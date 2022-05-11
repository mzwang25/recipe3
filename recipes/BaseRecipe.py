import sys
sys.path.append( '../ingredients' )

from Vegtables import *
from Spices import *

class BaseRecipe:
  ingredientList = None

  def totalCost( self ):
    acc = 0.0
    for items in self.ingredientList:
      acc += items.cost()

    return acc

  def printCostBreakdown( self ):
    for items in self.ingredientList:
      print( items, "$" + str( items.cost() ) )

