import arcpy, os, string

#Read input parameters from script tool
mxdList = string.split(arcpy.GetParameterAsText(0), ";")
outPDFpath = arcpy.GetParameterAsText(1)

#Create a new PDF object to store the results
outputPDF = arcpy.mapping.PDFDocumentCreate(outPDFpath)

#Loop through each MXD in the list, export, create a temporary PDF name,
# and append to final, output PDF
for mxdPath in mxdList:
    mxd = arcpy.mapping.MapDocument(mxdPath)
    PDFPath = mxdPath[:-4] + "_temp.pdf"
    arcpy.mapping.ExportToPDF(mxd, PDFPath)
    outputPDF.appendPages(str(PDFPath))


#Save the changes and open the result automatically   
outputPDF.saveAndClose()
os.startfile(outPDFpath)

#Remove variable reference to file
del outputPDF

