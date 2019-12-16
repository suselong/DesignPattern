#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：OperationFactory.p
# Site: }
# Author：along
# Date: 2019/12/8 12:30
# Software: PyCharm

from SimpleFactory.Operation.OperationAdd import OperationAdd
from SimpleFactory.Operation.OperationSub import OperationSub
from SimpleFactory.Operation.OperationDiv import OperationDiv
from SimpleFactory.Operation.OperationMul import OperationMul


class OperationFactory(object):
    @staticmethod
    def create_operate(operate):
        return {
            "+": OperationAdd(),
            "-": OperationSub(),
            "*": OperationMul(),
            "/": OperationDiv()
        }[operate]
