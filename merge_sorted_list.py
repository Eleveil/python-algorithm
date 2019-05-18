#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-18 23:29:05
# @Author  : Ivy Mong (davy0328meng@gmail.com)


arr1 = [1, 3, 4, 6, 10]
arr2 = [2, 5, 8, 11]

ind = 0
ans = arr1.copy()

for i in range(len(arr2)):
    while ind < len(arr1):
        if arr2[i] <= arr1[ind]:
            ans.insert(ind+i, arr2[i])
            break
        else:
            ind += 1

else:
    ans = ans + arr2[i:]

print(ans)