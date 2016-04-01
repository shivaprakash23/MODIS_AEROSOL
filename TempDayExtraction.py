# Name: Rename.py
# Developed: shivaprakash yaragal
# Description: Rename tiff file 

# Import system modules
import arcpy
from arcpy.sa import *

# Set workspace
arcpy.env.workspace = "D:\\Shivaprakash\\TEST\\project_aerosol\\TempDay"
#listing the raster 
rasterlist = arcpy.ListRasters("*","TIFF")
# raster renaming
for raster in rasterlist:
	raster1=raster.split('_')
	raster2=raster1[3].split('-')
	out="TD"+raster2[1]+raster2[0]
	print(out)
	arcpy.Rename_management(raster, out)


arcpy.env.workspace = "D:\\Shivaprakash\\TEST\\project_aerosol\\TempDay"
rasterlist = arcpy.ListRasters("*","TIFF")
input1="D:\\Shivaprakash\\TEST\\project_aerosol\\PrjData.gdb\\citiesTempDay"
ExtractMultiValuesToPoints(input1,rasterlist)




arcpy.env.workspace = "D:\\Shivaprakash\\TEST\\project_aerosol\\TempDay"
rasterlist = arcpy.ListRasters("*","TIFF")
input1="D:\\Shivaprakash\\TEST\\project_aerosol\\PrjData.gdb\\MegaCitiesTempDay"
ExtractMultiValuesToPoints(input1,rasterlist)



