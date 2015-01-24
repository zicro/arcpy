import arcpy, os

try:

    #Read input parameters from GP dialog
    layerName = arcpy.GetParameterAsText(0)
    layerFile = arcpy.GetParameterAsText(1)

    #Reference map document and layer files on disk
    mxd = arcpy.mapping.MapDocument("CURRENT")
    sourceLayer = arcpy.mapping.Layer(layerFile)

    #find layer with specified name
    for df in arcpy.mapping.ListDataFrames(mxd):
        for lyr in arcpy.mapping.ListLayers(mxd):
            if lyr.name == layerName:
                arcpy.mapping.UpdateLayer(df, lyr, sourceLayer, False)

    #Refresh the ArMap application
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()

    del mxd, sourceLayer

except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))
