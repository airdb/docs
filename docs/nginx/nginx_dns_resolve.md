## nginx的dns cache问题

最近遇到了一个奇怪现象，线上的某个api服务用nginx(A机器)反向代理到其他指定的机器(B机器)，突然有一天该服务报错，日志提示该服务对应的某个文件不存在，而实际文件是存在的，那么到底发生了什么？我的思路是这样的。

1. 查看nginx的日志，请求正常。
2. 查看反向代理的nginx日志，在问题发生的那一时刻，没有请求日志。
3. 查看当时的系统日志，没有发现异常。
4. 查看网卡也没有error，TIME_WAIT和CLOSE_WAIT也无异常。

经过上述排查后觉得这个问题很【奇怪】，无明显错误日志，当时的网络状态无异常，为何请求没有收到？于是做了如下实验。

1. 从A机器 ping B机器，可以ping通
2. A机器请求该api，B机器通过tcpdump抓包，发现B机器无法抓到该请求包

A机器的反向代理配置是这样的。

```bash
   location / {
       proxy_pass https://www.example.com/abc/;
   }
```

于是从A机器dig www.example.com ，解析是正常的，会不会反向代理到C机器上了(前不久该api服务从C机器迁移到了当前的B机器)，于是登录C机器发现，果然A机器的nginx反向代理的请求日志都落在了C机器上面。

google了一下nginx的dns service相关文章，在[官方blog](https://www.nginx.com/blog/dns-service-discovery-nginx-plus/)的一篇文章中发现了有如下一段描述，即nginx会忽略dns ttl，直到重启或reload nginx的配置，文章也给出了一些方案，比如在upstream模块的server用域名、set变量、resolver等等。
>NGINX caches the DNS records until the next restart or configuration reload, ignoring the records’ TTL values.

