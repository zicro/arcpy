import arcpy

try:
    #Read parameters from dialog
    folderLocation = arcpy.GetParameterAsText(0)
    layerFile = arcpy.GetParameterAsText(1)
    dfName = arcpy.GetParameterAsText(2)
    position = arcpy.GetParameterAsText(3)

    #Reference map document from within ArcMap
    mxd = arcpy.mapping.MapDocument("CURRENT")

    #Reference the layer file on disk and data frame
    addLayer = arcpy.mapping.Layer(layerFile)
    df = arcpy.mapping.ListDataFrames(mxd, dfName)[0]

    #Add layer file
    arcpy.mapping.AddLayer(df, addLayer, position)

    #Refresh TOC and ActiveView
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()

    del mxd, addLayer

except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))
