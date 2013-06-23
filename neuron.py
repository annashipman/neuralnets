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

def string_to_inputs( value ):
  text = bin( value )[2:].zfill(3)
  result = []
  for character in text:
    digit = int( character )
    result.append( digit )
  return result

class Neuron:
  def __init__( self, cutoff, weights ):
    self._agg = aggregator( cutoff, weights )

  def signal(self, inputs):
    return self._agg.aggregate(inputs)

  def generate_better_neuron( self ):
    self._agg = aggregator( 2, [ 1, 1, 1] ) 
