# Motion_Sensitive_Camera

This program is a motion sensitive camera that starts recording footage when it detects motion and pauses the recording when it stops detecting motion and continues the recording when it detects motion again.

A certain variable increments when it detects motion and when that variable reaches a certain number(60), it takes a screenshot and sends it to your gmail that you enter in the beginning.

It detects motion by taking the first frame and making it the 'background' and as the camera runs, if it detects a certain amount of different pixels at the same time, it takes it as motion and starts recording and after 300 frames, it treats the current frame as the new 'background'
