import sys
sys.path.append( '../ingredients' )

from BaseRecipe import BaseRecipe
from ingredients import *

class ChanaMasala( BaseRecipe ):
  def __init__( self, targetServingSize=None ):
    self.ingredientList = [

    ]

    super().__init__( targetServingSize )
if __name__ == '__main__':
  r = ChanaMasala()
  r.printCostBreakdown()
