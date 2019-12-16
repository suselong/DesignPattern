#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：Client.py
# Site: 
# Author：along
# Date: 2019/12/8 15:20
# Software: PyCharm

from AbstractFactory.DataObject.User import User
from AbstractFactory.DataObject.Department import Department
from AbstractFactory.Factory.AccessFactory import AccessFactory
from AbstractFactory.Factory.SqlServerFactory import SqlServerFactory


def main():
    user = User()
    dept = Department()
    factory = SqlServerFactory()
    factory = AccessFactory()
    iu = factory.create_user()
    iu.insert(user)
    iu.get_user(1)
    id = factory.create_department()
    id.insert(dept)
    id.get_department(1)

main()
