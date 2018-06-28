#<center>ubuntu16.04安装spark-2.3.1
###1.下载spark-2.3.1.tgz，[前往下载](http://spark.apache.org/downloads.html)
![](http://chuantu.biz/t6/335/1530154971x-1566688742.png)
选择spark-2.3.1-bin-hadoop2.7,该版本spark需要Scala2.11，和hadoop2.7+，所以我们还需要去[下载Scala2.11.12](https://scala-lang.org/download/2.11.12.html)和[hadoop2.7.6](http://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/hadoop-2.7.6/)
![](http://chuantu.biz/t6/335/1530155477x-1566688676.bmp)  
![](http://chuantu.biz/t6/335/1530155724x-1566688676.bmp)
###2.将三个文件分别解压到/usr/spark文件夹下,先创建/usr/spark
	mkdir /usr/spark
	tar -zxvf scala-2.11.12.tgz -C /usr/spark/
    tar -zxvf spark-2.3.1-bin-hadoop2.7.tgz -C /usr/spark/
    tar -zxvf hadoop-2.7.6.tar.gz -C /usr/spark/
设置环境变量gedit /etc/profile
```
sudo gedit /etc/profile
//在文件末尾追加如下代码，默认当前设备已设置了jdk1.8+；
#java environment
export JAVA_HOME=/home/fenglulu/java/jdk1.8.0_171 
export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH

#maven environment
export M2_HOME=/home/fenglulu/java/apache-maven-3.5.3
PATH=$M2_HOME/bin:$PATH

#scala env
export SCALA_HOME=/usr/spark/scala-2.11.12  
export PATH=$PATH:$SCALA_HOME/bin

#spark env
export SPARK_HOME=/usr/spark/spark-2.3.1-bin-hadoop2.7  
export PATH=$PATH:$SPARK_HOME/bin

#hadoop env
export HADOOP_HOME=/usr/spark/hadoop-2.7.6
export PATH=$PATH:HADOOP_HOME/bin
```
