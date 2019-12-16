#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：AccessFactory.py
# Site: 
# Author：along
# Date: 2019/12/8 15:19
# Software: PyCharm
from AbstractFactory.DBClass.AccessUser import AccessUser
from AbstractFactory.DBClass.AccessDepartment import AccessDepartment
from AbstractFactory.IFactory import IFactory


class AccessFactory(IFactory):
    def create_user(self):
        return AccessUser()

    def create_department(self):
        return AccessDepartment()
