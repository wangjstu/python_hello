#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s1 = 72
s2 = 85
s3 = s2-s1
print('''背景：小明和老师在办公室;
小明啊，我作为一个长者得跟你谈谈''')
print('你去年成绩:%d ,今年成绩：%d' %(s1,s2))
print('你的成绩提高了%d分 ,就是%d%%' % (s3,int(s3/s1*100)))
print('''我今天是作为一个长者跟你们讲。我不是老师，但是我见得太多了。我有这个必要好告诉你们一点人生的经验
你啊，我感觉你啊还要学习一个。你们毕竟还too young.明白我的意思吧？
唉，我也替你着急啊。
好了好了，出去吧。
顺便把下一个同学叫进来。''')
print('小明：吼啊,再见，老师.')
asdassfa=input('按回车开启剧情')
print('同学叫什么名字')
name=input('我叫：')
print('你上次考试多少分啊')
date1=input('老师，我考了：')
date1=int(date1)
print('那你这次考多少分啊')
date2=input('老师，我考了:')
date2=int(date2)
x=date2-date1
y=date1-date2
if x > 0:
    print(name,'，不错,继续努力。成绩提高了%0.1f%%' %(x/date1*100))
elif x < 0:
    print(name,'，干什么吃的,好好学。下降了%0.1f%%' %(y/date1*100))
else: 
    print('不错，继续努力')