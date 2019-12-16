#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：OperationAdd.py
# Site: }
# Author：along
# Date: 2019/12/8 12:24
# Software: PyCharm

from SimpleFactory.Operation.Operation import Operation


# 继承
class OperationDiv(Operation):
    def __init__(self):
        super(OperationDiv, self).__init__()

    def get_result(self):
        return self.number_1 / self.number_2
