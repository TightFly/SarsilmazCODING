# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sarsilmaz_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from dronekit import Command, connect, VehicleMode, LocationGlobalRelative
from PyQt5.QtWidgets import *
import time
from pymavlink import mavutil
import math




#DRONE BAĞLANTISI
#connection_string="127.0.0.1:14551"
connection_string="192.168.137.1:14550" 
global iha
#iha=connect(connection_string,wait_ready=True,timeout=100)
iha=connect(connection_string,wait_ready=True,timeout=100,baud=115200)








class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 866)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_mission = QtWidgets.QFrame(self.centralwidget)
        self.frame_mission.setGeometry(QtCore.QRect(520, 60, 111, 321))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.frame_mission.setFont(font)
        self.frame_mission.setAutoFillBackground(True)
        self.frame_mission.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mission.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mission.setObjectName("frame_mission")
        self.button_mission4 = QtWidgets.QPushButton(self.frame_mission)
        self.button_mission4.setGeometry(QtCore.QRect(10, 160, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_mission4.setFont(font)
        self.button_mission4.setObjectName("button_mission4")
        self.button_mission2 = QtWidgets.QPushButton(self.frame_mission)
        self.button_mission2.setGeometry(QtCore.QRect(10, 80, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_mission2.setFont(font)
        self.button_mission2.setObjectName("button_mission2")
        self.button_mission3 = QtWidgets.QPushButton(self.frame_mission)
        self.button_mission3.setGeometry(QtCore.QRect(10, 120, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_mission3.setFont(font)
        self.button_mission3.setObjectName("button_mission3")
        self.button_mission1 = QtWidgets.QPushButton(self.frame_mission)
        self.button_mission1.setGeometry(QtCore.QRect(10, 40, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_mission1.setFont(font)
        self.button_mission1.setStyleSheet("selection-background-color: rgb(238, 238, 236);")
        self.button_mission1.setObjectName("button_mission1")
        self.label_mission = QtWidgets.QLabel(self.frame_mission)
        self.label_mission.setGeometry(QtCore.QRect(20, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_mission.setFont(font)
        self.label_mission.setObjectName("label_mission")
        self.button_mission5 = QtWidgets.QPushButton(self.frame_mission)
        self.button_mission5.setGeometry(QtCore.QRect(10, 200, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_mission5.setFont(font)
        self.button_mission5.setObjectName("button_mission5")
        self.button_mission6 = QtWidgets.QPushButton(self.frame_mission)
        self.button_mission6.setGeometry(QtCore.QRect(10, 240, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_mission6.setFont(font)
        self.button_mission6.setObjectName("button_mission6")
        self.frame_mode = QtWidgets.QFrame(self.centralwidget)
        self.frame_mode.setGeometry(QtCore.QRect(730, 60, 111, 321))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.frame_mode.setFont(font)
        self.frame_mode.setAutoFillBackground(True)
        self.frame_mode.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mode.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mode.setObjectName("frame_mode")
        self.button_mode_poshold_2 = QtWidgets.QPushButton(self.frame_mode)
        self.button_mode_poshold_2.setGeometry(QtCore.QRect(10, 200, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_mode_poshold_2.setFont(font)
        self.button_mode_poshold_2.setObjectName("button_mode_poshold_2")
        self.button_mode_loiter_2 = QtWidgets.QPushButton(self.frame_mode)
        self.button_mode_loiter_2.setGeometry(QtCore.QRect(10, 240, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_mode_loiter_2.setFont(font)
        self.button_mode_loiter_2.setObjectName("button_mode_loiter_2")
        self.button_mode_althold_2 = QtWidgets.QPushButton(self.frame_mode)
        self.button_mode_althold_2.setGeometry(QtCore.QRect(10, 280, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_mode_althold_2.setFont(font)
        self.button_mode_althold_2.setObjectName("button_mode_althold_2")
        self.button_mode_land = QtWidgets.QPushButton(self.frame_mode)
        self.button_mode_land.setGeometry(QtCore.QRect(10, 80, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_mode_land.setFont(font)
        self.button_mode_land.setObjectName("button_mode_land")
        self.button_mode_guided = QtWidgets.QPushButton(self.frame_mode)
        self.button_mode_guided.setGeometry(QtCore.QRect(10, 160, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_mode_guided.setFont(font)
        self.button_mode_guided.setObjectName("button_mode_guided")
        self.button_mode_rtl = QtWidgets.QPushButton(self.frame_mode)
        self.button_mode_rtl.setGeometry(QtCore.QRect(10, 40, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_mode_rtl.setFont(font)
        self.button_mode_rtl.setObjectName("button_mode_rtl")
        self.labell_mode = QtWidgets.QLabel(self.frame_mode)
        self.labell_mode.setGeometry(QtCore.QRect(30, 11, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labell_mode.setFont(font)
        self.labell_mode.setObjectName("labell_mode")
        self.button_mode_stabilize = QtWidgets.QPushButton(self.frame_mode)
        self.button_mode_stabilize.setGeometry(QtCore.QRect(10, 120, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_mode_stabilize.setFont(font)
        self.button_mode_stabilize.setObjectName("button_mode_stabilize")
        self.frame_command = QtWidgets.QFrame(self.centralwidget)
        self.frame_command.setGeometry(QtCore.QRect(350, 60, 111, 201))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.frame_command.setFont(font)
        self.frame_command.setAutoFillBackground(True)
        self.frame_command.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_command.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_command.setObjectName("frame_command")
        self.button_disarm = QtWidgets.QPushButton(self.frame_command)
        self.button_disarm.setGeometry(QtCore.QRect(10, 80, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_disarm.setFont(font)
        self.button_disarm.setObjectName("button_disarm")
        self.button_arm = QtWidgets.QPushButton(self.frame_command)
        self.button_arm.setGeometry(QtCore.QRect(10, 40, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_arm.setFont(font)
        self.button_arm.setObjectName("button_arm")
        self.label_command = QtWidgets.QLabel(self.frame_command)
        self.label_command.setGeometry(QtCore.QRect(10, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_command.setFont(font)
        self.label_command.setObjectName("label_command")
        self.button_takeoff = QtWidgets.QPushButton(self.frame_command)
        self.button_takeoff.setGeometry(QtCore.QRect(10, 120, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_takeoff.setFont(font)
        self.button_takeoff.setObjectName("button_takeoff")
        self.frame_drone_control = QtWidgets.QFrame(self.centralwidget)
        self.frame_drone_control.setGeometry(QtCore.QRect(10, 60, 281, 201))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.frame_drone_control.setFont(font)
        self.frame_drone_control.setAutoFillBackground(True)
        self.frame_drone_control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_drone_control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_drone_control.setObjectName("frame_drone_control")
        self.button_up = QtWidgets.QPushButton(self.frame_drone_control)
        self.button_up.setGeometry(QtCore.QRect(0, 40, 132, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_up.setFont(font)
        self.button_up.setObjectName("button_up")
        self.button_down = QtWidgets.QPushButton(self.frame_drone_control)
        self.button_down.setGeometry(QtCore.QRect(150, 40, 131, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_down.setFont(font)
        self.button_down.setObjectName("button_down")
        self.button_left = QtWidgets.QPushButton(self.frame_drone_control)
        self.button_left.setGeometry(QtCore.QRect(0, 90, 132, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_left.setFont(font)
        self.button_left.setObjectName("button_left")
        self.button_right = QtWidgets.QPushButton(self.frame_drone_control)
        self.button_right.setGeometry(QtCore.QRect(150, 90, 131, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_right.setFont(font)
        self.button_right.setObjectName("button_right")
        self.button_backward = QtWidgets.QPushButton(self.frame_drone_control)
        self.button_backward.setGeometry(QtCore.QRect(0, 140, 132, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_backward.setFont(font)
        self.button_backward.setObjectName("button_backward")
        self.button_forward = QtWidgets.QPushButton(self.frame_drone_control)
        self.button_forward.setGeometry(QtCore.QRect(150, 140, 131, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_forward.setFont(font)
        self.button_forward.setObjectName("button_forward")
        self.label_dronecontrol = QtWidgets.QLabel(self.frame_drone_control)
        self.label_dronecontrol.setGeometry(QtCore.QRect(70, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_dronecontrol.setFont(font)
        self.label_dronecontrol.setObjectName("label_dronecontrol")
        self.frame_parameter_info = QtWidgets.QFrame(self.centralwidget)
        self.frame_parameter_info.setGeometry(QtCore.QRect(10, 300, 451, 511))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.frame_parameter_info.setFont(font)
        self.frame_parameter_info.setAutoFillBackground(True)
        self.frame_parameter_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_parameter_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_parameter_info.setObjectName("frame_parameter_info")
        self.label_home_location = QtWidgets.QLabel(self.frame_parameter_info)
        self.label_home_location.setGeometry(QtCore.QRect(10, 280, 131, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_home_location.setFont(font)
        self.label_home_location.setObjectName("label_home_location")
        self.label_arm = QtWidgets.QLabel(self.frame_parameter_info)
        self.label_arm.setGeometry(QtCore.QRect(320, 160, 81, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_arm.setFont(font)
        self.label_arm.setObjectName("label_arm")
        self.label_mode = QtWidgets.QLabel(self.frame_parameter_info)
        self.label_mode.setGeometry(QtCore.QRect(320, 60, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_mode.setFont(font)
        self.label_mode.setObjectName("label_mode")
        self.line_armable = QtWidgets.QLineEdit(self.frame_parameter_info)
        self.line_armable.setGeometry(QtCore.QRect(320, 130, 111, 21))
        self.line_armable.setReadOnly(True)
        self.line_armable.setObjectName("line_armable")
        self.line_arm = QtWidgets.QLineEdit(self.frame_parameter_info)
        self.line_arm.setGeometry(QtCore.QRect(320, 180, 113, 21))
        self.line_arm.setReadOnly(True)
        self.line_arm.setObjectName("line_arm")
        self.label_armable = QtWidgets.QLabel(self.frame_parameter_info)
        self.label_armable.setGeometry(QtCore.QRect(320, 110, 81, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_armable.setFont(font)
        self.label_armable.setObjectName("label_armable")
        self.label_altitude = QtWidgets.QLabel(self.frame_parameter_info)
        self.label_altitude.setGeometry(QtCore.QRect(320, 210, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_altitude.setFont(font)
        self.label_altitude.setObjectName("label_altitude")
        self.line_mode = QtWidgets.QLineEdit(self.frame_parameter_info)
        self.line_mode.setGeometry(QtCore.QRect(320, 80, 113, 21))
        self.line_mode.setReadOnly(True)
        self.line_mode.setObjectName("line_mode")
        self.line_velocity = QtWidgets.QLineEdit(self.frame_parameter_info)
        self.line_velocity.setGeometry(QtCore.QRect(320, 280, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_velocity.setFont(font)
        self.line_velocity.setReadOnly(True)
        self.line_velocity.setObjectName("line_velocity")
        self.label_velocity = QtWidgets.QLabel(self.frame_parameter_info)
        self.label_velocity.setGeometry(QtCore.QRect(320, 260, 81, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_velocity.setFont(font)
        self.label_velocity.setObjectName("label_velocity")
        self.line_altitude = QtWidgets.QLineEdit(self.frame_parameter_info)
        self.line_altitude.setGeometry(QtCore.QRect(320, 230, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_altitude.setFont(font)
        self.line_altitude.setReadOnly(True)
        self.line_altitude.setObjectName("line_altitude")
        self.label_airspeed = QtWidgets.QLabel(self.frame_parameter_info)
        self.label_airspeed.setGeometry(QtCore.QRect(320, 310, 81, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_airspeed.setFont(font)
        self.label_airspeed.setObjectName("label_airspeed")
        self.line_airspeed = QtWidgets.QLineEdit(self.frame_parameter_info)
        self.line_airspeed.setGeometry(QtCore.QRect(320, 330, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_airspeed.setFont(font)
        self.line_airspeed.setReadOnly(True)
        self.line_airspeed.setObjectName("line_airspeed")
        self.label_groundspeed = QtWidgets.QLabel(self.frame_parameter_info)
        self.label_groundspeed.setGeometry(QtCore.QRect(320, 360, 121, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_groundspeed.setFont(font)
        self.label_groundspeed.setObjectName("label_groundspeed")
        self.line_groundspeed = QtWidgets.QLineEdit(self.frame_parameter_info)
        self.line_groundspeed.setGeometry(QtCore.QRect(320, 380, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_groundspeed.setFont(font)
        self.line_groundspeed.setReadOnly(True)
        self.line_groundspeed.setObjectName("line_groundspeed")
        self.label_gps = QtWidgets.QLabel(self.frame_parameter_info)
        self.label_gps.setGeometry(QtCore.QRect(10, 390, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_gps.setFont(font)
        self.label_gps.setObjectName("label_gps")
        self.label_parameter_info = QtWidgets.QLabel(self.frame_parameter_info)
        self.label_parameter_info.setGeometry(QtCore.QRect(10, 20, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_parameter_info.setFont(font)
        self.label_parameter_info.setObjectName("label_parameter_info")
        self.label_battery = QtWidgets.QLabel(self.frame_parameter_info)
        self.label_battery.setGeometry(QtCore.QRect(10, 60, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_battery.setFont(font)
        self.label_battery.setObjectName("label_battery")
        self.label_global_location = QtWidgets.QLabel(self.frame_parameter_info)
        self.label_global_location.setGeometry(QtCore.QRect(10, 170, 141, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_global_location.setFont(font)
        self.label_global_location.setObjectName("label_global_location")
        self.plainText_battery = QtWidgets.QPlainTextEdit(self.frame_parameter_info)
        self.plainText_battery.setGeometry(QtCore.QRect(10, 80, 231, 81))
        self.plainText_battery.setReadOnly(True)
        self.plainText_battery.setObjectName("plainText_battery")
        self.plainText_global_location = QtWidgets.QPlainTextEdit(self.frame_parameter_info)
        self.plainText_global_location.setGeometry(QtCore.QRect(10, 190, 231, 81))
        self.plainText_global_location.setReadOnly(True)
        self.plainText_global_location.setObjectName("plainText_global_location")
        self.plainText_home_location = QtWidgets.QPlainTextEdit(self.frame_parameter_info)
        self.plainText_home_location.setGeometry(QtCore.QRect(10, 300, 231, 81))
        self.plainText_home_location.setReadOnly(True)
        self.plainText_home_location.setObjectName("plainText_home_location")
        self.plainText_gps = QtWidgets.QPlainTextEdit(self.frame_parameter_info)
        self.plainText_gps.setGeometry(QtCore.QRect(10, 410, 231, 81))
        self.plainText_gps.setReadOnly(True)
        self.plainText_gps.setObjectName("plainText_gps")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(520, 420, 321, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.button_goloc_go = QtWidgets.QPushButton(self.frame)
        self.button_goloc_go.setGeometry(QtCore.QRect(220, 80, 91, 121))
        self.button_goloc_go.setObjectName("button_goloc_go")
        self.line_goloc_altitude = QtWidgets.QLineEdit(self.frame)
        self.line_goloc_altitude.setGeometry(QtCore.QRect(10, 180, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_goloc_altitude.setFont(font)
        self.line_goloc_altitude.setReadOnly(False)
        self.line_goloc_altitude.setObjectName("line_goloc_altitude")
        self.label_goloc_altitude = QtWidgets.QLabel(self.frame)
        self.label_goloc_altitude.setGeometry(QtCore.QRect(10, 160, 91, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_goloc_altitude.setFont(font)
        self.label_goloc_altitude.setObjectName("label_goloc_altitude")
        self.line_goloc_longitude = QtWidgets.QLineEdit(self.frame)
        self.line_goloc_longitude.setGeometry(QtCore.QRect(10, 130, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_goloc_longitude.setFont(font)
        self.line_goloc_longitude.setReadOnly(False)
        self.line_goloc_longitude.setObjectName("line_goloc_longitude")
        self.label_goloc_latitude = QtWidgets.QLabel(self.frame)
        self.label_goloc_latitude.setGeometry(QtCore.QRect(10, 60, 81, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_goloc_latitude.setFont(font)
        self.label_goloc_latitude.setObjectName("label_goloc_latitude")
        self.label_goloc_longitude = QtWidgets.QLabel(self.frame)
        self.label_goloc_longitude.setGeometry(QtCore.QRect(10, 110, 91, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_goloc_longitude.setFont(font)
        self.label_goloc_longitude.setObjectName("label_goloc_longitude")
        self.line_goloc_latitude = QtWidgets.QLineEdit(self.frame)
        self.line_goloc_latitude.setGeometry(QtCore.QRect(10, 80, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_goloc_latitude.setFont(font)
        self.line_goloc_latitude.setReadOnly(False)
        self.line_goloc_latitude.setObjectName("line_goloc_latitude")
        self.label_mission_2 = QtWidgets.QLabel(self.frame)
        self.label_mission_2.setGeometry(QtCore.QRect(90, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_mission_2.setFont(font)
        self.label_mission_2.setObjectName("label_mission_2")
        self.frame.raise_()
        self.frame_mission.raise_()
        self.frame_mode.raise_()
        self.frame_command.raise_()
        self.frame_drone_control.raise_()
        self.frame_parameter_info.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_mission4.setText(_translate("MainWindow", "MISSION 4"))
        self.button_mission2.setText(_translate("MainWindow", "MISSION 2"))
        self.button_mission3.setText(_translate("MainWindow", "MISSION 3"))
        self.button_mission1.setText(_translate("MainWindow", "MISSION 1"))
        self.label_mission.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ef2929;\">MISSION</span></p></body></html>"))
        self.button_mission5.setText(_translate("MainWindow", "MISSION 5"))
        self.button_mission6.setText(_translate("MainWindow", "MISSION 6"))
        self.button_mode_poshold_2.setText(_translate("MainWindow", "POSHOLD"))
        self.button_mode_loiter_2.setText(_translate("MainWindow", "LOITER"))
        self.button_mode_althold_2.setText(_translate("MainWindow", "ALTHOLD"))
        self.button_mode_land.setText(_translate("MainWindow", "LAND"))
        self.button_mode_guided.setText(_translate("MainWindow", "GUIDED"))
        self.button_mode_rtl.setText(_translate("MainWindow", "RTL"))
        self.labell_mode.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ef2929;\">MODE</span></p></body></html>"))
        self.button_mode_stabilize.setText(_translate("MainWindow", "STABILIZE"))
        self.button_disarm.setText(_translate("MainWindow", "DISARM"))
        self.button_arm.setText(_translate("MainWindow", "ARM"))
        self.label_command.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ef2929;\">COMMAND</span></p></body></html>"))
        self.button_takeoff.setText(_translate("MainWindow", "TAKEOFF"))
        self.button_up.setText(_translate("MainWindow", "UP"))
        self.button_down.setText(_translate("MainWindow", "DOWN"))
        self.button_left.setText(_translate("MainWindow", "LEFT"))
        self.button_right.setText(_translate("MainWindow", "RIGHT"))
        self.button_backward.setText(_translate("MainWindow", "BACKWARD"))
        self.button_forward.setText(_translate("MainWindow", "FORWARD"))
        self.label_dronecontrol.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ef2929;\">DRONE CONTROL</span></p></body></html>"))
        self.label_home_location.setText(_translate("MainWindow", "HOME LOCATION"))
        self.label_arm.setText(_translate("MainWindow", "ARM"))
        self.label_mode.setText(_translate("MainWindow", "MODE"))
        self.label_armable.setText(_translate("MainWindow", "ARMABLE"))
        self.label_altitude.setText(_translate("MainWindow", "ALTITUDE"))
        self.label_velocity.setText(_translate("MainWindow", "VELOCITY"))
        self.label_airspeed.setText(_translate("MainWindow", "AIR SPEED"))
        self.label_groundspeed.setText(_translate("MainWindow", "GROUND SPEED"))
        self.label_gps.setText(_translate("MainWindow", "GPS"))
        self.label_parameter_info.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ef2929;\">PARAMETER &amp; SYSTEM INFORMATION</span></p><p><span style=\" text-decoration: underline;\"><br/></span></p></body></html>"))
        self.label_battery.setText(_translate("MainWindow", "BATTERY"))
        self.label_global_location.setText(_translate("MainWindow", "GLOBAL LOCATION"))
        self.button_goloc_go.setText(_translate("MainWindow", "GO"))
        self.label_goloc_altitude.setText(_translate("MainWindow", "ALTITUDE"))
        self.label_goloc_latitude.setText(_translate("MainWindow", "LATITUDE"))
        self.label_goloc_longitude.setText(_translate("MainWindow", "LONGITUDE"))
        self.label_mission_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ef2929;\">GO TO LOCATION</span></p></body></html>"))
            
        
            
        
            
            
            
            
        #PUSH BUTONA FONKSİYON ATANMASI
        self.button_mission1.clicked.connect(self.mission1)
        
        #**********************************************************************
        
        self.button_mode_land.clicked.connect(self.mod_degistir_land)
        self.button_mode_guided.clicked.connect(self.mod_degistir_guided)
        self.button_mode_rtl.clicked.connect(self.mod_degistir_rtl)
        self.button_mode_stabilize.clicked.connect(self.mod_degistir_stabilize)
        self.button_mode_poshold_2.clicked.connect(self.mod_degistir_poshold)
        self.button_mode_loiter_2.clicked.connect(self.mod_degistir_loiter)
        self.button_mode_althold_2.clicked.connect(self.mod_degistir_althold)
        
        #**********************************************************************
        
        self.button_forward.clicked.connect(self.direction_forward)
        self.button_backward.clicked.connect(self.direction_backward)
        self.button_right.clicked.connect(self.direction_right)
        self.button_left.clicked.connect(self.direction_left)
        self.button_up.clicked.connect(self.direction_up)
        self.button_down.clicked.connect(self.direction_down)
        
        #**********************************************************************
        self.button_arm.clicked.connect(self.arm)
        self.button_disarm.clicked.connect(self.disarm)
        #**********************************************************************
        self.button_takeoff.clicked.connect(self.takeoff)
    
    
    
    
    
    
    
    #ATANAN FONKSİYONLARIN TANIMI
    #**************************************************************************
    
    
        
    def mission1(self):
        
        while True:
            
         msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111111000,
          0, 4, 0, #pozisyonlar(metre)
          0, 0, 0,#hizlar(metre/s)
          0, 0, 0,#akselarasyon(fonksiyonsuz)
          0, math.radians(0))#yaw,yaw_rate(rad,rad/s)
    

         iha.send_mavlink(msg)
            
        
        


        
                
            
                 
                
                
                
                
           
    
    
        
       
        
        
        
        
        
        
        
        
    #**************************************************************************
    
    def mod_degistir_land(self):
        iha.mode = VehicleMode("LAND")
    
    
    def mod_degistir_rtl(self):
        iha.mode = VehicleMode("RTL")
    
    
    def mod_degistir_guided(self):
        iha.mode = VehicleMode("GUIDED")
    
    
    def mod_degistir_stabilize(self):
        
        
        if iha.mode != "STABILIZE":
            
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("WARNING")
            msgBox.setText("Are you sure ?");
            msgBox.setInformativeText("Stabilize mode leaves all control to the pilot. Not recommended.")
            msgBox.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
            ret = msgBox.exec()
            
            
            while not(ret == QMessageBox.Cancel or ret == QMessageBox.Yes):
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("WARNING")
                msgBox.setText("Are you sure ?");
                msgBox.setInformativeText("Stabilize mode leaves all control to the pilot. Not recommended.")
                msgBox.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
                ret = msgBox.exec()
            
            if  ret == QMessageBox.Yes:
                iha.mode = VehicleMode("STABILIZE")
            if  ret == QMessageBox.Cancel:
                iha.mode = iha.mode
        
            
       
            
           
            
       
            
        
    
    
    def mod_degistir_poshold(self):
        iha.mode = VehicleMode("POSHOLD")
    
    
    def mod_degistir_loiter(self):
        iha.mode = VehicleMode("LOITER")
    
    
    def mod_degistir_althold(self):
        iha.mode = VehicleMode("ALT_HOLD")
    
    #**************************************************************************
    
    
    
    
    def direction_forward(self):
        
#        msg = iha.message_factory.set_position_target_local_ned_encode(
#          0,
#          0, 0,
#          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
#          0b0000011111000111,
#          0, 0, 0, 
#          2, 0, 0,
#          0, 0, 0,
#          0, math.radians(0))
#        
#        iha.send_mavlink(msg)
         
         msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111111000,
          4, 0, 0, #pozisyonlar(metre)
          0, 0, 0,#hizlar(metre/s)
          0, 0, 0,#akselarasyon(fonksiyonsuz)
          0, math.radians(0))#yaw,yaw_rate(rad,rad/s)
    

         iha.send_mavlink(msg)
        
        
        
        
        
    def direction_backward(self):
        
#        msg = iha.message_factory.set_position_target_local_ned_encode(
#          0,
#          0, 0,
#          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
#          0b0000011111000111,
#          0, 0, 0, 
#          -2, 0, 0,
#          0, 0, 0,
#          0, math.radians(0))
#        
#        iha.send_mavlink(msg)
         
        
         msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111111000,
          -4, 0, 0, #pozisyonlar(metre)
          0, 0, 0,#hizlar(metre/s)
          0, 0, 0,#akselarasyon(fonksiyonsuz)
          0, math.radians(0))#yaw,yaw_rate(rad,rad/s)
    

         iha.send_mavlink(msg)
        
        
    def direction_right(self):
        
#        msg = iha.message_factory.set_position_target_local_ned_encode(
#          0,
#          0, 0,
#          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
#          0b0000011111000111,
#          0, 0, 0, 
#          0, 2, 0,
#          0, 0, 0,
#          0, math.radians(0))
#        
#        iha.send_mavlink(msg)
         
        
         msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111111000,
          0, 4, 0, #pozisyonlar(metre)
          0, 0, 0,#hizlar(metre/s)
          0, 0, 0,#akselarasyon(fonksiyonsuz)
          0, math.radians(0))#yaw,yaw_rate(rad,rad/s)
    

         iha.send_mavlink(msg)
        
        
    def direction_left(self):
        
#        msg = iha.message_factory.set_position_target_local_ned_encode(
#          0,
#          0, 0,
#          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
#          0b0000011111000111,
#          0, 0, 0, 
#          0, -2, 0,
#          0, 0, 0,
#          0, math.radians(0))
#        
#        iha.send_mavlink(msg)
        
         msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111111000,
          0, -4, 0, #pozisyonlar(metre)
          0, 0, 0,#hizlar(metre/s)
          0, 0, 0,#akselarasyon(fonksiyonsuz)
          0, math.radians(0))#yaw,yaw_rate(rad,rad/s)
    

         iha.send_mavlink(msg)
        
    def direction_up(self):
         
#        msg = iha.message_factory.set_position_target_local_ned_encode(
#          0,
#          0, 0,
#          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
#          0b0000011111000111,
#          0, 0, 0, 
#          0, 0, -2,
#          0, 0, 0,
#          0, math.radians(0))
#        
#        iha.send_mavlink(msg)
         
         msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111111000,
          0, 0, -4, #pozisyonlar(metre)
          0, 0, 0,#hizlar(metre/s)
          0, 0, 0,#akselarasyon(fonksiyonsuz)
          0, math.radians(0))#yaw,yaw_rate(rad,rad/s)
    

         iha.send_mavlink(msg)
        
    def direction_down(self):
        
#        msg = iha.message_factory.set_position_target_local_ned_encode(
#          0,
#          0, 0,
#          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
#          0b0000011111000111,
#          0, 0, 0, 
#          0, 0, 2,
#          0, 0, 0,
#          0, math.radians(0))
#        
#        iha.send_mavlink(msg)
        
        
        
         msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111111000,
          0, 0, 4, #pozisyonlar(metre)
          0, 0, 0,#hizlar(metre/s)
          0, 0, 0,#akselarasyon(fonksiyonsuz)
          0, math.radians(0))#yaw,yaw_rate(rad,rad/s)
    

         iha.send_mavlink(msg)
         
         
         
         
         
         
    #**************************************************************************
    def arm(self):
        iha.armed = True
    def disarm(self):
        iha.armed = False
    #**************************************************************************
    def takeoff(self):
        iha.simple_takeoff(5)
        
        if   iha.mode != "GUIDED":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("WARNING")
            msgBox.setText("The TAKEOFF command cannot run without GUIDED mode.");
            msgBox.setInformativeText("Set the drone's mode to GUIDED")
            ret = msgBox.exec()
        elif iha.armed == False :
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("WARNING")
            msgBox.setText("The TAKEOFF command cannot run without ARM.");
            msgBox.setInformativeText("Set the drone to ARM")
            ret = msgBox.exec()
        elif (iha.mode == "GUIDED" and iha.armed == True) :
             iha.simple_takeoff(5)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    
    def update_line():
        ui.line_altitude.setText(str(iha.location.global_relative_frame.alt))
        ui.line_mode.setText(str(iha.mode.name))
        ui.plainText_battery.setPlainText(str(iha.battery))
        ui.plainText_battery.setPlainText("Voltage:  {}\nCurrent:  {}\nLevel:  {}".format(iha.battery.voltage, iha.battery.current, iha.battery.level))
        ui.line_armable.setText(str(iha.is_armable))
        ui.line_velocity.setText(str(iha.velocity))
        ui.line_arm.setText(str(iha.armed))
        ui.plainText_global_location.setPlainText("Latitude:  {}\nLongitude:  {}".format(iha.location.global_relative_frame.lat, iha.location.global_relative_frame.lon))
        ui.plainText_home_location.setPlainText(str(iha.home_location))
        ui.plainText_gps.setPlainText(str(iha.gps_0))
        ui.line_airspeed.setText(str(round(iha.airspeed,4)))
        ui.line_groundspeed.setText(str(round(iha.groundspeed,4)))
        
        
    timer = QtCore.QTimer()
    timer.timeout.connect(update_line)
    timer.start(500)
    
    sys.exit(app.exec_())
