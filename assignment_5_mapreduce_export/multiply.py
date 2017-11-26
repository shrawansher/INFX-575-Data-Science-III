import MapReduce
import sys

"""
Assume you have two matrices A and B in a sparse matrix format,
where each record is of the form i, j, value.
Design a MapReduce algorithm to compute matrix multiplication: A x B
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

N = 5

def mapper(record):

    # Key is row or col  depending on the matrix
    # Value is the the matrix identifier and the value of the element in the row or col

    matrix, row, col, val = record
    if matrix == 'a':
        for n in range(N):
            k = record[1]
            mr.emit_intermediate((k, n), [matrix, col, val])
    else:
        for n in range(N):
            k = record[2]
            mr.emit_intermediate((n, k), [matrix, row, val])


def reducer(key, list_of_values):

    # The reduce function has the format (i, j, value) where each element is an integer.

    a_result = [e for e in list_of_values if e[0] == 'a']
    b_result = [e for e in list_of_values if e[0] == 'b']
    result = 0
    for a in a_result:
        for b in b_result:
            if a[1] == b[1]:
                result += a[2] * b[2]
    mr.emit((key[0], key[1], result))


# Do not modify below this line
# =============================

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)