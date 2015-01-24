import arcpy, string

#Read input parameters from script tool
mxdPath = arcpy.GetParameterAsText(0)
pageList = string.split(arcpy.GetParameterAsText(3), ";")
printer = arcpy.GetParameterAsText(4)

#Reference the map and the data driven page object
mxd = arcpy.mapping.MapDocument(mxdPath)
ddp = mxd.dataDrivenPages
for eachPage in pageList:
    arcpy.AddMessage(str(eachPage))
    pageID = ddp.getPageIDFromName(str(eachPage.strip("'")))
    ddp.currentPageID = pageID
    ddp.printPages(printer, "CURRENT")

#Remove variable reference to file
del mxd
