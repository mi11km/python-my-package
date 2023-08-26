#!/usr/bin/env python
# import sys
# from collections import Counter
#
# if __name__ == '__main__':
#     for line in sys.stdin:
#         for word, count in Counter(line.rstrip('\n').split(' ')).items():
#             print(word, count)

import sys

if __name__ == '__main__':
    result = {}
    for line in sys.stdin:
        word, count = line.rstrip('\n').split(' ')
        if word in result:
            result[word] += count
        else:
            result[word] = count
    for word, count in result.items():
        print(word, count)
