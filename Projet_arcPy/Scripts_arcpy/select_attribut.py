import arcpy
from arcpy import env

arcpy.env.workspace = r"C:\cities" #added raw string indicateur r
M1 = r"C:\cities\rivers.shp" # (r"C:\cities\rivers.shp") is a tuple, not a string
# parcourir un ensemble d'enregistrements de la table ou d'une classe d'entité, en renvoyant un objet Row
rows = arcpy.SearchCursor(M1,'"NAME" = \'Misslssippi\'')
row = rows.next()
largeur = row.getValue("MILES")
where = '"MILES">'+str(largeur)
arcpy.SelectLayerAttribute_management("rivers","New_SELECTION",where)
arcpy.RefreshActiveView()