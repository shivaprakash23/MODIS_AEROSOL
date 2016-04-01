import arcpy, os
India_shp = "D:\\Shivaprakash\\design cities\\Megapolies\\megalopolis.gdb\\india.shp"

arcpy.env.workspace = "D:\\Shivaprakash\\TEST\\Aerosol\\New"

rasterlist = arcpy.ListRasters("*","TIFF")

for raster in rasterlist:
	raster1=raster.split('_')
	raster2=raster1[4].split('-')
	tx_name = os.path.join("D:\\Shivaprakash\\TEST\\out", "AOD" + raster2[1]+raster2[0])
	print(tx_name)
	arcpy.Clip_management(raster, "#", tx_name, India_shp, "", "ClippingGeometry", "")