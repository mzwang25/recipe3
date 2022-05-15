import sys
sys.path.append( '../ingredients' )

from BaseRecipe import BaseRecipe
from ingredients import *

class Chili( BaseRecipe ):
  def __init__( self, targetServingSize=None ):
    self.ingredientList = [
      Cumin( 2, 'tbsp' ),
      Oregano( 2, 'tbsp' ),
      Coriander( 2, 'tbsp' ),
      Cinnamon( 1, 'tbsp' ),
      CocoaPowder( 2, 'tbsp' ),
      CannedChipotleChilesInAdobo( 3, 'cnt' ),
      GroundBeef( 2, 'lbs' ),
      Onions( 2, 'cnt' ),
      Garlic( 6, 'cnt' ),
      GreenPepper( 2, 'cnt' )
      Carrots( 2, 'cnt' )
      # ... TODO

    ]
    self.servingSize = 12

    super().__init__( targetServingSize )
if __name__ == '__main__':
  r = Chili()
  r.printCostBreakdown()
