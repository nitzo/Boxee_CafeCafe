import mc

def GetFocusedListItem(list):
	
	focusedItemId = list.GetFocusedItem()
	return list.GetItem(focusedItemId)