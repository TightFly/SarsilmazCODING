#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sarsilmaz_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from dronekit import Command, connect, VehicleMode, LocationGlobalRelative
import time
from pymavlink import mavutil
import math


#DRONE BAĞLANTISI
connection_string="127.0.0.1:14550"
global iha
iha=connect(connection_string,wait_ready=True,timeout=100)


#connection_string="/dev/serial/by-id/usb-ArduPilot_Pixhawk4_250033001051393130343139-if00" 
#global iha
#iha=connect(connection_string,wait_ready=True,timeout=100,baud=57600)






class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 659)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labell_mode = QtWidgets.QLabel(self.centralwidget)
        self.labell_mode.setGeometry(QtCore.QRect(40, 281, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labell_mode.setFont(font)
        self.labell_mode.setObjectName("labell_mode")
        self.button_mode_home = QtWidgets.QPushButton(self.centralwidget)
        self.button_mode_home.setGeometry(QtCore.QRect(20, 310, 89, 25))
        self.button_mode_home.setObjectName("button_mode_home")
        self.button_mode_land = QtWidgets.QPushButton(self.centralwidget)
        self.button_mode_land.setGeometry(QtCore.QRect(20, 350, 89, 25))
        self.button_mode_land.setObjectName("button_mode_land")
        self.button_mode_stabilize = QtWidgets.QPushButton(self.centralwidget)
        self.button_mode_stabilize.setGeometry(QtCore.QRect(20, 390, 89, 25))
        self.button_mode_stabilize.setObjectName("button_mode_stabilize")
        self.button_mode_guided = QtWidgets.QPushButton(self.centralwidget)
        self.button_mode_guided.setGeometry(QtCore.QRect(20, 430, 89, 25))
        self.button_mode_guided.setObjectName("button_mode_guided")
        self.label_parameter = QtWidgets.QLabel(self.centralwidget)
        self.label_parameter.setGeometry(QtCore.QRect(370, 40, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_parameter.setFont(font)
        self.label_parameter.setObjectName("label_parameter")
        self.label_velocity = QtWidgets.QLabel(self.centralwidget)
        self.label_velocity.setGeometry(QtCore.QRect(370, 170, 81, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_velocity.setFont(font)
        self.label_velocity.setObjectName("label_velocity")
        self.line_velocity = QtWidgets.QLineEdit(self.centralwidget)
        self.line_velocity.setGeometry(QtCore.QRect(370, 190, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_velocity.setFont(font)
        self.line_velocity.setReadOnly(True)
        self.line_velocity.setObjectName("line_velocity")
        self.label_altitude = QtWidgets.QLabel(self.centralwidget)
        self.label_altitude.setGeometry(QtCore.QRect(370, 120, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_altitude.setFont(font)
        self.label_altitude.setObjectName("label_altitude")
        self.line_altitude = QtWidgets.QLineEdit(self.centralwidget)
        self.line_altitude.setGeometry(QtCore.QRect(370, 140, 111, 21))
        self.line_altitude.setReadOnly(True)
        self.line_altitude.setObjectName("line_altitude")
        self.label_armable = QtWidgets.QLabel(self.centralwidget)
        self.label_armable.setGeometry(QtCore.QRect(500, 70, 81, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_armable.setFont(font)
        self.label_armable.setObjectName("label_armable")
        self.line_armable = QtWidgets.QLineEdit(self.centralwidget)
        self.line_armable.setGeometry(QtCore.QRect(500, 90, 113, 21))
        self.line_armable.setReadOnly(True)
        self.line_armable.setObjectName("line_armable")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(360, 30, 541, 201))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line_battery = QtWidgets.QLineEdit(self.frame)
        self.line_battery.setGeometry(QtCore.QRect(270, 60, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_battery.setFont(font)
        self.line_battery.setText("")
        self.line_battery.setReadOnly(True)
        self.line_battery.setObjectName("line_battery")
        self.label_battery = QtWidgets.QLabel(self.frame)
        self.label_battery.setGeometry(QtCore.QRect(270, 40, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_battery.setFont(font)
        self.label_battery.setObjectName("label_battery")
        self.label_mode = QtWidgets.QLabel(self.frame)
        self.label_mode.setGeometry(QtCore.QRect(10, 40, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_mode.setFont(font)
        self.label_mode.setObjectName("label_mode")
        self.line_mode = QtWidgets.QLineEdit(self.frame)
        self.line_mode.setGeometry(QtCore.QRect(10, 60, 113, 21))
        self.line_mode.setReadOnly(True)
        self.line_mode.setObjectName("line_mode")
        self.label_local_location = QtWidgets.QLabel(self.frame)
        self.label_local_location.setGeometry(QtCore.QRect(140, 90, 131, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_local_location.setFont(font)
        self.label_local_location.setObjectName("label_local_location")
        self.line_local_location = QtWidgets.QLineEdit(self.frame)
        self.line_local_location.setGeometry(QtCore.QRect(140, 110, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line_local_location.setFont(font)
        self.line_local_location.setText("")
        self.line_local_location.setReadOnly(True)
        self.line_local_location.setObjectName("line_local_location")
        self.label_global_location = QtWidgets.QLabel(self.frame)
        self.label_global_location.setGeometry(QtCore.QRect(140, 140, 141, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_global_location.setFont(font)
        self.label_global_location.setObjectName("label_global_location")
        self.line_global_location = QtWidgets.QLineEdit(self.frame)
        self.line_global_location.setGeometry(QtCore.QRect(140, 160, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line_global_location.setFont(font)
        self.line_global_location.setText("")
        self.line_global_location.setReadOnly(True)
        self.line_global_location.setObjectName("line_global_location")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 30, 281, 201))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.frame_2.setFont(font)
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.button_up = QtWidgets.QPushButton(self.frame_2)
        self.button_up.setGeometry(QtCore.QRect(0, 40, 132, 25))
        self.button_up.setObjectName("button_up")
        self.button_down = QtWidgets.QPushButton(self.frame_2)
        self.button_down.setGeometry(QtCore.QRect(150, 40, 131, 25))
        self.button_down.setObjectName("button_down")
        self.button_left = QtWidgets.QPushButton(self.frame_2)
        self.button_left.setGeometry(QtCore.QRect(0, 90, 132, 25))
        self.button_left.setObjectName("button_left")
        self.button_right = QtWidgets.QPushButton(self.frame_2)
        self.button_right.setGeometry(QtCore.QRect(150, 90, 131, 25))
        self.button_right.setObjectName("button_right")
        self.button_backward = QtWidgets.QPushButton(self.frame_2)
        self.button_backward.setGeometry(QtCore.QRect(0, 140, 132, 25))
        self.button_backward.setObjectName("button_backward")
        self.button_forward = QtWidgets.QPushButton(self.frame_2)
        self.button_forward.setGeometry(QtCore.QRect(150, 140, 131, 25))
        self.button_forward.setObjectName("button_forward")
        self.label_dronecontrol = QtWidgets.QLabel(self.frame_2)
        self.label_dronecontrol.setGeometry(QtCore.QRect(70, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_dronecontrol.setFont(font)
        self.label_dronecontrol.setObjectName("label_dronecontrol")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(180, 270, 111, 281))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.frame_3.setFont(font)
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.button_mission4 = QtWidgets.QPushButton(self.frame_3)
        self.button_mission4.setGeometry(QtCore.QRect(10, 160, 89, 25))
        self.button_mission4.setObjectName("button_mission4")
        self.button_mission2 = QtWidgets.QPushButton(self.frame_3)
        self.button_mission2.setGeometry(QtCore.QRect(10, 80, 89, 25))
        self.button_mission2.setObjectName("button_mission2")
        self.button_mission3 = QtWidgets.QPushButton(self.frame_3)
        self.button_mission3.setGeometry(QtCore.QRect(10, 120, 89, 25))
        self.button_mission3.setObjectName("button_mission3")
        self.button_mission1 = QtWidgets.QPushButton(self.frame_3)
        self.button_mission1.setGeometry(QtCore.QRect(10, 40, 89, 25))
        self.button_mission1.setStyleSheet("selection-background-color: rgb(238, 238, 236);")
        self.button_mission1.setObjectName("button_mission1")
        self.label_mission = QtWidgets.QLabel(self.frame_3)
        self.label_mission.setGeometry(QtCore.QRect(20, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_mission.setFont(font)
        self.label_mission.setObjectName("label_mission")
        self.button_mission5 = QtWidgets.QPushButton(self.frame_3)
        self.button_mission5.setGeometry(QtCore.QRect(10, 200, 89, 25))
        self.button_mission5.setObjectName("button_mission5")
        self.button_mission6 = QtWidgets.QPushButton(self.frame_3)
        self.button_mission6.setGeometry(QtCore.QRect(10, 240, 89, 25))
        self.button_mission6.setObjectName("button_mission6")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 270, 111, 321))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.frame_4.setFont(font)
        self.frame_4.setAutoFillBackground(True)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.button_mode_poshold = QtWidgets.QPushButton(self.frame_4)
        self.button_mode_poshold.setGeometry(QtCore.QRect(10, 200, 89, 25))
        self.button_mode_poshold.setObjectName("button_mode_poshold")
        self.button_mode_loiter = QtWidgets.QPushButton(self.frame_4)
        self.button_mode_loiter.setGeometry(QtCore.QRect(10, 240, 89, 25))
        self.button_mode_loiter.setObjectName("button_mode_loiter")
        self.button_mode_althold = QtWidgets.QPushButton(self.frame_4)
        self.button_mode_althold.setGeometry(QtCore.QRect(10, 280, 89, 25))
        self.button_mode_althold.setObjectName("button_mode_althold")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(360, 270, 111, 121))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.frame_5.setFont(font)
        self.frame_5.setAutoFillBackground(True)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.button_disarm = QtWidgets.QPushButton(self.frame_5)
        self.button_disarm.setGeometry(QtCore.QRect(10, 80, 89, 25))
        self.button_disarm.setObjectName("button_disarm")
        self.button_arm = QtWidgets.QPushButton(self.frame_5)
        self.button_arm.setGeometry(QtCore.QRect(10, 40, 89, 25))
        self.button_arm.setObjectName("button_arm")
        self.label_mission_2 = QtWidgets.QLabel(self.frame_5)
        self.label_mission_2.setGeometry(QtCore.QRect(10, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_mission_2.setFont(font)
        self.label_mission_2.setObjectName("label_mission_2")
        self.frame_5.raise_()
        self.frame_4.raise_()
        self.frame.raise_()
        self.labell_mode.raise_()
        self.button_mode_home.raise_()
        self.button_mode_land.raise_()
        self.button_mode_stabilize.raise_()
        self.button_mode_guided.raise_()
        self.label_parameter.raise_()
        self.label_velocity.raise_()
        self.line_velocity.raise_()
        self.label_altitude.raise_()
        self.line_altitude.raise_()
        self.label_armable.raise_()
        self.line_armable.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SARSILMAZ GUI"))
        self.labell_mode.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ef2929;\">MODE</span></p></body></html>"))
        self.button_mode_home.setText(_translate("MainWindow", "RTL"))
        self.button_mode_land.setText(_translate("MainWindow", "LAND"))
        self.button_mode_stabilize.setText(_translate("MainWindow", "STABILIZE"))
        self.button_mode_guided.setText(_translate("MainWindow", "GUIDED"))
        self.label_parameter.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ef2929;\">PARAMETER &amp; SYSTEM INFORMATION</span></p><p><span style=\" text-decoration: underline;\"><br/></span></p></body></html>"))
        self.label_velocity.setText(_translate("MainWindow", "VELOCITY"))
        self.label_altitude.setText(_translate("MainWindow", "ALTITUDE"))
        self.label_armable.setText(_translate("MainWindow", "ARMABLE"))
        self.label_battery.setText(_translate("MainWindow", "BATTERY"))
        self.label_mode.setText(_translate("MainWindow", "MODE"))
        self.label_local_location.setText(_translate("MainWindow", "LOCAL LOCATION"))
        self.label_global_location.setText(_translate("MainWindow", "GLOBAL LOCATION"))
        self.button_up.setText(_translate("MainWindow", "UP"))
        self.button_down.setText(_translate("MainWindow", "DOWN"))
        self.button_left.setText(_translate("MainWindow", "LEFT"))
        self.button_right.setText(_translate("MainWindow", "RIGHT"))
        self.button_backward.setText(_translate("MainWindow", "BACKWARD"))
        self.button_forward.setText(_translate("MainWindow", "FORWARD"))
        self.label_dronecontrol.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ef2929;\">DRONE CONTROL</span></p></body></html>"))
        self.button_mission4.setText(_translate("MainWindow", "MISSION 4"))
        self.button_mission2.setText(_translate("MainWindow", "MISSION 2"))
        self.button_mission3.setText(_translate("MainWindow", "MISSION 3"))
        self.button_mission1.setText(_translate("MainWindow", "MISSION 1"))
        self.label_mission.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ef2929;\">MISSION</span></p></body></html>"))
        self.button_mission5.setText(_translate("MainWindow", "MISSION 5"))
        self.button_mission6.setText(_translate("MainWindow", "MISSION 6"))
        self.button_mode_poshold.setText(_translate("MainWindow", "POSHOLD"))
        self.button_mode_loiter.setText(_translate("MainWindow", "LOITER"))
        self.button_mode_althold.setText(_translate("MainWindow", "ALTHOLD"))
        self.button_disarm.setText(_translate("MainWindow", "DISARM"))
        self.button_arm.setText(_translate("MainWindow", "ARM"))
        self.label_mission_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ef2929;\">COMMAND</span></p></body></html>"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        
        
        
        #PUSH BUTONA FONKSİYON ATANMASI
        self.button_mission1.clicked.connect(self.arm_ol_ve_yuksel)
        
        #**********************************************************************
        
        self.button_mode_land.clicked.connect(self.mod_degistir_land)
        self.button_mode_guided.clicked.connect(self.mod_degistir_guided)
        self.button_mode_home.clicked.connect(self.mod_degistir_home)
        self.button_mode_stabilize.clicked.connect(self.mod_degistir_stabilize)
        self.button_mode_poshold.clicked.connect(self.mod_degistir_poshold)
        self.button_mode_loiter.clicked.connect(self.mod_degistir_loiter)
        self.button_mode_althold.clicked.connect(self.mod_degistir_althold)
        
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
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    #ATANAN FONKSİYONLARIN TANIMI
    #**************************************************************************
    
    
        
    def arm_ol_ve_yuksel(self):
    
    
        
        
        while iha.is_armable == False:
            print("arm icin gerekli sartlar saglanamadi")
            time.sleep(1)
        
        print("Iha arm edilebilir")
        
        
        
        #drone modunu belirleme
        
        if iha.mode != 'GUIDED':
            iha.mode = VehicleMode("GUIDED")
            
            
            while iha.mode == 'GUIDED':
                print("Guided moduna gecis yapiliyor")
                time.sleep(1)
            
            
            print("Guided moduna gecis yapildi")
        
        
        
        #ihanın arm edilmesi
        iha.armed = True
        
        while iha.armed == False:
            print("Arm için bekleniliyor")
            time.sleep(1)
            
        print("Iha arm edildi")
        
        
        
        #ihanın yükselmesi
        iha.simple_takeoff(5)
        
        
        
        
        
        
        
        
    #**************************************************************************
    
    def mod_degistir_land(self):
        iha.mode = VehicleMode("LAND")
    def mod_degistir_home(self):
        iha.mode = VehicleMode("RTL")
    def mod_degistir_guided(self):
        iha.mode = VehicleMode("GUIDED")
    def mod_degistir_stabilize(self):
        iha.mode = VehicleMode("STABILIZE")
    def mod_degistir_poshold(self):
        iha.mode = VehicleMode("POSHOLD")
    def mod_degistir_loiter(self):
        iha.mode = VehicleMode("LOITER")
    def mod_degistir_althold(self):
        iha.mode = VehicleMode("ALT_HOLD")
    
    
    
    
    #**************************************************************************
    
    
    
    
    def direction_forward(self):
        
        msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111000111,
          0, 0, 0, 
          0.33, 0, 0,
          0, 0, 0,
          0, math.radians(0))
        
        iha.send_mavlink(msg)
        
        
    def direction_backward(self):
        
        msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111000111,
          0, 0, 0, 
          -0.33, 0, 0,
          0, 0, 0,
          0, math.radians(0))
        
        iha.send_mavlink(msg)
        
        
    def direction_right(self):
        
        msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111000111,
          0, 0, 0, 
          0, 0.33, 0,
          0, 0, 0,
          0, math.radians(0))
        
        iha.send_mavlink(msg)
        
        
    def direction_left(self):
        
        msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111000111,
          0, 0, 0, 
          0, -0.33, 0,
          0, 0, 0,
          0, math.radians(0))
        
        iha.send_mavlink(msg)
        
    def direction_up(self):
        
        msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111000111,
          0, 0, 0, 
          0, 0, -0.33,
          0, 0, 0,
          0, math.radians(0))
        
        iha.send_mavlink(msg)
        
    def direction_down(self):
        
        msg = iha.message_factory.set_position_target_local_ned_encode(
          0,
          0, 0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
          0b0000011111000111,
          0, 0, 0, 
          0, 0, 0.33,
          0, 0, 0,
          0, math.radians(0))
        
        iha.send_mavlink(msg)
    
    
    
    #**************************************************************************
    def arm(self):
        iha.armed = True
        
    def disarm(self):
        iha.armed = False
        



































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
        ui.line_battery.setText(str(iha.battery))
        ui.line_armable.setText(str(iha.is_armable))
        ui.line_velocity.setText(str(iha.velocity))
        ui.line_local_location.setText(str(iha.location.local_frame))
        ui.line_global_location.setText(str(iha.location.global_frame))
        
        

    
    
    timer = QtCore.QTimer()
    timer.timeout.connect(update_line)
    timer.start(500)
    
    
    sys.exit(app.exec_())
























