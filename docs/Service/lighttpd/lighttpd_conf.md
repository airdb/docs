lighttpd.conf
===

配置 
       修改/etc/lighttpd/lighttpd.conf 
       1）server.modules 
       取消需要用到模块的注释，mod_rewrite，mod_access，mod_fastcgi，mod_simple_vhost，mod_cgi，       mod_compress，mod_accesslog是一般需要用到的。 
       我们放开                                "mod_rewrite" 
                                              "mod_compress",
       2）server.document-root, server.error-log，accesslog.filename需要指定相应的目录 
          server.document-root         = "/www/phc/html/" 
          mkdir /usr/local/lighttpd/logs 
          chmod 777 /usr/local/lighttpd/logs/ 
           touch /usr/local/lighttpd/logs/error.log 
           chmod 777 /usr/local/lighttpd/logs/error.log
          server.errorlog              = "/usr/local/lighttpd/logs/error.log" 
accesslog.filename              = "|/usr/sbin/cronolog /usr/local/lighttpd/logs/%Y/%m/%d/accesslog.log"
       3）用什么权限来运行lighttpd 
          server.username             = "nobody" 
          server.groupname            = "nobody" 
          从安全角度来说，不建议用root权限运行web server，可以自行指定普通用户权限。
        4）静态文件压缩 
           mkdir /usr/local/lighttpd/compress 
           chmod 777 /usr/local/lighttpd/compress/ 
compress.cache-dir          = "/usr/local/lighttpd/compress/" 
compress.filetype           = ("text/plain", "text/html","text/javascript","text/css")
           可以指定某些静态资源类型使用压缩方式传输，节省带宽， 
           对于大量AJAX应用来说，可以极大提高页面加载速度。
         5）server.port                 = 81
         6）#$HTTP["url"] =~ ".pdf$" { 
     131 #  server.range-requests = "disable" 
     132 #}
     4，优化 
      1 最大连接数
             默认是1024 
             修改 server.max-fds,大流量网站推荐2048.
             因为lighttpd基于线程,而apache(MPM-prefork)基于子进程, 
             所以apache需要设置startservers,maxclients等,这里不需要 
      2 stat() 缓存
                stat() 这样的系统调用,开销也是相当明显的. 
               缓存能够节约时间和环境切换次数(context switches)
               一句话,lighttpd.conf加上 
               server.stat-cache-engine = “fam”
               lighttpd还另外提供simple(缓存1秒内的stat()),disabled选项. 
               相信没人会选disabled吧. 
       3 常连接(HTTP Keep-Alive)
              一般来说,一个系统能够打开的文件个数是有限制的(文件描述符限制) 
             常连接占用文件描述符,对非并发的访问没有什么意义.
             (文件描述符的数量和许多原因有关,比如日志文件数量,并发数目等)
            这是lighttpd在keep-alive方面的默认值. 
server.max-keep-alive-requests = 128 
server.max-keep-alive-idle = 30
换言之,lighttpd最多可以同时承受30秒长的常连接,每个连接最多请求128个文件. 
但这个默认值确实不适合非并发这种多数情况.
lighttpd.conf 中减小 
server.max-keep-alive-requests 
server.max-keep-alive-idle 
两个值,可以减缓这种现象.
甚至可以关闭lighttpd keep-alive. 
server.max-keep-alive-requests = 0 
4 事件处理
对于linux kernel 2.6来说,没有别的可说 
lighttpd.conf中加上这一句足矣 
server.event-handler = “linux-sysepoll”
另外, 
linux 2.4 使用 linux-rtsig 
freebsd 使用 freebsd-kqueue 
unix 使用 poll 
5 网络处理
lighttpd 大量使用了 sendfile() 这样一个高效的系统调用. 
减少了从应用程序到网卡间的距离. 
(同时也减少了lighttpd对cpu的占用,这部分占用转嫁到内核身上了)
根据平台,可以设置不同的参数. 
server.network-backend = “linux-sendfile” 
(linux) 
freebsd: freebsd-sendfile 
unix: writev
如果有兴趣的话,也可以看看lighttpd在async io(aio)上的实现,仅限 lighttpd 1.5 
(linux-aio-sendfile, posix-aio, gthread-aio)
此外,网络方面,核心的参数也需要适当进行修改, 
这里就不需要详细说明了.
     5,启动 
     6,配置日志 
     logrotate & cronolog 
logrotate很粗暴,直接把进程砍了然后移动日志 
cronolog就是比较不错的方式. 
lighttpd用法: 
accesslog.filename = " |/usr/sbin/cronolog /var/log/lighttpd/%Y/%m/%d/access_XXXX.log"
     7,安装pcre 
       从何处下载? 
       
http://www.pcre.org/

        wget 
ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-7.4.tar.bz2

      安装过程： 
        　　./configure 
　　make clean 
　　make 
　　make install
8,支持fam 
    gamin默认已安装了此包 
    yum install gamin-devel
    另外配置时需添加： 
    ./configure --prefix=/usr/local/lighttpd --with-fam
9,测试lighttpd的启动： 
/usr/local/lighttpd/sbin/lighttpd -f /usr/local/lighttpd/etc/lighttpd.conf
10,防止盗链 
  #$HTTP["referer"] !~ "^($|http://.*.(chinafotopress.com|chinafotopress.cn))" {       
#     $HTTP["url"] =~ ".(jpg|jpeg|png|gif|rar|zip|mp3)$" { 
#        #url.redirect = (".*"     => "
http://www.baidu.com/
") 
#         url.access-deny = (".jpg") 
#     } 
#}
#$HTTP["referer"] == "" { 
#     $HTTP["url"] =~ ".(jpg|jpeg|png|gif|rar|zip|mp3)$" { 
#        #url.redirect = (".*"     => "
http://www.baidu.com/
") 
#         url.access-deny = (".jpg") 
#     } 
#}
日志处理

Sometimes, Google Analytics just isn't enough when it comes to
keeping and interpreting server stats. After finding a suitable log
file analyzer, AWStats, the next step involved separating out the log
files on a per domain basis. When the server was first set up,
everything was shuttled to one set of access and error log files. While
AWStats could technically analyze this log, the suggested set up
involves having one set per domain. This article details the process of
separating out the log files and making sure that these new files get
rotated correctly. 
Create Log Directories
While it would be possible to keep all of the files in one directory
and to just name them relative to the domain, for this tutorial we will
assume that we will create subdirectories based on the domain name. The
first step would be to create a directory for each domain.
sudo -u www-data mkdir /var/log/lighttpd/www.example1.com 
sudo -u www-data mkdir /var/log/lighttpd/www.example2.com 
Update lighttpd.conf
After creating the directories, it's time to update the lighttpd
conf file in /etc/lighttpd. We'll want to set the log files by host
name. We already had directives setting the server.document-root for
these domains so we only added the bolded lines.
$HTTP["host"] =~ "(^|\.)example1.com"$" { 
server.document-root = "/var/www/www.example1.com", 
server.errorlog = "/var/log/lighttpd/www.example1.com/error.log", 
accesslog.filename = "/var/log/lighttpd/www.example1.com/access.log", 
}
$HTTP["host"] =~ "(^|\.)example2.com$" { 
server.document-root = "/var/www/www.example2.com", 
server.errorlog = "/var/log/lighttpd/www.example2.com/error.log", 
accesslog.filename = "/var/log/lighttpd/www.example2.com/access.log", 
}
After adding these directives, you will need to restart the server.
sudo /etc/init.d/lighttpd restart 
Update Logrotate
Finally, we will want logrotate to rotate these new directories.
Since our main goal is to integrate the logs with AWStats, it made
sense to add a separate entry for each log directory. However, if you
don't need call different scripts for the different domains, feel free
to create one directive. We just copied the existing logrotate
configuration and editted it for each of the domains. Below are
examples of what this might look like.
/var/log/lighttpd/*.log { 
daily 
missingok 
copytruncate 
rotate 60 
compress 
notifempty 
sharedscripts 
postrotate 
if [ -f /var/run/lighttpd.pid ]; then \ 
kill -HUP $( 
fi; 
endscript 
} 
/var/log/lighttpd/www.example1.com/*.log { 
daily 
missingok 
copytruncate 
rotate 60 
compress 
notifempty 
sharedscripts 
postrotate 
if [ -f /var/run/lighttpd.pid ]; then \ 
kill -HUP $( 
fi; 
endscript 
} 
/var/log/lighttpd/www.example2.com/*.log { 
daily 
missingok 
copytruncate 
rotate 60 
compress 
notifempty 
sharedscripts 
postrotate 
if [ -f /var/run/lighttpd.pid ]; then \ 
kill -HUP $( 
fi; 
endscript 
}
To make just one configuration entry, it would look like this:
"/var/log/lighttpd/*.log" "/var/log/lighttpd/www.example1.com/*.log" "/var/log/lighttpd/www.example2.com/*.log" { 
daily 
missingok 
copytruncate 
rotate 60 
compress 
notifempty 
sharedscripts 
postrotate 
if [ -f /var/run/lighttpd.pid ]; then \ 
kill -HUP $( 
fi; 
endscript 
} 
Sources
     * Lighttpd rotating log files with logrotate tool 
     * Howto: Lighttpd web server setting up virtual hosting
Trackback URL for this post: 
http://tracy.hurleyit.com/trackback/1140
lighttpd虚拟主机配置 
$HTTP["host"] == "bbs.xxx.com" { 
server.name = "bbs.xxx.com" 
server.document-root = "/var/www/bbs" 
server.errorlog = "/var/www/bbs/error.log" 
accesslog.filename = "/var/www/bbs/access.log" 
} 
else
lighttpd.conf解释
server.use-ipv6 = "disable" # 缺省为禁用 
server.event-handler = "linux-sysepoll" # Linux环境下epoll系统调用可提高吞吐量 
#server.max-worker = 10 # 如果你的系统资源没跑满，可考虑调高 lighttpd进程数 
server.max-fds = 4096 # 默认的，应该够用了，可根据实际情况调整 
server.max-connections = 4096 # 默认等于 server.max-fds 
server.network-backend = "linux-sendfile" 
server.max-keep-alive-requests = 0 # 在一个keep-alive会话终止连接前能接受处理的最大请求数。0为禁止
# 设置要加载的module 
server.modules = ( 
  "mod_rewrite", 
  "mod_redirect", 
# "mod_alias", 
  "mod_access", 
# "mod_cml", 
# "mod_trigger_b4_dl", 
  "mod_auth", 
  "mod_expire", 
# "mod_status", 
# "mod_setenv", 
  "mod_proxy_core", 
  "mod_proxy_backend_http", 
  "mod_proxy_backend_fastcgi", 
# "mod_proxy_backend_scgi", 
# "mod_proxy_backend_ajp13", 
# "mod_simple_vhost", 
  "mod_evhost", 
# "mod_userdir", 
# "mod_cgi", 
  "mod_compress", 
# "mod_ssi", 
# "mod_usertrack", 
# "mod_secdownload", 
# "mod_rrdtool", 
  "mod_accesslog" )
# 网站根目录 
server.document-root = "/var/www/"
# 错误日志位置 
server.errorlog = "/var/log/lighttpd/error.log"
# 网站Index 
index-file.names = ( "index.php", "index.html", 
  "index.htm", "default.htm" )
# 访问日志, 以及日志格式 (combined), 使用X-Forwarded-For可越过代理读取真实ip 
accesslog.filename = "/var/log/lighttpd/access.log" 
accesslog.format = "%{X-Forwarded-For}i %v %u %t \"%r\" %s %b \"%{User-Agent}i\" \"%{Referer}i\""
# 设置禁止访问的文件扩展名 
url.access-deny = ( "~", ".inc", ".tpl" )
# 服务监听端口 
server.port = 80
# 进程id记录位置 
server.pid-file = "/var/run/lighttpd.pid"
# virtual directory listings 如果没有找到index文件就列出目录。建议disable。 
dir-listing.activate = "disable"
# 服务运行使用的用户及用户组 
server.username = "www" 
server.groupname = "www"
# gzip压缩存放的目录以及需要压缩的文件类型 
compress.cache-dir = "/tmp/lighttpd/cache/compress/" 
compress.filetype = ("text/plain", "text/html")
# fastcgi module 
# for PHP don't forget to set cgi.fix_pathinfo = 1 in the php.ini 
$HTTP["url"] =~ "\.php$" { 
  proxy-core.balancer = "round-robin" 
  proxy-core.allow-x-sendfile = "enable" 
# proxy-core.check-local = "enable" 
  proxy-core.protocol = "fastcgi" 
  proxy-core.backends = ( "unix:/tmp/php-fastcgi1.sock","unix:/tmp/php-fastcgi2.sock" ) 
  proxy-core.max-pool-size = 16 
}
# 权限控制 
auth.backend = "htpasswd" 
auth.backend.htpasswd.userfile = "/var/www/htpasswd.userfile"
# 基于 evhost 的虚拟主机 针对域名 
$HTTP["host"] == "a.lostk.com" { 
  server.document-root = "/var/www/lostk/" 
  server.errorlog = "/var/log/lighttpd/lostk-error.log" 
  accesslog.filename = "/var/log/lighttpd/lostk-access.log"
  # 设定文件过期时间 
  expire.url = ( 
  "/css/" => "access 2 hours", 
  "/js/" => "access 2 hours", 
  )
  # url 跳转 
  url.redirect = ( 
  "^/$" => "/xxx/index.html", 
  )
  # url 重写 (cakephp可用) 
  url.rewrite = ( 
  "^/(css|js)/(.*)$" => "/$1/$2", 
  "^/([^.]+)$" => "/index.php?url=$1", 
  )
  # 权限控制 
  auth.require = ( "" => 
  ( 
  "method" => "basic", 
  "realm" => "admin only", 
  "require" => "user=admin1|user=admin2" # 允许的用户, 用户列表文件 在上面配置的auth.backend.htpasswd.userfile 里 
  ), 
  ) 
}
# 针对端口的虚拟主机 
$SERVER["socket"] == "192.168.0.1:8000" { 
  server.document-root = "/var/www/xxx/" 
  server.errorlog = "/var/log/lighttpd/test-error.log" 
  accesslog.filename = "/var/log/lighttpd/test-access.log"
  # ... 
}
