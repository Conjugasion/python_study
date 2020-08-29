"""
  @author Lucas
  @date 2020/8/29 12:45
  满速御魂快来！
"""
import random

import pyautogui

if __name__ == '__main__':
    pyautogui.PAUSE = 1.5  # 每个函数执行后停顿1.5秒
    pyautogui.FAILSAFE = True  # 鼠标移到左上角会触发FailSafeException，因此快速移动鼠标到左上角也可以停止

    # 总的屏幕尺寸
    w, h = pyautogui.size()  # 1920 1080
    while True:
        # 挪到魂土开始界面的蛇眼睛双击
        pyautogui.click(1189, 214, button='left', clicks=2, interval=random.uniform(0.1, 0.3), duration=random.uniform(0.5, 1))
        # 开始刷
        pyautogui.click(1472, 768, button='left', clicks=1, duration=random.uniform(0.5, 1))
        # 单纯移动
        pyautogui.moveTo(1240, 188, duration=random.uniform(0.5, 1))
        # 接受可能弹出的协作任务
        pyautogui.click(786, 566, button='left', clicks=2, interval=random.uniform(0.1, 0.3), duration=random.uniform(0.5, 1))
        # 接受自动邀请组队
        pyautogui.click(439, 406, button='left', clicks=1, duration=random.uniform(0.5, 1))
        # 单纯移动
        pyautogui.moveTo(350, 590, duration=random.uniform(0.5, 1))


