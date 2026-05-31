import pygame
import sys

# --- 字体 ---#
from pathlib import Path
script_path = Path(__file__).resolve().parent.parent# 获取当前脚本的绝对路径的父级文件
font_path = script_path / 'fonts' / 'msyh.ttc'
font = pygame.font.Font(font_path, 36)
font_big = pygame.font.Font(font_path, 50)
font_low = pygame.font.Font(font_path, 25)

# --- 读取各类数据 ---#
from datetime import datetime
from datetime import datetime, date
from python.classes import Font_Surface# type: ignore
from python.classes import Line_Surface# type: ignore

def get_gaokao_countdown():
    today = date.today()# 获取今天的日期
    this_year_gaokao = date(today.year, 6, 7)# 设定今年的高考日期 (6月7日)
    
    # 逻辑判断：如果今年的高考日期已经过了，就计算明年的高考
    if today > this_year_gaokao:target_gaokao = date(today.year + 1, 6, 7) 
    else:target_gaokao = this_year_gaokao

    days_left = (target_gaokao - today).days# 计算天数差
    return target_gaokao.year, days_left

def get_time_left():
    now = datetime.now()# 获取当前系统时间
    end_of_day = datetime.combine(now.date(), datetime.max.time())# 获取今天的最后一刻 (23:59:59.9)
    time_left = end_of_day - now# 计算时间差
    
    hours = time_left.seconds // 3600# 提取时、分、秒
    minutes = (time_left.seconds % 3600) // 60
    seconds = time_left.seconds % 60
    return hours, minutes, seconds

class Data:
    def __init__(self):
        self.h,self.m,self.s = get_time_left()# 执行计算
        self.year,self.days = get_gaokao_countdown()
        self.render=f"今天还有{self.h}:{self.m}:{self.s}结束"
        self.cut=(f"距离 {self.year} 年的高考还有 {self.days} 天")

    def define(self):
        self.h,self.m,self.s = get_time_left()# 执行计算
        self.year,self.days = get_gaokao_countdown()
        self.render=f"今天还有{self.h}:{self.m}:{self.s}结束"
        self.cut=(f"距离 {self.year} 年的高考还有 {self.days} 天")

# -- 前置准备 -- #
data=Data()
x,y=(550,150)
sound_path=Path(__file__).resolve().parent.parent/'sound'/'quit.wav'

class fundament:#ui界面列表
    dicts={'render':Font_Surface(data.render,(x/2,y/3),font),
           'line':Line_Surface((x,3),(x/2,y/2)),
           'cut':Font_Surface(data.cut,(x/2,y*2/3),font)}
    if data.days<=10:dicts['cut']=Font_Surface(data.cut,(x/2,y*2/3),font,color=(255,0,0))
    for name,item in dicts.items():item.name=name#重命名

    def display(screen):
        output=None
        for index,item in fundament.dicts.items():
            input=None#检测初始化
            input=item.display(screen)
            if input!=None:output=input#判断是否有反馈
        return output
    
def ui(screen,screen_mode):
    data.screen=screen_mode

    '''元素'''
    fundament.display(screen)

    # --- 事件处理 ---#
    '''基础判定'''
    h, m, s = get_time_left()# 执行计算
    if (data.h,data.m,data.s)!=(h,m,s):
        data.define()#同步&更新
        fundament.dicts['render'].item=font.render(data.render,True,(255,255,255))

    year, days = get_gaokao_countdown()
    if (year,days)!=(data.year,data.days):
        data.define()#同步&更新
        fundament.dicts['day'].item=font.render(data.cut,True,(255,255,255))

    '''事件判定'''#如果没有这个，界面获得焦点时会崩溃
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#退出事件
            pygame.mixer.Sound(sound_path).play()#播放关闭音效

    return data.screen
