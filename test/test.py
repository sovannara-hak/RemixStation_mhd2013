from IPython import embed
import mhd


mhd.pygame.init()
mhd.mix.pre_init(44100,-16,2,2048)
mhd.pm.init()

cm = mhd.MidiDevice()
cm.list_devices()
  
cm.setDevice(3)

testmp3 = "/home/sovan/compil/julesverne/share/echo-nest-remix-examples/music/Raleigh_Moncrief-Guppies.mp3" 
path = "/tmp/"
prefix = "Ral"

mp = mhd.MusicParser(testmp3)

print "Analize..."
mp.analize_bars()
print "Write samples..."
mp.write_bars_sample(path, prefix)

rs = mhd.RemixStation(cm, path, prefix, mp.number_items)
print "Loading..."
rs.load()
#rs.play()

def go():
  while 1:
    msg = cm.device.read(1)
    if len(msg):
      if msg[0][0][0] == 144:
	print msg
embed()

