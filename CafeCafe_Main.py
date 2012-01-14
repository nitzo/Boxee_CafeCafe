import mc
import jobmanager
import scrollAdsJob

myJobManager = 0

def onload():
	global myJobManager
	
	#Set Ads Container Path & Load Content
	xmlpath = "www.macam.ac.il/nitzan/Boxee/1.xml"
	mc.ShowDialogNotification(xmlpath)
	mc.GetWindow(14001).GetList(123).SetContentURL("rss://"+xmlpath)
	
	#Create JobManager (For Ads Scrolling)
	myJobManager = jobmanager.BoxeeJobManager(10)
	scrollAds()

def onunload():
	global myJobManager
	mc.LogDebug("Closing window !!16:25!!")
	myJobManager.stop()
	
	
	
	
def playVideo():
	mc.ActivateWindow(14001)
	item = mc.ListItem(mc.ListItem.MEDIA_VIDEO_CLIP)
	item.SetPath('/media/unnamed/1.mp4')
	item.SetContentType('video/mp4')
	mc.GetPlayer().PlayInBackground(item)


def scrollAds():
	global myJobManager
	
	myJob = scrollAdsJob.ScrollAdsJob(10)
	myJobManager.addJob(myJob)
	myJobManager.run()
	




	
def open(url):
    import sys
    import os
    p=sys.platform
    url='"'+url+'"'
    if p[:3] == "win":
        return os.startfile(url)
    if p == "darwin":
        return os.system("open "+url)
#TODO linux
    return os.system("xdg-open "+url)

	
	
	

