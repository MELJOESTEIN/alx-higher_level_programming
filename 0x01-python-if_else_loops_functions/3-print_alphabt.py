#!/usr/bin/python3
for ch in range(ord('a'), ord('z')+1):
    if chr(ch) not in 'qe':
        print("{:c}".format(ch), end='')
