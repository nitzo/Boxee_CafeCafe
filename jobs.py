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
		
		



