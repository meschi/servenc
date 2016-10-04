# ncserver+ - Serial Trumpf NC Program supplier
This tool is a open source implementation of the ncserver written in python.

### Usage:
`./serv.py #linux`

`python2.7 serv.py #windows`

The program will print a list of serial ports and ask you to chose one.
After that it will listen on the serial port for file requests from the Trumpf. It tries to open the File in the path specified in the `path` variable (you may change it in the source) and sends it over the serial port to the machine. If it doesn't find the file it will do nothing.

### Configuration
* Baud rate: Variable `s_baud` in the source (serv.py)
* Byte size: Variable `s_bytesiz` in the source (serv.py)
* Parity: Variable `s_parity` in the source (serv.py)

Defaults are 9600:7:Even
