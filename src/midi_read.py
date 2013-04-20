import pygame.midi as pm

class MidiDevice (object):

  def __init__(self):
    self.device_id = None
    self.device_name = None
    self.device_type = None
    self.device_opened = None

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
      self.device_id = idnum
      self.device_name = r[1]
      if r[2]:
	self.device_type = "input"
      elif r[3]:
	self.device_type = "output"
      self.device_opened = r[4]

