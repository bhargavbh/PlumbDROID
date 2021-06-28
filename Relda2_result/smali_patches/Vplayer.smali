.line 117
if-eqz v1, :cond_1

.line 120
invoke-virtual {v1}, Landroid/os/PowerManager$WakeLock;->release()V

------

.line 292
if-eqz v1, :cond_1

invoke-virtual {v4}, Landroid/os/PowerManager$WakeLock;->release()V

******
Vplayer/smali/android/com/WakefulBroadcastReceiver.smali
