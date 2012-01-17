import mc
import jobmanager
import jobs

myJobManager = 0
rssRoot = "www.macam.ac.il/nitzan/Boxee/"

def onload():
	global myJobManager
	global rssRoot
		
	#Set Ads Container Path & Load Content
	xmlpath = rssRoot + "ads.xml"
	mc.ShowDialogNotification(xmlpath)
	mc.GetWindow(14000).GetList(120).SetContentURL("rss://"+xmlpath)
	
	#Set Menu Contaier Path
	xmlpath = rssRoot + "menu1.xml"
	mc.GetWindow(14000).GetList(130).SetContentURL("rss://"+xmlpath)
	
	#Create JobManager (For Ads Scrolling)
	myJobManager = jobmanager.BoxeeJobManager(2)
	
	#Add Ads Scroll Job To JobManager
	myJob = jobs.ContainerScrollJob(10, mc.GetWindow(14000).GetList(120))
	myJobManager.addJob(myJob)
	
	#Start Job Manager
	myJobManager.start()
	

def onunload():
	global myJobManager
	myJobManager.stop()	
	
	
