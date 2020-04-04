关于tcp网络通信的小技巧
1.在创建套节字对象之后，利用套节字属性s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
  可以及时释放端口使得在服务端重启的时候，服务端不会被占用端口
2.SO_REUSEADDR :当socket关闭之后，本地端用于该socket的端口号立刻就可以被重用．
　通常来说，只有经过系统定义一段时间后才能被重用
3.返回布尔值，也就是1

------------------------------------------------------
套节字属性笔记：
套接字对象
  s代表一个套接字

  s.family:获取套接字地址族类型
  s.type:获取套接字类型
  s.getsockname():获取套接字的绑定地址

  s.fileno():获取套接字的文件描述符--->和IO的知识有关
  文件描述符：每一个IO事件操作系统都会分配一个不同的正整数
  作为编号，改正正整数即为这个IO的文件描述符。

  *文件描述符是操作系统识别IO的唯一标志
   stdin -->0
   stdout-->1
   stderr-->2

  s.getpeername():获取客户端连接套接字的对应地址

  s.setsockopt(level,option,value)
  功能：设置套接字选项，丰富或者修改套接字属性功能
  参数：level 选项类别 SOL_SOCKET
        option 具体选项 SO_REUSEADDR
	value 选项值

   <图片解释>两张图
   
  s.getsockopt(level,option)
  功能：设置套接字选项，丰富或者修改套接字属性功能
  参数：level 选项类别 SOL_SOCKET
        option 具体选项 SO_REUSEADDR
  返回值：选项值

  *如果要设置套接字选项，在创建套接字之后立即设置
