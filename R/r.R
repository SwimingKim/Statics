install.packages(c("ROAuth","twitteR"))
library(ROAuth)
library(twitteR)
download.file(url="http://curl.haxx.se/ca/cacert.pem",destfile = "cacert.pem")
APIkey<-"9ghh5pLqVPm09WL2TIXfckD26"
APIsecret<-"wqsLicQsiUflm0Y4AKxtHl1kDXAj0V6eMGPLzeG97rW8BgdcvY"
RequestTokenURL<-"https://api.twitter.com/oauth/request_token"
AcessTokenURL<-"https://api.twitter.com/oauth/access_token"
AuthroizeURL<-"https://api.twitter.com/oauth/authorize"
twitCred<-OAuthFactory$new(consumerKey=APIkey, consumerSecret=APIsecret, requestURL=RequestTokenURL, accessURL=AcessTokenURL, authURL=AuthroizeURL)
twitCred
twitCred$handshake(cainfo=system.file("CurlSSL","cacert.pem",package = "RCurl"))

setup_twitter_oauth(consumer_key = "9ghh5pLqVPm09WL2TIXfckD26", consumer_secret = "wqsLicQsiUflm0Y4AKxtHl1kDXAj0V6eMGPLzeG97rW8BgdcvY",
 access_token = "984049026-N3BDM8LST4zquONmLpDBXoaxl7jx8zCtp0mVdxHR",access_secret = "omqL7TnKsR2BRvE6W91vzyStBLVgtP0hjdcgtSW5ht3On")



install.packages(c("wordcloud","tm"))
library(tm)
library(wordcloud)
obamaTweets <- searchTwitter("BarackObama",lang="en",n=1000)
obamaTweets <- searchTwitter('BarackObama',lang='en',n=1000)
df<-do.call("rbind",lapply(obamaTweets,as.data.frame))
myCorpus<-Corpus(VectorSource(df$text))
removeComment<-function(x)gsub("[[:alnum:]]*","",x)
myCorpus<-tm_map(myCorpus,removeComment)
removeAt<-function(x)gsub("@[[:alnum:]]*","",x)
myCorpus<-tm_map(myCorpus,removeAt)
myCorpus<-tm_map(myCorpus,tolower)
myCorpus<-tm_map(myCorpus,removePunctuation)
myCorpus<-tm_map(myCorpus,removeNumbers)
removeChar<-function(x)gsub("\u0080[[:alnum:]]*","",x)
myCorpus<-tm_map(myCorpus,removeChar)
myStopwords<-c(stopwords('english'),"president","president","obama","obamas","watch","americans","american","live","make","now","get","take","keep","add","will","name","just","can","one","us","time")
myCorpus<-tm_map(myCorpus,removeWords,myStopwords)
myCorpusCopy<-myCorpus
myCorpus<-tm_map(myCorpus,stemDocument)
myCorpus<-tm_map(myCorpus,stemCompletion, dictionary=myCorpusCopy)
removeURL<-function(x)gsub("http[[:alnum:]]*","",x)
myCorpus<-tm_map(myCorpus,removeURL)


myCorpus <- tm_map(myCorpus, PlainTextDocument)
tdm <- TermDocumentMatrix(myCorpus, control=list(wordLengths=c(2,Inf)))
m<-as.matrix(tdm)
wordFreq<-sort(rowSums(m),decreasing = TRUE)
set.seed(375)
wordcloud(words=names(wordFreq),freq=wordFreq,scale=c(4,.5),min.freq = 10, random.order = F)








