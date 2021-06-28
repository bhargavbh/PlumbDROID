.line 117
if-eqz v1, :cond_1

.line 120
invoke-virtual {v1}, Landroid/os/PowerManager$WakeLock;->release()V

------

.line 168
if-eqz v0, :cond_0

.line 171
invoke-virtual {v0}, Landroid/os/PowerManager$WakeLock;->release()V

------

.line 261
invoke-virtual {v0}, Landroid/os/PowerManager$WakeLock;->release()V

------

.line 292
invoke-virtual {v4}, Landroid/os/PowerManager$WakeLock;->release()V

******
Impeller/smali/android/support/v4/content/WakefulBroadcastReceiver.smali

######

.line 102
invoke-virtual {v0}, Landroid/bluetooth/BluetoothAdapter;->cancelDiscovery()Z

------

.line 232
invoke-virtual {v0}, Landroid/bluetooth/BluetoothAdapter;->cancelDiscovery()Z

******
Impeller/smali/org/fdroid/fdroid/localrepo/peers/BluetoothFinder.smali
