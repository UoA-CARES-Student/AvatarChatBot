
class Configuration:
	def __init__(self, **kwargs):
		self.data = {}

		for key, value in kwargs.items():
			self.data[key] = value

	def __getattr__(self, key):
		if key not in self.data:
			raise AttributeError("'HParams' object has no attribute %s" % key)
		return self.data[key]

	def set_hparam(self, key, value):
		self.data[key] = value
  

confg = Configuration(
    
    AUDIO_FILE_PATH = "./resources/audo",
    FACE_FILE_PATH = "./resources/face",
    VIDEO_FILE_PATH = "./resources/video",
	
)
