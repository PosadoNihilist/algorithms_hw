line_count = 0
import sys

def strip(line):
    line = line.lstrip("#")
    line = line.lstrip(" ")
    line = line.rstrip(" ")
    line = line.rstrip("\t")
    return line
    
for line in sys.stdin:
    line_count += 1 
    line = line.lstrip("\t")
    line = line.lstrip(" ")
    if line.startswith("#"):
        line = strip(line)
        print("Line "+ str(line_count) + ": "+ line)
