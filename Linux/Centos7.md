http://isoredirect.centos.org/centos/7/isos/x86_64/Centos 7
===

yum -y install vim  bash-completion git svn httpd gcc gcc-c++ strace net-tools curl wget psmisc lftp tmux lrzsz lighttpd nginx nc docker-io libcgroup kernel-doc libcgroup-tools telnet dos2unix  ruby puppet bind-utils tree man-pages


yum -y install cobbler cobbler-web dhcp
yum install -y http://yum.theforeman.org/releases/latest/el6/x86_64/foreman-release-1.5.2-1.el6.noarch.rpm



centos Srpm
http://vault.centos.org/6.4/os/Source/SPackages/

http://isoredirect.centos.org/centos/7/isos/x86_64/

时区问题：
cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

bond vlan配置
https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Networking_Guide/index.html

PyMySQL
(python3 django1.6)
关于Django1.6中DATABASES的设置也是一样不用做任何修改，跟以前MySQLdb的时候一样，如下所示：

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #数据库引擎
        'NAME': 'test',                       #数据库名
        'USER': 'root',                       #用户名
        'PASSWORD': 'root',                   #密码
        'HOST': '',                           #数据库主机，默认为localhost
        'PORT': '',                           #数据库端口，MySQL默认为3306
        'OPTIONS': {
            'autocommit': True,
        },
    }
}

最关键的一点，在站点的__init__.py文件中，我们添加如下代码：

1 import pymysql
2 pymysql.install_as_MySQLdb()

pip list
argparse (1.2.1)
backports.ssl-match-hostname (3.4.0.2)
chardet (2.0.1)
Cheetah (2.4.4)
cobbler (2.6.5)
configobj (4.7.2)
decorator (3.4.0)
Django (1.6.5)
ecdsa (0.11)
Fabric (1.9.1)
gyp (0.1)
iniparse (0.4)
javapackages (1.0.0)
kitchen (1.1.1)
lxml (3.2.1)
Markdown (2.4.1)
mysql-connector-python (1.1.6)
MySQL-python (1.2.3)
mysql-utilities (1.3.6)
netaddr (0.7.5)
paramiko (1.14.0)
pcp (0.3)
Pillow (2.0.0)
pycrypto (2.6.1)
pycurl (7.19.0)
Pygments (1.4)
pygobject (3.8.2)
pygpgme (0.3)
pyliblzma (0.5.3)
pyudev (0.15)
pyxattr (0.5.1)
PyYAML (3.10)
simplejson (3.3.3)
slip (0.4.0)
slip.dbus (0.4.0)
South (1.0)
stevedore (0.15)
thrift (1.0.0-dev)
urlgrabber (3.10)
virtualenv (1.10.1)
virtualenv-clone (0.2.5)
virtualenvwrapper (4.3.1)
wsgiref (0.1.2)
yum-metadata-parser (1.1.4)



http  markdown
    RewriteEngine on
    #RewriteRule  ^(.*)$ http://www.baidu.com
    RewriteRule  ^(.*)md$ /docdemo/markdown/controller.php
    
    

[root@tc-oped-zhanglei19.tc.baidu.com ~]# time tar -c --xz   -f /tmp/thrift.tar.xz thrift

real	1m47.152s
user	1m47.297s
sys	0m1.408s

[root@tc-oped-zhanglei19.tc.baidu.com tmp]# time tar -x --xz   -f /tmp/thrift.tar.xz

real	0m3.528s
user	0m3.478s
sys	0m0.894s
[root@tc-oped-zhanglei19.tc.baidu.com ~]# time tar -c --xz   -f /tmp/thrift.tar.xz thrift

real	1m46.623s
user	1m46.765s
sys	0m1.395s
[root@tc-oped-zhanglei19.tc.baidu.com ~]# ll /tmp/thrift.tar.*
-rw-r--r--. 1 root root 31267934 Aug 23 00:04 /tmp/thrift.tar.lzma
-rw-r--r--. 1 root root 31244680 Aug 23 00:07 /tmp/thrift.tar.xz

默认enp11sf1有个dhcp的进程
[root@tc-oped-zhanglei19 ~]# ps aux | grep dhc
root     17881  0.0  0.0 102312 15612 ?        S    02:52   0:00 /sbin/dhclient -d -sf /usr/libexec/nm-dhcp-helper -pf /var/run/dhclient-enp11s0f1.pid -lf /var/lib/NetworkManager/dhclient-a373eaf0-5fbb-4354-98ba-97fde62d19fe-enp11s0f1.lease -cf /var/lib/NetworkManager/dhclient-enp11s0f1.conf enp11s0f1
enp11s0f1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.26.201.253  netmask 255.255.255.0  broadcast 10.26.201.255


dhcp给分了个253的地址
kill，配置文件BOOTPROTO=dhcp改为=static


https://sourceware.org/binutils/docs-2.18/ld/index.html

indent -kr -i4 -ts8 -sob -l80  -ss -bs -bbb -bl -bli0 -nce -psl my_module.c

epel.repo
rpm -ivh http://dl.fedoraproject.org/pub/epel/beta/7/x86_64/epel-release-7-0.2.noarch.rpm

How to Enable EPEL Repository for RHEL/CentOS 
http://www.tecmint.com/how-to-enable-epel-repository-for-rhel-centos-6-5/


http://blog.csdn.net/fisher_jiang/article/details/6783922


https://github.com/docker/docker
https://github.com/dongweiming/docker-desktop


dockerFile:
FROM centos:latest
RUN yum -y install net-tools vim hostname passwd openssh-server
RUN useradd work && echo work | passwd work --stdin
MAINTAINER CSA.zhang@gmail.com
#USER：作为container运行时，启动程序使用的用户身份
USER work
#ENTRYPOINT：作为container运行时的启动程序
ENTRYPOINT echo "Welcome!" && /bin/bash
#EXPOSE：作为container运行时需要监听的端口号
#EXPOSE 22
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"] 

ip  route add   10.0.0.0/8 via 10.26.201.1 dev enp11s0f1



docker run -i --privileged -t --name="dean" -d -p 8000:8000 centos7:latest  /bin/bash -c "python -m SimpleHTTPServer 8000"
docker run -i --privileged -t centos:latest  /bin/bash

docker run -i -v /opt/volume1 -v /opt/volume2 --name Volume_Container centos7:latest /bin/bash

docker run -i --privileged -t --name="1.dean" -d --memory="50m" --hostname="1.dean" -v /opt  -p 8000:8000 centos7:latest  /bin/bash -c "python -m SimpleHTTPServer 8000"

docker run -i --privileged -t --name="1.dean" -d --memory="50m" --hostname="1.dean" -v /host:/home/tmp -p 8000:8000 centos7:latest  /bin/bash

docker run -i --privileged -t --name="1.dean" -d --memory="50m" --hostname="1.dean" -v /host:/container/mount:rw -p 8000:8000 centos:latest  /bin/bash
docker run -i --privileged -t --name="1.dean" -d --memory="50m" --hostname="1.dean" -v /host:/container/mount:rw -p 8000:8000 centos:latest  /bin/bash -c "python -m SimpleHTTPServer 8000"

docker run -i --privileged -t --name="1.dean"  --memory="50m" --hostname="1-dean" -v /host:/root/tmp --env=[HOSTNAME=1.DEAN] --workdir="/home/tmp" -p 8000:8000 centos7:latest  /bin/bash


docker run -t -i --rm=true --privileged  --name="1.dean"  --memory="50m" --hostname="1-dean" -v /host:/root/tmp --env=[HOSTNAME=1.DEAN] --workdir="/home/tmp" -p 8000:8000 centos7:latest  /bin/bash

http://0pointer.de/blog/projects/systemd.html

http://blog.csdn.net/junjun16818/article/details/30623033

http://www.sjsjw.com/kf_system/article/163_30151_2868.asp
http://www.infoq.com/cn/news/2013/04/Docker
http://soft.chinabyte.com/database/270/12802270.shtml


http://docker.widuu.com/

运行交互性的shell（就像运行一个单独的linux）
# 使用ubuntu运行一个交互性的shell,
# 分配一个伪终端，附带stdin和stdout(输入/输出流)
# 如果你想退出分离出来的伪终端,
# 可以使用CTRL -p+CTRL -q --就像先按CTRL -p 然后CTRL -q
sudo docker run -i -t ubuntu /bin/bash



Cpuset：用于指定tasks使用的cpu及memory nodes，等价于sched_setaffinity，set_mempolicy的效果；
Ns：命名空间服务；
Cpu:用于设置tasks对cpu的利用率；
Cpuacct：用于记录cpu的统计信息；
Memory：用于设置tasks对内存的使用量；
Devices：用于设置tasks对devices的使用（whitelist，read，write,mknod）；
Freezer：用于挂起或恢复tasks；
Net_cls：使用等级识别符(classid)标记网络数据包，允许linux流量控制(tc)识别从具体cgroup中生成的数据包；
Blkio：控制并监控tasks对块设备的I/O访问；

创建一个cgroup: mkdir
删除一个cgroup: rmdir

给cgroup加入一个task
echo pid >> tasks

http://blog.csdn.net/wudongxu/article/details/8474456
 linux调度器（二）——CFS模型
http://blog.csdn.net/wudongxu/article/details/8574723

Linux Cgroups详解(一)
http://www.cnblogs.com/lisperl/archive/2012/04/17/2453838.html
Linux Cgroups详解(二)
http://www.cnblogs.com/lisperl/archive/2012/04/18/2455027.html
Linux Cgroups详解(三)
http://www.cnblogs.com/lisperl/archive/2012/04/23/2466151.html
Linux Cgroups详解(四)
http://www.cnblogs.com/lisperl/archive/2012/04/23/2466721.html
Linux Cgroups详解(五)
http://www.cnblogs.com/lisperl/archive/2012/04/24/2468170.html
Linux Cgroups详解(六)
http://www.cnblogs.com/lisperl/archive/2012/04/25/2469587.html
Linux Cgroups详解(七)
http://www.cnblogs.com/lisperl/archive/2012/04/26/2471776.html
Linux Cgroups详解(八)
http://www.cnblogs.com/lisperl/archive/2012/04/28/2474872.html
Linux Cgroups详解(九)
http://www.cnblogs.com/lisperl/archive/2012/05/02/2478817.html


Linux Namespaces机制
http://www.cnblogs.com/lisperl/archive/2012/05/03/2480316.html
nux Namespaces机制——实现
http://www.cnblogs.com/lisperl/archive/2012/05/03/2480573.html




linux gb2312 转 UTF-8
iconv -f "gbk" -t "utf-8" < infile > outfile
piconv -f "gbk" -t "utf-8" < infile > outfile

#! /bin/bash
ICONV=iconv

if ! which $ICONV &> /dev/null
   then
      ICONV=piconv
fi
 
for i in $(ls *.c)
  do
     $ICONV -f "gbk" -t "utf-8" < "$i" > "$i.utf8"
     ret=$?
     if [ $ret -eq 0 ] ; then
        mv -f "$i" "$i.backup"
        mv -f "$i.utf8" "$i"
       else
         echo "fail to convert $i from gbk to utf-8"
       fi
   done
  exit $ret

#end 
