library(ggplot2)
library(plotly)
Country=c("China","India","Canada","United States","Russia","Germany","Kenya")
CPSPD<-data.frame(read.csv("../Dataset/consumption-per-smoker-per-day.csv", header = TRUE, sep = ","))
CPSPD<-edit(CPSPD)
#for a particular country
Y<-subset(CPSPD,Entity%in%Country)
ggplotly(ggplot(Y,aes(x=Year,y=cigarette,fill=factor(Code)))+
  geom_bar(stat="identity",position="dodge")+
  scale_fill_discrete("Code")+
  xlab("Year")+ylab("Cigarette")+ggtitle("Bar chart of different countries C/S"))
ggplotly(ggplot(subset(Y,Entity=="India"),aes(x=Year,y=cigarette,fill=factor(Code)))+
  geom_bar(stat="identity",position="dodge")+
  scale_fill_discrete("Code")+
  xlab("Year")+ylab("Cigarette")+ggtitle("C/S for india from 1980-2012"))
NDS<-data.frame(read.csv("../Dataset/number-of-total-daily-smokers.csv", header = TRUE,sep = ","))
NDS<-edit(NDS)
ND <- subset(NDS,Entity%in%Country,select=1:4)
ND12 <- subset(ND, Year==2012,select=1:4)
ND00 <- subset(ND, Year==2000,select=1:4)
ND80 <- subset(ND, Year==1980 ,select=1:4)

par(mfrow=c(1,3))
pie(ND80$NDS, labels=ND80$Entity)
pie(ND00$NDS, labels=ND00$Entity)
pie(ND12$NDS, labels=ND12$Entity)

p<-ggplotly(ggplot(Y, aes(x=Entity, y=cigarette, fill=Code)) +
    geom_boxplot(width=.01)+geom_violin()+  xlab("Country")+ylab("Cigarettes per smoker")+
    ggtitle("Violin plot of no. of cigarettes per smoker"))
p
i<-ggplotly(ggplot(ND, aes(x=Entity, y=NDS, fill=Code)) +
              ggtitle("box plot of no. of smokers")+
  geom_boxplot(outlier.colour="red", outlier.shape=8,
               outlier.size=4)+  xlab("Country")+ylab("Number of daily smokers"))
i

CD<-data.frame(read.csv("../Dataset/smoking-and-secondhand-deaths.csv", header = TRUE, sep = ","))
CD<-subset(CD,Entity%in%Country)
CD<-edit(CD)
CDCHN<-subset(CD, Entity=="China")
ggplotly(ggplot(CDCHN, aes(x=Year, y=SD)) +
  geom_point(size=2, shape=18, color='red')+
  geom_smooth(method=lm, linetype="dashed",
              color="darkred")+ylab("Smoker death")+ggtitle("Scatter- regression of smoker deaths in china"))
CDIND<-subset(CD, Entity=="India")
ggplotly(ggplot(CDIND, aes(x=Year, y=SD)) +
  geom_point(size=2, shape=18, color='Blue')+
  geom_smooth(method=lm, linetype="dashed",
              color="darkred")+ylab("Smoker death")+ggtitle("Scatter- regression of smoker deaths in India"))
SDbA<-data.frame(read.csv("../Dataset/share-of-cancer-deaths-attributed-to-tobacco.csv", header=TRUE,sep=","))
SDbA<-edit(SDbA)
SDbA<-subset(SDbA,Year==2010)
p=ggplotly(ggplot(SDbA, aes(x=SDbA$AgeStd, fill=Entity)) +
  geom_histogram()+
    ggtitle("Histogram of Age standardized death % among all countries")+
    xlab("Age Std %")+ylab("No,of countries"))
p
