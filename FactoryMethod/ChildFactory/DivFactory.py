#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：DivFactory.py
# Site:
# Author：along
# Date: 2019/12/8 13:51
# Software: PyCharm

from FactoryMethod.IFactory import IFactory
from SimpleFactory.Operation.OperationDiv import OperationDiv


class DivFactory(IFactory):
    def create_operation(self):
        return OperationDiv()

