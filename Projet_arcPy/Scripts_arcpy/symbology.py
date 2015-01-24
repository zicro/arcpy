import arcpy
import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
df = mapping.ListDataFrames(mxd)[0]
updateLayer = mapping.ListLayers(mxd, "rivers", df)[0]
sourceLayer = mapping.Layer(r"C:\test\world_rivers.lyr")
mapping.updateLayer(df,updateLayer,sourceLayer,True)
if updateLayer.symbologyType == "GRADUATED_COLORS":
	updateLayer.symbology.valueField = "MILES"
	updateLayer.symbology.numClasses = 7
mxd.save()
	