import sys
"""
Author name: Huang, Chunyu
This script counts the lines in standard input
Input: text from the system
Test
"""
count = 0
for line in sys.stdin:
	count +=1
print (count, "lines in standrad input")
