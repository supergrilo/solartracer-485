#!/usr/bin/env python
import minimalmodbus
import datetime

def readNumberAndSaveToTable(instrument, address, table):
	try:
   		reading = instrument.read_register(address, 2, 4)
   		print("Reading " + table + ": " + str(reading))
	except IOError:
		print("Failed to read from instrument")

instrument = minimalmodbus.Instrument('/dev/ttyXRUSB0', 1)
instrument.serial.baudrate = 115200
instrument.serial.bytesize = 8
instrument.serial.parity   = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 1.2
instrument.mode = minimalmodbus.MODE_RTU

#Read Solar Voltage
readNumberAndSaveToTable(instrument, 0x3100, "solar_voltage")

#Read Battery Voltage
readNumberAndSaveToTable(instrument, 0x3104, "battery_voltage")

#Read Solar Amps
readNumberAndSaveToTable(instrument, 0x3101, "solar_amps")

#Read Battery Amps
readNumberAndSaveToTable(instrument, 0x3105, "battery_amps")

#Read Battery Amps
readNumberAndSaveToTable(instrument, 0x310D, "load_amps")

#Read Battery Temperature
readNumberAndSaveToTable(instrument, 0x311B, "temperature")

#Read Daily Use
readNumberAndSaveToTable(instrument, 0x3304, "daily_kw_used")

#Read Daily Generated
readNumberAndSaveToTable(instrument, 0x330C, "daily_kw_generated")

print("FINISHED")
