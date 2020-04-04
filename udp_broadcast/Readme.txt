#设置能够发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

udp应用之广播

1.广播：一点发送，多点接收

  1.广播地址：一个网段内有一个指定的广播地址，是该网段的
    最大地址。192.168.101.255

    In [1]: s="{} is a {}".format("TOM",'BOY')

    In [3]: s
    Out[3]: 'TOM is a BOY'

    In [4]: s="{1} is a {0}".format("TOM",'BOY')
    In [5]: s
    Out[5]: 'BOY is a TOM'
2.广播风暴：一个网络中有大量的1广播就会产生广播风暴，占用大量
            带宽，影响正常的访问速度。










