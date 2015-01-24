import arcpy, os, string

#Read input parameters from script tool
PDFList = string.split(arcpy.GetParameterAsText(0), ";")
outPDFpath = arcpy.GetParameterAsText(1)

#Create a new PDF object to store the results
outputPDF = arcpy.mapping.PDFDocumentCreate(outPDFpath)

#Loop through and append each PDF in the list
for eachPDF in PDFList:
    outputPDF.appendPages(str(eachPDF))

#Save the changes and open the result automatically   
outputPDF.saveAndClose()
os.startfile(outPDFpath)

#Remove variable reference to file
del outputPDF

