import sys
sys.path.append( '../ingredients' )

from Vegtables import *
from Spices import *

class BaseRecipe:
  ingredientList = None
  maxPaddingLen = None # Number of spaces before price printout

  def __init__( self ):
    self.maxPaddingLen = 0
    for items in self.ingredientList:
      self.maxPaddingLen = max( 10, len( str( items ) ), self.maxPaddingLen )

  def totalCost( self ):
    acc = 0.0 
    for items in self.ingredientList:
      acc += items.cost()

    return acc

  def printCostBreakdown( self ):
    for items in self.ingredientList:
      paddingLen = self.maxPaddingLen - len( str( items ) )
      padding = " " * paddingLen
      print( items, padding + "$" + str( items.cost() ) )

