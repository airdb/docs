ulimit -c unlimited


ulimint -a 用来显示当前的各种用户进程限制
Linux对于每个用户，系统限制其最大进程数，为提高性能，可以根据设备资源情况，
设置个Linux用户的最大进程数，一些需要设置为无限制：
数据段长度：ulimit -d unlimited
最大内存大小：ulimit -m unlimited
堆栈大小：ulimit -s unlimited

我们在用这个命令的时候主要是为了产生core文件，就是程序运行发行段错误时的文件：

ulimit -c unlimited   

生成core文件,

#######################################################
以下来自；http://hi.baidu.com/jrckkyy/blog/item/2562320a5bdbc534b1351d95.html

查看限制情况 ulimit -a

可以看到如下信息

core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
file size               (blocks, -f) unlimited
pending signals                 (-i) 1024
max locked memory       (kbytes, -l) 32
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
stack size              (kbytes, -s) 10240
cpu time               (seconds, -t) unlimited
max user processes              (-u) 4096
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited

而我们需要修改的是open files (-n) 1024的值

于是命令就是limit -n 2048(随各自需要设置)

-----------------------------------------------------------------------------------

 

功能说明：控制shell程序的资源。

语　　法：ulimit [-aHS][-c <core文件上限>][-d <数据节区大小>][-f <文件大小>][-m <内存大小>][-n <文件数目>][-p <缓冲区大小>][-s <堆叠大小>][-t <CPU时间>][-u <程序数目>][-v <虚拟内存大小>]

补充说明：ulimit为shell内建指令，可用来控制shell执行程序的资源。

参　　数：
   -a 　显示目前资源限制的设定。 
   -c <core文件上限> 　设定core文件的最大值，单位为区块。 
   -d <数据节区大小> 　程序数据节区的最大值，单位为KB。 
   -f <文件大小> 　shell所能建立的最大文件，单位为区块。 
   -H 　设定资源的硬性限制，也就是管理员所设下的限制。 
   -m <内存大小> 　指定可使用内存的上限，单位为KB。 
   -n <文件数目> 　指定同一时间最多可开启的文件数。 
   -p <缓冲区大小> 　指定管道缓冲区的大小，单位512字节。 
   -s <堆叠大小> 　指定堆叠的上限，单位为KB。 
   -S 　设定资源的弹性限制。 
   -t <CPU时间> 　指定CPU使用时间的上限，单位为秒。 
   -u <程序数目> 　用户最多可开启的程序数目。 
   -v <虚拟内存大小> 　指定可使用的虚拟内存上限，单位为KB。

------------------

 

1,说明:
ulimit用于shell启动进程所占用的资源.

2,类别:
shell内建命令

3,语法格式:
ulimit [-acdfHlmnpsStvw] [size]

4,参数介绍:

QUOTE:
-H 设置硬件资源限制.
-S 设置软件资源限制.
-a 显示当前所有的资源限制.
-c size:设置core文件的最大值.单位:blocks
-d size:设置数据段的最大值.单位:kbytes
-f size:设置创建文件的最大值.单位:blocks
-l size:设置在内存中锁定进程的最大值.单位:kbytes
-m size:设置可以使用的常驻内存的最大值.单位:kbytes
-n size:设置内核可以同时打开的文件描述符的最大值.单位:n
-p size:设置管道缓冲区的最大值.单位:kbytes
-s size:设置堆栈的最大值.单位:kbytes
-t size:设置CPU使用时间的最大上限.单位:seconds
-v size:设置虚拟内存的最大值.单位:kbytes

5,简单实例:

1]在RH8的环境文件/etc/profile中,我们可以看到系统是如何配置ulimit的:

CODE:
#grep ulimit /etc/profile
ulimit -S -c 0 > /dev/null 2>&1

这条语句设置了对软件资源和对core文件大小的设置

2]如果我们想要对由shell创建的文件大小作些限制,如:

CODE:
#ll h
-rw-r--r-- 1 lee lee 150062 7月 22 02:39 h
#ulimit -f 100 #设置创建文件的最大块(一块=512字节)
#cat h>newh
File size limit exceeded
#ll newh
-rw-r--r-- 1 lee lee 51200 11月 8 11:47 newh

文件h的大小是150062字节,而我们设定的创建文件的大小是512字节x100块=51200字节
当然系统就会根据你的设置生成了51200字节的newh文件.

3]可以像实例1]一样,把你要设置的ulimit放在/etc/profile这个环境文件中.

 

------------------------------------------------------------------------------------------------------------------

当系统中的一些程序在遇到一些错误以及crash时，系统会自动产生core文件记录crash时刻系统信息，包括内存和寄存器信息，用以程序员日 后debug时可以使用。这些错误包括段错误、非法指令、总线错误或用户自己生成的退出信息等等，一般地，core文件在当前文件夹中存放。

core文件有时可能在你发生错误时，并没有出现在你当前的文件夹中，发生这种情况的原因有两个：一个是当前终端被设置为不能弹出core文件；另一种则是core文件被指定了路径。

对于前者，我们可以使用ulimit命令对core文件的大小进行设定。一般默认情况下，core文件的大小被设置为0，这样系统就不dump出core文件了。这时，使用命令：ulimit -c unlimited进行设置，就可以把core文件的大小设置为无限大，同时也可以使用数字来替代unlimited，对core文件的上限制做更精确的设定。

除了可以设置core文件的大小之外，还可以对core文件的名称进行一些规定。这种设置是对/proc/sys/kernel/core_pattern和/proc/sys/kernel/core_uses_pid这两个文件进行修改。改动这两个文件的方法如下：

echo <pattern> > /proc/sys/kernel/core_pattern

echo <"0"/"1"> /proc/sys/kernel/core_uses_pid

并且注意，只有超级用户才可以修改这两个表。

core_pattern接受的是core文件名称的pattern，它包含任何字符串，并且用%作为转移符号生成一些标示符，为core文件名称加入特殊含义。已定义的标示符有如下这些：

%%：相当于%

%p：相当于<pid>

%u：相当于<uid>

%g：相当于<gid>

%s：相当于导致dump的信号的数字

%t：相当于dump的时间

%e：相当于执行文件的名称

%h：相当于hostname

除以上这些标志位外，还规定：

1、末尾的单个%可以直接去除；

2、%加上除上述以外的任何字符，%和该字符都会被去除；

3、所有其他字符都作为一般字符加入名称中；

4、core文件的名称最大值为64个字节（包括'\0'）；

5、core_pattern中默认的pattern为core；

6、为了保持兼容性，通过设置core_uses_pid，可以在core文件的末尾加上%p；

7、pattern中可以包含路径信息。

------------------------------------------------------------------------------------------------------------------

下面的资料是从互联网上整理的来的，参考文献如下：

http://blog.csdn.net/hanchaoman/archive/2009/08/03/4405655.aspx

http://www.mysys-admin.org/category/general/

 

 

1. 可以用ulimit -a 查看一下栈的大小。
在内核2.6.20下， stack size 为8192 kbytes
如果这里没有限制，就栈的大小就只受内存的限制。2G是上限。

2. core 文件
    * 开启或关闭core文件的生成
ulimit -c 可以查看是否打开此选项，若为0则为关闭；
ulimit -c 0可手动关闭
ulimit -c 1000 为设置core文件大小最大为1000k

ulimit -c unlimited 设置core文件大小为不限制大小

 

很多系统在默认的情况下是关闭生成core文件的，这个命令可以加到你的profile中去

3.设置Core Dump的核心转储文件目录和命名规则

 

在默认的情况下，很多系统的core文件是生成在你运行程序的目录下，或者你在程序中chdir后的那个目录，然后在core文件的后面加了一个 pid。在实际工作中，这样可能会造成很多目录下产生core文件，不便于管理，实际上，在2.6下，core文件的生成位置和文件名的命名都是可以配置 的。

 

/proc/sys/kernel/core_uses_pid可以控制产生的core文件的文件名中是否添加pid作为扩展，如果添加则文件内容为1，否则为0
proc/sys/kernel/core_pattern可以设置格式化的core文件保存位置或文件名，比如原来文件内容是core-%e
可以这样修改:
echo "/tmp/core-%e-%p" > core_pattern
将会控制所产生的core文件会存放到/corefile目录下，产生的文件名为core-命令名-pid-时间戳
以下是参数列表:
    %p - insert pid into filename 添加pid
    %u - insert current uid into filename 添加当前uid
    %g - insert current gid into filename 添加当前gid
    %s - insert signal that caused the coredump into the filename 添加导致产生core的信号
    %t - insert UNIX time that the coredump occurred into filename 添加core文件生成时的unix时间
    %h - insert hostname where the coredump happened into filename 添加主机名
    %e - insert coredumping executable name into filename 添加命令名

当然，你可以用下列方式来完成
sysctl -w kernel.core_pattern=/tmp/core-%e-%p

 

这些操作一旦计算机重启，则会丢失，如果你想持久化这些操作，可以在 /etc/sysctl.conf文件中增加：
kernel.core_pattern=/tmp/core%p

 

加好后，如果你想不重启看看效果的话，则用下面的命令：
sysctl -p /etc/sysctl.conf

------------------------------------------------------------------------------------------------------------------

高手指教：

    解决的问题：
         现有一程序P 长期在服务器上运行，目前经常是每1天死掉一次（段错误）。

    目前解决方法：
         用SecureCRT开一个终端，并在服务其上设置ulimit -c nulimited，然后启动程序P。用ulimite -a 命令查询结果如下：

         core file size       (blocks, -c) unlimited
         data seg size           (kbytes, -d) unlimited
         file size             (blocks, -f) unlimited
         pending signals                 (-i) 1024
         max locked memory    (kbytes, -l) 32
          ............
         表明core文件可以生成。

         并测试利用kill -6 pid能够core文件。

   目前的困难：

         当运行ulimit -c nulimited终端 （并且该终端将程序P启动到后台了 ./P &）关闭，程序P死掉后并没有生成 core文件。
         经试验后发现ulimit 命令与终端有关。

   高手指教：
          如何设置能够生成core 文件，与终端无关
          即，程序启动，关闭终端，当程序死掉（段错误）后能够生成core文件。

在
/etc/security/limits.conf （中设置 redhat衍生系linux）
或
/etc/profile中的：
# No core files by default
ulimit -S -c 0 > /dev/null 2>&1

注释掉上面一行。

还有其他UNIX类操作系统也有自己的配置文件可以设置。

------------------------------------------------------------------------------------------------------------------

gdb core 多线程
在linux环境下调试多线程，总觉得不像.NET那么方便。这几天就为找一个死锁的bug折腾好久，介绍一下用过的方法吧。

多线程如果dump，多为段错误，一般都涉及内存非法读写。可以这样处理，使用下面的命令打开系统开关，让其可以在死掉的时候生成core文件。   
ulimit -c unlimited
这样的话死掉的时候就可以在当前目录看到core.pid(pid为进程号)的文件。接着使用gdb:
gdb ./bin ./core.pid 
进去后，使用bt查看死掉时栈的情况，在使用frame命令。

还有就是里面某个线程停住，也没死，这种情况一般就是死锁或者涉及消息接受的超时问题(听人说的，没有遇到过)。遇到这种情况，可以使用：
gcore pid （调试进程的pid号）
手动生成core文件，在使用pstack(linux下好像不好使)查看堆栈的情况。如果都看不出来，就仔细查看代码，看看是不是在 if，return，break，continue这种语句操作是忘记解锁，还有嵌套锁的问题，都需要分析清楚了。

最后，说一句，静心看代码，捶胸顿足是没有用的。

-------------------------------------

1,说明:
ulimit用于shell启动进程所占用的资源.
2,类别:
shell内建命令
3,语法格式:
ulimit [-acdfHlmnpsStvw] [size]
4,参数介绍:
-H 设置硬件资源限制.
-S 设置软件资源限制.
-a 显示当前所有的资源限制.
-c size:设置core文件的最大值.单位:blocks
-d size:设置数据段的最大值.单位:kbytes
-f size:设置创建文件的最大值.单位:blocks
-l size:设置在内存中锁定进程的最大值.单位:kbytes
-m size:设置可以使用的常驻内存的最大值.单位:kbytes
-n size:设置内核可以同时打开的文件描述符的最大值.单位:n
-p size:设置管道缓冲区的最大值.单位:kbytes
-s size:设置堆栈的最大值.单位:kbytes
-t size:设置CPU使用时间的最大上限.单位:seconds
-v size:设置虚拟内存的最大值.单位:kbytes 5,简单实例: 
5.举例
在Linux下写程序的时候，如果程序比较大，经常会遇到“段错误”（segmentation fault）这样的问题，这主要就是由于Linux系统初始的堆栈大小（stack size）太小的缘故，一般为10M。我一般把stack size设置成256M，这样就没有段错误了！命令为：
ulimit   -s 262140 
如果要系统自动记住这个配置，就编辑/etc/profile文件，在 “ulimit -S -c 0 > /dev/null 2>&1”行下，添加“ulimit   -s 262140”，保存重启系统就可以了！ 
1]在RH8的环境文件/etc/profile中,我们可以看到系统是如何配置ulimit的:
#grep ulimit /etc/profile
ulimit -S -c 0 > /dev/null 2>&1
这条语句设置了对软件资源和对core文件大小的设置
2]如果我们想要对由shell创建的文件大小作些限制,如:
#ll h
-rw-r--r-- 1 lee lee 150062 7月 22 02:39 h
#ulimit -f 100 #设置创建文件的最大块(一块=512字节)
#cat h>newh
File size limit exceeded
#ll newh
-rw-r--r-- 1 lee lee 51200 11月 8 11:47 newh
文件h的大小是150062字节,而我们设定的创建文件的大小是512字节x100块=51200字节
当然系统就会根据你的设置生成了51200字节的newh文件.
3]可以像实例1]一样,把你要设置的ulimit放在/etc/profile这个环境文件中.
用途 
设置或报告用户资源极限。
语法 
ulimit [ -H ] [ -S ] [ -a ] [ -c ] [ -d ] [ -f ] [ -m ] [ -n ] [ -s ] [ -t ] [ Limit ]
描述 
ulimit 命令设置或报告用户进程资源极限，如 /etc/security/limits 文件所定义。文件包含以下缺省值极限： 
fsize = 2097151
core = 2097151
cpu = -1
data = 262144
rss = 65536
stack = 65536
nofiles = 2000 
当新用户添加到系统中时，这些值被作为缺省值使用。当向系统中添加用户时，以上值通过 mkuser 命令设置，或通过 chuser 命令更改。 
极限分为软性或硬性。通过 ulimit 命令，用户可将软极限更改到硬极限的最大设置值。要更改资源硬极限，必须拥有 root 用户权限。 
很多系统不包括以上一种或数种极限。 特定资源的极限在指定 Limit 参数时设定。Limit 参数的值可以是每个资源中指定单元中的数字，或者为值 unlimited。要将特定的 ulimit 设置为 unlimited，可使用词 unlimited。 
    注：在 /etc/security/limits 文件中设置缺省极限就是设置了系统宽度极限， 而不仅仅是创建用户时用户所需的极限。 
省略 Limit 参数时，将会打印出当前资源极限。除非用户指定 -H 标志，否则打印出软极限。当用户指定一个以上资源时，极限名称和单元在值之前打印。如果未给予选项，则假定带有了 -f 标志。 
由于 ulimit 命令影响当前 shell 环境，所以它将作为 shell 常规内置命令提供。如果在独立的命令执行环境中调用该命令，则不影响调用者环境的文件大小极限。以下示例中正是这种情况： 
nohup ulimit -f 10000
env ulimit 10000 
一旦通过进程减少了硬极限，若无 root 特权则无法增加，即使返回到原值也不可能。 
关于用户和系统资源极限的更多信息，请参见 AIX 5L Version 5.3 Technical Reference: Base Operating System and Extensions Volume 1 中的 getrlimit、setrlimit 或 vlimit 子例程。
标志
-a     列出所有当前资源极限。
-c     以 512 字节块为单位，指定核心转储的大小。
-d     以 K 字节为单位指定数据区域的大小。
-f     使用 Limit 参数时设定文件大小极限（以块计），或者在未指定参数时报告文件大小极限。缺省值为 -f 标志。
-H     指定设置某个给定资源的硬极限。如果用户拥有 root 用户权限，可以增大硬极限。任何用户均可减少硬极限。
-m     以 K 字节为单位指定物理存储器的大小。
-n     指定一个进程可以拥有的文件描述符的数量的极限。
-s     以 K 字节为单位指定堆栈的大小。
-S     指定为给定的资源设置软极限。软极限可增大到硬极限的值。如果 -H 和 -S 标志均未指定，极限适用于以上二者。
-t     指定每个进程所使用的秒数。
退出状态 
返回以下退出值：
0     成功完成。
>0     拒绝对更高的极限的请求，或发生错误。
示例 
要将文件大小极限设置为 51,200 字节，输入： 
ulimit -f 100
