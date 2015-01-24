import arcpy, os

#Read parameters from dialog
mxdPath = arcpy.GetParameterAsText(0)
dfName = arcpy.GetParameterAsText(1)
layerName = arcpy.GetParameterAsText(2)
layerFile = arcpy.GetParameterAsText(3)
outMXD = arcpy.GetParameterAsText(4)

#Update layer symbology
mxd = arcpy.mapping.MapDocument(mxdPath)
df = arcpy.mapping.ListDataFrames(mxd, dfName)[0]
updateLayer = arcpy.mapping.ListLayers(mxd, layerName)[0]
sourceLayer = arcpy.mapping.Layer(layerFile)
arcpy.mapping.UpdateLayer(df, updateLayer, sourceLayer, True)

#Save changes to new MXD and automatically open
mxd.saveACopy(outMXD)
os.startfile(outMXD)
del mxd, sourceLayer

