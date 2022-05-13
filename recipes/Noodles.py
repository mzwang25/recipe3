import sys
sys.path.append( '../ingredients' )

from BaseRecipe import BaseRecipe
from ingredients import *

class Noodles( BaseRecipe ):
  ingredientList = [
    Flour( 300, 'g' ),
  ]

if __name__ == '__main__':
  r = Noodles()
  r.printCostBreakdown()
  print()
  print( r.totalCost() )
