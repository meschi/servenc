# servenc - Serial Trumpf NC Program supplier
This tool is a modern open source server implementation for supplying nc files over serial to a CNC-machine control unit. This tool is aimed at Trumpf machines. It is used in production, you may need to adapt the source to work with your control unit, however.


### Usage:
On Linux
`./serv.py`

On Windows
`python2.7 serv.py`

The program will print a list of serial ports and ask you to chose one.
It will listen on the selected serial port for requests, try to open the File in the path specified by the source (`path` variable) and sends it over the serial port to the control unit. If the file is not found the server will send nothing.

### Configuration
* Baud rate: Variable `s_baud` in the source (serv.py)
* Byte size: Variable `s_bytesiz` in the source (serv.py)
* Parity: Variable `s_parity` in the source (serv.py)

Defaults are 9600:7:Even
