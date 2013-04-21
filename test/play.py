from IPython import embed
import mhd
import threading
import time

import sys

class RS(threading.Thread):
  def __init__(self, rs, name = ''):
    threading.Thread.__init__(self)
    self.name = name
    self._stopevent = threading.Event( )
    self.rs = rs
  def run(self):
    i = 0
    while not self._stopevent.isSet():
      self.rs.play()
      self._stopevent.wait(0.1)
    print self.name +" stop"
  def stop(self):
    self._stopevent.set( )
    print "Rec: ", self.rs.log

mhd.pygame.init()
mhd.mix.pre_init(44100,-16,2,2048)
mhd.pm.init()

cm = mhd.MidiDevice()
#cm.list_devices()
  
cm.setDevice(3)

testmp3 = "/home/sovan/compil/julesverne/share/echo-nest-remix-examples/music/Raleigh_Moncrief-Guppies.mp3" 
testmp3 = "/home/sovan/paradise.mp3"
#testmp3 = "/home/sovan/coffinb.mp3"
#testmp3 = "/home/sovan/blood.m4a"
testmp3 = "/home/sovan/juan.mp3"

if len(sys.argv) == 2:
  testmp3 = sys.argv[1]

path = "/tmp/"
prefix = "Ral"

mp = mhd.MusicParser(testmp3)

mp.analyze_bars()
mp.write_sample(path, prefix)

rs = mhd.RemixStation(cm, path, prefix, mp.number_items)
print "Loading..."
rs.load()
#rs.play()

RemixStation = RS(rs)
RemixStation.start()
def go():
  while 1:
    msg = cm.device.read(1)
    if len(msg):
      if msg[0][0][0] == 144:
	print msg

def rec():
  rs.rec()

def pause():
  rs.pause()

def stop():
  RemixStation.stop()

def render(out):
  mp.render(rs.log, out)

def preview(size):
  rs.preview(size)

embed()

