# Test docker 
# @Dean
# http://blog.csdn.net/wsscy2004/article/details/25878223

#docker inspect  --format "{{.State.Pid}}" ((docker  ps -a -q) | head -n1)
#docker inspect  --format "{{.State.Pid}}" $((docker  ps -a -q) | head -n1)

nsenter --target $PID --mount --uts --ipc --net --pid

FROM centos:latest
MAINTAINER Dean CSA.zhang@gmail.com

RUN yum -y --downloaddir=http://yum.noah.baidu.com/centos install net-tools vim hostname passwd openssh-server

RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/beta/7/x86_64/epel-release-7-0.2.noarch.rpm
RUN yum -y install puppet


RUN useradd work && echo work | passwd work --stdin
RUN useradd admin
RUN echo "root:admin" | chpasswd 
RUN echo "admin:admin" | chpasswd 
RUN echo "admin   ALL=(ALL)       ALL" >> /etc/sudoers


# Set locale (fix the locale warnings)
#RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || :


# 启动sshd服务并且暴露22端口
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_ecdsa_key
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN mkdir /var/run/sshd  

ENV LANG en_US.UTF-8 
ENV LC_ALL en_US.UTF-8
ENV PATH /usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin

#USER：作为container运行时，启动程序使用的用户身份
USER root
WORKDIR /root

#ONBUILD USER /home
#ONBUILD WORKDIR /home/work

# Copy the files into the container
ADD /tmp /opt

#VOLUME

#ENTRYPOINT：作为container运行时的启动程序
#ENTRYPOINT echo "Welcome!" 

# Start xdm and ssh services.
#CMD ["/bin/bash", "service sshd start"]

#EXPOSE：作为container运行时需要监听的端口号
#EXPOSE 22
