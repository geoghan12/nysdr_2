setwd("/Users/sophiegeoghan/Desktop/nysdr")

GynoBK=read.csv("GynoBK.csv",col.names=c("Malpractice","Education","Name","Field"))
GynoMan=read.csv("GynoMan.csv",col.names=c("Malpractice","Education","Name","Field"))

allNYS=read.csv("allNYS.csv",col.names=c("Malpractice","Education","Name","Field"))

kagglePhys=read.csv("Physician_Compare_National_Downloadable_File.csv")
