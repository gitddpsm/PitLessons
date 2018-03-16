# utf 8

simple_tuple = (1, 2, 3, 4, 5)
print(simple_tuple)

# Operations


# add
simple_tuple += (6, )
print(simple_tuple)

# tuples
# tuples are immutable
empty_tuple = tuple() # show __builtin__
tuple1 = (1, )
tuple2 = (1, )
not_a_tuple = (99) # this is not a tuple!

print(
    tuple1 == tuple2,
    tuple2 == not_a_tuple,
    '\nnot_a_tuple type =',
    type(not_a_tuple),
    '\n', not_a_tuple
)
print ( (1, 2) == (1, 2, ) )

# tuple operations:

#a add

tuple1 = tuple1 + tuple2
print(tuple1)
print(len(tuple()))

