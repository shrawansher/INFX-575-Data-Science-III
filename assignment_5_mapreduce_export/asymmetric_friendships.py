import MapReduce
import sys

"""
Friend Asymmetry Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):

    sorted_record = sorted(record)
    personA = sorted_record[0]
    personB = sorted_record[1]
    mr.emit_intermediate(personA+personB, record)

def reducer(key, list_of_values):
    # key: person
    # value: list of friend counts
    if len(list_of_values) == 1:
        print(list_of_values[0])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
