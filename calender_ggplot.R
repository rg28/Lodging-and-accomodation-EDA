setwd("C:/Users/HP/Desktop/meals/eda")
list.files()

#creating data in required format
require(XLConnect)
require(readxl)
library(dplyr)
cal=read.csv("calendar.csv")
View(cal)
dim(cal)
cal=filter(cal,cal$available=="t")
cal=subset(cal,select = -c(available))
cal$price=as.character(cal$price)
cal$price_number=substr(cal$price,2,length(cal$price))
cal$price_number=as.numeric(cal$price_number)
cal$date=as.POSIXct(cal$date)
cal$day=format(cal$date,"%w")
cal$month=format(cal$date,"%m")
cal$day=as.factor(cal$day)
cal$month=as.factor(cal$month)

#visuals
library(ggplot2)
#after plotting and seeing how huge the values are divided the price by 1000 and visualized
cal$price_number=cal$price_number/1000

p1 <- ggplot(cal,aes(month,price_number)) + 
  geom_bar(stat="sum",na.rm=TRUE,show.legend=FALSE)+labs(x="month",y="sum of price")
plot(p1)
p1 <- ggplot(cal,aes(day,price_number),show.legend=FALSE) + 
  geom_bar(stat="sum",na.rm=TRUE,show.legend=FALSE)+labs(x="day",y="price")
  
plot(p1)


