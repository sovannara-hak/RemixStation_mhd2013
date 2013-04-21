import pygame.midi as pm

import pygame
import pygame.mixer as mix

import time

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
    key = 48
    for i in range(20):
      self.keymap[str(key)] = "C"
      key += 1
      self.keymap[str(key)] = "C#"
      key += 1
      self.keymap[str(key)] = "D"
      key += 1
      self.keymap[str(key)] = "D#"
      key += 1
      self.keymap[str(key)] = "E"
      key += 1
      self.keymap[str(key)] = "F"
      key += 1
      self.keymap[str(key)] = "F#"
      key += 1
      self.keymap[str(key)] = "G"
      key += 1
      self.keymap[str(key)] = "G#"
      key += 1
      self.keymap[str(key)] = "A"
      key += 1
      self.keymap[str(key)] = "A#"
      key += 1
      self.keymap[str(key)] = "B"
      key += 1


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
    self.log_enabled = False
    self.play_mode = True
    self.log = []

  def load(self):
    self.sound = []
    for i in range(self.number_items):
      self.sound.append(mix.Sound(self.path+self.prefix+str(i)+".wav"))

  def rec(self):
    self.log_enabled = True
    print "Start recording"

  def pause(self):
    self.log_enabled = False
    print "Stop recording"

  def preview(self, size=0):
    if size == 0:
      list_index = self.log
    else:
      list_index = self.log[-size:]

    for l in list_index:
      s = self.sound[l]
      l=s.get_length()
      s.play()
      time.sleep(l)


  def play(self):
    #while self.play_mode:
      msg = self.midi_dev.device.read(1)
      if len(msg):
	if msg[0][0][0] == 144:
	  key = msg[0][0][1]
	  self.sound[key-48].play()
	  if str(key) in self.midi_dev.keymap:
	    print self.midi_dev.keymap[str(key)]
	  if self.log_enabled:
	    self.log.append(key-48)
	if msg[0][0][0] == 128:
	  key = msg[0][0][1]
	  self.sound[key-48].stop()




