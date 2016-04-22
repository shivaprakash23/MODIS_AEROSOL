aerosol=read.csv("test3D.csv",header=TRUE)
aod <- aerosol$AOD
temp <- aerosol$TEMP
apr<- aerosol$APR
month <- aerosol$month
library(scatterplot3d)
source('http://www.sthda.com/sthda/RDoc/functions/addgrids3d.r')
colors <- c("#999999", "#E69F00", "#56B4E9","#000000","#000070","#7FFFD4","#B33F26","#481B2A","#E4D93C","#981BA2","#EBEFFA","#ACE5B4")
colors <- colors[as.numeric(month)]
shapes = c(16, 17, 18,12,13,14,15,19,20,21,22,23)
shapes <- shapes[as.numeric(month)]
aod3d <- scatterplot3d(apr,aod,temp,pch=shapes,color=colors,type="h",grid=TRUE,box=FALSE, main="3D Scatter Plot for Aerosol",xlab="ARP in Percentage",zlab="Temperature Anomoly in Celcius",ylab="AOD")
addgrids3d(apr,aod,temp, grid = c("xy", "xz", "yz"))
legend("topright", legend = levels(month),pch = c(16, 17, 18,12,13,14,10,11,9,21,22,23))