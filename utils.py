import mc
import jobs
from params import *

def SetScrollAds(adsList, adImage, myJobManager):
	global adInterval
	
	if (adSource == "rss"):
		adsList.SetVisible(True)
		
		#Set Ads Container Path & Load Content
		adsList.SetContentURL("rss://"+rssRoot+"Ads/ads.xml")
		
		#Add Ads Scroll Job To JobManager
		myJob = jobs.ContainerScrollJob(adInterval, adsList)
		myJobManager.addJob(myJob)
	
	elif (adSource == "local"):
		adImage.SetVisible(True)
		
		#Create Local Image Scroll Job To JobManager
		myJob = jobs.LocalImageScrollJob(adInterval, adImage, localAdList)
		#Process First Image
		myJob.process()
		#Add to Job Manager
		myJobManager.addJob(myJob)
		
def SetBreakingNews(windowId, myJobManager):
	global breakingNewsInterval, breakingNewsDuration
	#Add Breaking News Job To JobManager
	myJob = jobs.BreakingNewsJob(breakingNewsInterval, windowId, breakingNewsDuration)
	myJobManager.addJob(myJob)
	


################################
#####	General Utilities	####
################################

def GetFocusedListItem(list):
	
	focusedItemId = list.GetFocusedItem()
	return list.GetItem(focusedItemId)