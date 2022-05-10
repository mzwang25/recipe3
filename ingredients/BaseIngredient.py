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

    # TODO: For now only use the first pricePair
    priceType = pricePairs[ pricePairs.keys()[ 0 ] ][ 1 ]
    if priceType == "byLbs":
      self._amount = amountNeeded * massConvert[ units ]
    elif priceType == "byFlOz":
      self._amount = amountNeeded * volumeConvert[ units ]


