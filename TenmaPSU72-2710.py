#!/usr/bin/python3
import click
import serial
import time

@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.obj['DEBUG'] = debug

@cli.command()
@click.pass_context 
@click.argument('portselect', default='No port selected')
@click.argument('volt',type=str, default=0)
def SetVolt(ctx,portselect,volt):
	if portselect == ('No port selected'):
		click.echo(f'Select Port')
	else:
		click.echo(f'Opening communucations port {portselect}')
		ser = serial.Serial(
			port= portselect,
			baudrate=9600,
			parity='N',
			stopbits=1,
			rtscts = 0,
			xonxoff=0,
			timeout=1
		)
		try:
			ser.close()
			ser.open()
			ser.write(bytearray("VSET1:"+ str(volt)+"\r\n'",'ascii'))			
			ser.close()
		except serial.SerialException:
			click.echo(click.style('Error opening port',fg='red'))
			raise

@cli.command()
@click.pass_context 
@click.argument('portselect', default='No port selected')
@click.argument('current',type=str, default=0)
def SetCurrent(ctx,portselect,current):
	if portselect == ('No port selected'):
		click.echo(f'Select Port')
	else:
		click.echo(f'Opening communucations port {portselect}')
		ser = serial.Serial(
			port= portselect,
			baudrate=9600,
			parity='N',
			stopbits=1,
			rtscts = 0,
			xonxoff=0,
			timeout=1
		)
		try:
			ser.close()
			ser.open()
			ser.write(bytearray("ISET1:"+ str(current)+"\r\n'",'ascii'))			
			ser.close()
		except serial.SerialException:
			click.echo(click.style('Error opening port',fg='red'))
			raise

@cli.command()
@click.pass_context 
@click.argument('portselect', default='No port selected')
def GetCurrentLimit(ctx,portselect):
	if portselect == ('No port selected'):
		click.echo(f'Select Port')
	else:
		click.echo(f'Opening communucations port {portselect}')
		ser = serial.Serial(
			port= portselect,
			baudrate=9600,
			parity='N',
			stopbits=1,
			rtscts = 0,
			xonxoff=0,
			timeout=1
		)
		try:
			ser.close()
			ser.open()
			ser.write(b"ISET1?")
			print(ser.readline())			
			ser.close()
		except serial.SerialException:
			click.echo(click.style('Error opening port',fg='red'))
			raise


@cli.command()
@click.pass_context 
@click.argument('portselect', default='No port selected')
def GetVoltSet(ctx,portselect):
	if portselect == ('No port selected'):
		click.echo(f'Select Port')
	else:
		click.echo(f'Opening communucations port {portselect}')
		ser = serial.Serial(
			port= portselect,
			baudrate=9600,
			parity='N',
			stopbits=1,
			rtscts = 0,
			xonxoff=0,
			timeout=1
		)
		try:
			ser.close()
			ser.open()
			ser.write(b"VSET1?")
			print(ser.readline().decode('utf-8'))			
			ser.close()
		except serial.SerialException:
			click.echo(click.style('Error opening port',fg='red'))
			raise


@cli.command()
@click.pass_context 
@click.argument('portselect', default='No port selected')
def GetIdent(ctx,portselect):
	if portselect == ('No port selected'):
		click.echo(f'Select Port')
	else:
		click.echo(f'Opening communucations port {portselect}')
		ser = serial.Serial(
			port= portselect,
			baudrate=9600,
			parity='N',
			stopbits=1,
			rtscts = 0,
			xonxoff=0,
			timeout=1
		)
		try:
			ser.close()
			ser.open()
			ser.write(b"*IDN?")
			print(ser.readline().decode('utf-8'))			
			ser.close()
		except serial.SerialException:
			click.echo(click.style('Error opening port',fg='red'))
			raise

@cli.command()
@click.pass_context 
@click.argument('portselect', default='No port selected')
def GetVoltage(ctx,portselect):
	if portselect == ('No port selected'):
		click.echo(f'Select Port')
	else:
		click.echo(f'Opening communucations port {portselect}')
		ser = serial.Serial(
			port= portselect,
			baudrate=9600,
			parity='N',
			stopbits=1,
			rtscts = 0,
			xonxoff=0,
			timeout=1
		)
		try:
			ser.close()
			ser.open()
			ser.write(b"VOUT1?")
			print(ser.readline().decode('utf-8'))			
			ser.close()
		except serial.SerialException:
			click.echo(click.style('Error opening port',fg='red'))
			raise
			
@cli.command()
@click.pass_context 
@click.argument('portselect', default='No port selected')
def GetCurrent(ctx,portselect):
	if portselect == ('No port selected'):
		click.echo(f'Select Port')
	else:
		click.echo(f'Opening communucations port {portselect}')
		ser = serial.Serial(
			port= portselect,
			baudrate=9600,
			parity='N',
			stopbits=1,
			rtscts = 0,
			xonxoff=0,
			timeout=1
		)
		try:
			ser.close()
			ser.open()
			ser.write(b"IOUT1?")
			print(ser.readline().decode('utf-8'))			
			ser.close()
		except serial.SerialException:
			click.echo(click.style('Error opening port',fg='red'))
			raise

@cli.command()
@click.pass_context 
@click.argument('portselect', default='No port selected')
@click.argument('switch',type=str, default=0)

def Output(ctx,portselect,switch):
	if portselect == ('No port selected'):
		click.echo(f'Select Port')
	else:
		click.echo(f'Opening communucations port {portselect}')
		ser = serial.Serial(
			port= portselect,
			baudrate=9600,
			parity='N',
			stopbits=1,
			rtscts = 0,
			xonxoff=0,
			timeout=1
		)
		try:
			ser.close()
			ser.open()
			if switch ==('OFF'):
				ser.write(b"OUT0")
			if switch ==('ON'):
				ser.write(b"OUT1")
			else:
				click.echo(f'Please set ON or OFF')
			ser.close()
		except serial.SerialException:
			click.echo(click.style('Error opening port',fg='red'))
			raise
			
if __name__ == '__main__':
    cli(obj={})
