from map import get_Map
from map import getColorByRGB
from insertflag import insertFlag
from insertflag import clickBlank

mine_map = 0

# 获取当前的数字布局
def getMineMap():
    global mine_map
    mine_map  = get_Map()
    return mine_map

# 插雷
def pvp():
    #获取扫雷状态图
    global mine_map
    tmap = getMineMap()
    print(tmap)
    n = 1
    m = 1
    num = 0
    blank_num = 0#计数器，计算周围有多少空白
    flag_num = 0
    while m < 17:
        while n < 32 :
            if tmap[n][m]<9 :
                temp = int(tmap[n][m])
                # print(temp)
                a = []
                a.append(tmap[n-1][m-1])
                a.append(tmap[n][m-1])
                a.append(tmap[n+1][m-1])
                a.append(tmap[n-1][m])
                a.append(tmap[n+1][m])
                a.append(tmap[n-1][m+1])
                a.append(tmap[n][m+1])
                a.append(tmap[n+1][m+1])
                for i in range(0,len(a)):
                    if a[i] == 10 :
                        blank_num += 1
                        num += 1
                    if a[i] == 11:
                        flag_num +=1
                        num += 1
                if blank_num != 0 and num == temp :
                    if tmap[n-1][m-1]==10 :
                        tmap[n-1][m-1] = 11
                        insertFlag(n-1,m-1)
                    if tmap[n][m-1]==10 :
                        tmap[n][m-1] = 11
                        insertFlag(n,m-1)
                    if tmap[n+1][m-1]==10 :
                        tmap[n+1][m-1] = 11
                        insertFlag(n+1,m-1)
                    if tmap[n-1][m]==10 :
                        tmap[n-1][m] = 11
                        insertFlag(n-1,m)
                    if tmap[n+1][m]==10 :
                        tmap[n+1][m] = 11
                        insertFlag(n+1,m)
                    if tmap[n-1][m+1]==10 :
                        tmap[n-1][m+1] = 11
                        insertFlag(n-1,m+1)
                    if tmap[n][m+1]==10 :
                        tmap[n][m+1] = 11
                        insertFlag(n,m+1)
                    if tmap[n+1][m+1]==10 :
                        tmap[n+1][m+1] = 11
                        insertFlag(n+1,m+1)
                flag_num = 0
                blank_num = 0
                num = 0
                n += 1
                continue
            else:
                flag_num = 0
                blank_num = 0
                n += 1
                continue
        n = 1
        flag_num = 0
        blank_num = 0
        num = 0
        m += 1
    mine_map = tmap
    return tmap

# 对于点开是数字的试试能不能再排雷
def flagAgain(tmap,n,m):
    print("试试能不能试着排一次雷")
    num = 0
    blank_num = 0
    flag_num = 0
    temp = int(tmap[n][m])
    # print(temp)
    a = []
    a.append(tmap[n - 1][m - 1])
    a.append(tmap[n][m - 1])
    a.append(tmap[n + 1][m - 1])
    a.append(tmap[n - 1][m])
    a.append(tmap[n + 1][m])
    a.append(tmap[n - 1][m + 1])
    a.append(tmap[n][m + 1])
    a.append(tmap[n + 1][m + 1])
    for i in range(0, len(a)):
        if a[i] == 10:
            blank_num += 1
            num += 1
        if a[i] == 11:
            flag_num += 1
            num += 1
    if blank_num != 0 and num == temp:
        if tmap[n - 1][m - 1] == 10:
            tmap[n - 1][m - 1] = 11
            insertFlag(n - 1, m - 1)
            print("又排雷一次")
        if tmap[n][m - 1] == 10:
            tmap[n][m - 1] = 11
            insertFlag(n, m - 1)
            print("又排雷一次")
        if tmap[n + 1][m - 1] == 10:
            tmap[n + 1][m - 1] = 11
            insertFlag(n + 1, m - 1)
            print("又排雷一次")
        if tmap[n - 1][m] == 10:
            tmap[n - 1][m] = 11
            insertFlag(n - 1, m)
            print("又排雷一次")
        if tmap[n + 1][m] == 10:
            tmap[n + 1][m] = 11
            insertFlag(n + 1, m)
            print("又排雷一次")
        if tmap[n - 1][m + 1] == 10:
            tmap[n - 1][m + 1] = 11
            insertFlag(n - 1, m + 1)
            print("又排雷一次")
        if tmap[n][m + 1] == 10:
            tmap[n][m + 1] = 11
            insertFlag(n, m + 1)
            print("又排雷一次")
        if tmap[n + 1][m + 1] == 10:
            tmap[n + 1][m + 1] = 11
            insertFlag(n + 1, m + 1)
            print("又排雷一次")
    return tmap

# 对于点开是数字的试试是否能再点
def clickAgain(tmap,n,m):
    print("试试能不能再点")
    flag_num = 0
    temp = tmap[n][m]
    a = []
    a.append(tmap[n - 1][m - 1])
    a.append(tmap[n][m - 1])
    a.append(tmap[n + 1][m - 1])
    a.append(tmap[n - 1][m])
    a.append(tmap[n + 1][m])
    a.append(tmap[n - 1][m + 1])
    a.append(tmap[n][m + 1])
    a.append(tmap[n + 1][m + 1])
    for i in range(0, len(a)):
        if a[i] == 11:
            flag_num += 1
    if flag_num == temp:
        if tmap[n - 1][m - 1] == 10:
            clickBlank(n - 1, m - 1)
            tmap[n - 1][m - 1] = getColorByRGB(n - 1, m - 1)
            tmap_temp = flagAgain(tmap, n - 1, m - 1)
            if tmap != tmap_temp:
                tmap = tmap_temp
            else:
                tmap = clickAgain(tmap, n - 1, m - 1)
            print("又点开一次",n,m)
        if tmap[n][m - 1] == 10:
            clickBlank(n, m - 1)
            tmap[n][m - 1] = getColorByRGB(n, m - 1)
            tmap_temp = flagAgain(tmap, n, m - 1)
            if tmap != tmap_temp:
                tmap = tmap_temp
            else:
                tmap = clickAgain(tmap, n, m - 1)
            print("又点开一次",n,m)
        if tmap[n + 1][m - 1] == 10:
            clickBlank(n + 1, m - 1)
            tmap[n + 1][m - 1] = getColorByRGB(n + 1, m - 1)
            tmap_temp = flagAgain(tmap, n + 1, m - 1)
            if tmap != tmap_temp:
                tmap = tmap_temp
            else:
                tmap = clickAgain(tmap, n + 1, m - 1)
            print("又点开一次",n,m)
        if tmap[n - 1][m] == 10:
            clickBlank(n - 1, m)
            tmap[n - 1][m] = getColorByRGB(n - 1, m)
            tmap_temp = flagAgain(tmap, n - 1, m)
            if tmap != tmap_temp:
                tmap = tmap_temp
            else:
                tmap = clickAgain(tmap, n - 1, m)
            print("又点开一次",n,m)
        if tmap[n + 1][m] == 10:
            clickBlank(n + 1, m)
            tmap[n + 1][m] = getColorByRGB(n + 1, m)
            tmap_temp = flagAgain(tmap, n + 1, m)
            if tmap != tmap_temp:
                tmap = tmap_temp
            else:
                tmap = clickAgain(tmap, n + 1, m)
            print("又点开一次",n,m)
        if tmap[n - 1][m + 1] == 10:
            clickBlank(n - 1, m + 1)
            tmap[n - 1][m + 1] = getColorByRGB(n - 1, m + 1)
            tmap_temp = flagAgain(tmap, n - 1, m + 1)
            if tmap != tmap_temp:
                tmap = tmap_temp
            else:
                tmap = clickAgain(tmap, n - 1, m + 1)
            print("又点开一次",n,m)
        if tmap[n][m + 1] == 10:
            clickBlank(n, m + 1)
            tmap[n][m + 1] = getColorByRGB(n, m + 1)
            tmap_temp = flagAgain(tmap, n, m + 1)
            if tmap != tmap_temp:
                tmap = tmap_temp
            else:
                tmap = clickAgain(tmap, n, m + 1)
            print("又点开一次",n,m)
        if tmap[n + 1][m + 1] == 10:
            clickBlank(n + 1, m + 1)
            tmap[n + 1][m + 1] = getColorByRGB(n + 1, m + 1)
            tmap_temp = flagAgain(tmap, n + 1, m + 1)
            if tmap != tmap_temp:
                tmap = tmap_temp
            else:
                tmap = clickAgain(tmap, n + 1, m + 1)
            print("又点开一次",n,m)
    return tmap

# 点开空白函数
def funClick(tmap):
    n = 1
    m = 1
    flag_num = 0  # 计数器，计算周围有多少雷
    while m < 17:
        while n < 32:
            if tmap[n][m] < 9:
                temp = int(tmap[n][m])
                # print(temp)
                a = []
                a.append(tmap[n - 1][m - 1])
                a.append(tmap[n][m - 1])
                a.append(tmap[n + 1][m - 1])
                a.append(tmap[n - 1][m])
                a.append(tmap[n + 1][m])
                a.append(tmap[n - 1][m + 1])
                a.append(tmap[n][m + 1])
                a.append(tmap[n + 1][m + 1])
                for i in range(0, len(a)):
                    if a[i] == 11:
                        flag_num += 1
                if flag_num == temp:
                    if tmap[n - 1][m - 1] == 10:
                        clickBlank(n - 1, m - 1)
                        tmap[n-1][m-1] = getColorByRGB(n-1,m-1)
                        tmap_temp = flagAgain(tmap,n-1,m-1)
                        if tmap != tmap_temp:
                            tmap = tmap_temp
                        else:
                            tmap = clickAgain(tmap,n-1,m-1)
                    if tmap[n][m - 1] == 10:
                        clickBlank(n, m - 1)
                        tmap[n][m-1] = getColorByRGB(n,m-1)
                        tmap_temp = flagAgain(tmap,n,m-1)
                        if tmap != tmap_temp:
                            tmap = tmap_temp
                        else:
                            tmap = clickAgain(tmap,n,m-1)
                    if tmap[n + 1][m - 1] == 10:
                        clickBlank(n + 1, m - 1)
                        tmap[n+1][m-1] = getColorByRGB(n+1,m-1)
                        tmap_temp = flagAgain(tmap,n+1,m-1)
                        if tmap != tmap_temp:
                            tmap = tmap_temp
                        else:
                            tmap = clickAgain(tmap,n+1,m-1)
                    if tmap[n - 1][m] == 10:
                        clickBlank(n - 1, m)
                        tmap[n-1][m] = getColorByRGB(n-1,m)
                        tmap_temp = flagAgain(tmap,n-1,m)
                        if tmap != tmap_temp:
                            tmap = tmap_temp
                        else:
                            tmap = clickAgain(tmap,n-1,m)
                    if tmap[n + 1][m] == 10:
                        clickBlank(n + 1, m)
                        tmap[n+1][m] = getColorByRGB(n+1,m)
                        tmap_temp = flagAgain(tmap,n+1,m)
                        if tmap != tmap_temp:
                            tmap = tmap_temp
                        else:
                            tmap = clickAgain(tmap,n+1,m)
                    if tmap[n - 1][m + 1] == 10:
                        clickBlank(n - 1, m + 1)
                        tmap[n-1][m+1] = getColorByRGB(n-1,m+1)
                        tmap_temp = flagAgain(tmap,n-1,m+1)
                        if tmap != tmap_temp:
                            tmap = tmap_temp
                        else:
                            tmap = clickAgain(tmap,n-1,m+1)
                    if tmap[n][m + 1] == 10:
                        clickBlank(n, m + 1)
                        tmap[n][m+1] = getColorByRGB(n,m+1)
                        tmap_temp = flagAgain(tmap,n,m+1)
                        if tmap != tmap_temp:
                            tmap = tmap_temp
                        else:
                            tmap = clickAgain(tmap,n,m+1)
                    if tmap[n + 1][m + 1] == 10:
                        clickBlank(n + 1, m + 1)
                        tmap[n+1][m+1] = getColorByRGB(n+1,m+1)
                        tmap_temp = flagAgain(tmap,n+1,m+1)
                        if tmap != tmap_temp:
                            tmap = tmap_temp
                        else:
                            tmap = clickAgain(tmap,n+1,m+1)
                flag_num = 0
                n += 1
                continue
            else:
                flag_num = 0
                n += 1
                continue
        n = 1
        flag_num = 0
        m += 1
    return tmap


# 点开空白
def click():
    global mine_map
    tmap = pvp()
    print("这是排过雷的图。。。。。。。。。。。。")
    print(tmap)
    mine_map = funClick(tmap)
    return mine_map


# 全新算法
#好难写，写不出来