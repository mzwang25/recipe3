from BaseRecipe import BaseRecipe
import sys
sys.path.append( '../ingredients' )

from ingredients import *

class ChickenAdobo( BaseRecipe ):
  ingredientList = [
    ChickenBreast( 8, 'cnt' ),
    RiceVinegar( 0.75, 'cup' ),
    SoySauce( 0.25, 'cup' ),
    Garlic( 2, 'cnt' ),
    BlackPepper( 0.5, 'tsp' ),
    BayLeaves( 2, 'cnt' ),
    OliveOil( 2, 'tbsp' ),
    Potatoes( 2, 'cnt' ),
    Carrots( 4, 'cnt' ),
    LongRice( 2, 'cup' ),
    Cornstarch( 2, 'tbsp' )
  ]

if __name__ == "__main__":
  r = ChickenAdobo()
  r.printCostBreakdown()
  print()
  print( r.totalCost() )
