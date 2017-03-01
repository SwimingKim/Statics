library(party)
library(e1071)
library(nnet)
library(caret)

setwd("C:/Users/SuYoung/Desktop/새 폴더/CLAIM")

#claim데이터
data <- read.csv("BGCON_CLAIM_DATA.csv", sep=",")
str(data)

column<- c("CUST_ID","POLY_NO",	"ACCI_OCCP_GRP1",	"ACCI_OCCP_GRP2",
           "CHANG_FP_YN",	"CNTT_RECP_SQNO",	"RECP_DATE",	
           "ORIG_RESN_DATE",	"RESN_DATE"	,"CRNT_PROG_DVSN",	"ACCI_DVSN",	
           "CAUS_CODE",	"CAUS_CODE_DTAL",	"DSAS_NAME",	"DMND_RESN_CODE",
           "DMND_RSCD_SQNO",	"HOSP_OTPA_STDT",	"HOSP_OTPA_ENDT",
           "RESL_CD1",	"RESL_NM1",	"VLID_HOSP_OTDA",	"HOUSE_HOSP_DIST",	
           "HOSP_CODE",	"ACCI_HOSP_ADDR",	"HOSP_SPEC_DVSN",	"CHME_LICE_NO",
           "PAYM_DATE",	"DMND_AMT",	"PAYM_AMT",	"PMMI_DLNG_YN",	"SELF_CHAM",	
           "NON_PAY",	"TAMT_SFCA",	"PATT_CHRG_TOTA",	"DSCT_AMT",	
           "COUNT_TRMT_ITEM",	"DCAF_CMPS_XCPA",	"NON_PAY_RATIO",	"HEED_HOSP_YN",
           "SIU_CUST_YN")
view <- subset(data,select=column)
#view<-view[complete.cases(view),] #NA제거

set.seed(1234)
index <- sample(2, nrow(view), replace=TRUE, prob = c(0.7,0.3))

# train과 test의 구분이 이상하다
# view[index,]로 작성하면 사기데이터가 누락
# view[index==1,]로 작성하면 모든 test데이터가 나오지 않는
train<- view[,]#전체 데이터
test<-view[-index,]

write.csv(train,"tr_claim.csv")
write.csv(test,"te_claim.csv")

nb<-naiveBayes(as.factor(SIU_CUST_YN)~.,data=train,laplace = 10)
nb

pred<-predict(nb,test,type = "raw")
write.csv(pred,"result_raw.csv")

pred<-predict(nb,test)
write.csv(pred,"result.csv")

CrossTable(pred, test$SIU_CUST_YN, prop.chisq = FALSE, prop.t = FALSE, dnn = c('predicted', 'actual'))
conf.mat<-table(pred,test$SIU_CUST_YN)
conf.mat

#confusionMatrix(pred, test$SIU_CUST_YN)

(accuravy<-sum(diag(conf.mat))/sum(conf.mat)*100)

# pvalue 수준 높아지는 게 중요하지 확률이 안 중요하다
# 설명력이 중요하다!
