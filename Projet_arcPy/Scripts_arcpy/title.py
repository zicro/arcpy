import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
print mxd.title
mxd.title = "Geo Map World"
mxd.saveACopy(r"C:\cities\projet.mxd")