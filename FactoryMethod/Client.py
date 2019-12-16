#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：Main.py
# Site: }
# Author：along
# Date: 2019/12/8 11:14
# Software: PyCharm
from FactoryMethod.ChildFactory import *


# 客户端
def main():
    try:
        # 修改点
        switch = {"+": AddFactory(), "-": SubFactory(),
                  "*": MulFactory(), "/": DivFactory(),}
        oper = switch[input("请选择运算符号(+,-,*,/):")].create_operation()
        oper.number_1 = eval(input("请输入数字A："))
        oper.number_2 = eval(input("请输入数字B:"))
        print(f"结果是:{oper.get_result()}")
    except Exception as e:
        print(f"输入有误:{e},请重新输入")


while True:
    main()
