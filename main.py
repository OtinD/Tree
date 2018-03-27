#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-27 19:04:56
# @Author  : ${Rongbo Wu} (${rnwu@siom.ac.cn})

class Node(object):
    def __init__(self, elem=None, lchile=None, rchild=None):
        self.elem = elem
        self.lchild = lchile
        self.rchild = rchild


class Tree(object):
    def __init__(self):
        self.root = Node()
        # myqueue中存的是没有填满的节点
        self.myqueue = []

    def add(self, elem):
        if self.root.elem == None:
            self.root.elem = elem
            self.myqueue.append(self.root)
        else:
            treenode = self.myqueue[0]
            if treenode.lchild == None:
                treenode.lchild = Node(elem)
                self.myqueue.append(treenode.lchild)
            else:
                treenode.rchild = Node(elem)
                self.myqueue.append(treenode.rchild)
                self.myqueue.pop(0)

    def front_digui(self, root):
        if root == None:
            return
        print root.elem
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self, root):
        if root == None:
            return
        self.middle_digui(root.lchild)
        print root.elem
        self.middle_digui(root.rchild)

    def later_digui(self, root):
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)  
        print root.elem      

    def front_stack(self, root):
        if root == None:
            return
        mystack = []
        node = root
        while node or mystack:
            while node:
                print node.elem
                mystack.append(node)
                node = node.lchild
            node = mystack.pop()
            node = node.rchild

    def middle_stack(self, root):
        if root == None:
            return
        mystack = []
        node = root
        while node or mystack:
            while node:
                mystack.append(node)
                node = node.lchild
            node = mystack.pop()
            print node.elem
            node = node.rchild

    # 从右往左的先序遍历反过来即位后序遍历，用ABC三角形容易理解
    def later_stack(self, root):
        if root == None:
            return
        mystack = []
        mystack0 = []
        node = root
        while node or mystack:
            while node:
                mystack0.append(node.elem)
                mystack.append(node)
                node = node.rchild
            node = mystack.pop()
            node = node.lchild
        while mystack0:
            print mystack0.pop() 

    def leval_stack(self, root):
        if root == None:
            return
        mystack = []
        node = root
        mystack.append(node)
        while node or mystack:
            if node.lchild:
                mystack.append(node.lchild)
            if node.rchild:
                mystack.append(node.rchild)
            print mystack.pop(0).elem
            if mystack:
                node = mystack[0]
            else:
                node = None


A = Tree()
for i in range(0, 10):
    A.add(i)

A.leval_stack(A.root)