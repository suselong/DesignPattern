#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：Operation.py
# Site: }
# Author：along
# Date: 2019/12/8 10:56
# Software: PyCharm

class Operation(object):
    def __init__(self, number_1, number_2, operate):
        self.number_1 = number_1
        self.number_2 = number_2
        self.operate = operate
        self.result = self.run()

    # 如果需要增加平方根，我需要修改这个类，并且需要重新编译该类所有代码，包括之前的+ - * /
    def run(self):
        return {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y
        }[self.operate](self.number_1, self.number_2)
