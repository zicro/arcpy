import arcpy, os
import arcpy.mapping as MAP

#Read parameters from dialog
mxdPath = arcpy.GetParameterAsText(0)
xShift = arcpy.GetParameterAsText(1)
yShift = arcpy.GetParameterAsText(2)
outPath = arcpy.GetParameterAsText(3)

#Reference the map document
MXD = MAP.MapDocument(mxdPath)

#Loop through each page layout element and shift the x and y values
for elm in MAP.ListLayoutElements(MXD):
    elm.elementPositionX = elm.elementPositionX + float(xShift)
    elm.elementPositionY = elm.elementPositionY + float(yShift)

#Save changes to new MXD and automatically open
MXD.saveACopy(outPath)
os.startfile(outPath)
