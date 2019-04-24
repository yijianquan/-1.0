import calculation as cal

mine_map_temp = 0
mine_map = 0
def begin():
    global mine_map_temp
    global mine_map
    while 1:
        if mine_map_temp==0 :
            mine_map_temp = cal.click()
        elif mine_map == mine_map_temp:
            mine_map_temp = cal.click()
        else:
            print("扫雷结束，我不行了，扫不出来了")
            break
        if mine_map == mine_map_temp:
            print("扫雷结束，我不行了，扫不出来了")
            break
        mine_map = mine_map_temp

begin()