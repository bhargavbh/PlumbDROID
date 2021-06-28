.line 117
iget-object v0, p0, Lcom/SipDroid/android/activity/ImageViewerActivity;->Camera:Landroid/Hardware/Camera;

invoke-virtual {v0}, Landroid/Hardware/Camera;->stopPreview()V

------

.line 120
invoke-virtual {v1}, Landroid/Hardware/Camera;->release()V

******
SipDroid/smali/android/com/content/SurfaceCreator/ImageActivity2.smali

.line 171
if-neq v0, :cond_2

invoke-virtual {v0}, Landroid/Hardware/Camera;->release()V

------

.line 261
if-neq v0, :cond_2

invoke-virtual {v0}, Landroid/Hardware/Camera;->release()V

******
SipDroid/smali/android/com/content/SurfaceCreator/ImageActivity3.smali
