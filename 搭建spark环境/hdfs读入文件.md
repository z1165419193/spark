##hfs文件系统读入本地txt文件
###首先启动hadoop的hdfs文件系统  

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
   
