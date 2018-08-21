library(party)
library(e1071)
library(nnet)
library(caret)

setwd("C:/Users/SuYoung/Desktop/새 폴더/CNTT")

#cust데이터
data<-read.csv("BGCON_CNTT_DATA.csv")

str(data)
#column<- c("POLY_NO",	"CUST_ID",	"CUST_ROLE",	"IRKD_CODE_DTAL",	"IRKD_CODE_ITEM",	"GOOD_CLSF_CDNM",
#           "CNTT_YM",	"CLLT_FP_PRNO",	"REAL_PAYM_TERM",	"SALE_CHNL_CODE",	"CNTT_STAT_CODE",	
#            "EXPR_YM",	"EXTN_YM",	"LAPS_YM",	"PAYM_CYCL_CODE",	"MAIN_INSR_AMT",	"SUM_ORIG_PREM",	
#           "RECP_PUBL",	"CNTT_RECP",	"MNTH_INCM_AMT",	"DISTANCE",	"SIU_CUST_YN")
column<- c("CUST_ID","SIU_CUST_YN", "CNTT_YM", "SUM_ORIG_PREM", "REAL_PAYM_TERM",
           "DISTANCE", "IRKD_CODE_ITEM", "CNTT_STAT_CODE")

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

nb<-naiveBayes(as.factor(SIU_CUST_YN)~.,data=train)
nb

pred<-predict(nb,test,type = "raw")
write.csv(pred,"result_raw.csv")

pred<-predict(nb,test)
write.csv(pred,"result.csv")

conf.mat<-table(pred,test$SIU_CUST_YN)
conf.mat

#confusionMatrix(pred, test$SIU_CUST_YN)

(accuravy<-sum(diag(conf.mat))/sum(conf.mat)*100)
