import echonest.remix.audio as audio


class MusicParser(object):
  def __init__(self, file_name):
    self.filename = file_name
    self.bars = None
    try:
      self.audio_file = audio.LocalAudioFile(self.filename)
    except EOFError:
      self.audio_file = None
      print "File does not exist"
      return

  def analize_bars(self):
    self.bars = self.audio_file.analysis.bars

  def write_bars_sample(self, path, prefix):
    suffix = 0
    if self.bars is not None:
      for bar in self.bars:
	audio.getpieces(self.audio_file, [bar]).encode(path+prefix+str(suffix)+".wav")
	suffix += 1
    else:
      print "Analyze bars first"

