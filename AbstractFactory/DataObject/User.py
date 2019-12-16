#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：User.py
# Site: 
# Author：along
# Date: 2019/12/8 15:21
# Software: PyCharm


class User(object):
    def __init__(self):
        self.__id = None
        self.__name = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
