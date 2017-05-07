library(party)
library(e1071)
library(nnet)
library(caret)

setwd("C:/Users/SuYoung/Desktop/새 폴더/CUST")

#cust데이터
data<-read.csv("BGCON_CUST_DATA.csv")

str(data)
#column<- c("CUST_ID","DIVIDED_SET","SIU_CUST_YN","SEX","AGE","RESI_COST","RESI_TYPE_CODE",
#           "FP_CAREER","CUST_RGST","CTPR","OCCP_GRP_1","OCCP_GRP_2","TOTALPREM","MINCRDT",
#           "MAXCRDT","WEDD_YN","MATE_OCCP_GRP_1","MATE_OCCP_GRP_2","CHLD_CNT",
#           "MAX_PAYM_YM","MAX_PRM","CUST_INCM","RCBASE_HSHD_INCM","JPBASE_HSHD_INCM")

column<- c("CUST_ID","DIVIDED_SET","SIU_CUST_YN","LTBN_CHLD_AGE", "MAX_PRM", "CUST_INCM", 
           "MAXCRDT", "RESI_COST", "CUST_RGST")

view <- subset(data,select=column)
#view<-view[complete.cases(view),] #NA제거

set.seed(1234)
index <- sample(2, nrow(view), replace=TRUE, prob = c(0.7,0.3))

# train과 test의 구분이 이상하다
# view[index,]로 작성하면 사기데이터가 누락
# view[index==1,]로 작성하면 모든 test데이터가 나오지 않는
train<- view[,]#전체 데이터
test<-view[-index,]

write.csv(train,"tr.csv")
write.csv(test,"te.csv")

nb<-naiveBayes(as.factor(SIU_CUST_YN)~.,data=train, laplace = 10)
nb

pred<-predict(nb,test,type = "raw")
write.csv(pred,"result_raw.csv")

pred<-predict(nb,test)
write.csv(pred,"result.csv")

conf.mat<-table(pred,test$SIU_CUST_YN)
conf.mat

#confusionMatrix(pred, test$SIU_CUST_YN)

(accuravy<-sum(diag(conf.mat))/sum(conf.mat)*100)
