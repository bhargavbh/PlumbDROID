.line 217
iget-object v0, p0, Lcom/QRScan/android/activity/ImageViewerActivity;->Camera:Landroid/Hardware/Camera;

invoke-virtual {v0}, Landroid/Hardware/Camera;->stopPreview()V

------

.line 320
invoke-virtual {v1}, Landroid/Hardware/Camera;->release()V

------

.line 371
if-neq v0, :cond_2

invoke-virtual {v0}, Landroid/Hardware/Camera;->release()V

******
QRScan/smali/android/com/content/SurfaceCreator/ImageActivity1.smali
