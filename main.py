import mc
import jobmanager
import jobs
import utils

myJobManager = 0
rssRoot = "www.macam.ac.il/nitzan/Boxee/"

adsList = 0
leftMenuList = 0
rightMenuList = 0

def onload():
	global myJobManager, rssRoot, adsList, leftMenuList, rightMenuList

	#Set Global Lists
	adsList = mc.GetActiveWindow().GetList(120)
	rightMenuList = mc.GetActiveWindow().GetList(130)
	leftMenuList = mc.GetActiveWindow().GetList(140)

	
	#Set Ads Container Path & Load Content
	adsList.SetContentURL("rss://"+rssRoot+"Ads/ads.xml")
		
	#Set Left Menu Container Path
	leftMenuList.SetContentURL("rss://"+rssRoot+"Menus/menus.xml")
	
	#Scroll Right Menu To First Item
	scrollMenu()
	
	#Create JobManager
	myJobManager = jobmanager.BoxeeJobManager(2)
	
	#Add Ads Scroll Job To JobManager
	myJob = jobs.ContainerScrollJob(10, adsList)
	myJobManager.addJob(myJob)
	
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
	

	
	
