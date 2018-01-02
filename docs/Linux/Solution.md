Linux 常见问题解决办法
====


tar: Exiting with failure status due to previous errors
解决办法：tar: Exiting with failure status due to previous errors 原来是待压缩的文件夹是root权限创建的，而执行tar的时候未加sudo。


svn: Can't convert string from 'UTF-8' to native encoding 的解决办法
svn 版本库中有文件是以中文字符命名的，在 Linux 下 checkout 会报错：svn: Can't convert string from 'UTF-8' to native encoding
然后 checkout 程序就退出了！
解决办法很简单，正确设置当前系统的 locale：
export LC_CTYPE="zh_CN.UTF-8"
然后重新 checkout 即可。
注意，根据你的系统字符集设置变量，如果 zh_CN.UTF-8 不行，有可能要改成 GB2312：
export LC_CTYPE="zh_CN.GB2312"
另外，看别人的帖子，有的变量名不同，用的是：
export LANG="zh_CN.UTF-8"
