Dean
====

1. sshpass:
http://sourceforge.net/projects/sshpass/

不需要输入密码进行ssh, scp操作
#sshpass [-f|-d|-p|-e] [-hV] command parameters
demo: sshpass -p 'googletest' ssh root@ns1.google.com

2. dropbear:
http://matt.ucc.asn.au/dropbear/dropbear.html

Dropbear是一个相对较小的SSH服务器和客户端。它运行在一个基于POSIX的各种平台。 Dropbear是开源软件，在麻省理工学院式的许可证。 
demo: dropbear -p 22

3. fping,iftop
https://github.com/schweikert/fping
