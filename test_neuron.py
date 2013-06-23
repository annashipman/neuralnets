from logic_gates import *

agg = aggregator( 0.5, [ 2.5, 0.5 ] )
assert ( agg.aggregate( [ 0, 0 ] ) == 0 )
assert ( agg.aggregate( [ 1, 0 ] ) == 1 )
assert ( agg.aggregate( [ 0, 1 ] ) == 0 )
assert ( agg.aggregate( [ 1, 1 ] ) == 1 )

assert ( NAND(0,0) == 1 )
assert ( NAND(0,1) == 1 )
assert ( NAND(1,0) == 1 )
assert ( NAND(1,1) == 0 )

assert ( NOT(0) == 1 )
assert ( NOT(1) == 0 )

assert ( AND(0,0) == 0 )
assert ( AND(0,1) == 0 )
assert ( AND(1,0) == 0 )
assert ( AND(1,1) == 1 )

assert ( OR(0,0) == 0 )
assert ( OR(0,1) == 1 )
assert ( OR(1,0) == 1 )
assert ( OR(1,1) == 1 )
