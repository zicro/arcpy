import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
mapping.ExportToPDF(mxd,r"C:\cities\PageLayout.pdf")