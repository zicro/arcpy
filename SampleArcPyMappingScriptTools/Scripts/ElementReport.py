import arcpy, os, datetime

#Read parameters from tool
mxdPath = arcpy.GetParameterAsText(0)
output = arcpy.GetParameterAsText(1)

try:

    #Create r/w output file
    outFile = open(output, "w")

    #Generate Report header
    outFile.write("Rapport du Mise en page: \n")
    outFile.write("\n")
    outFile.write("ce Rapport liste les differentes proprietes pour chaque couche du Projet (.MXD). \n")
    outFile.write("\n")
    outFile.write("MXD location: " + mxdPath + "\n")
    outFile.write("\n")
    outFile.write("Date: " + str(datetime.datetime.today().strftime("%B %d, %Y")) + "\n")
    outFile.write("\n")

    #Reference MXD file
    mxd = arcpy.mapping.MapDocument(mxdPath)
                
    #Report data frame elements
    if len(arcpy.mapping.ListLayoutElements(mxd, "DATAFRAME_ELEMENT")) > 0:
        outFile.write("\n")
        outFile.write(" DATA FRAME ELEMENTS: \n")
        
        for elm in arcpy.mapping.ListLayoutElements(mxd, "DATAFRAME_ELEMENT"):
            outFile.write("\n")
            outFile.write("\t Name:                " + elm.name + "\n")
            outFile.write("\t X Position:          " + str(elm.elementPositionX) + "\n")
            outFile.write("\t Y Position:          " + str(elm.elementPositionY) + "\n")
            outFile.write("\t Height:              " + str(elm.elementHeight) + "\n")
            outFile.write("\t Width:               " + str(elm.elementWidth) + "\n")

    #Report graphic elements
    if len(arcpy.mapping.ListLayoutElements(mxd, "GRAPHIC_ELEMENT")) > 0:
        outFile.write("\n")
        outFile.write(" GRAPHIC ELEMENTS: \n")
        
        for elm in arcpy.mapping.ListLayoutElements(mxd, "GRAPHIC_ELEMENT"):
            outFile.write("\n")
            outFile.write("\t Name:                " + elm.name + "\n")
            outFile.write("\t X Position:          " + str(elm.elementPositionX) + "\n")
            outFile.write("\t Y Position:          " + str(elm.elementPositionY) + "\n")
            outFile.write("\t Height:              " + str(elm.elementHeight) + "\n")
            outFile.write("\t Width:               " + str(elm.elementWidth) + "\n")

    #Report legend elements
    if len(arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT")) > 0:
        outFile.write("\n")
        outFile.write(" LEGEND ELEMENTS: \n")
        
        for elm in arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT"):
            outFile.write("\n")
            outFile.write("\t Name:                " + elm.name + "\n")
            outFile.write("\t Parent data frame:   " + elm.parentDataFrameName + "\n")
            outFile.write("\t Title:               " + elm.title + "\n")
            outFile.write("\t X Position:          " + str(elm.elementPositionX) + "\n")
            outFile.write("\t Y Position:          " + str(elm.elementPositionY) + "\n")
            outFile.write("\t Height:              " + str(elm.elementHeight) + "\n")
            outFile.write("\t Width:               " + str(elm.elementWidth) + "\n")

    #Report map surround elements
    if len(arcpy.mapping.ListLayoutElements(mxd, "MAPSURROUND_ELEMENT")) > 0:
        outFile.write("\n")
        outFile.write(" MAP SURROUND ELEMENTS: \n")
        
        for elm in arcpy.mapping.ListLayoutElements(mxd, "MAPSURROUND_ELEMENT"):
            outFile.write("\n")
            outFile.write("\t Name:                " + elm.name + "\n")
            outFile.write("\t Parent data frame:   " + elm.parentDataFrameName + "\n")
            outFile.write("\t X Position:          " + str(elm.elementPositionX) + "\n")
            outFile.write("\t Y Position:          " + str(elm.elementPositionY) + "\n")
            outFile.write("\t Height:              " + str(elm.elementHeight) + "\n")
            outFile.write("\t Width:               " + str(elm.elementWidth) + "\n")

    #Report picture elements
    if len(arcpy.mapping.ListLayoutElements(mxd, "PICTURE_ELEMENT")) > 0:
        outFile.write("\n")
        outFile.write(" PICTURE ELEMENTS: \n")
        
        for elm in arcpy.mapping.ListLayoutElements(mxd, "PICTURE_ELEMENT"):
            outFile.write("\n")
            outFile.write("\t Name:                " + elm.name + "\n")
            outFile.write("\t X Position:          " + str(elm.elementPositionX) + "\n")
            outFile.write("\t Y Position:          " + str(elm.elementPositionY) + "\n")
            outFile.write("\t Height:              " + str(elm.elementHeight) + "\n")
            outFile.write("\t Width:               " + str(elm.elementWidth) + "\n")

    #Report text elements
    if len(arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")) > 0:
        outFile.write("\n")
        outFile.write(" TEXT ELEMENTS: \n")
        
        for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
            outFile.write("\n")
            outFile.write("\t Name:                " + elm.name + "\n")
            outFile.write("\t Text string:         " + elm.text + "\n")
            outFile.write("\t X Position:          " + str(elm.elementPositionX) + "\n")
            outFile.write("\t Y Position:          " + str(elm.elementPositionY) + "\n")
            outFile.write("\t Height:              " + str(elm.elementHeight) + "\n")
            outFile.write("\t Width:               " + str(elm.elementWidth) + "\n")

    #Close the file
    outFile.close()

    #Automatically open the file in associated TXT application
    os.startfile(output)

    #Delete all variables
    del mxdPath, outFile, mxd, output

except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))
