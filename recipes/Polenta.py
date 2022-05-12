from BaseRecipe import BaseRecipe
import sys
sys.path.append( '../ingredients' )

from ingredients import *

class Polenta( BaseRecipe ):
  ingredientList = [
    Cornmeal( 0.5, 'cups' ),
    OliveOil( 1, 'tbsp' ),
    Spinich( 4, 'cup' ),
    Garlic( 3, 'cnt' ),
    ChiliFlakes( 0.5, 'tsp' ),
    Eggs( 2, 'cnt' )
  ]

if __name__ == "__main__":
  r = Polenta()
  r.printCostBreakdown()
  print()
  print( r.totalCost() )
