# Wind Chime Detection
Using YOLO to detect wind chimes in images/videos/webcam. Welcome to leave comments or questions. I'd try my best to help. :wink:
<p>My result: (not perfect & still need more training)
  
  
![](https://media.giphy.com/media/39rHBYIoG02OtrdPYO/giphy.gif)

## Working environment, app, packages & resources
* Macbook Air 
* Atom IDE (https://ide.atom.io/)
* Jupyter Notebook
* tensorflow

<p> For the packages below, you may follow Mark Jay's Youtube series for installation
  
* **darkflow** (https://github.com/thtrieu/darkflow) 
  
  darkflow command options and explanation:`python flow --help`
* YOLO weights and models (https://pjreddie.com/darknet/yolo/)

### Study Materials:
Youtube Series from Mark Jay (https://www.youtube.com/watch?v=bDaxeg4HKQY&index=3&list=PLX-LrBk6h3wSGvuTnxB2Kj358XfctL4BM)

I borrowed some methods from the video series. If you are a beginner and want to learn, I strongly recommend following his instructions. 


## 1. Download images with desired keyword(s) 
Many scraping methods with Google Search don't work anymore. 
Icrawler is simple and work. 

*Reference: https://github.com/hellock/icrawler*

*My code: get_images_icrawler.py*

## 2. Organize and clean images
Delete the undesired images.
Rename images and put them into one folder.
*My code: rename.py*

## 3. Draw annotation box
*My code: draw_box.py*

## 4. Generate annotation xml
*My code: generate_xml.py*
<p> It's a long process. I added in functions to allow quitting in between and resuming the progress later.

## 5. Train your model
<p>general format:

`flow --model cfg/(your cfg file) --model bin/(downloaded yolo weight file) --train --annotation (your annotation folder) --dataset (your training image folder) --epoch (num of epoch)`
<p>my code:

`python flow --model cfg/yolov2-tiny-voc-1c.cfg --load bin/yolov2-tiny-voc.weights --train --annotation new_model_data/annotations --dataset new_model_data/images --epoch 300 `

My minimum loss is around *1.3* and stop improving since step 3000.

## 6. Test your model!!
I used Iphone to take pictures and record videos for testing.

### Image (Command Line)
<p>general format:

`flow --imgdir <test_image folder> --model cfg/(your cfg file) --load <step number you want to retrieve>`
<p>my code:

`python flow --imgdir new_model_data/test --model cfg/yolov2-tiny-voc-1c.cfg --load 3000`
It will automatically generate labeled images.

### Image (Jupyter notebook)
*My code: test_image_pred_0.ipynb*
<p> If you have the darkflow not found error for importing TFNET, try the following
  
 `import os`
 
 `os.chdir("<your path>/darkflow_master")`
<p> The model has higher confidence when the photo has good lighting.

### Video
*My code: test_video_predict.py*
<p>The code output an annotated video file. The fourcc code I used was good for Mac.
<p>OpenCV Video Writer on Mac OS X (https://gist.github.com/takuma7/44f9ecb028ff00e2132e)
