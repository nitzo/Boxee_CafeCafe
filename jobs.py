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
	
	def __init__(self, interval, dialogId, duration, imageId, imageArr):
		self.interval = interval
		self.dialogId = dialogId
		self.duration = duration
		self.imageArr = imageArr
		self.imageId = imageId
		self.position = 0
		jobmanager.BoxeeJob.__init__(self, "Breaking News Job", interval)

	def process(self):
		mc.ActivateWindow(self.dialogId)
		mc.GetWindow(self.dialogId).GetImage(self.imageId).SetTexture(self.imageArr[self.position])
		self.position = self.position + 1
		if (self.position == len(self.imageArr)):
			self.position = 0
		
		time.sleep(self.duration)
		xbmc.executebuiltin("Dialog.Close("+ str(self.dialogId) +")")
		
class MenuScrollJob(jobmanager.BoxeeJob):	## TODO ##
	
	def __init__(self, interval, size, leftImage, rightImage, topImage):
		self.size = size
		self.interval = interval
		self.leftImage = leftImage
		self.rightImage = rightImage
		self.topImage = topImage
		self.counter = 1
		jobmanager.BoxeeJob.__init__(self, "Menu Scroll Job", interval)

	def process(self):
		self.leftImage.SetTexture(str(self.counter) + "Left.png")
		self.rightImage.SetTexture(str(self.counter) + "right.png")
		self.topImage.SetTexture(str(self.counter) + "Middle.png")
		self.counter = self.counter + 1
		
		if (self.counter > self.size):
			self.counter = 1
		
		



