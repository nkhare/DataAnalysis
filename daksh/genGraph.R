args<-commandArgs(trailingOnly = TRUE)

print(args)
filename = args[1]
imagename = args[2]
print(filename)

df = read.csv(filename)
par(mar=c(20, 4.1, 4.1, 2.1))
png(imagename)
barplot(df$score[1:6], names.arg=df$issue[1:6],lwd=1,density=c(10,15,20,25,30), las = 2)

dev.off()





