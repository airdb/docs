
# Linux作业调度: at、 crontab、cron、 anacron
------

Sun Mar  9 02:48:26 CST 2014 © [阿正_Dean](http://user.qzone.qq.com/137780017 "Dean Qzone")

tags: `Linux作业调度` `Linux任务调度` `计划任务`  `at` `crontab` `cron` `anacron` 




[Linux技巧: 用cron和at调度作业](http://www.ibm.com/developerworks/cn/linux/l-job-scheduling.html "Title")

[LPI 102 考试准备，主题111:管理任务](http://www.ibm.com/developerworks/cn/education/linux/l-lpic1111/index.html)

[使用Linux文件恢复工具](http://www.ibm.com/developerworks/cn/linux/1312_caoyq_linuxrestore/index.html)

[LPI 102 考试准备，主题111:管理任务](http://www.ibm.com/developerworks/cn/education/linux/l-lpic1111/index.html#accounts)

# 一、 简述
&emsp;&emsp;系统管理员需要在系统负载低的午夜运行作业，或者需要每天或每月运行作业，同时又不愿意牺牲睡眠时间或假期。调度任务的其他原因包括自动执行日常任务或者确保每次都以相同的方式处理任务。本文帮助您使用 cron 和 at 功能调度作业定期运行或在指定的时间运行一次。

&emsp;&emsp;Linux® 和 UNIX® 系统允许调度任务在以后执行一次，或者重复运行。在 Linux 系统上，许多管理任务必须频繁地定期执行。这些任务包括轮转日志文件以避免装满文件系统、备份数据和连接时间服务器来执行系统时间同步。在本文中，学习Linux中提供的调度机制，包括 cron 和 anacron 设施以及 crontab 和 at 命令。即使系统常常关机 anacron 也可以帮助调度作业。 


<table>
  <tr><td>调度方式</td> <td>作用软件层</td><td>调度周期</td><td>作用</td></tr>
  <tr><td>at</td> <td> 系统层、应用层</td><td>分钟级以上</td><td>单次执行，应用于网络或服务器的可预期调整</td></tr>
  <tr><td>crontab</td> <td>系统层、应用层</td><td>分钟级以上</td><td>定时执行，主要应用于备份，清理日志，同步数据</td></tr>
  <tr><td>cron</td> <td>系统层</td><td>小时级以上</td><td>多次执行，应用同步ntp，清理系统级日志，机器健康自检查</td></tr>
  <tr><td>anacron</td> <td>系统层</td><td>天级别以上</td><td>多次执行，应用于PC机，执行频率低的任务。</td></tr>
</table>


# 二、 任务调度命令及使用方式

##1、at 计划任务
&emsp;&emsp;在**指定的时间执行一次任务**，应用于网络或服务器的可预期调整。 与cronttab不同的是只*执行一次*。


+ a、Base 
>- 安装包: at-3.1.10-43.el6_2.1.x86_64 
>- 服务名：atd
>- 命令: at, atq(at queue), atrm(at delete), 
>- 特殊命令：batch(when the load average drops below 0.8, /etc/sysconfig/atd OPTS="-l 0.8 -b 60")
>- 任务路径： /var/spool/at/a0001401629c78, 权限为用户权限


+ b、Permit
>- /etc/at.allow: root允许使用at帐户。
>- /etc/at.deny : root禁止使用at的帐户。

&emsp;&emsp;注： **allow比at.deny优先级高**, 存在/etc/at.allow，则/etc/at.deny不生效。

+ c、Usage 

        $ at -h
        Usage: at [-V] [-q x] [-f file] [-mldbv] time
               at -c job ...
               atq [-V] [-q x]
               atrm [-V] job ...
               batch

    > **参数** :
    >
    >- **-V** : 印出版本编号
    >- **-q** : 使用指定的伫列(Queue)来储存，at的资料是存放在所谓的queue中，使用者可以同时使用多个 ****queue，而queue的编号为 a, b, c... z以及 A, B, ... Z共52个。
    >- **-m** : 即使程序/指令执行完成后没有输出结果, 也要寄封信给使用者
    >- **-f** : file : 读入预先写好的命令档。使用者不一定要使用交谈模式来输入，可以先将所有的指定先写****入档案后再一次读入
    >- **-l** : 列出所有的指定 (使用者也可以直接使用 atq 而不用 at -l)
    >- **-d** : 删除指定 (使用者也可以直接使用 atrm 而不用 at -d)
    >- **-v** : 列出所有已经完成但尚未删除的指定
    >- **-c **:  cats the jobs listed on the command line to standard output.


+ d、**at demo**

    1. 当晚4:51 点执行 at.sh脚本 :

            $ cat at.sh
			#!/bin/bash
			date > /tmp/log
			$ ls -l at.sh 
			-rw-r--r-- 1 root root 28 Mar  9 04:49 at.sh
			$ cat at.sh
			#!/bin/bash
			date > /tmp/log
			$ at -f at.sh 4:51
			job 17 at 2014-03-09 04:51
			$ at -c 17 | tail -n 5
			${SHELL:-/bin/sh} << 'marcinDELIMITER4f7214d9'
			#!/bin/bash
			date > /tmp/log
			
			marcinDELIMITER4f7214d9
			$ at -l
			17	2014-03-09 04:51 a root
			$ cat /tmp/log
			Sun Mar  9 04:51:00 CST 2014
			$ at -l
    2. 三个星期后的下午5点执行 /bin/ls :

            echo "/bin/ls" | at 5pm + 2 weeks
    3. 明天的 17:20 执行 /bin/date :

            echo "/bin/date > /tmp/log" | at 17:20 tomorrow
    4. 1999 年的最后一天的最后一分钟印出 the end of world !

            echo "echo the end of world !" | at 23:59 12/31/1999 


+ e、说明

    - at 可以让使用者指定在 TIME 这个特定时刻执行某个程序或指令，TIME 的格式是 HH:MM其中的 HH 为小时，MM 为分钟，甚至你也可以指定 am, pm, midnight, noon, teatime(就是下午 4 点钟)等口语词。

    - 以一定的时间间隔运行作业需要使用cron设施进行管理，它由crond守护进程和一组表（描述执行哪些操作和采用什么样的频率）组成。这个守护进程每分钟唤醒一次，并通过检查crontab判断需要做什么。用户使用 crontab 命令管理 crontab。crond守护进程常常是在系统启动时由init进程启动的。

    - 如果想要指定超过一天内的时间，则可以用 MMDDYY 或者 MM/DD/YY 的格式，其中 MM 是分钟，DD 是第几日，YY 是指年份。另外，使用者甚至也可以使用像是 now + 时间间隔来弹性指定时间，其中的时间间隔可以是 minutes, hours, days, weeks。
    
    - 另外，使用者也可指定 today 或 tomorrow 来表示今天或明天。当指定了时间并按下 enter 之后，at 会进入交谈模式并要求输入指令或程序，当你输入完后按下 ctrl+D 即可完成所有动作，至于执行的结果将会寄回你的帐号中。

##2、crontab 定时任务
------

&emsp;&emsp;业务运维，经常有备份，清理日志，同步数据等操作，权限一般为work帐户，通常是周期性操作，此时使用crontab会大大减小运维工作量。
&emsp;&emsp;任务调度的crond常驻命令。crond是linux用来定期执行程序的命令。当安装完成操作系统之后，默认不会启动此任务调度命令。_crond命令**每分锺**会定期检查是否有要执行的工作，如果有要执行的工作便会自动执行该工作_。

&emsp;&emsp;linux任务调度的工作主要分为以下两类：

> 1. 系统定时任务：系统周期性所要执行的工作，如同步ntp、清理缓存等, root执行。
> 2. 业务定时任务：某个用户定期要做的工作，如执行日志清理脚本， work用户执行。

+ a、Base                                                                                                                           
>- 安装包: cronie-1.4.4-12.el6.x86_64
>- 服务名：crond
>- 命令：  crontab
>- 任务路径： /var/spool/cron/work, 权限为用户权限
+ b、Permit
&emsp;&emsp;Crontab是UNIX系统下的定时任务触发器，其使用者的权限记载在下列两个文件中
<table align="center">
  <tr><td>文件</td> <td>含义</td></tr>
  <tr><td>/etc/cron.deny</td> <td>该文件中所列的用户不允许使用Crontab命令</td></tr>
  <tr><td>/etc/cron.allow</td> <td>该文件中所列的用户允许使用Crontab命令</td></tr>
  <tr><td> /var/spool/cron/work </td> <td>work用户的crontab文件, cron目录文件权限700</td></tr>
</table>
+ c、Usage 
&emsp;&emsp;Crontab命令用法为：crontab –l|-r|-e|-i [-u user] file，其参数含义如表一： 
<table>
  <tr><td>参数名称</td> <td>含义</td></tr>
  <tr><td>-l</td> <td> 显示用户的Crontab文件的内容 </td></tr>
  <tr><td>-u</td> <td>对指定用户的crontab进行操作</td></tr>
  <tr><td>-e</td> <td>编辑用户的Crontab文件</td></tr>
  <tr><td>file</td> <td>crontab最终目标配置文件</td></tr>
  <tr><td>-r</td> <td>从Crontab目录中删除用户的Crontab文件</td></tr>
  <tr><td>-i</td> <td>删除用户的Crontab文件前给提示</td></tr>
</table>

&emsp;&emsp;注： 

* 用户所建立的Crontab文件存于/var/spool/cron中，其文件名与用户名一致。创建crontab后，*不用重启crond服务，可直接生效*。
* 使用者也可以将所有的设定先存放在档案 file 中，用 crontab file 的方式来设定crontab, **file文件内容是最终的crontab配置文件**。 

+ d、**crontab conf**
模板配置文件： /etc/crontab

`$cat /etc/crontab`

    SHELL=/bin/bash
    PATH=/sbin:/bin:/usr/sbin:/usr/bin
    MAILTO=root
    HOME=/

    # For details see man 4 crontabs

    # Example of job definition:
    # .---------------- minute (0 - 59)
    # |  .------------- hour (0 - 23)
    # |  |  .---------- day of month (1 - 31)
    # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
    # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
    # |  |  |  |  |
    # *  *  *  *  * user-name command to be executed

**分段及含义**：
<table>
  <tr><td>段</td> <td>含义</td></tr>
  <tr><td>第1段（分）</td> <td> minute (0 - 59)</td></tr>
  <tr><td>第2段（时）</td> <td>hour (0 - 23)</td></tr>
  <tr><td>第3段（日）</td> <td>day of month (1 - 31)</td></tr>
  <tr><td>第4段（月）</td> <td>month(1-12) OR jan,feb,mar,apr</td></tr>
  <tr><td>第5段（星期）</td> <td>day of weekday,sun(0|7),mon,tue,wed,thu,fri,sat</td></tr>
  <tr><td>第6段至行末（命令）</td> <td>指定用户或不指定用户的自定义执行命令</td></tr>
</table>

**具体说明**：

    * * * * * work /bin/echo  $(date +%s) > /tmp/log
    

* 其中 f1 是表示分钟，f2 表示小时，f3 表示一个月份中的第几日，f4 表示月份，f5 表示一个星期中的第几天。 work为执行command的用户，*使用root时，需要注意*。 `/bin/echo $(date +%s) > /tmp/log`表示要执行的命令。

* 当 f1 为 * 时表示每分钟都要执行 ，f2 为 * 时表示每小时都要执行程序，其余类推。

* 当 f1 为 a-b 时表示从第 a 分钟到第 b 分钟这段时间内要执行，f2 为 a-b 时表示从第 a 到第 b 小时都要执行，其余类推。

* 当 f1 为 */n 时表示每 n 分钟个时间间隔执行一次，f2 为 */n 表示每 n 小时个时间间隔执行一次，其余类推。

* 当 f1 为 a, b, c,... 时表示第 a, b, c,... 分钟要执行，f2 为 a, b, c,... 时表示第 a, b, c...个小时要执行，其余类推。




+ e、**crontab demo**
# 五、 常用配置示例：

1. 每月每天每小时的第 0 分钟执行一次 /bin/ls :

        0 7 * * * /bin/ls  

2.  在 12 月内, 每天的早上 6 点到 12 点中，每隔 20 分钟执行一次 /usr/bin/backup :

         0 6-12/3 * 12 * /usr/bin/backup  
3. 周一到周五每天下午 5:00 寄一封信给 alex@domain.name : 

         0 17 * * 1-5 mail -s "hi" Dean@baidu.com  /dev/null 2>&1 

4. 意思是每两个小时重启一次apache 

        0 */2 * * * /sbin/service httpd restart
5. 每天7：50开启ssh服务 

        50 7 * * * /sbin/service sshd start
6. 每月1号和15号检查/home 磁盘 

        0 0 1,15 * * fsckHome.sh
7. 每小时的第一分执行, 

        1 * * * * /home/work/opbin/backup.sh
8. 每周一至周五3点钟，在目录/home/work中，查找文件名为*.log.*的文件，并删除4天前的文件。

        00 03 * * 1-5 find /home/work/ "*.log*" -mtime +4 -exec rm {} \;
        00 03 * * 1-5 find /home/work/ "*.log*" -ctime +60 -exec rm {} \;  
9. 意思是每月的1、11、21、31日是的6：30执行一次ls命令

        30 6 */10 * * ls
10. 每隔六个小时的整点开始，每一分钟执行clean.sh脚本（执行60次）

        * */6 * * * /home/work/opbin/clean.sh


![alt text](http://e.hiphotos.baidu.com/zhidao/pic/item/94cad1c8a786c917bb699163c83d70cf3bc75706.jpg "Title")

---------------


3/8/2014 16:51:01    &copy; [阿正_Dean](https://github.com/DeanChina/  "Free Engineer")
