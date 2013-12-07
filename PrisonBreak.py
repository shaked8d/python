#!/usr/bin/python


def prisonbreak(mes, push):
    """
    enter a message, and the number of each push to get the actual message
    """

    phone = ([], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z'])
    new = []
    mes = list(mes)
    push = list(push)

    for i in range (len(mes)):
        new.append(phone[int(mes[i])][int(push[i])-1])
    return new
