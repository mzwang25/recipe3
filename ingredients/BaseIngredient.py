class BaseIngredient:
  _priceTypes = [ 
    "byCnt",
    "byLbs",
    "byFlOz",
  ]
  _prices = {}
  _amount = None

  # Conversion into fl-oz
  _volumeConvert = { 
    "tsp" : 0.167,
    "tbsp" : 0.5,
    "floz" : 1,
    "cup" : 8,
    "pint" : 16,
    "quart" : 32,
    "ml" : 0.034,
  }

  # Conversion into oz
  _massConvert = {
    "lbs" : 16,
    "oz" : 1,
    "mg" : (1/28350),
    "g" : (1/28.35),
  }

  _originalUnits = None
  _isVolume = None

  def __init__( self, amountNeeded, units, pricePairs):
    # pricePairs is a dictionary 
    # ex.
    #    "Ralphs" -> (12, "byCnt")
    #    "Vons" -> (11, "byCnt" )

    for key in pricePairs:
      assert( pricePairs[ key ][ 1 ] in self._priceTypes )

    self._prices = pricePairs
    self._amount = amountNeeded
    self._originalUnits = units
    priceType = self.getPriceType()

    self._amount = self.convertUnitToOz( "lbs", amountNeeded )

    self._orignalUnits = units
    self._isVolume = ( priceType == "byFlOz" )

  def getPriceType( self ):
    # TODO: For now only use the first pricePair
    return self._prices[ "Ralphs" ][ 1 ]

  def convertUnitToOz( self, inUnit, value ):
    # Converts to either oz or fl-oz
    priceType = self.getPriceType()

    amount = None
    if priceType == "byLbs":
      amount = value * self._massConvert[ inUnit ]
    elif priceType == "byFlOz":
      amount = value * self._volumeConvert[ inUnit ]

    return amount

  def amountInUnit( self, unit ):
    pass

  def cost( self ):
    pricePair = self._prices[ "Ralphs" ]
    costPer = pricePair[ 0 ]
    costBy = pricePair[ 1 ]

    print( costPer, costBy )
    print(self._amount)
