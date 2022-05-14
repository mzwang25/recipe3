import sys
sys.path.append( '../ingredients' )

from BaseRecipe import BaseRecipe
from ingredients import *

class Noodles( BaseRecipe ):
  ingredientList = [
    Flour( 300, 'g' ),
    Eggs( 1, 'cnt' ),
  ]

  servingSize = 5

if __name__ == '__main__':
  r = Noodles()
  r.printCostBreakdown()
