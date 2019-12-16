#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：IUser.py
# Site: 
# Author：along
# Date: 2019/12/8 15:07
# Software: PyCharm

import abc


class IUser(object):
    @abc.abstractmethod
    def insert(self, user):
        """"""

    @abc.abstractmethod
    def get_user(self, id):
        """"""
