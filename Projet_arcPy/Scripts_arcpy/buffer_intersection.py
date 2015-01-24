import arcpy
arcpy.enc.workspace = "c:\cities"
arcpy.env.overwriteOutput = True

#script arguments
cities_shp = arcpy.GetParameterAsText(0)
rivers_shp = arcpy.GetParameterAsText(1)
citiesNearRivers = arcpy.GetParameterAsText(2)

#Local variabkes
rivers_Buffer = "rivers_buffer.shp"

#Process : Zone Tampon
arcpy.Buffer_analysis(rivers_shp,rivers_Buffer,"10 Miles")

#Process : Intersection
#(Separation du nom des clases d'entites en entree dans une liste)
clipfeatures = rivers_Buffer + ";" + cities_shp 
arcpy.Intersect_analysis(clipfeatures,citiesNearRivers)