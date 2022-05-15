import sys
sys.path.append( '../ingredients' )

from Vegtables import *
from Spices import *

class BaseRecipe:
  ingredientList = None
  maxPaddingLen = None # Number of spaces before price printout
  servingSize = None
  daysGoodFor = 3
  warnMsg = []

  def __init__( self, targetServingSize=None ):
    self.maxPaddingLen = 0
    for items in self.ingredientList:
      self.maxPaddingLen = max( 10, len( str( items ) ), self.maxPaddingLen )

    if targetServingSize:
      self.adjustServingSize( targetServingSize )

    assert( self.ingredientList and "You forgot to list recipe ingredients" )
    assert( self.servingSize and "You forgot to add servingSize" )
    assert( self.daysGoodFor and "daysGoodFor must be set" )

  def totalCost( self ):
    acc = 0.0 
    for items in self.ingredientList:
      acc += items.cost()

    return acc

  def printCostBreakdown( self ):
    for items in self.ingredientList:
      paddingLen = self.maxPaddingLen - len( str( items ) )
      padding = " " * paddingLen
      print( items, padding + "$" + "{:.3f}".format( items.cost() ) +
                    "   " +
                    "{:.3f}".format( items._originalVal ) + " " +
                    str( items._originalUnits ) )

    cost = self.totalCost()
    perServe = cost / self.servingSize
    print()
    print( "${}/Total\n${}/Serving".format( self.totalCost(), perServe ) )
    print()

    for msg in self.warnMsg:
      print( "!!! " + msg )

  def adjustServingSize( self, targetSize ):
    factorToMultiply = float( targetSize ) / float( self.servingSize )
    for ing in self.ingredientList:
      units = ing._originalUnits
      val = ing._originalVal
      ing.__init__( val * factorToMultiply , units )

    self.servingSize = targetSize 

