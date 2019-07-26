#!/usr/bin/env python3
import minimalmodbus
import datetime
import socket
import sys

from pyzabbix import ZabbixMetric, ZabbixSender

hostname = sys.argv[2]
packet =[]

def readNumberAndSaveToTable(instrument, address, table):
	global packet
	try:
                reading = instrument.read_register(address, 2, 4)
                packet.append(ZabbixMetric(hostname, table, str(reading)))
	except IOError:
		print("Failed to read from instrument")

instrument = minimalmodbus.Instrument(sys.argv[1], 1)
instrument.serial.baudrate = 115200
instrument.serial.bytesize = 8
instrument.serial.parity   = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 1.2
instrument.mode = minimalmodbus.MODE_RTU

#Battery 

readNumberAndSaveToTable(instrument, 0x3104, "battery_voltage")
readNumberAndSaveToTable(instrument, 0x3105, "battery_amps")
readNumberAndSaveToTable(instrument, 0x311B, "temperature")
readNumberAndSaveToTable(instrument, 0x3200, "batt_status")
readNumberAndSaveToTable(instrument, 0x311A, "batt_remain")

#Solar

readNumberAndSaveToTable(instrument, 0x3100, "solar_voltage")
readNumberAndSaveToTable(instrument, 0x3101, "solar_amps")

#Controller 

readNumberAndSaveToTable(instrument, 0x3111, "temp_inside")
readNumberAndSaveToTable(instrument, 0x3112, "temp_heatsink")
readNumberAndSaveToTable(instrument, 0x310D, "load_amps")
readNumberAndSaveToTable(instrument, 0x3304, "daily_kw_used")
readNumberAndSaveToTable(instrument, 0x330C, "daily_kw_generated")

print(packet)
#result = ZabbixSender(use_config=True).send(packet)
