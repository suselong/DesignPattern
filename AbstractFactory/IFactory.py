#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：IFactory.py
# Site: 
# Author：along
# Date: 2019/12/8 15:15
# Software: PyCharm

import abc


class IFactory(object):
    @abc.abstractmethod
    def create_user(self):
        """"""

    @abc.abstractmethod
    def create_department(self):
        """"""
