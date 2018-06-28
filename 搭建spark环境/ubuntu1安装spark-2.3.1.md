#ubuntu16.04安装spark-2.3.1

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

注意：使用`source /etc/profile` 命令使其生效  

###3、设置hasoop配置文件  

####（1）新建以下目录  

```
cd /usr/spark
sudo mkdir hadoop
fenglulu@fenglulu-Aspire-E5-572G:/usr/spark$ sudo mkdir hadoop/hdfs
fenglulu@fenglulu-Aspire-E5-572G:/usr/spark$ sudo mkdir hadoop/hdfs/data
fenglulu@fenglulu-Aspire-E5-572G:/usr/spark$ sudo mkdir hadoop/hdfs/name
fenglulu@fenglulu-Aspire-E5-572G:/usr/spark$ sudo mkdir hadoop/temp
```
####(2)修改`/usr/spark/hadoop-2.7.6/etc/hadoop/`文件夹下的多个配置文件  

a.修改core-site.xml  

```
<configuration>
 <property>
    <name>fs.default.name</name>
    <value>hdfs://master:9000</value>
    <description>HDFS的URI，文件系统://namenode标识:端口号</description>
</property>
<property>
    <name>hadoop.tmp.dir</name>
    <value>file:/usr/spark/hadoop/temp</value>
    <description>namenode上本地的hadoop临时文件夹</description>
</property>
</configuration>
```
b.修改hdfs-site.xml  

```
<configuration>
<property>
    <name>dfs.name.dir</name>
    <value>file:/usr/spark/hadoop/hdfs/name</value>
    <description>namenode上存储hdfs名字空间元数据 </description> 
</property>
<property>
    <name>dfs.data.dir</name>
    <value>file:/usr/spark/hadoop/hdfs/data</value>
    <description>datanode上数据块的物理存储位置</description>
</property>
<property>
    <name>dfs.replication</name>
    <value>1</value>
    <description>副本个数，配置默认是3,应小于datanode机器数量</description>
</property>
<property>
        <name>dfs.namenode.secondary.http-address</name>  
        <value>master:9001</value> 
</property>
</configuration>
```
c.修改mapred-site.xml  

```   
<property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
</property>
<property>  
       <name>mapreduce.jobhistory.address</name>  
        <value>master:10020</value>  
</property>  
<property>  
       <name>mapreduce.jobhistory.webapp.address</name>  
        <value>master:19888</value>  
</property> 
```
d.修改yarn-site.xml  

```
<configuration>

<!-- Site specific YARN configuration properties -->
    <property>  
       <name>yarn.nodemanager.aux-services</name>  
       <value>mapreduce_shuffle</value>  
    </property>  
    <property>                                                                 
       <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>  
       <value>org.apache.hadoop.mapred.ShuffleHandler</value>  
    </property>  
    <property>  
       <name>yarn.resourcemanager.address</name>  
        <value>master:8032</value>  
    </property>  
    <property>  
        <name>yarn.resourcemanager.scheduler.address</name>  
        <value>master:8030</value>  
    </property>  
    <property>  
       <name>yarn.resourcemanager.resource-tracker.address</name>  
        <value>master:8031</value>  
    </property>  
    <property>  
       <name>yarn.resourcemanager.admin.address</name>  
        <value>master:8033</value>  
    </property>  
    <property>  
       <name>yarn.resourcemanager.webapp.address</name>  
        <value>master:8088</value>  
    </property>  
</configuration>
```
e.接着将hadoop-env.sh,mapred-env.sh,yarn-env.sh中的JAVA_HOME都修改为我们配置好的java路径（根据个人jdk设置而定）  

比如，我的是`JAVA_HOME=/home/fenglulu/java/jdk1.8.0_171`  

<1>查看hadoop-env.sh  

```
#The java implementation to use.
export JAVA_HOME=${JAVA_HOME}
```
JAVA_HOME已导入

<2>查看yarn-env-sh  

```
# some Java parameters
# export JAVA_HOME=/home/y/libexec/jdk1.6.0/

if [ "$JAVA_HOME" != "" ]; then
  #echo "run java in $JAVA_HOME"
  JAVA_HOME=$JAVA_HOME
fi
```
能够自动导入JAVA_HOME  

<3>查看mapred-env.sh  

添加JAVA_HOME
```
# export JAVA_HOME=/home/y/libexec/jdk1.6.0/
export JAVA_HOME=${JAVA_HOME}
export HADOOP_JOB_HISTORYSERVER_HEAPSIZE=1000
```
####4、  
《未完待续》
