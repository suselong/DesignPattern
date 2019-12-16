#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：SqlserverUser.py
# Site: 
# Author：along
# Date: 2019/12/8 15:10
# Software: PyCharm

from AbstractFactory.IDepartment import IDepartment


class SqlserverDepartment(IDepartment):
    def insert(self, dept):
        print("在SQL Server插入一条部门数据")

    def get_department(self, id):
        print("在SQL Server获取一条部门数据")
        return None
