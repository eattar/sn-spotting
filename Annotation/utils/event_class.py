

class Event:

	def __init__(self, label=None, half=None, time=None, team=None, position= None, visibility=None, confidence=None):

		self.label = label
		self.half = half
		self.time = time
		self.team = team
		self.position = position
		self.visibility = visibility
		self.confidence = confidence

	def to_text(self):
		# For predictions with confidence, show a cleaner format
		if self.confidence is not None:
			conf_percent = f"{float(self.confidence)*100:.1f}%"
			return self.time + " || " + self.label + " (" + conf_percent + ")"
		# For ground truth annotations, show full details
		else:
			return self.time + " || " + self.label + " - " + self.team  + " - " + str(self.half) + " - " + str(self.visibility)

	def __lt__(self, other):
		self.position < other.position

def ms_to_time(position):
	minutes = int(position//1000)//60
	seconds = int(position//1000)%60
	return str(minutes).zfill(2) + ":" + str(seconds).zfill(2)