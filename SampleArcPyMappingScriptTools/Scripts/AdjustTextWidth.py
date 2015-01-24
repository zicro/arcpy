import arcpy

#Read input parameters from script tool
elmName = arcpy.GetParameterAsText(0)
elmText = arcpy.GetParameterAsText(1)
elmWidth = arcpy.GetParameterAsText(2)

try:

    #Reference the current map document
    mxd = arcpy.mapping.MapDocument("CURRENT")         

    #Find the appropriate text element, start with a size of 100 and reduce until the text fits
    #the specified width.
    for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        if elm.name == elmName:
            x = 100
            elm.text = "<FNT name=\"Arial\" size=\"" + str(x) + "\">" + elmText + "</FNT>"
            while elm.elementWidth > float(elmWidth):
                elm.text = "<FNT name=\"Arial\" size=\"" + str(x) + "\">" + elmText + "</FNT>"
                x = x - 1

    #Refresh the display
    arcpy.RefreshActiveView()
                
except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))
