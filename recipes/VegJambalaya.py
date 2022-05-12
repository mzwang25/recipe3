from BaseRecipe import BaseRecipe
import sys
sys.path.append( '../ingredients' )

from ingredients import *

class VegJambalaya( BaseRecipe ):
  ingredientList = [
    OliveOil( 2, 'tbsp' ),
    Onion( 1, 'cnt' ),
    GreenPepper( 1, 'cnt' ),
    Celery( 3, 'cnt' ),
    #GreenChili( 0.5, 'cnt' ),
    Tomatoes( 2, 'cnt' ),
    BayLeaves( 2, 'cnt' ),
    Paprika( 1, 'tsp' ),
    GarlicPowder( 1, 'tsp' ),
    Cayenne( 1, 'tsp' ),
    #Thyme( 0.5, 'tsp' ),
    Oregano( 0.5, 'tsp' ),
    SoySauce( 1, 'tsp' ),
    LongRice( 0.75, 'cup' ),
    ChickenBroth( 3, 'cup' ),
  ]

if __name__ == "__main__":
  r = VegJambalaya()
  r.printCostBreakdown()
  print()
  print( r.totalCost() )
