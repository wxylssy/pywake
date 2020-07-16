# pywake
定时唤醒，使用的rtcwake命令，需要root权限。

# 查看系统支持的模式
```
cat /sys/power/state
```

也可以使用文件的方式

# 休眠
```
echo mem > /sys/power/state
```

# 10秒后自动唤醒
```
echo +10 > /sys/class/rtc/rtc0/wakealarm
```
