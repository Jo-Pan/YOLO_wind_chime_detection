import os
import cv2

#import sys
#sys.path.insert(0, "<your_path>/darkflow_master")

from darkflow.net.build import TFNet
import numpy as np
import time

options = {
    'model': 'cfg/yolov2-tiny-voc-1c.cfg',
    'load': 3000,
    'threshold': 0.2
}

tfnet = TFNet(options)

capture = cv2.VideoCapture('new_model_data/wind_chime.mov')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('new_model_data/output.avi',fourcc, 30.0, (360, 640))
colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

while (capture.isOpened()):
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            text_tl=(result['topleft']['x'], result['topleft']['y']+30)
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            text = '{:.0f}% {}'.format(confidence * 100,label)
            frame = cv2.rectangle(frame, tl, br, color, 8)
            frame = cv2.putText(frame, text, text_tl, cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 3)
        frame=cv2.resize(frame, (360, 640)) #30%
        out.write(frame)
        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        capture.release()
        out.release()
        cv2.destroyAllWindows()
        break
