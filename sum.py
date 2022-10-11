
l = [1, 5, 7, 9, 8]
k = 6
i = 0
while i < len(l):
    if l[i]+l[i-1] == k:
        print('TRUE')
    i = i+1
