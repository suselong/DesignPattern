#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：SubFactory.py
# Site: }
# Author：along
# Date: 2019/12/8 13:51
# Software: PyCharm

from FactoryMethod.IFactory import IFactory
from SimpleFactory.Operation.OperationSub import OperationSub


class SubFactory(IFactory):
    def create_operation(self):
        return OperationSub()
