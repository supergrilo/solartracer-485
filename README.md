# zabbix-epsolar-tracer
Tools for Connecting Tracer BN Solar Charger to Raspberry Pi with Python via rs485 and send to zabbix via sender protocol
===================================================

This is how I setup a  Raspberry Pi with  a RS485 adapter to track statistics from a Tracer 4215BN Solar Charger. This should work with any of the tracer BN series charge controllers.

The first generation controller used RS-232 and a different protocol. see https://github.com/xxv/tracer. This could be adapted to work with that.


Linux driver for Exar USB UART
------------------------------
Heres how to install the driver for a usb to rs-485 similar to the one [found here](https://www.amazon.com/gp/product/B016RU8JUY/ref=oh_aui_search_detailpage?ie=UTF8&psc=1)
The [xr_usb_serial_common](xr_usb_serial_common-1a/) directory contains the makefile and instructions that will compile properly on Rasbian OS on a raspberry pi 3. Before compiling be sure to install the linux headers with
`sudo apt-get install raspberrypi-kernel-headers`

After installing the headers be sure to `sudo bundle` then `sudo make`.
The resulting `xr_usb_serial_common.ko` file will need to be moved to `/lib/modules/YOUR_LINUX_VERSION/extra/`.
After building and moving the module, remove the cdc-acm driver that automatically installs for the usb-485 adapter.

`rmmod cdc-acm`
`modprobe -r usbserial`
`modprobe usbserial`

You will also need to add the cdc-acm to the system blacklist:

`echo blacklist cdc-acm > /etc/modprobe.d/blacklist-cdc-acm.conf`
Note: If echo doesnt work you will need to add `blacklist cdc-acm` manually to the blacklist with vim `vi /etc/modprobe.d/blacklist-cdc-acm.conf`

Finally add `xr_usb_serial_common` to '/etc/modules' to autoload the module on startup.

After all of this is done make sure that the new driver loads correctly by reloading the linux dependency list `depmod -ae`
Then load the module with `modprobe xr_usb_serial_common`

If all goes well you should see `ttyXRUSB` when listing `ls /dev/tty*`

Reboot and enjoy!

Protocol
--------
[Protocol](http://www.solar-elektro.cz/data/dokumenty/1733_modbus_protocol.pdf)

Cheers!


