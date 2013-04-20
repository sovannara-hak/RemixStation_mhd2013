from IPython import embed
import mhd

mhd.pm.init()

cm = mhd.MidiDevice()
cm.list_devices()
  

embed()
