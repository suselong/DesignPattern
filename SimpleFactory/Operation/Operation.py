#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：Operation.py
# Site: }
# Author：along
# Date: 2019/12/8 12:13
# Software: PyCharm

class Operation(object):
    def __init__(self):
        self.__number_1 = 0
        self.__number_2 = 0

    @property
    def number_1(self):
        return self.__number_1

    @number_1.setter
    def number_1(self, value):
        self.__number_1 = value

    @property
    def number_2(self):
        return self.__number_2

    @number_2.setter
    def number_2(self, value):
        self.__number_2 = value

    def get_result(self):
        result = 0
        return result
