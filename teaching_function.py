from neuron import *
import random

def generate_random_weights_for( number_of_inputs ):
  return [ 1, 1, 1 ]

def generate_random_cutoff():
  return 1

def pick_training_target():
  return random.randint(0,2)

def not_trained():
  return True

def adjust_weights( eta, inputs, y, ws, o ):
  return [ 1, 1, 1 ]

def adjust_cutoff( eta, inputs, y, b, o ):
  return 1

def create_trained_neuron():
  d = 3
  eta = 0.5
  ws = generate_random_weights_for(3)
  b = generate_random_cutoff()
  neuron = Neuron(b, ws)
  while ( not_trained() ):
    n = pick_training_target()
    inputs = string_to_inputs(n)
    if ( n % d ) == 0:
      y = 1
    else:
      y = 0
    o = neuron.signal(inputs)
    if ( o != y ):
      ws = adjust_weights(eta, inputs, y, ws, o)
      b = adjust_cutoff(eta, inputs, y, b, o)
    neuron = Neuron(b, ws)
  return neuron


