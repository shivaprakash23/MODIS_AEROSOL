library(rgl)
plot3d(apr,aod,temp,col=heat.colors(1000))
plot3d(apr,aod,temp,xlab="Aerosol Partical Radius",ylab="AOD",zlab="Temperature Anomoly",type="s",col=heat.colors(1000))