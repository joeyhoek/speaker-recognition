#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: gen_result.py
# Date: Sat Dec 07 23:59:58 2013 +0800
# Author: Yuxin Wu <ppwwyyxxc@gmail.com>

import operator
import string
enroll_names = map(string.strip,
                   open("scores_enroll_labels.txt").readlines())
test_names = map(string.strip,
                 open("scores_test_labels.txt").readlines())

scores = []
with open("scores.txt") as f:
    for line in f:
        line = map(float, line.strip().split())
        scores.append(line)

cnt = 0
right = 0
for tst in xrange(len(test_names)):
    match = max([(idx, score[tst]) for (idx, score) in
                 enumerate(scores)], key=operator.itemgetter(1))
    print "test", tst, test_names[tst], ":"
    print match, enroll_names[match[0]]
    cnt += 1
    if int(test_names[tst]) == int(enroll_names[match[0]]):
        right += 1
print right, cnt, float(right) / cnt


