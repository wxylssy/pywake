# pywake
定时唤醒

# 查看系统支持的模式
cat /sys/power/state

# 休眠
echo mem > /sys/power/state

# 10秒后自动唤醒
echo +10 > /sys/class/rtc/rtc0/wakealarm

# 或者使用命令：
rtcwake -m mem -s 10
