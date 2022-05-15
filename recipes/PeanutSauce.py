import sys
sys.path.append( '../ingredients' )

from BaseRecipe import BaseRecipe
from ingredients import *

class PeanutSauce( BaseRecipe ):
  def __init__( self, targetServingSize=None ):
    self.ingredientList = [
      Jalapeno( 1, 'cnt' ),
      Garlic( 3, 'cnt' ),
      Onion( 1, 'cnt' ),
      OliveOil( 1, 'tsp' ),
      CoconutMilk( 1, 'cup' ),
      PeanutButter( 0.5, 'cup' ),
      SoySauce( 1, 'tbsp' )
    ]

    self.servingSize = 10 #???

    super().__init__( targetServingSize )
if __name__ == '__main__':
  r = PeanutSauce()
  r.printCostBreakdown()
