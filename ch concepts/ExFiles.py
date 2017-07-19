import sys
import os

for line in sys.stdin:
    cleaned = line.strip()
    if os.path.exists(cleaned):
        print(cleaned)