import echonest.remix.audio as audio


class MusicParser(object):
  def __init__(self, file_name):
    self.filename = file_name
    self.samples = None
    try:
      self.audio_file = audio.LocalAudioFile(self.filename)
    except EOFError:
      self.audio_file = None
      print "File does not exist"
      return

  def analyze_bars(self):
    self.samples = []
    self.samples = self.audio_file.analysis.bars
    self.number_items = len(self.samples)

  def analyze_sections(self):
    self.samples = []
    self.samples = self.audio_file.analysis.sections
    self.number_items = len(self.samples)

  def analyze_segments(self):
    self.samples = []
    self.samples = self.audio_file.analysis.segments
    self.number_items = len(self.samples)

  def analyze_tatums(self):
    self.samples = []
    self.samples = self.audio_file.analysis.tatums
    self.number_items = len(self.samples)

  def analyze_beats(self):
    self.samples = []
    self.samples = self.audio_file.analysis.beats
    self.number_items = len(self.samples)

  def write_sample(self, path, prefix):
    suffix = 0
    if self.samples is not None:
      for sample in self.samples:
	audio.getpieces(self.audio_file, [sample]).encode(path+prefix+str(suffix)+".wav")
	suffix += 1
    else:
      print "Analyze first"

