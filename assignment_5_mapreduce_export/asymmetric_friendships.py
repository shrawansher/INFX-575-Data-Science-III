import MapReduce
import sys

"""
Friend Asymmetry Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    #Key: friend
    # value: count
    friendTo = record[0]
    friendOf = record[1]
    mr.emit_intermediate((friendTo,friendOf), 1)
    mr.emit_intermediate((friendOf, friendTo), 1)

def reducer(key, list_of_values):
    # key: person
    # value: list of friend counts
    if len(list_of_values) == 1:
        mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
