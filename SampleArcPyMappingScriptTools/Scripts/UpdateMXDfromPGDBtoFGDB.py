import arcpy, os

try:

    #Read parameters from dialog
    inputGDB = arcpy.GetParameterAsText(0)
    outputGDB = arcpy.GetParameterAsText(1)
    inputMXD = arcpy.GetParameterAsText(2)
    outputMXD = arcpy.GetParameterAsText(3)
    updateSQL = arcpy.GetParameter(4)

    #Update pGDB TO fGDB
    mxd = arcpy.mapping.MapDocument(inputMXD)
    mxd.replaceWorkspaces(inputGDB, "ACCESS_WORKSPACE", outputGDB, "FILEGDB_WORKSPACE")

    #Update query definitions
    if updateSQL:
        for lyr in arcpy.mapping.ListLayers(mxd):
            if lyr.supports("definitionQuery"):
                lyr.definitionQuery = lyr.definitionQuery.replace("[","\"")
                lyr.definitionQuery = lyr.definitionQuery.replace("]","\"")
            if lyr.supports("labelClasses"):
                for lblClass in lyr.labelClasses:
                    lblClass.SQLQuery = lblClass.SQLQuery.replace("[", "\"")
                    lblClass.SQLQuery = lblClass.SQLQuery.replace("]", "\"")

    #Save and open resulting MXD
    mxd.saveACopy(outputMXD)
    os.startfile(outputMXD)

except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))
