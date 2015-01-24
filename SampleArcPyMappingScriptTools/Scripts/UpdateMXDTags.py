import arcpy, os

try:

    #Read parameters from dialog
    mxdPath = arcpy.GetParameterAsText(0)
    outputMXD = arcpy.GetParameterAsText(1)

    #Reference Map Document
    mxd = arcpy.mapping.MapDocument(mxdPath)

    #Generate unique, sorted list of layer names
    layers = arcpy.mapping.ListLayers(mxd)
    layerList = []
    for lyr in layers:
        if not lyr.isGroupLayer:
            layerList.append(lyr.name)
    uniqueList = list(set(layerList))
    uniqueList.sort()

    #Update map document tags
    tagList = ",".join(uniqueList)  
    mxd.tags = tagList

    #save map document
    mxd.saveACopy(outputMXD)
    os.startfile(outputMXD)

    del mxd
    
except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))



