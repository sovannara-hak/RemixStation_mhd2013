from IPython import embed
import mhd


mhd.pm.init()

cm = mhd.MidiDevice()
cm.list_devices()
  
cm.setDevice(3)

def go():
  while 1:
    msg = cm.device.read(1)
    if len(msg):
      if msg[0][0][1] == 48 and msg[0][0][0] == 144:
	print "yo "
      if msg[0][0][1] == 50 and msg[0][0][0] == 144:
	print "ya "
      if msg[0][0][1] == 52 and msg[0][0][0] == 144:
	break;
embed()

