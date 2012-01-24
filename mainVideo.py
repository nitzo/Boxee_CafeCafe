import mc
import jobmanager
import jobs
import utils
from params import *

myJobManager = 0
adsList = 0
adImage = 0

def onload():
	global myJobManager, rssRoot, adsList, adImage
	
	
	#Set Global Lists
	adsList = mc.GetActiveWindow().GetList(120)
	adImage = mc.GetActiveWindow().GetImage(150)

	#Create JobManager
	myJobManager = jobmanager.BoxeeJobManager(1)
	
	utils.SetScrollAds(adsList, adImage, myJobManager)
	utils.SetBreakingNews(14010, myJobManager)
	
	#Start Job Manager
	myJobManager.start()
	
	#Play Video
	item = mc.ListItem(mc.ListItem.MEDIA_VIDEO_CLIP)
	item.SetPath('/media/unnamed/1.mp4')
	item.SetContentType('video/mp4')
	mc.GetPlayer().PlayInBackground(item)
	

def onunload():
	global myJobManager
	myJobManager.stop()	

