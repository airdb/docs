Linux下crontab命令的用法 
===

------

3/8/2014 16:51:01    &copy;[阿正_Dean](https://github.com/DeanChina/  "Free Engineer")

tags: `linxu`, `crontab`, `定时任务`



# 一、 作用
&emsp;&emsp;任务调度的crond常驻命令。crond是linux用来定期执行程序的命令。当安装完成操作系统之后，默认不会启动此任务调度命令。_crond命令**每分锺**会定期检查是否有要执行的工作，如果有要执行的工作便会自动执行该工作_。

&emsp;&emsp;linux任务调度的工作主要分为以下两类：

> 1. 系统工作：系统周期性所要执行的工作，如备份系统数据、清理缓存, root执行。
> 2. 个人工作：某个用户定期要做的工作，如执行脚本， work用户执行。


# 二、 权限控制
&emsp;&emsp;Crontab是UNIX系统下的定时任务触发器，其使用者的权限记载在下列两个文件中

<table align="center">
  <tr><td>文件</td> <td>含义</td></tr>
  <tr><td>/etc/cron.deny</td> <td>该文件中所列的用户不允许使用Crontab命令</td></tr>
  <tr><td>/etc/cron.allow</td> <td>该文件中所列的用户允许使用Crontab命令</td></tr>
  <tr><td> /var/spool/cron/work </td> <td>work用户的crontab文件, cron目录文件权限700</td></tr>
</table>


	# ls -ld /var/spool/cron 
	drwx------. 2 root root 4096 Mar  8 17:42 /var/spool/cron
	# 
	# ls -l /var/spool/cron/work
	-rw------- 1 test test 23 Mar  8 17:42 /var/spool/cron/work
	# cat /var/spool/cron/work
	* * * * * work /bin/ls

# 三、 命令
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

# 四、 crontab配置文件
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
