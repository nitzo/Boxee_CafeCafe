import mc
import jobmanager

class ScrollAdsJob(jobmanager.BoxeeJob):
	# Add your own variables to constructor.
	def __init__(self, interval):
		self.interval = interval
		# Be sure to always inherit the constructor from the base BoxeeJob class.
		jobmanager.BoxeeJob.__init__(self, "ScrollAds", interval)

	def process(self):
		# This is the base function that is always called for every job and the one you should extend.
		mc.ShowDialogNotification("Hello")
		



