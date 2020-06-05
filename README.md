# ESP32-TCP
Wifi Communication over ESP32 To Linux

There are two file
1. Client
2. Server

Hardware requirement:
1. ESP32-wroom-32
2. Linux System
3. DHT sensor

Preparation:
1. Get update and upgrade it: 
   sudo apt-get update && sudo apt-get upgrade
2. Get esptool for erasing and flashing memory of ESP32:
   sudo pip3 install esptool
3. Connect ESP32 with Linux system via USB and check if it is detected
   command : dmesg | grep ttyUSB
   output  :[45229.735143] usb 2-1.3: cp210x converter now attached to ttyUSB0
   
   ttyUSB0 is important
4. check flash id if the ESP32
   command : esptool.py --port /dev/ttyUSB0 flash_id
   output  : esptool.py v2.8
             Serial port /dev/ttyUSB0
             Connecting........_____....._____....._____...
             Detecting chip type... ESP32
             Chip is ESP32D0WDQ6 (revision 1)
             Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
             Crystal is 40MHz
             MAC: <MAC ADDRESS of ESP32>
             Uploading stub...
             Running stub...
             Stub running...
             Manufacturer: 20
             Device: 4016
             Detected flash size: 4MB
             Hard resetting via RTS pin...
5.  Erase Everything on ESP32
    command: esptool.py --port /dev/ttyUSB0 erase_flash
    
6. Download Firmware for ESP32
   esp32-idf3-20180511-v1.9.4.bin
7. Flash firmware to the ESP32
   command : esptool.py --chip esp32 --baud 115200 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin
   if you get error-> try to change baud rate:9600, try to add in code: -fm dio


Now, ESP32 is ready to use. you can access the REPL (Python prompt) over UART0 (GPIO1=TX, GPIO3=RX) or via USB cable


Procedure: 
get REPL: sudo apt-get install picocom
1. try some python command
2. to get more familiar get : sudo apt-get install rshell(another way of access REPL terminal + file management)
3. Start RSHELL: rshell --buffer-size=30 -p /dev/ttyUSB0 
                 /home/pi>     (this is a file management terminal)
4. See if Board is connected: /home/pi>boards
                              pyboard @ /dev/ttyUSB0 connected Dirs: /boot.py
5. start REPL : /home/pi> repl
                Entering REPL. Use Control-X to exit.
                >
                MicroPython v1.9.4 on 2018-05-11; ESP32 module with ESP32
                Type "help()" for more information.
                >>> 
                >>> 5+3
                8
                >>> print('boom')
                boom
                >>> 12**78
                1500158654173824244445901346699938405046228479331843405109463057079932580570809237504
                >>> 
 6. press : Ctrl +X to go to file management terminal
 7. Download the file server and client from this section and edit file for IP and PORT(IP will be you Linux system wlan ip:     type command : hostname -I at linux terminal. (get IP:192.168.x.x) both should be same in bath file)
 9. edit client.py for <Wifi SSID> and <wifi-password> 
 10. connect DHT11 sensor
                       pin1            to ESP32 3v3
                       pin3(last pin)  to ESP32 GND
                       pin2            to ESP32 D21
     connect DHT22 sensor
                       pin1            to ESP32 3v3
                       pin4(last pin)  to ESP32 GND
                       pin2            to ESP32 D21 
11. change according in client file if needed( just replace DHT11 with DHT22)
13. copy client file to ESP32: /home/pi> cp <path to client.py> /pyboard
14. start server in python terminal
15. start REPL: /home/pi>repl
                Entering REPL. Use Control-X to exit.
                >
                MicroPython v1.9.4 on 2018-05-11; ESP32 module with ESP32
                Type "help()" for more information.
                >>>
                >>>
16. start ESP32 to send signal to linux by typing: >>> import client
  
  
  if you get error of EHOSTUNRCH .... then disable your linux system firewall setting
  https://linuxize.com/post/how-to-disable-firewall-on-ubuntu-18-04/
  
