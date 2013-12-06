#!/usr/bin/python

first = 0
second = 1

count = 0
user = 6

while (count != user):
    last = first + second
    count += 1
    first = second
    second = last

print first
