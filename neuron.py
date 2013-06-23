class aggregator:
  def __init__( self, cutoff, weights ):
    self._cutoff = cutoff
    self._weights = weights

  def aggregate( self, inputs ):
    assert( len(self._weights) == len(inputs) )
    total = 0.0
    for i in range(len(inputs)):
      value = inputs[i]
      multiplier = self._weights[i]
      total += value * multiplier
    if total > self._cutoff:
      return 1
    return 0

def NAND( value1, value2 ):
  agg = aggregator( -1.5, [ -1, -1 ] )
  return agg.aggregate( [value1, value2] )

def NOT( value ):
  return NAND( value, value )

def AND( value1, value2 ):
  return NOT( NAND( value1, value2 ) )

def OR( value1, value2 ):
  notAandA = NOT(AND(value1, value1))
  notBandB = NOT(AND(value2, value2))
  return NOT( AND(notAandA, notBandB) )
