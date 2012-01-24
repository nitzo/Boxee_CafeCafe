import mc
import jobmanager
import time
import xbmc

class ContainerScrollJob(jobmanager.BoxeeJob):
	
	def __init__(self, interval, list):
		self.interval = interval
		self.list = list
		jobmanager.BoxeeJob.__init__(self, "Container Scroll Job", interval)

	def process(self):
		self.list.ScrollPageDown()
		
class LocalImageScrollJob(jobmanager.BoxeeJob):
	
	def __init__(self, interval, image, imageArr):
		self.interval = interval
		self.image = image
		self.imageArr = imageArr
		self.position = 0
		jobmanager.BoxeeJob.__init__(self, "Local Image Scroll Job", interval)

	def process(self):
		self.image.SetTexture(self.imageArr[self.position])
		self.position = self.position + 1
		if (self.position == len(self.imageArr)):
			self.position = 0
		
		
class BreakingNewsJob(jobmanager.BoxeeJob):
	
	def __init__(self, interval, dialogId, duration):
		self.interval = interval
		self.dialogId = dialogId
		self.duration = duration
		jobmanager.BoxeeJob.__init__(self, "Breaking News Job", interval)

	def process(self):
		mc.ActivateWindow(self.dialogId)
		time.sleep(self.duration)
		xbmc.executebuiltin("Dialog.Close("+ str(self.dialogId) +")")
		
		



