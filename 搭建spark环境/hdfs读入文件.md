##hfs文件系统读入本地txt文件
###1.首先启动hadoop的hdfs文件系统  

```
#进入hadoop安装包下
cd /usr/spark/hadoop-2.7.6
#启动hdfs文件系统
sbin/start-dfs.sh
```  
注意：这个步骤可能会有warn警示，内容如下：  
`18/07/06 16:09:01 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
`

   在博客中查找解决方法得知，解决办法如下：  
   ```
   #在/etc/profile中添加一条命令
   export  HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib:$HADOOP_COMMON_LIB_NATIVE_DIR"
   #接着将HADOOP_HEME/lib/native中的所有文件复制到HADOOP_HOME/lib中
   #接着使用下面的命令使上面的设置生效
   source /etc/profile
   ```  
`hdfs dfs -mkdir /wc`  创建了文件夹wc  
然后使用`hdfs dfs -copyFromLocal /home/fenglulu/java/news/henanshifandaxue.txt /wc/ `上传至hdfs文件系统中
如图所示：
![](http://chuantu.biz/t6/340/1531039229x-1566688742.bmp)  

×注意：在idea中通过url-hdfs://master:9000/wc/henanshifandaxue.txt加载hdfs文件系统中的数据失败×  报错内容如下：
```
ERROR SparkContext: Error initializing SparkContext.
org.apache.spark.SparkException: A master URL must be set in your configuration
	at org.apache.spark.SparkContext.<init>(SparkContext.scala:367)
	at ReadHdfs$.main(ReadHdfs.scala:7)
	at ReadHdfs.main(ReadHdfs.scala)
18/07/08 16:33:14 ERROR Utils: Uncaught exception in thread main
java.lang.NullPointerException
	at org.apache.spark.SparkContext.org$apache$spark$SparkContext$$postApplicationEnd(SparkContext.scala:2389)
	at org.apache.spark.SparkContext$$anonfun$stop$1.apply$mcV$sp(SparkContext.scala:1904)
```  
读取文件后的主题聚类，在周末两天的查阅博客下仍无法清楚明白算法如何实现，，，
   
