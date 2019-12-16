#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：AccessUser.py
# Site: 
# Author：along
# Date: 2019/12/8 15:12
# Software: PyCharm

from AbstractFactory.IUser import IUser


class AccessUser(IUser):
    def insert(self, user):
        print("在Access中插入一条用户数据")

    def get_user(self, id):
        print("在Access中获取一条用户数据")
        return None
