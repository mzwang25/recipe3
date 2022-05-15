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
  _originalVal = None
  _isVolume = None
  _flOzPerOz = None

  def __init__( self, amountNeeded, units, pricePairs, massVolConv=None):
    # pricePairs is a dictionary 
    # ex.
    #    "Ralphs" -> (12, "byCnt")
    #    "Vons" -> (11, "byCnt" )

    for key in pricePairs:
      assert( pricePairs[ key ][ 1 ] in self._priceTypes )

    self._prices = pricePairs
    self._amount = amountNeeded
    self._originalUnits = units
    self._originalVal = amountNeeded
    priceType = self.getPriceType()

    self._amount = self.convertUnitToOz( units, amountNeeded )

    self._orignalUnits = units
    self._isVolume = ( priceType == "byFlOz" )

    if massVolConv != None:
      self.setupMassVolumeConv( massVolConv )

    if ( self.getUnitType( units ) != priceType ):
      assert( self._flOzPerOz and "Need mass to vol conversion!" )
      if ( self.getUnitType( units ) == "byFlOz" ):
        # flOz -> oz
          self._amount /= self._flOzPerOz 
      else:
          self._amount *= self._flOzPerOz 


  def getPriceType( self ):
    # TODO: For now only use the first pricePair
    return self._prices[ "Ralphs" ][ 1 ]

  def getUnitType( self, unit ):
    if unit in self._massConvert:
      return "byLbs"
    elif unit in self._volumeConvert:
      return "byFlOz"
    else:
      return "byCnt"

  def convertUnitToOz( self, inUnit, value ):
    # Converts to either oz or fl-oz
    priceType = self.getUnitType( inUnit )

    amount = None
    if priceType == "byLbs":
      amount = value * self._massConvert[ inUnit ]
    elif priceType == "byFlOz":
      amount = value * self._volumeConvert[ inUnit ]
    elif priceType == "byCnt":
      amount = value

    return amount

  def convertOzToUnit( self, outUnit, value ):
    # Converts to either oz or fl-oz
    priceType = self.getUnitType( outUnit )

    amount = None
    if priceType == "byLbs":
      amount = value / self._massConvert[ outUnit ]
    elif priceType == "byFlOz":
      amount = value / self._volumeConvert[ outUnit ]
    elif priceType == "byCnt":
      amount = value

    return amount

  def convertUnitToUnit( self, inUnit, outUnit, value ):
    if inUnit == outUnit:
      return value

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
    rateUnit = None
    
    if priceType == "byLbs":
      rateUnit = "lbs"
    elif priceType == "byFlOz":
      rateUnit = "floz"
    else:
      rateUnit = "cnt"

    costPer = pricePair[ 0 ]
    costInUnit = self.convertPricePerUnit( rateUnit, self._originalUnits,  costPer ) 

    amountInUnit = self.amountInUnit( self._originalUnits )

    return float( "{:.3f}".format( amountInUnit * costInUnit ) )

  def setupMassVolumeConv( self, convList ):
    sep = convList.split( ' ' )

    val1 = float( sep[ 0 ] )
    unit1 = sep[ 1 ]
    val2 = float( sep[ 2 ] )
    unit2 = sep[ 3 ]

    flOz = None
    oz = None

    if unit1 in self._volumeConvert:    
      # Unit 1 is a volume and Unit 2 is a mass
      flOz = self.convertUnitToOz( unit1, val1 )
      oz = self.convertUnitToOz( unit2, val2 )

    else:
      # Unit 2 is a volume and Unit 1 is a mass
      flOz = self.convertUnitToOz( unit2, val2 )
      oz = self.convertUnitToOz( unit1, val1 )

    self._flOzPerOz = float( flOz ) / oz


  def __str__( self ):
    return self.__class__.__name__

