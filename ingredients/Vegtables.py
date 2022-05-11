from BaseIngredient import BaseIngredient

class GreenBeans ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 1.99, "byLbs" ),
    }
  )
class BrusselSprouts ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 2.99, "byLbs" ),
    }
  )
class Onion ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 0.6, "byCnt" ),
    }
  )
class GreenPepper ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 1, "byCnt" ),
    }
  )
class Celery ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 0.25, "byCnt" ),
    }
  )
class Tomatoes ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 0.75, "byCnt" ),
    }
  )
class Potatoes ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 1, "byCnt" ),
    }
  )
class Carrots ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 0.15, "byCnt" ),
    }
  )
class Garlic ( BaseIngredient ):
  def __init__( self, amountNeeded, units ):
    super().__init__( amountNeeded, units, {
      "Ralphs" : ( 0.69, "byCnt" ),
    }
  )
