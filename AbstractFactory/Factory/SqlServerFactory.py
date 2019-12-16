#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：SqlServerFactory.py
# Site: 
# Author：along
# Date: 2019/12/8 15:16
# Software: PyCharm

from AbstractFactory.IFactory import IFactory
from AbstractFactory.DBClass.SqlserverUser import SqlserverUser
from AbstractFactory.DBClass.SqlserverDepartment import SqlserverDepartment


class SqlServerFactory(IFactory):
    def create_user(self):
        return SqlserverUser()

    def create_department(self):
        return SqlserverDepartment()
