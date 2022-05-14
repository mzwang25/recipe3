import sys
sys.path.append( '../ingredients' )

from BaseRecipe import BaseRecipe
from ingredients import *

class Noodles( BaseRecipe ):
  def __init__( self, targetServingSize=None ):
    self.ingredientList = [
        Flour( 300, 'g' ),
        Eggs( 1, 'cnt' ),
      ]
    self.servingSize = 3
    super().__init__( targetServingSize )


if __name__ == '__main__':
  r = Noodles()
  r.printCostBreakdown()
