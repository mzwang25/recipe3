import sys
sys.path.append( '../ingredients' )

from BaseRecipe import BaseRecipe
from ingredients import *

class PeanutChickenBrocolli( BaseRecipe ):
  def __init__( self, targetServingSize=None ):
    self.ingredientList = [
      LongRice( 1.5, 'cup' ),
      CoconutMilk( 13.5, 'floz' ),
      ChickenBreast( 6, 'cnt' ),
      OliveOil( 2, 'tsp' ),
      Brocolli( 6, 'cup' ), # 1 large bunch
      # PeanutSauce( 0.5, 'cup' ) // Sep Recipe Needed
    ]

    self.warnMsg = [ "Requires PeanutSauce recipe" ]

    self.servingSize = 3

    super().__init__( targetServingSize )
if __name__ == '__main__':
  r = PeanutChickenBrocolli()
  r.printCostBreakdown()
