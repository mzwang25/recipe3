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

    self._amount = self.convertUnitToOz( units, amountNeeded )

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

  def convertOzToUnit( self, outUnit, value ):
    # Converts to either oz or fl-oz
    priceType = self.getPriceType()

    amount = None
    if priceType == "byLbs":
      amount = value / self._massConvert[ outUnit ]
    elif priceType == "byFlOz":
      amount = value / self._volumeConvert[ outUnit ]

    return amount

  def convertUnitToUnit( self, inUnit, outUnit, value ):
    convertToOz = self.convertUnitToOz( inUnit, value )
    return self.convertOzToUnit( outUnit, convertToOz )

  def amountInUnit( self, unit ):
    return self.convertOzToUnit( unit, self._amount )

  def convertPricePerUnit( self, inUnit, outUnit, price ):
    conversionFactor = self.convertUnitToUnit( inUnit, outUnit, 1 )
    return price / conversionFactor

  def cost( self ):
    pricePair = self._prices[ "Ralphs" ]
    priceType = self.getPriceType()
    rateUnit = "lbs" if priceType == "byLbs" else "floz"

    costPer = pricePair[ 0 ]
    costInUnit = self.convertPricePerUnit( rateUnit, self._originalUnits,  costPer ) 
    amountInUnit = self.amountInUnit( self._originalUnits )

    return "{:.3f}".format( amountInUnit * costInUnit )

