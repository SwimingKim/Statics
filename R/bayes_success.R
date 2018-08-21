library(party)
library(e1071)
library(nnet)
library(caret)
library(gmodels)



setwd("C:/Users/SuYoung/Desktop/challenge_data/챌린지리그_데이터")
data<-read.csv("BGCON_CUST_DATA.csv")

str(data)
column<- c('SIU_CUST_10', 'SEX', 'AGE', 'RESI_COST', 'RESI_T1PE_CODE',
            'FP_CAREER','CUST_RGST', 'CTPR', 'OCCP_GRP_1', 'OCCP_GRP_2',
            'TOTALPREM','MI0CRDT','MAXCRDT','WEDD_10', 'MATE_OCCP_GRP_1',
           'MATE_OCCP_GRP_2','CHLD_C0T','LTB0_CHLD_AGE','MAX_PA1M_1M',
           'MAX_PRM','CUST_I0CM','RCBASE_HSHD_I0CM','JPBASE_HSHD_I0CM')

view <- subset(data,select=column, drop=TRUE)
#view<-view[complete.cases(view),] #NA제거

#write.csv(view, "middle.csv")

#index <- createDataPartition(data$DIVIDED_SET, p=0.75, list=FALSE)
index <- sample(2, nrow(view), replace=TRUE, prob = c(0.7,0.3))
train<- view[index==1,]
test<-view[index==2,]

write.csv(train,"tr.csv")
write.csv(test,"te.csv")


nb<-naiveBayes(as.factor(SIU_CUST_10)~.,data=train,laplace = 1)

pred<-predict(nb,test,type = "raw")
write.csv(pred,"result_raw.csv")

pred<-predict(nb,test)
write.csv(pred,"result.csv")

CrossTable(pred, test$SIU_CUST_10, prop.chisq = FALSE, prop.t = FALSE, dnn = c('predicted', 'actual'))
conf.mat<-table(pred,test$SIU_CUST_10)
conf.matBGCON_CUST_DATABGCON_CUST_DATA

(accuravy<-sum(diag(conf.mat))/sum(conf.mat)*100)
