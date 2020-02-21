import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
import numpy as np

#x0 y0
#x1 y1
#.....
#xn yn

XY = np.array(read().split(), np.int64)
