# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_v4.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

# Credits:
#
# Original Neural Network made by: Samay Shamdasani [1]
#
# Neural Network edits and UI design by: Aleksi Surakka
#
# Original idea and support by: Arto Kaarna
#
# [1]:
# Samay Shamdasani. 4.11.2017
# Build a Neural Network. An introduction to building a basic feed-forward neural network with backpropagation in Python.
# URL:https://enlight.nyc/projects/neural-network/ (referenced 18. 02. 2020).

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1188, 549)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 17, 23, 1, 1, QtCore.Qt.AlignHCenter)
        self.feedback_2 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_2.setObjectName("feedback_2")
        self.gridLayout.addWidget(self.feedback_2, 15, 10, 1, 1)
        self.weight_bias_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_bias_2.setStyleSheet("background:green;color:white")
        self.weight_bias_2.setObjectName("weight_bias_2")
        self.gridLayout.addWidget(self.weight_bias_2, 5, 4, 1, 1)
        self.output = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output.setFont(font)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 16, 25, 4, 1)
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setMinimumSize(QtCore.QSize(150, 60))
        self.runButton.setObjectName("runButton")
        self.gridLayout.addWidget(self.runButton, 0, 25, 1, 1)
        self.horizontalSlider_7 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_7.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_7.setMinimum(-100)
        self.horizontalSlider_7.setMaximum(100)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.gridLayout.addWidget(self.horizontalSlider_7, 30, 2, 1, 2)
        self.activation_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.activation_3.setMinimumSize(QtCore.QSize(66, 20))
        self.activation_3.setStyleSheet("background:blue;color:white")
        self.activation_3.setReadOnly(True)
        self.activation_3.setObjectName("activation_3")
        self.gridLayout.addWidget(self.activation_3, 29, 15, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 13, 0, 1, 1)
        self.input3 = QtWidgets.QSpinBox(self.centralwidget)
        self.input3.setMaximum(1)
        self.input3.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.input3.setObjectName("input3")
        self.gridLayout.addWidget(self.input3, 33, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 11, 0, 1, 5)
        self.feedback_bias_4 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_bias_4.setObjectName("feedback_bias_4")
        self.gridLayout.addWidget(self.feedback_bias_4, 6, 22, 1, 1)
        self.weight_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_3.setStyleSheet("background:blue;color:white")
        self.weight_3.setObjectName("weight_3")
        self.gridLayout.addWidget(self.weight_3, 16, 4, 1, 1)
        self.activation_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.activation_1.setMinimumSize(QtCore.QSize(66, 20))
        self.activation_1.setStyleSheet("background:red;color:white")
        self.activation_1.setReadOnly(True)
        self.activation_1.setObjectName("activation_1")
        self.gridLayout.addWidget(self.activation_1, 15, 15, 1, 1)
        self.input_bias_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.input_bias_2.setMinimumSize(QtCore.QSize(66, 20))
        self.input_bias_2.setReadOnly(True)
        self.input_bias_2.setMinimum(1)
        self.input_bias_2.setMaximum(1)
        self.input_bias_2.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.input_bias_2.setObjectName("input_bias_2")
        self.gridLayout.addWidget(self.input_bias_2, 6, 15, 1, 1)
        self.feedback_9 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_9.setObjectName("feedback_9")
        self.gridLayout.addWidget(self.feedback_9, 34, 10, 1, 1)
        self.weight_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_12.setStyleSheet("background:blue;color:white")
        self.weight_12.setObjectName("weight_12")
        self.gridLayout.addWidget(self.weight_12, 29, 21, 1, 1)
        self.weight_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_6.setStyleSheet("background:blue;color:white")
        self.weight_6.setObjectName("weight_6")
        self.gridLayout.addWidget(self.weight_6, 28, 4, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 17, 0, 1, 5)
        self.feedback_4 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_4.setObjectName("feedback_4")
        self.gridLayout.addWidget(self.feedback_4, 18, 10, 1, 1)
        self.feedback_6 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_6.setObjectName("feedback_6")
        self.gridLayout.addWidget(self.feedback_6, 28, 10, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setMinimumSize(QtCore.QSize(180, 60))
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 0, 18, 1, 1)
        self.weight_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_7.setStyleSheet("background:red;color:white")
        self.weight_7.setObjectName("weight_7")
        self.gridLayout.addWidget(self.weight_7, 30, 4, 1, 1)
        self.input1 = QtWidgets.QSpinBox(self.centralwidget)
        self.input1.setMaximum(1)
        self.input1.setObjectName("input1")
        self.gridLayout.addWidget(self.input1, 15, 0, 1, 1)
        self.horizontalSlider_bias_1 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_bias_1.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_bias_1.setMinimum(-100)
        self.horizontalSlider_bias_1.setMaximum(100)
        self.horizontalSlider_bias_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_bias_1.setObjectName("horizontalSlider_bias_1")
        self.gridLayout.addWidget(self.horizontalSlider_bias_1, 4, 2, 1, 2)
        self.output_num = QtWidgets.QLineEdit(self.centralwidget)
        self.output_num.setMinimumSize(QtCore.QSize(66, 20))
        self.output_num.setStyleSheet("background:black;color:white")
        self.output_num.setReadOnly(True)
        self.output_num.setObjectName("output_num")
        self.gridLayout.addWidget(self.output_num, 18, 24, 1, 1)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_4.setMinimum(-100)
        self.horizontalSlider_4.setMaximum(100)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.gridLayout.addWidget(self.horizontalSlider_4, 18, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(110, 0))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 21, 1, 1, QtCore.Qt.AlignHCenter)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 29, 0, 1, 5)
        self.input_bias = QtWidgets.QSpinBox(self.centralwidget)
        self.input_bias.setReadOnly(True)
        self.input_bias.setMinimum(1)
        self.input_bias.setMaximum(1)
        self.input_bias.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.input_bias.setObjectName("input_bias")
        self.gridLayout.addWidget(self.input_bias, 5, 0, 1, 1)
        self.weight_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_2.setStyleSheet("background:green;color:white")
        self.weight_2.setObjectName("weight_2")
        self.gridLayout.addWidget(self.weight_2, 15, 4, 1, 1)
        self.horizontalSlider_bias_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_bias_2.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_bias_2.setMinimum(-100)
        self.horizontalSlider_bias_2.setMaximum(100)
        self.horizontalSlider_bias_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_bias_2.setObjectName("horizontalSlider_bias_2")
        self.gridLayout.addWidget(self.horizontalSlider_bias_2, 5, 2, 1, 2)
        self.horizontalSlider_bias_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_bias_4.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_bias_4.setMinimum(-100)
        self.horizontalSlider_bias_4.setMaximum(100)
        self.horizontalSlider_bias_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_bias_4.setObjectName("horizontalSlider_bias_4")
        self.gridLayout.addWidget(self.horizontalSlider_bias_4, 6, 16, 1, 5)
        self.sum_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.sum_3.setMinimumSize(QtCore.QSize(66, 20))
        self.sum_3.setStyleSheet("background:blue;color:white")
        self.sum_3.setReadOnly(True)
        self.sum_3.setObjectName("sum_3")
        self.gridLayout.addWidget(self.sum_3, 29, 13, 1, 2)
        self.feedback_bias_1 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_bias_1.setObjectName("feedback_bias_1")
        self.gridLayout.addWidget(self.feedback_bias_1, 4, 10, 1, 1)
        self.weight_bias_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_bias_3.setStyleSheet("background:blue;color:white")
        self.weight_bias_3.setObjectName("weight_bias_3")
        self.gridLayout.addWidget(self.weight_bias_3, 6, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 30, 0, 1, 1)
        self.horizontalSlider_11 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_11.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_11.setMinimum(-100)
        self.horizontalSlider_11.setMaximum(100)
        self.horizontalSlider_11.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_11.setObjectName("horizontalSlider_11")
        self.gridLayout.addWidget(self.horizontalSlider_11, 18, 16, 1, 5)
        self.feedback_3 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_3.setObjectName("feedback_3")
        self.gridLayout.addWidget(self.feedback_3, 16, 10, 1, 1)
        self.weight_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_8.setStyleSheet("background:green;color:white")
        self.weight_8.setObjectName("weight_8")
        self.gridLayout.addWidget(self.weight_8, 33, 4, 1, 1)
        self.weight_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_11.setStyleSheet("background:green;color:white")
        self.weight_11.setObjectName("weight_11")
        self.gridLayout.addWidget(self.weight_11, 18, 21, 1, 1)
        self.sum_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.sum_2.setMinimumSize(QtCore.QSize(66, 20))
        self.sum_2.setStyleSheet("background:green;color:white")
        self.sum_2.setReadOnly(True)
        self.sum_2.setObjectName("sum_2")
        self.gridLayout.addWidget(self.sum_2, 18, 13, 1, 2)
        self.input2 = QtWidgets.QSpinBox(self.centralwidget)
        self.input2.setMaximum(1)
        self.input2.setObjectName("input2")
        self.gridLayout.addWidget(self.input2, 19, 0, 1, 1)
        self.weight_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_9.setStyleSheet("background:blue;color:white")
        self.weight_9.setObjectName("weight_9")
        self.gridLayout.addWidget(self.weight_9, 34, 4, 1, 1)
        self.weight_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_5.setStyleSheet("background:green;color:white")
        self.weight_5.setObjectName("weight_5")
        self.gridLayout.addWidget(self.weight_5, 19, 4, 1, 1)
        self.feedback_5 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_5.setObjectName("feedback_5")
        self.gridLayout.addWidget(self.feedback_5, 19, 10, 1, 1)
        self.horizontalSlider_bias_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_bias_3.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_bias_3.setMinimum(-100)
        self.horizontalSlider_bias_3.setMaximum(100)
        self.horizontalSlider_bias_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_bias_3.setObjectName("horizontalSlider_bias_3")
        self.gridLayout.addWidget(self.horizontalSlider_bias_3, 6, 2, 1, 2)
        self.feedback_1 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_1.setObjectName("feedback_1")
        self.gridLayout.addWidget(self.feedback_1, 13, 10, 1, 1)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_2.setMinimum(-100)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout.addWidget(self.horizontalSlider_2, 15, 2, 1, 2)
        self.horizontalSlider_6 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_6.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_6.setMinimum(-100)
        self.horizontalSlider_6.setMaximum(100)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.gridLayout.addWidget(self.horizontalSlider_6, 28, 2, 1, 2)
        self.feedback_12 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_12.setObjectName("feedback_12")
        self.gridLayout.addWidget(self.feedback_12, 29, 22, 1, 1)
        self.feedback_7 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_7.setObjectName("feedback_7")
        self.gridLayout.addWidget(self.feedback_7, 30, 10, 1, 1)
        self.activation_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.activation_2.setMinimumSize(QtCore.QSize(66, 20))
        self.activation_2.setStyleSheet("background:green;color:white")
        self.activation_2.setReadOnly(True)
        self.activation_2.setObjectName("activation_2")
        self.gridLayout.addWidget(self.activation_2, 18, 15, 1, 1)
        self.weight_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_4.setStyleSheet("background:red;color:white")
        self.weight_4.setObjectName("weight_4")
        self.gridLayout.addWidget(self.weight_4, 18, 4, 1, 1)
        self.weight_bias_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_bias_4.setStyleSheet("background:rgb(255,0,255);color:white")
        self.weight_bias_4.setObjectName("weight_bias_4")
        self.gridLayout.addWidget(self.weight_bias_4, 6, 21, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(110, 32))
        self.label_5.setMaximumSize(QtCore.QSize(110, 32))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.feedback_bias_3 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_bias_3.setObjectName("feedback_bias_3")
        self.gridLayout.addWidget(self.feedback_bias_3, 6, 10, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setMinimumSize(QtCore.QSize(66, 20))
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 15, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalSlider_5 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_5.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_5.setMinimum(-100)
        self.horizontalSlider_5.setMaximum(100)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.gridLayout.addWidget(self.horizontalSlider_5, 19, 2, 1, 2)
        self.sum_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.sum_1.setMinimumSize(QtCore.QSize(66, 20))
        self.sum_1.setStyleSheet("background:red;color:white")
        self.sum_1.setReadOnly(True)
        self.sum_1.setObjectName("sum_1")
        self.gridLayout.addWidget(self.sum_1, 15, 13, 1, 2)
        self.weight_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_10.setStyleSheet("background:red;color:white")
        self.weight_10.setObjectName("weight_10")
        self.gridLayout.addWidget(self.weight_10, 15, 21, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 13, 15, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalSlider_9 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_9.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_9.setMinimum(-100)
        self.horizontalSlider_9.setMaximum(100)
        self.horizontalSlider_9.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_9.setObjectName("horizontalSlider_9")
        self.gridLayout.addWidget(self.horizontalSlider_9, 34, 2, 1, 2)
        self.feedback_10 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_10.setObjectName("feedback_10")
        self.gridLayout.addWidget(self.feedback_10, 15, 22, 1, 1)
        self.horizontalSlider_12 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_12.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_12.setMinimum(-100)
        self.horizontalSlider_12.setMaximum(100)
        self.horizontalSlider_12.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_12.setObjectName("horizontalSlider_12")
        self.gridLayout.addWidget(self.horizontalSlider_12, 29, 16, 1, 5)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_3.setMinimum(-100)
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout.addWidget(self.horizontalSlider_3, 16, 2, 1, 2)
        self.horizontalSlider_10 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_10.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_10.setMinimum(-100)
        self.horizontalSlider_10.setMaximum(100)
        self.horizontalSlider_10.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_10.setObjectName("horizontalSlider_10")
        self.gridLayout.addWidget(self.horizontalSlider_10, 15, 16, 1, 5)
        self.feedback_bias_2 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_bias_2.setObjectName("feedback_bias_2")
        self.gridLayout.addWidget(self.feedback_bias_2, 5, 10, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 18, 0, 1, 1)
        self.weight_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_1.setStyleSheet("background:red;color:white")
        self.weight_1.setObjectName("weight_1")
        self.gridLayout.addWidget(self.weight_1, 13, 4, 1, 1)
        self.weight_bias_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_bias_1.setStyleSheet("background:red;color:white")
        self.weight_bias_1.setObjectName("weight_bias_1")
        self.gridLayout.addWidget(self.weight_bias_1, 4, 4, 1, 1)
        self.horizontalSlider_1 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_1.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_1.setMinimum(-100)
        self.horizontalSlider_1.setMaximum(100)
        self.horizontalSlider_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_1.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_1.setTickInterval(0)
        self.horizontalSlider_1.setObjectName("horizontalSlider_1")
        self.gridLayout.addWidget(self.horizontalSlider_1, 13, 2, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 17, 24, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.feedback_11 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_11.setObjectName("feedback_11")
        self.gridLayout.addWidget(self.feedback_11, 18, 22, 1, 1)
        self.sum_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.sum_4.setMinimumSize(QtCore.QSize(66, 20))
        self.sum_4.setStyleSheet("background:black;color:white")
        self.sum_4.setReadOnly(True)
        self.sum_4.setObjectName("sum_4")
        self.gridLayout.addWidget(self.sum_4, 18, 23, 1, 1)
        self.feedback_8 = QtWidgets.QLabel(self.centralwidget)
        self.feedback_8.setObjectName("feedback_8")
        self.gridLayout.addWidget(self.feedback_8, 33, 10, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 13, 13, 1, 2, QtCore.Qt.AlignHCenter)
        self.horizontalSlider_8 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_8.setMinimumSize(QtCore.QSize(111, 22))
        self.horizontalSlider_8.setMinimum(-100)
        self.horizontalSlider_8.setMaximum(100)
        self.horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_8.setObjectName("horizontalSlider_8")
        self.gridLayout.addWidget(self.horizontalSlider_8, 33, 2, 1, 2)
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setMinimumSize(QtCore.QSize(180, 60))
        self.loadButton.setObjectName("loadButton")
        self.gridLayout.addWidget(self.loadButton, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1188, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionTrain = QtWidgets.QAction(MainWindow)
        self.actionTrain.setObjectName("actionTrain")
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionTrain)
        self.menuFile.addAction(self.actionRun)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # These commands are triggered through menu or shortcut key
        # load weights
        self.actionLoad.triggered.connect(lambda: self.getWeights())
        self.actionLoad.triggered.connect(lambda: self.clicked("Painokertoimet ladattu"))
        # save weights and save weights to file
        self.actionSave.triggered.connect(lambda: self.setWeights())
        #self.actionSave.triggered.connect(lambda: NN.saveWeights()) # Save to file
        # train the network
        self.actionTrain.triggered.connect(lambda: NN.trainNetwork())
        self.actionTrain.triggered.connect(lambda: self.getWeights())
        self.actionTrain.triggered.connect(lambda: self.runNetwork())
        self.actionTrain.triggered.connect(lambda: self.getHiddenWeights())
        # run the network with given inputs
        self.actionRun.triggered.connect(lambda: self.runNetwork())
        self.actionRun.triggered.connect(lambda: self.getHiddenWeights())
        # These commands are triggered through buttons
        # load weights
        self.loadButton.clicked.connect(lambda: self.getWeights())
        self.loadButton.clicked.connect(lambda: self.clicked("Painokertoimet ladattu"))
        # save weights
        self.saveButton.clicked.connect(lambda: self.setWeights())
        # run the network with given inputs
        self.runButton.clicked.connect(lambda: self.getWeights())
        self.runButton.clicked.connect(lambda: self.runNetwork())
        self.runButton.clicked.connect(lambda: self.getHiddenWeights())
        # sliders
        self.horizontalSlider_1.valueChanged.connect(lambda: self.valueChange(self.weight_1, self.horizontalSlider_1.value()))
        self.horizontalSlider_2.valueChanged.connect(lambda: self.valueChange(self.weight_2, self.horizontalSlider_2.value()))
        self.horizontalSlider_3.valueChanged.connect(lambda: self.valueChange(self.weight_3, self.horizontalSlider_3.value()))
        self.horizontalSlider_4.valueChanged.connect(lambda: self.valueChange(self.weight_4, self.horizontalSlider_4.value()))
        self.horizontalSlider_5.valueChanged.connect(lambda: self.valueChange(self.weight_5, self.horizontalSlider_5.value()))
        self.horizontalSlider_6.valueChanged.connect(lambda: self.valueChange(self.weight_6, self.horizontalSlider_6.value()))
        self.horizontalSlider_7.valueChanged.connect(lambda: self.valueChange(self.weight_7, self.horizontalSlider_7.value()))
        self.horizontalSlider_8.valueChanged.connect(lambda: self.valueChange(self.weight_8, self.horizontalSlider_8.value()))
        self.horizontalSlider_9.valueChanged.connect(lambda: self.valueChange(self.weight_9, self.horizontalSlider_9.value()))
        self.horizontalSlider_10.valueChanged.connect(lambda: self.valueChange(self.weight_10, self.horizontalSlider_10.value()))
        self.horizontalSlider_11.valueChanged.connect(lambda: self.valueChange(self.weight_11, self.horizontalSlider_11.value()))
        self.horizontalSlider_12.valueChanged.connect(lambda: self.valueChange(self.weight_12, self.horizontalSlider_12.value()))
        self.horizontalSlider_bias_1.valueChanged.connect(lambda: self.valueChange(self.weight_bias_1, self.horizontalSlider_bias_1.value()))
        self.horizontalSlider_bias_2.valueChanged.connect(lambda: self.valueChange(self.weight_bias_2, self.horizontalSlider_bias_2.value()))
        self.horizontalSlider_bias_3.valueChanged.connect(lambda: self.valueChange(self.weight_bias_3, self.horizontalSlider_bias_3.value()))
        self.horizontalSlider_bias_4.valueChanged.connect(lambda: self.valueChange(self.weight_bias_4, self.horizontalSlider_bias_4.value()))
        # inputs
        self.input1.valueChanged.connect(lambda: self.getWeights())
        self.input1.valueChanged.connect(lambda: self.runNetwork())
        self.input1.valueChanged.connect(lambda: self.getHiddenWeights())

        self.input2.valueChanged.connect(lambda: self.getWeights())
        self.input2.valueChanged.connect(lambda: self.runNetwork())
        self.input2.valueChanged.connect(lambda: self.getHiddenWeights())

        self.input3.valueChanged.connect(lambda: self.getWeights())
        self.input3.valueChanged.connect(lambda: self.runNetwork())
        self.input3.valueChanged.connect(lambda: self.getHiddenWeights())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Neuroverkon opetussovellus"))
        self.label_9.setText(_translate("MainWindow", "Summa"))
        self.feedback_2.setText(_translate("MainWindow", "+/-"))
        self.weight_bias_2.setPlaceholderText(_translate("MainWindow", "weight_bias_2"))
        self.runButton.setText(_translate("MainWindow", "Aja neuroverkko"))
        self.activation_3.setPlaceholderText(_translate("MainWindow", "aktivaatio_3"))
        self.label.setText(_translate("MainWindow", "Sisäpitoinen"))
        self.feedback_bias_4.setText(_translate("MainWindow", "+/-"))
        self.weight_3.setPlaceholderText(_translate("MainWindow", "weight_3"))
        self.activation_1.setPlaceholderText(_translate("MainWindow", "aktivaatio_1"))
        self.feedback_9.setText(_translate("MainWindow", "+/-"))
        self.weight_12.setPlaceholderText(_translate("MainWindow", "weight_12"))
        self.weight_6.setPlaceholderText(_translate("MainWindow", "weight_6"))
        self.feedback_4.setText(_translate("MainWindow", "+/-"))
        self.feedback_6.setText(_translate("MainWindow", "+/-"))
        self.saveButton.setText(_translate("MainWindow", "Tallenna painokertoimet"))
        self.weight_7.setPlaceholderText(_translate("MainWindow", "weight_7"))
        self.output_num.setPlaceholderText(_translate("MainWindow", "Lopputulos"))
        self.label_6.setText(_translate("MainWindow", "Painokertoimet"))
        self.weight_2.setPlaceholderText(_translate("MainWindow", "weight_2"))
        self.sum_3.setPlaceholderText(_translate("MainWindow", "summa_3"))
        self.feedback_bias_1.setText(_translate("MainWindow", "+/-"))
        self.weight_bias_3.setPlaceholderText(_translate("MainWindow", "weight_bias_3"))
        self.label_3.setText(_translate("MainWindow", "Taskut"))
        self.feedback_3.setText(_translate("MainWindow", "+/-"))
        self.weight_8.setPlaceholderText(_translate("MainWindow", "weight_8"))
        self.weight_11.setPlaceholderText(_translate("MainWindow", "weight_11"))
        self.sum_2.setPlaceholderText(_translate("MainWindow", "summa_2"))
        self.weight_9.setPlaceholderText(_translate("MainWindow", "weight_9"))
        self.weight_5.setPlaceholderText(_translate("MainWindow", "weight_5"))
        self.feedback_5.setText(_translate("MainWindow", "+/-"))
        self.feedback_1.setText(_translate("MainWindow", "+/-"))
        self.feedback_12.setText(_translate("MainWindow", "+/-"))
        self.feedback_7.setText(_translate("MainWindow", "+/-"))
        self.activation_2.setPlaceholderText(_translate("MainWindow", "aktivaatio_2"))
        self.weight_4.setPlaceholderText(_translate("MainWindow", "weight_4"))
        self.weight_bias_4.setPlaceholderText(_translate("MainWindow", "weight_bias_4"))
        self.label_5.setText(_translate("MainWindow", "Painokertoimet"))
        self.feedback_bias_3.setText(_translate("MainWindow", "+/-"))
        self.label_11.setText(_translate("MainWindow", "Bias"))
        self.sum_1.setPlaceholderText(_translate("MainWindow", "summa_1"))
        self.weight_10.setPlaceholderText(_translate("MainWindow", "weight_10"))
        self.label_8.setText(_translate("MainWindow", "Aktivaatio"))
        self.feedback_10.setText(_translate("MainWindow", "+/-"))
        self.feedback_bias_2.setText(_translate("MainWindow", "+/-"))
        self.label_2.setText(_translate("MainWindow", "Tuulenpitävä"))
        self.weight_1.setPlaceholderText(_translate("MainWindow", "weight_1"))
        self.weight_bias_1.setPlaceholderText(_translate("MainWindow", "weight_bias_1"))
        self.label_10.setText(_translate("MainWindow", "Aktivaatio"))
        self.label_4.setText(_translate("MainWindow", "Bias"))
        self.feedback_11.setText(_translate("MainWindow", "+/-"))
        self.sum_4.setPlaceholderText(_translate("MainWindow", "summa_4"))
        self.feedback_8.setText(_translate("MainWindow", "+/-"))
        self.label_7.setText(_translate("MainWindow", "Summa"))
        self.loadButton.setText(_translate("MainWindow", "Lataa painoketoimet"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionLoad.setStatusTip(_translate("MainWindow", "Load weights"))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save weights"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionTrain.setText(_translate("MainWindow", "Train"))
        self.actionTrain.setStatusTip(_translate("MainWindow", "Train Network"))
        self.actionTrain.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionRun.setStatusTip(_translate("MainWindow", "Run network with given input"))
        self.actionRun.setShortcut(_translate("MainWindow", "Ctrl+R"))

    def clicked(self, text):
        self.output.setText(text)

    def getWeights(self):
        # Load the weights from NN to ui and set the sliders accordingly
        self.weight_1.setText(str(NN.getWeights1(0,0)))
        self.horizontalSlider_1.setValue(int(NN.getWeights1(0,0)*10))
        self.weight_2.setText(str(NN.getWeights1(0,1)))
        self.horizontalSlider_2.setValue(int(NN.getWeights1(0,1)*10))
        self.weight_3.setText(str(NN.getWeights1(0,2)))
        self.horizontalSlider_3.setValue(int(NN.getWeights1(0,2)*10))
        self.weight_4.setText(str(NN.getWeights1(1,0)))
        self.horizontalSlider_4.setValue(int(NN.getWeights1(1,0)*10))
        self.weight_5.setText(str(NN.getWeights1(1,1)))
        self.horizontalSlider_5.setValue(int(NN.getWeights1(1,1)*10))
        self.weight_6.setText(str(NN.getWeights1(1,2)))
        self.horizontalSlider_6.setValue(int(NN.getWeights1(1,2)*10))
        self.weight_7.setText(str(NN.getWeights1(2,0)))
        self.horizontalSlider_7.setValue(int(NN.getWeights1(2,0)*10))
        self.weight_8.setText(str(NN.getWeights1(2,1)))
        self.horizontalSlider_8.setValue(int(NN.getWeights1(2,1)*10))
        self.weight_9.setText(str(NN.getWeights1(2,2)))
        self.horizontalSlider_9.setValue(int(NN.getWeights1(2,2)*10))
        self.weight_10.setText(str(NN.getWeights2(0,0)))
        self.horizontalSlider_10.setValue(int(NN.getWeights2(0,0)*10))
        self.weight_11.setText(str(NN.getWeights2(1,0)))
        self.horizontalSlider_11.setValue(int(NN.getWeights2(1,0)*10))
        self.weight_12.setText(str(NN.getWeights2(2,0)))
        self.horizontalSlider_12.setValue(int(NN.getWeights2(2,0)*10))
        self.weight_bias_1.setText(str(NN.getWeights1(3,0)))
        self.horizontalSlider_bias_1.setValue(int(NN.getWeights1(3,0)*10))
        self.weight_bias_2.setText(str(NN.getWeights1(3,1)))
        self.horizontalSlider_bias_2.setValue(int(NN.getWeights1(3,1)*10))
        self.weight_bias_3.setText(str(NN.getWeights1(3,2)))
        self.horizontalSlider_bias_3.setValue(int(NN.getWeights1(3,2)*10))
        self.weight_bias_4.setText(str(NN.getWeights2(3,0)))
        self.horizontalSlider_bias_4.setValue(int(NN.getWeights2(3,0)*10))

    def getHiddenWeights(self):
        # Get the feedback from the hidden NN to ui
        self.feedback1,self.feedback2 = NN.trainHiddenNetwork()
        self.feedback_1.setText(self.getFeedback(self.feedback1[0,0], NN.W1[0,0]))
        self.feedback_2.setText(self.getFeedback(self.feedback1[0,1], NN.W1[0,1]))
        self.feedback_3.setText(self.getFeedback(self.feedback1[0,2], NN.W1[0,2]))
        self.feedback_4.setText(self.getFeedback(self.feedback1[1,0], NN.W1[1,0]))
        self.feedback_5.setText(self.getFeedback(self.feedback1[1,1], NN.W1[1,1]))
        self.feedback_6.setText(self.getFeedback(self.feedback1[1,2], NN.W1[1,2]))
        self.feedback_7.setText(self.getFeedback(self.feedback1[2,0], NN.W1[2,0]))
        self.feedback_8.setText(self.getFeedback(self.feedback1[2,1], NN.W1[2,1]))
        self.feedback_9.setText(self.getFeedback(self.feedback1[2,2], NN.W1[2,2]))
        self.feedback_bias_1.setText(self.getFeedback(self.feedback1[3,0], NN.W1[3,0]))
        self.feedback_bias_2.setText(self.getFeedback(self.feedback1[3,1], NN.W1[3,1]))
        self.feedback_bias_3.setText(self.getFeedback(self.feedback1[3,2], NN.W1[3,2]))
        self.feedback_10.setText(self.getFeedback(self.feedback2[0,0], NN.W2[0,0]))
        self.feedback_11.setText(self.getFeedback(self.feedback2[1,0], NN.W2[1,0]))
        self.feedback_12.setText(self.getFeedback(self.feedback2[2,0], NN.W2[2,0]))
        self.feedback_bias_4.setText(self.getFeedback(self.feedback2[3,0], NN.W2[3,0]))

    def getFeedback(self, hidden, true):
        # Defines what kind of feedback is set to the ui
        if(abs(float(hidden)-float(true)) >=0.0 and abs(float(hidden)-float(true)) <= 0.1):
          return "="
        elif(float(hidden)-float(true) > 0.0 and float(hidden)-float(true) < 0.5):
          return "+"
        elif(float(hidden)-float(true) > 0.5 and float(hidden)-float(true) < 1.5):
          return "++"
        elif(float(hidden)-float(true) > 1.5):
          return "+++"
        elif(float(hidden)-float(true) < 0.0 and float(hidden)-float(true) > -0.5):
          return "-"
        elif(float(hidden)-float(true) < -0.5 and float(hidden)-float(true) > -1.5):
          return "--"
        elif(float(hidden)-float(true) < -1.5):
          return "---"
        else:
          return "?" # This shows that something unexpected happened

    def valueChange(self, weight, value):
        weight.setText(str(value/10))

    def setWeights(self):
        # Try and save the weights from ui to NN
        try:
            NN.setWeights1(self.weight_1.text(),0,0)
            NN.setWeights1(self.weight_2.text(),0,1)
            NN.setWeights1(self.weight_3.text(),0,2)
            NN.setWeights1(self.weight_4.text(),1,0)
            NN.setWeights1(self.weight_5.text(),1,1)
            NN.setWeights1(self.weight_6.text(),1,2)
            NN.setWeights1(self.weight_7.text(),2,0)
            NN.setWeights1(self.weight_8.text(),2,1)
            NN.setWeights1(self.weight_9.text(),2,2)
            NN.setWeights2(self.weight_10.text(),0,0)
            NN.setWeights2(self.weight_11.text(),1,0)
            NN.setWeights2(self.weight_12.text(),2,0)
            NN.setWeights1(self.weight_bias_1.text(),3,0)
            NN.setWeights1(self.weight_bias_2.text(),3,1)
            NN.setWeights1(self.weight_bias_3.text(),3,2)
            NN.setWeights2(self.weight_bias_4.text(),3,0)
            self.clicked("Painokertoimet tallennettu!")
        # If the previous step failed, then remind the user to load or manually set the weights first
        except:
            self.clicked("Aseta ensin painokertoimet!")

    def runNetwork(self):
        # runs the NN with given weights and returns the sums, activation functions and classification result
        input_nn = np.array([int(self.input1.text()),int(self.input2.text()),int(self.input3.text())])
        result = NN.classification(input_nn) # result is a list of two items, value and class
        self.sum_1.setText(str(np.round(NN.z[0],3))) # sum of node 1 (red)
        self.sum_2.setText(str(np.round(NN.z[1],3))) # sum of node 2 (green)
        self.sum_3.setText(str(np.round(NN.z[2],3))) # sum of node 3 (blue)
        self.sum_4.setText(str(np.round(NN.z3,3))[1:-1]) # sum of node 4 (black), "[1:-1] removes brackets"
        self.activation_1.setText(str(np.round(NN.z2[0],3))) # activation function of node 1 (red)
        self.activation_2.setText(str(np.round(NN.z2[1],3))) # activation function of node 2 (green)
        self.activation_3.setText(str(np.round(NN.z2[2],3))) # activation function of node 3 (blue)
        self.output_num.setText(str(np.round(result[0],3))[1:-1]) # output value (black), "[1:-1] removes brackets"
        self.output.setText(str(result[1])) # output class

class Neural_Network(object):
  def __init__(self):
    #parameters
    self.inputSize = 3
    self.outputSize = 1
    self.hiddenSize = 3
    self.bias = 1
    #weights
    self.W1 = np.random.randn(self.inputSize + self.bias, self.hiddenSize) # (4x3) weight matrix from input to hidden layer
    self.W2 = np.random.randn(self.hiddenSize + self.bias, self.outputSize) # (4x1) weight matrix from hidden to output layer

  def forward_hidden(self, W1_hidden, W2_hidden, X):
    # forward propagation through our network
    self.z_hidden = np.dot(X, W1_hidden[0:3]) + np.dot(self.bias, W1_hidden[3]) # dot product of X (input) and first set of 3x3 weights
    self.z2_hidden = self.sigmoid(self.z_hidden) # activation function
    self.z3_hidden = np.dot(self.z2_hidden, W2_hidden[0:3]) + np.dot(self.bias, W2_hidden[3]) # dot product of hidden layer (z2) and second set of 3x1 weights
    o = self.sigmoid(self.z3_hidden) # final activation function
    return o

  def train_hidden (self, W1_hidden, W2_hidden, X, y):
    o = self.forward_hidden(W1_hidden, W2_hidden, X)
    self.backward_hidden(W1_hidden, W2_hidden, X, y, o)

  def trainHiddenNetwork(self):
    # trains the hidden NN that is used to give feedback for the ui
    W1_hidden = self.W1.copy() # copy the current weights for layer 1
    W2_hidden = self.W2.copy() # copy the current weights for layer 2
    X = np.array([[1,0,1], [0,1,1], [1,0,0], [1,1,1], [1,1,0], [0,0,0], [0,1,0]]) # input data
    y = np.array([[1], [0.66], [0.38], [0.12], [0.12], [0.12], [0.66]]) # output
    for i in range(500): # trains the hidden NN given times
      self.train_hidden(W1_hidden, W2_hidden,X, y)
    return W1_hidden, W2_hidden

  def forward(self, X):
    # forward propagation through our network
    self.z = np.dot(X, self.W1[0:3]) + np.dot(self.bias, self.W1[3]) # dot product of X (input) and first set of 3x3 weights + dot product of bias
    self.z2 = self.sigmoid(self.z) # activation function
    self.z3 = np.dot(self.z2, self.W2[0:3]) + np.dot(self.bias, self.W2[3]) # dot product of hidden layer (z2) and second set of 3x1 weights + dot product of bias
    o = self.sigmoid(self.z3) # final activation function
    return o

  def sigmoid(self, s):
    # activation function
    return 1/(1+np.exp(-s))

  def sigmoidPrime(self, s):
    # derivative of sigmoid
    return s * (1 - s)

  def backward(self, X, y, o):
    # backward propagate through the network
    self.o_error = y - o # error in output
    self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error
    self.o_delta_bias = np.sum(self.o_delta, axis=0) # How much the second bias needs to be changed

    self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
    self.z2_delta = self.z2_error[:,:3]*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error
    self.z2_delta_bias = np.sum(self.z2_delta, axis=0) # How much the first bias needs to be changed

    self.W1[:3] += X.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
    self.W1[3] += self.z2_delta_bias # adjusting first set (input --> hidden) bias weights

    self.W2[:3] += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights
    self.W2[3] += self.o_delta_bias # adjusting second set (hidden --> output) bias weights

  def backward_hidden(self, W1_hidden, W2_hidden, X, y, o):
    # backward propagate through the network
    self.o_error_hidden = y - o # error in output
    self.o_delta_hidden = self.o_error_hidden*self.sigmoidPrime(o) # applying derivative of sigmoid to error
    self.o_delta_bias_hidden = np.sum(self.o_delta_hidden, axis=0)

    self.z2_error_hidden = self.o_delta_hidden.dot(W2_hidden.T) # z2 error: how much our hidden layer weights contributed to output error
    self.z2_delta_hidden = self.z2_error_hidden[:,:3]*self.sigmoidPrime(self.z2_hidden) # applying derivative of sigmoid to z2 error
    self.z2_delta_bias_hidden = np.sum(self.z2_delta_hidden, axis=0)

    W1_hidden[:3] += X.T.dot(self.z2_delta_hidden) # adjusting first set (input --> hidden) weights
    W1_hidden[3] += self.z2_delta_bias_hidden

    W2_hidden[:3] += self.z2_hidden.T.dot(self.o_delta_hidden) # adjusting second set (hidden --> output) weights
    W2_hidden[3] += self.o_delta_bias_hidden

  def train (self, X, y):
    o = self.forward(X)
    self.backward(X, y, o)

  def saveWeights(self):
    # Save weights to two seperate files
    np.savetxt("w1_nn11_4.txt", self.W1, fmt="%s")
    np.savetxt("w2_nn11_4.txt", self.W2, fmt="%s")

  def getWeights1(self, index1, index2):
    return round(self.W1[index1, index2],3)

  def getWeights2(self, index1, index2):
    return round(self.W2[index1, index2],3)

  def setWeights1(self, text, index1, index2):
    self.W1[index1,index2] = text

  def setWeights2(self, text, index1, index2):
    self.W2[index1,index2] = text

  def trainNetwork(self):
    X = np.array([[1,0,1], [0,1,1], [1,0,0], [1,1,1], [1,1,0], [0,0,0], [0,1,0]]) # input data
    y = np.array([[1], [0.66], [0.38], [0.12], [0.12], [0.12], [0.66]]) # output
    for i in range(20): # trains the NN given times
      self.train(X, y)

  def classification(self, xPredicted):
    object_class = self.forward(xPredicted)
    if (object_class > 0.75):
      object_string = "Housut"
      return object_class, object_string
    elif (object_class > 0.5):
      object_string = "Takki"
      return object_class, object_string
    elif (object_class > 0.26):
      object_string = "T-Paita"
      return object_class, object_string
    else:
      object_string = "Tuntematon"
      return object_class, object_string

if __name__ == "__main__":
    import sys
    NN = Neural_Network()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
