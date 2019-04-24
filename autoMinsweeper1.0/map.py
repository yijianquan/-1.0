from getRGB import get_color
import autopy


def getColorByRGB(transverse,portrait):

    # 10表示是未知，
    # 9表示是空的
    # 11是旗子
    # 12是标记雷
    # 13是未知

    a = 13  # 暂时的参数，获取到的数值将短暂存储到a
    x = 23  # 第一个格子的中心坐标
    y = 169  # 第二个格子的中心坐标
    xx = 39  # 第一个格子左上的x坐标
    yy = 185  # 第二个格子左上的y坐标
    distance = 28 # 每个格子中心点之间的距离

    #扫雷前需要找到每个颜色的RGB参数
    blank = [188, 188, 188]
    none = [238, 238, 238]
    flag = [184, 67, 67]
    thunder = [0, 0, 0]
    blue_1 = [0, 5, 255]
    green_2 = [24, 132, 53]
    red_3 = [231, 67, 67]
    purple_4 = [43, 44, 136]
    blood_red_5 = [154, 67, 67]
    pale_blue_6 = [67, 147, 147]

    rgb = get_color(x+distance*transverse, y+distance*portrait)
    if rgb == blank:
        a = 10
    elif rgb == blue_1:
        a = 1
    elif rgb == green_2:
        a = 2
    elif rgb == red_3:
        a = 3
    elif rgb == purple_4:
        a = 4
    elif rgb == blood_red_5:
        a = 5
    elif rgb == pale_blue_6:
        a = 6
    elif rgb == flag:
        a = 11
    elif rgb == thunder:
        a = 12
    else:
        a = 13
    if a == 10:
        rgb = get_color(xx + distance * transverse, yy + distance * portrait)
        if rgb == none:
            a = 10
        else:
            a = 9
    return a

#读取当前图像
def get_Map():
    # 10表示是未知，
    # 9表示是空的
    # 11是旗子
    # 12是标记雷
    # 13是未知

    Minesweeper_arr = [ [''] * 18 for i in range(33)]
    X = 23  # 固定不变的X，
    Y = 169
    x = 23 #第一个格子左上的x坐标
    y = 169 #第一个格子左上的y坐标
    distance = 28 #每个相邻格子中心点的横向、纵向距离
    x_length = X+distance*32
    y_length = Y+distance*17

    blank = [188, 188, 188]
    none = [238, 238, 238]
    flag = [184, 67, 67]
    thunder = [0,0,0]
    blue_1 = [0,5,255]
    green_2 = [24, 132, 53]
    red_3 = [231, 67, 67]
    purple_4 = [43, 44, 136]
    blood_red_5 = [154, 67, 67]
    pale_blue_6 = [67, 147, 147]

    times = 0 #已经识别的格子数目
    transverse = 0 #横向坐标
    portrait = 0 #纵向坐标
    while y <= y_length :
        while x <= x_length :
            # autopy.mouse.move(x,y)
            if transverse == 0 or portrait==0 or transverse == 32 or portrait == 17 :
                Minesweeper_arr[transverse][portrait] = 9
            else:
                rgb = get_color(x,y)
                if rgb == blank :
                    Minesweeper_arr[transverse][portrait] = 10
                elif rgb == blue_1 :
                    Minesweeper_arr[transverse][portrait] = 1
                elif rgb == green_2 :
                    Minesweeper_arr[transverse][portrait] = 2
                elif rgb == red_3 :
                    Minesweeper_arr[transverse][portrait] = 3
                elif rgb == purple_4 :
                    Minesweeper_arr[transverse][portrait] = 4
                elif rgb == blood_red_5 :
                    Minesweeper_arr[transverse][portrait] = 5
                elif rgb == pale_blue_6 :
                    Minesweeper_arr[transverse][portrait] = 6
                elif rgb == flag :
                    Minesweeper_arr[transverse][portrait] = 11
                elif rgb == thunder :
                    Minesweeper_arr[transverse][portrait] = 12
                else :
                    Minesweeper_arr[transverse][portrait] = 13
            transverse += 1
            x += distance
        x = X
        transverse = 0
        y += distance
        portrait += 1
    print(Minesweeper_arr)
    portrait = 1
    transverse = 1
    x = 51 # 第一个格子中心的x坐标
    y = 197 # 第二个格子中心的y坐标
    x_length = x_length - distance
    y_length = y_length - distance
    while y <= y_length :
        while x <= x_length :
            if Minesweeper_arr[transverse][portrait] == 10 :
                rgb = get_color(39+distance*(transverse-1),185+distance*(portrait-1))
                if rgb == none :
                    transverse += 1
                    x += distance
                    continue
                else :
                    Minesweeper_arr[transverse][portrait] = 9
            transverse += 1
            x += distance
        x = 51
        transverse = 1
        y += distance
        portrait += 1

    return Minesweeper_arr