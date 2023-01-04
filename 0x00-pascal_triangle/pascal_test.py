#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triLists = []

    for i in range(1, n+1):
        row = []

        if i == 1:
            row.append(i)
            triLists.append(row)
            continue

        preList = triLists[i - 2]

        for j in range(len(preList)):
            if j == 0:
                row.append(1)
                continue

            row.append(preList[j-1] + preList[j])

        row.append(1)
        triLists.append(row)
    return triLists
    

print(pascal_triangle(6))
