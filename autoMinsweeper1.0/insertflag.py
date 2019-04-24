import pyautogui as pag

x = 23 #基础距离
y = 169 #基础距离
distance = 28 #间距
def insertFlag(n,m):
    pag.moveTo(x + distance*n, y + distance*m, 0.1, pag.easeOutQuad)
    pag.rightClick()
    print('插了一面旗子')

def clickBlank(n,m):
    pag.moveTo(x + distance * n, y + distance * m, 0.1, pag.easeOutQuad)
    pag.click()
    print('点开了空白')