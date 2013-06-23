from neuron import *
from teaching_function import * 

trained = False

assert( string_to_inputs( 0 ) == [ 0, 0, 0 ] )
assert( string_to_inputs( 1 ) == [ 0, 0, 1 ] )
assert( string_to_inputs( 5 ) == [ 1, 0, 1 ] )

neuron = create_trained_neuron()
neuron.signal( 1 )

#neuron = Neuron()
#
#while (not trained):
#  if ( neuron.signal(0) != 1 ):
#    neuron.generate_better_neuron()
#  else:
#    if ( neuron.signal(1) != 0 ):
#      neuron.generate_better_neuron()
#    else:
#      if (neuron.signal(2) != 0 ):
#        neuron.generate_better_neuron()
#      else:
#        trained = True
