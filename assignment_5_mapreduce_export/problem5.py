import MapReduce
import sys

"""
DNA Trim Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: num of machines

    nucleotides = record[1]
    key = nucleotides[:10]
    mr.emit_intermediate(key,1 )

def reducer(key, list_of_values):
    # key: person
    # value: list of friend counts
    #total = 0
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
