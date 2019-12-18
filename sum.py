"""
 File Name: sum.py
 Version  : 1.0
 Author   : Gary
 Date     : 2019/11/15 15:00
 Software : PyCharm
 
"""
l = [193.00,634.00,963.00,139.84,244.80,43.11,252.00,61.59,193.00,1009.00,298.00,1469.00,398.00,634.00,963.00,252.96,96.72,260.40,56.38,193.00,1009.00,963.00,245.48,252.00,50.61,93.73,193.00,963.00,55.17,96.59,260.40,252.28,193.00,1902.00,398.00,193.00,38.50,128.80,5.73,125.46,334.32,40.02,15.00]


def combination(l, n):
    l = list(sorted(filter(lambda x: x <= n, l)))
    combination_impl(l, n, [])


def combination_impl(l, n, stack):
    if n == 0:
        print(stack)
        return
    for i in range(0, len(l)):
        if l[i] <= n:
            stack.append(l[i])
            combination_impl(l[i + 1:], n - l[i], stack)
            stack.pop()
        else:
            break


combination(l, 3130.41)