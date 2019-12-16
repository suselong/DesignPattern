#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：AddFactory.py
# Site: }
# Author：along
# Date: 2019/12/8 13:51
# Software: PyCharm

from FactoryMethod.IFactory import IFactory
from SimpleFactory.Operation.OperationAdd2 import OperationAdd


class AddFactory(IFactory):
    def create_operation(self):
        return OperationAdd()
