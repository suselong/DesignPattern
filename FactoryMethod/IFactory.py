#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：IFactory.py
# Site: }
# Author：along
# Date: 2019/12/8 13:47
# Software: PyCharm

import abc


class IFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_operation(self):
        """
        工厂接口方法
        """
