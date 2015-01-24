import arcpy

try:
	mxd 		= arcpy.mapping.MapDocument("CURRENT")
	df 			= arcpy.mapping.ListDataFrames(mdx)[0]
	newlayer_1 	= arcpy.mapping.Layer(r"c:\cities\cities.shp")
	print newlayer_1
	arcpy.mapping.Addlayer(df,newlayer_1,"top")

	newlayer_2 = arcpy.mapping.Layer(r"C:\cities\rivers.shp")
	print newlayer_2
	arcpy.mapping.Addlayer(df,newlayer_2,"top")

	newlayer_3 = arcpy.mapping.Layer(r"C:\cities\lakes.shp")
	print newlayer_3
	arcpy.mapping.Addlayer(df,newlayer_3,"top")

	newlayer_4 = arcpy.mapping.Layer(r"C:\cities\counties.shp")
	print newlayer_4
	arcpy.mapping.Addlayer(df,newlayer_4,"top")

	arcpy.RefreshActiveView()
	arcpy.RefreshTOC()

	# enregistrer la carte to persist the added layer

	mxd.save()

except Exception as ex:
	print ex.args[0]




