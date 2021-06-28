.line267
iget-object v2, p0, Lcom/irccloud/android/NetworkConnection;->wifiLock:Landroid/net/wifi/WifiManager$WifiLock;

invoke-virtual {v2}, Landroid/net/wifi/WifiManager$WifiLock;->release()V

------
.line348
iget-object v3, p0, Lcom/irccloud/android/NetworkConnection;->wifiLock:Landroid/net/wifi/WifiManager$WifiLock;

invoke-virtual {v3}, Landroid/net/wifi/WifiManager$WifiLock;->release()V

****
BlueChat/smali/com/BlueChat/android/NetworkConnection.smali

##########

.line571
if-eqz v0, :cond_2

iget-object v0, p0, Lcom/irccloud/android/activity/ImageViewerActivity;->player:Landroid/media/MediaPlayer;

invoke-virtual {v0}, Landroid/media/MediaPlayer;->release()V

----
.line779
iget-object v0, p0, Lcom/google/android/gms/ads/internal/overlay/Landroid/media/MediaPlayer;

invoke-virtual {v0}, Landroid/media/MediaPlayer;->release()V

----
.line1582
iget-object v1, p0, Lcom/google/android/gms/ads/internal/overlay/Landroid/media/MediaPlayer;

invoke-virtual {v1}, Landroid/media/MediaPlayer;->release()V

******

BlueChat/smali/com/BlueChat/android/LayeredActivity2.smali
