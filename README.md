# Tenma-PSU-72-2710
Command Line interface for the Tenma 72-2710 Power Supply

To use from the command line


Usage: TenmaPSU72-2710.py [OPTIONS] COMMAND [ARGS]...

Options:
  --debug / --no-debug
  --help                Show this message and exit.

Commands:
  getcurrent
  getcurrentlimit
  getident
  getvoltage
  getvoltset
  output
  setcurrent
  setvolt

Example if the power supply is connected to COM4 will set the power Supply to 20.0V out

python TenmaPSU72-2710.py setvolt COM4 20.0

The program PSU Efficiency Logger.py uses a Tenma 72-2710 power supply and a KP184 to log the efficiency of a switch mode power supply and sace to the CSV in filename, alter variables for your individual settings

EL="com5"
PSU="COM4"
Start = 100
End=1000 #End of current range in mA
Step=100 #Step size in mA
PSUstart=30
PSUstop=32

It will output data as a csv in the format below and as a table on the screen.

  VIN    IIN    VOUT    IOUT    EFF
-----  -----  ------  ------  -----
   30  0.08   12.017     0.1  0.501
   30  0.145  11.99      0.2  0.551
   30  0.217  11.978     0.3  0.552
   30  0.29   11.973     0.4  0.55
   30  0.361  11.968     0.5  0.553
   30  0.434  11.963     0.6  0.551
   30  0.506  11.959     0.7  0.551
   30  0.579  11.955     0.8  0.551
   30  0.656  11.948     0.9  0.546
   31  0.084  12.016     0.1  0.461
   31  0.148  11.986     0.2  0.522
   31  0.218  11.973     0.3  0.532
   31  0.288  11.967     0.4  0.536
   31  0.359  11.963     0.5  0.537
   31  0.431  11.96      0.6  0.537
   31  0.503  11.957     0.7  0.537
   31  0.577  11.952     0.8  0.535
   31  0.653  11.934     0.9  0.531

This has a dependancy on the excellent Kunkin KP184 command line client downloadable from

https://github.com/cskilbeck/modbus


All files should be installed in the same directory and run from the command shell

Hope it is useful
