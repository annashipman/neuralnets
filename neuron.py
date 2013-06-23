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

