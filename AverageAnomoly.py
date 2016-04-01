import arcpy
from arcpy import env
env.workspace = "D:/Shivaprakash/TEST/project_aerosol/PrjData.gdb"
fields="D:/Shivaprakash/TEST/project_aerosol/PrjData.gdb/citiesTempNight"
	
fieldList = arcpy.ListFields(fields)
table="citiesTempNight"

count=0

for f in fieldList:
	if (f.name != "OBJECTID" and f.name != "Shape" and f.name != "name" and f.name != "latitude" and f.name != "longitude" and f.name !="Stata" and f.name !="population" and f.name !="sex_ratio" and f.name !="literacy" and count<181 ):
		print(f.name)
		count=count+1
		print(count)
		field_name="TA"+f.name[2:]
		print(field_name)
		arcpy.AddField_management(table,field_name,"Double","9","5","","","","")

featureClass = "D:/Shivaprakash/TEST/project_aerosol/PrjData.gdb/citiesTempNight"

for f in fieldList:
	cursor = arcpy.UpdateCursor(fields)
	for row in cursor:
		count=0
		
		if (f.name != "OBJECTID" and f.name != "Shape" and f.name != "name" and f.name != "latitude" and f.name != "longitude" and f.name !="Stata" and f.name !="population" and f.name !="sex_ratio" and f.name !="literacy" and count<181 ):
			field1="TN"+f.name[2:]
			field2="TD"+f.name[2:]
			print(field1,field2)
			value=0
			if(row.getValue(field1) != None and row.getValue(field2) != None ):
				value=(row.getValue(field1)+row.getValue(field2))/2
				field3="TA"+f.name[2:]
				row.setValue(field3,value )
				cursor.updateRow(row)
			else:
				print("null encountered")
			count=count+1
			

			
			
