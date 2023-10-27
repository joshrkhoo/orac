inputFile = open("landin.txt", "r")

x, y = map(int, inputFile.readline().split())

"""
given a coordinate 
need to find the page left at that square
(0,0) is page 0

(1, 0)
(1, 1)
(0, 1)
(-1, 1)
(-1, 0)
(-1, -1)
(0, -1)
"""

