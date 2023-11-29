#!/usr/bin/python3
"""Module containing pascal_triangle() function"""


def pascal_triangle(n):
    """Returns a list of list of integers"""
    # return an empty list if n is less than or equal to zero
    if (n <= 0):
        return []

    else:
        # initialize big list that will hold the smaller lists
        bigList = []

        # initialize previous list
        prevList = []
        curList = []

        # iterate creating the smaller lists
        for i in range(1, (n + 1)):
            # the first list will always contain the integer 1 only
            # print(f"This is iteration: {i} of {n}")
            for index in range(i):
                if len(bigList) == 0:
                    curList = [1]

                else:
                    curInd = index
                    preInd = index - 1

                    try:
                        curValue = prevList[curInd]

                    except IndexError:
                        curValue = 0

                    try:
                        if preInd < 0:
                            preValue = 0
                        else:
                            preValue = prevList[preInd]

                    except IndexError:
                        preValue = 0

                    curList.append(curValue + preValue)

            # print(f'Revised prevlist from {prevList} to {curList}')
            prevList = curList.copy()
            bigList.append(curList)
            curList = []

    return bigList
