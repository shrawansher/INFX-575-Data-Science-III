import MapReduce
import sys

"""
DNA Trim Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key:unique nucleotide

    nucleotides = record[1]
    key = nucleotides[:-10]
    #Value doesn't matter here
    mr.emit_intermediate(key,1 )

def reducer(key, list_of_values):
    # prints all unique nucleotides
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
