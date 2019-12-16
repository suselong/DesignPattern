#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：SqlserverUser.py
# Site: 
# Author：along
# Date: 2019/12/8 15:10
# Software: PyCharm

from AbstractFactory.IUser import IUser


class SqlserverUser(IUser):
    def insert(self, user):
        print("在SQL Server插入一条用户数据")

    def get_user(self, id):
        print("在SQL Server获取一条用户数据")
        return None
