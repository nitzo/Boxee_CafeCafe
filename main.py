import mc
import jobmanager
import jobs
import utils
from params import *

myJobManager = 0
adsList = 0
leftMenuList = 0
rightMenuList = 0
adImage = 0

def onload():
	global myJobManager, rssRoot, adsList, leftMenuList, rightMenuList, adImage
	
	
	#Set Global Lists
	adsList = mc.GetActiveWindow().GetList(120)
	rightMenuList = mc.GetActiveWindow().GetList(130)
	leftMenuList = mc.GetActiveWindow().GetList(140)

	adImage = mc.GetActiveWindow().GetImage(150)
			
	#Set Left Menu Container Path
	leftMenuList.SetContentURL("rss://"+rssRoot+"Menus/menus.xml")
	
	#Scroll Right Menu To First Item
	scrollMenu()
	
	#Create JobManager
	myJobManager = jobmanager.BoxeeJobManager(1)
	
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
	

	
	
