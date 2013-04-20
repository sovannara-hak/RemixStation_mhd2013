import pygame.midi as pm

import pygame
import pygame.mixer as mix

class MidiDevice (object):

  def __init__(self):
    self.device_id = None
    self.device_name = None
    self.device_type = None
    self.device_opened = None
    self.device = None
    self.keymap = {}
    self.fill_keymap()

  def fill_keymap(self):
    self.keymap["48"] = "C"
    self.keymap["49"] = "C#"
    self.keymap["50"] = "D"
    self.keymap["51"] = "D#"
    self.keymap["52"] = "E"
    self.keymap["53"] = "F"
    self.keymap["54"] = "F#"
    self.keymap["55"] = "G"
    self.keymap["56"] = "G#"
    self.keymap["57"] = "A"
    self.keymap["58"] = "A#"
    self.keymap["59"] = "B"
    self.keymap["60"] = "C"
    self.keymap["61"] = "C#"
    self.keymap["62"] = "D"
    self.keymap["63"] = "D#"
    self.keymap["64"] = "E"
    self.keymap["65"] = "F"
    self.keymap["66"] = "F#"
    self.keymap["67"] = "G"
    self.keymap["68"] = "G#"
    self.keymap["69"] = "A"
    self.keymap["70"] = "A#"
    self.keymap["71"] = "B"

  def show_info(self):
    print "Device ID: ", self.device_id
    print "Device name: ", self.device_name
    print "Device type: ", self.device_type
    print "Device opened: ", self.device_opened

  def list_devices(self):
    for i in range(pm.get_count()):
      r = pm.get_device_info(i)
      (interf, name, input, output, opened) = r
      in_out = ""
      if input:
	in_out = "(input)"
      if output:
	in_out = "(output)"
      print ("%2i: interface :%s:, name :%s:, opened :%s: %s" % (i,interf,name,opened,in_out))

  def setDevice(self, idnum):
    r = pm.get_device_info(idnum)
    if r is not None:
      self.device = pm.Input(idnum)

      self.device_id = idnum
      self.device_name = r[1]
      if r[2]:
	self.device_type = "input"
      elif r[3]:
	self.device_type = "output"
      self.device_opened = r[4]

class RemixStation(object):
  def __init__(self, midi_dev, path, prefix, number_items):
    self.midi_dev = midi_dev
    self.path = path
    self.prefix = prefix
    self.number_items = number_items
    self.log_enabled = True
    self.log = []

  def load(self):
    self.sound = []
    for i in range(self.number_items):
      self.sound.append(mix.Sound(self.path+self.prefix+str(i)+".wav"))

  def play(self):
    while 1:
      msg = self.midi_dev.device.read(1)
      if len(msg):
	if msg[0][0][0] == 144:
	  key = msg[0][0][1]
	  self.sound[key-48].play()
	  if str(key) in self.midi_dev.keymap:
	    print self.midi_dev.keymap[str(key)]
	  if self.log_enabled:
	    self.log.append(key-48)
	#if msg[0][0][0] == 128:
	#  self.sound[key-48].stop()




