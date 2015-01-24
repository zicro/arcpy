import arcpy, os, sys

try:

    #Read input parameters from GP dialog
    mxdPath = arcpy.GetParameterAsText(0)
    layerName = arcpy.GetParameterAsText(1)
    layerFile = arcpy.GetParameterAsText(2)
    outMXD = arcpy.GetParameterAsText(3)

    #Reference map document and layer files on disk
    mxd = arcpy.mapping.MapDocument(mxdPath)
    newLayer = arcpy.mapping.Layer(layerFile)

    #find layer with specified name
    for df in arcpy.mapping.ListDataFrames(mxd):
        for lyr in arcpy.mapping.ListLayers(mxd, data_frame=df):
            if lyr.name == layerName:
                arcpy.mapping.UpdateLayer(df, lyr, newLayer, False)

    #Save and open output            
    mxd.saveACopy(outMXD)
    os.startfile(outMXD)

    del mxd, newLayer
    
except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))
