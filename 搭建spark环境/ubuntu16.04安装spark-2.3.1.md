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

###3、设置hadoop配置文件  

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

####4、配置hadoop节点信息  
修改/usr/spark/hadoop-2.7.6/etc/hadoop/下的slaves文件，添加节点，本次预计使用三个slave节点,内容如下：  
```
localhost
slave1
slave2
slave3
```  
修改主机hosts文件，内容如下：  

![](http://chuantu.biz/t6/336/1530256065x-1404729680.bmp)  
修改主机名称gedit /etc/hostname  

```
gedit /etc/hostname
```  
5、配置ssh无密码登录

(1)ubuntu自带ssh-client，我们还需要ssh-server

apt-get install openssh-server

(2)启动ssh服务

/etc/init.d/ssh start

(3)查看sshd是否启动

ps -e | grep ssh  

(4)root账户默认不允许登录ssh，修改权限

`gedit /etc/ssh/sshd_config`

找到Authentication，修改PermitRootLogin yes，保存

```
/etc/init.d/ssh restart
```

(5)ssh登录本地

`ssh localhost`

SSH首次登录会有提示，直接输入yes即可，这时是需要密码的

(6)生成秘钥

`ssh-keygen -t rsa`

之后一直按Enter键，默认将秘钥保存在.shh/id_rsa文件中

(7)RSA公钥加入授权文件

`cd .ssh`

`cp id_rsa.pub authorized_keys`

(8)重新登录，实现免密码登录localhost

6、配置master免密码登录slave1

这里使用scp命令，可自行搜索相关信息，配置确保slave1节点已安装ssh-server

(1)将master根目录下密码复制到slave1的根目录下

`root@master:~# scp ~/.ssh/id_rsa.pub root@slave1:~/.ssh`

(2)在slave1节点将RSA公钥加入授权文件

`root@slave:~# cp .ssh/id_rsa.pub authorized_keys`

如有多台计算机，重复以上操作即可

(3)在master节点上ssh登录slave1,实现免密码登录

`ssh slave1`

7、配置slave1节点的hadoop，同master节点，复制过去即可

8、Hadoop运行

(1)格式化分布式文件系统，在master节点下

`cd /usr/local/hadoop/hadoop-2.7.3`

`bin/hadoop namenode -format`

(2)启动hadoop守护进程

`sbin/start-all.sh`

(3)检测启动情况

`jps`

这时在master节点可以看到NameNode，SecondaryNameNode，ResourceManager

在slave1节点可以看到DataNode，NodeManager，因为我也将master节地点添加为slaves，所以也能看到类似信息

(4)停止hadoop进程

`sbin/stop-all.sh  `

9、修改spark配置文件

1)$SPARK_HOME/conf/spark-env.sh

    `cp spark-env.sh.template spark-env.sh`  
    
    添加以下内容:  
    ```
    export SCALA_HOME=/usr/spark/scala-2.11.12
    export JAVA_HOME=/home/fenglulu/java/jdk1.8.0_171
    export SPARK_MASTER_IP=master
    export SPARK_WORKER_MEMORY=512m
    export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
```  

2)$SPARK_HOME/conf/slaves

    `cp slaves.template slaves`  
    
    添加以下内容:
    ```
    master
    slave1
```  

3.以上配置均在master节点进行，接下来将配置好的文件复制到slave节点，确保路径等均一致，不清楚的可以先看配置hadoop的文章

10. 集群启动

启动spark集群  
 
`cd $SPARK_HOME`
`sbin/start-all.sh`  

2.查看

`jps`

3.结果  
master节点  
```
    8608 Worker
    8488 Master
    8670 Jps
```
slave1节点：

```
    6737 Worker
    6774 Jps

4.关闭集群

`sbin/stop-all.sh`  

《未完待续》
