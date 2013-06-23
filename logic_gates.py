from neuron import *

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
