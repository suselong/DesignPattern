#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：Department.py
# Site: 
# Author：along
# Date: 2019/12/8 15:21
# Software: PyCharm


class Department(object):
    def __init__(self):
        self.__id = None
        self.__department = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        self.__department = value
