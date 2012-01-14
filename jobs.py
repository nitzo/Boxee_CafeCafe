import mc
import jobmanager

class ContainerScrollJob(jobmanager.BoxeeJob):
	

	# Add your own variables to constructor.
	def __init__(self, interval, list):
		self.interval = interval
		self.list = list
		jobmanager.BoxeeJob.__init__(self, "Container Scroll Job", interval)

	def process(self):
		self.list.ScrollPageDown()
		
		



