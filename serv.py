#!/usr/bin/env python

import sys
import glob
import serial
import time
import os
import optparse


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*[0-9]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def choose_port(ports):
    i = 0
    for port in ports:
        print "(%i)" % i + " " + port
        i += 1


    while True:
        choice = raw_input("Select port: ")

        if choice.isdigit():
            index = int(choice)

            if index >= 0 and index < len(ports):
                return ports[index]
        else:
            if choice in ports:
                return choice

        print "Try again..."


path = "/run/user/1000/gvfs/smb-share:server=cad-fabi-pc,share=cnc/"
s_bytesiz = 7
s_parity = serial.PARITY_EVEN
s_baud = 9600
choice = "/dev/ttyS0"

if __name__ == '__main__':
    '''
    parser = optparse.OptionParser()
    parser.add_option("--ask-for-serial-port", action="store_true", default=False)
    parser.add_option('-b', action="store", dest="b", default=9600, type="int")
    parser.add_option('-B', action="store", dest="B", default=7, type="int")
    parser.add_option('-p', action="store", dest="p")
    '''
    ports = serial_ports()
    if not ports:
        print "No serial ports found...\n" \
            "Check if you have the permissions to open a serial port!"

    choice = choose_port(ports)
    print "Listening on " + choice

    ser = serial.Serial(choice, s_baud, bytesize=s_bytesiz, parity=s_parity)

    #print ser.name

    while True:

        print "Waiting for request..."
        lines = []
        while True:

            lines.append(ser.readline().strip())

            if len(lines) >= 1 and lines[-1][0] is "Q":
                break

        filename = lines[-1][1:] + ".500"


        stanzweg = ""
        with open(path+filename, "r") as fhandle:
            if os.path.isfile(fhandle):
                print "File %s was requested. Serving file..." % filename
                stanzweg = fhandle.read()
            else:
                print "ERROR: %s: File not found" %filename
                continue


        time.sleep(5)
        ser.write(b"%s\r\n" % stanzweg)
