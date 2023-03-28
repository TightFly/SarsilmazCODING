# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""

import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
DCPIN = 22
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
GPIO.setmode(GPIO.BCM)
kit = ServoKit(channels=8)
GPIO.setup(DCPIN, GPIO.OUT)

kit.servo[0].angle = 90     # YUKARI AŞAĞI ALT SINIR 60  ust SINIR 120 ORTA  100
kit.servo[1].angle = 120     #SAĞ SOL SINIRLAR    SOL SINIR 175  SAĞ SINIR 90 ORTA  120
kit.servo[2].angle = 165      # İTTİRME 30    ÇEKME 165



