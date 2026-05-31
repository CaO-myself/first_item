import pygame
import importlib
import os
import ctypes
from pathlib import Path

# --- 环境变量 ---#
x,y=(550,150)
pygame.init()#创建&初始化pygame
info = pygame.display.Info()#屏幕size的读取
width = info.current_w
height = info.current_h
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{width-x},{0}'

### --- pygame ---###
pygame.init()#创建&初始化pygame
pygame.mixer.init()#创建混音器
clock = pygame.time.Clock() # 创建时间
FPS=2#设置帧率

# --- 窗口 ---#
screen_mode=None#设置初始界面
screens=pygame.display.set_mode((x, y),pygame.NOFRAME)
#核心代码】强制从任务栏移除
hwnd = pygame.display.get_wm_info()["window"]#获取窗口句柄
# 获取当前的扩展样式
ex_style = ctypes.windll.user32.GetWindowLongW(hwnd, -20) # -20 对应 GWL_EXSTYLE
# 添加 WS_EX_TOOLWINDOW 样式 (0x00000080)
# 这个样式告诉 Windows：这是一个工具窗口，不要给它画任务栏按钮
ctypes.windll.user32.SetWindowLongW(hwnd, -20, ex_style | 0x00000080)
pygame.display.set_caption('高考倒计时')#设定窗口名字
try: pygame.display.set_icon(pygame.image.load('sound/zone_compory_logo.png') )#加载并设置自定义图标
except FileNotFoundError:print("未找到图标文件，将使用默认图标")
screen_mode='ui'

# --- 字体 ---#
font_path=Path(__file__).resolve().parent/'fonts'/'msyh.ttc'#获取当前脚本所在的文件夹的绝对路径
font=pygame.font.Font(font_path,36)

#####---# 正式运行 #---#####
sound_path=Path(__file__).resolve().parent/'sound'/'key.wav'
pygame.mixer.Sound(sound_path).play()#播放开启音效

while True:
    if screen_mode=='ui':
        tick=0  #主界面切换的时间重置
        
        # --- 声明(重载)ui函数 ---#
        import screen.ui
        importlib.reload(screen.ui)
        from screen.ui import ui

    while screen_mode=='ui':
        # --- 背景 ---#
        screens.fill((10,10,15))

        ### ---# 运行 #--- ###
        screen_mode=ui(screens,screen_mode)

        # --- 更新结算 ---#
        tick+=1
        pygame.display.flip()   
        clock.tick(FPS)
