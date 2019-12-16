#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：AccessUser.py
# Site: 
# Author：along
# Date: 2019/12/8 15:12
# Software: PyCharm

from AbstractFactory.IDepartment import IDepartment


class AccessDepartment(IDepartment):
    def insert(self, department):
        print("在Access中插入一条部门数据")

    def get_department(self, id):
        print("在Access中获取一条部门数据")
        return None
