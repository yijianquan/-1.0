# 写代码中的练习过程


# import autopy
#autopy.mouse.move(191,189) # 鼠标瞬间移动到坐标
# autopy.mouse.smooth_move(191,189) # 平滑移动到坐标
# autopy.mouse.rightClick() # 单击
# autopy.mouse.toggle(True) # 按下左键
# autopy.mouse.toggle(False) # 松开左键

# import pyautogui as pag
# pag.moveTo(500, 300, 2, pag.easeOutQuad)
# pag.rightClick()

# from win32api import GetSystemMetrics
# from win32con import SM_CXSCREEN
# from win32con import SM_CYSCREEN
# nWidth = GetSystemMetrics(SM_CXSCREEN)
# nWidth = str(nWidth)
# nHeight = GetSystemMetrics(SM_CYSCREEN)
# nHeight = str(nHeight)
# Resolving_power =  nHeight + "*" + nWidth
# print(Resolving_power) #得到屏幕分辨率


# #获取屏幕某像素的RGB
# from ctypes import *
# def get_color(x, y):
#     gdi32 = windll.gdi32
#     user32 = windll.user32
#     hdc = user32.GetDC(None)  # 获取颜色值
#     pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
#     r = pixel & 0x0000ff
#     g = (pixel & 0x00ff00) >> 8
#     b = pixel >> 16
#     return [r, g, b]
#
# #未知39 185 [238, 238, 238]
# #空[188, 188, 188]
# x = 39
# y = 185
# x1 = 39 + 6*28
# y1 = 185 +3*28
# color_arr = get_color(x,y)
# color_arr1 = get_color(x1,y1)
# print('x = ',x)
# print('y = ',y)
# print(color_arr)
# color_arr1 = get_color(x1,y1)
# print('x1 = ',x1)
# print('y1 = ',y1)
# print(color_arr1)
# print()

# a = 0
#
# def func():
#     global a
#     a = [1,2,3]
#
# func()
# print(a)
#
# from map import get_Map
# mine_map = 0
#
# def getMineMap():
#     global mine_map
#     mine_map = get_Map()
#
# getMineMap()
# print(mine_map)


# n = 1
# m = 2
# print("ssssss+",n,m)

# from map import getColorByRGB
# n = 8
# m = 1
# a = getColorByRGB(n,m)
# print(a)
#
# a = [1,2,3]
# b = [1,2,3]
# if a== b:
#     print("ok")
# else:
#     print("not ok")