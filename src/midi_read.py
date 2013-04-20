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
	#if msg[0][0][0] == 128:
	#  self.sound[key-48].stop()


