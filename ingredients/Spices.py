from BaseIngredient import BaseIngredient

class GarlicPowder ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 16.64, "byLbs" ),
    }
  )
class SambalOelek ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 3.98, "byLbs" ),
    }
  )
class Flour ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 1.096, "byFlOz" ),
    }
  )
class SourCream ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 2.28, "byLbs" ),
    }
  )
class BayLeaves ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 1.08, "byCnt" ),
    }
  )
