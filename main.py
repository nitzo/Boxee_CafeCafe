import mc
import jobmanager
import jobs
import utils
from params import *

myJobManager = 0
adsList = 0
leftImage = 0
rightImage = 0
topImage = 0
adImage = 0

def onload():
	global myJobManager, rssRoot, adsList, leftImage, rightImage, topImage, adImage
	
	
	#Set Global Lists/Images
	adsList = mc.GetActiveWindow().GetList(120)
	
	leftImage = mc.GetActiveWindow().GetImage(300)
	rightImage = mc.GetActiveWindow().GetImage(310)
	topImage = mc.GetActiveWindow().GetImage(320)

	adImage = mc.GetActiveWindow().GetImage(150)
			
	#Create JobManager
	myJobManager = jobmanager.BoxeeJobManager(1)
	
	#Scroll Menu Automatically	
	myJob = jobs.MenuScrollJob(menuInterval, 6, leftImage, rightImage, topImage)
	myJob.process()
	myJobManager.addJob(myJob)
		
	utils.SetScrollAds(adsList, adImage, myJobManager)
		
	utils.SetBreakingNews(14010, myJobManager)
	
	#Start Job Manager
	myJobManager.start()
	

def onunload():
	global myJobManager
	myJobManager.stop()	

#Scroll Left & Right Menus according to scrollDirection
def scrollMenu(scrollDirection="none"):
	global leftMenuList, rightMenuList
	
	#Scroll Menu List
	{
		"left" : leftMenuList.ScrollPageUp,
		"right": leftMenuList.ScrollPageDown,
		"none" : leftMenuList.GetFocusedItem		#Do Nothing
	}[scrollDirection]()
		
		
	#Get Focused ListItem
	focusedItem = utils.GetFocusedListItem(leftMenuList)
	
	#focusedItem.Dump()
	#mc.ShowDialogNotification(focusedItem.GetPath())
	
	#Set Right Menu Content Url Based on focusedItem
	rightMenuList.SetContentURL(focusedItem.GetPath())
	


	
	
