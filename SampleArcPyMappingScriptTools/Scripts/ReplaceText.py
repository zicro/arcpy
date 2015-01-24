import arcpy, string, os 

#Read input parameters from script tool
mxdPath = arcpy.GetParameterAsText(0)
oldText = arcpy.GetParameterAsText(1)
newText = arcpy.GetParameterAsText(2)
case = arcpy.GetParameter(3)
exact = arcpy.GetParameter(4)
outputMXD = arcpy.GetParameterAsText(5)

try:
    #Referent the map document
    mxd = arcpy.mapping.MapDocument(mxdPath)         

    #Find all page layout text elements
    for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):     
        if exact:
            if case:
                if oldText == elm.text:
                    elmText = elm.text.replace(oldText, newText)
                    elm.text = elmText
            else:
                if oldText.upper() == elm.text.upper():
                    elmText = elm.text.upper().replace(oldText, newText)
                    elm.text = elmText   
        else:
            if case:
                if oldText in elm.text:
                    elmText = elm.text.replace(oldText, newText)
                    elm.text = elmText
            else:
                if oldText.upper() in elm.text.upper():
                    elmText = elm.text.upper().replace(oldText, newText)
                    elm.text = elmText                  
    mxd.saveACopy(outputMXD)
    os.startfile(outputMXD)

    del mxd

except Exception, e:
    import traceback
    map(arcpy.AddError, traceback.format_exc().split("\n"))
    arcpy.AddError(str(e))
