#!/usr/bin/python3
# coding=utf-8
# Project：DesignPattern
# FileName：IDepartment.py
# Site: 
# Author：along
# Date: 2019/12/8 15:28
# Software: PyCharm

import abc


class IDepartment(object):
    @abc.abstractmethod
    def insert(self, department):
        """"""

    @abc.abstractmethod
    def get_department(self, id):
        """"""
