# ML-Toolbox-Image-Classification

## Project Description <a name="descrip"/> 

This is an image classification model that discerns different species of snakes.  This model is trained using transfer learning.  The model utilizes the feature extraction portion of the Inception-v3 model inorder to preprocess the snake images.  These preprocessed snake images are then used to train a new classifier.  

Links: 
1) https://www.tensorflow.org/hub/tutorials/image_retraining
2) https://cloud.google.com/ml-engine/docs/tensorflow/flowers-tutorial

## Table of Contents

[Project Description](#descrip) 

[Background](#background)

[Requirements](#requirements)

[How to Run](#run)

[License](#license)
 
## Background <a name="background"/>

[File Information](#fileInfo)
 
[Helpful Links](#concepts)


### File Information <a name="fileInfo"/>

1. train.py - 

2. validate.py - 

3. App Engine Folder - 

    1.  app.yaml
    2.  appengine_config.py
    3.  main.py
    4.  main_test.py

### Helpful Links <a name="concepts"/>

1. Further explaination of transfer learning process: https://codelabs.developers.google.com/codelabs/cpb102-txf-learning/index.html?index=..%2F..%2Findex#0


## Requirements <a name="requirements"/>

1. Python 3 - https://www.python.org/getit/
2. TensorFlow - https://www.tensorflow.org/install/
3. Google Cloud - https://cloud.google.com/products/
    * Cloud Datalab - https://cloud.google.com/datalab/
    * App Engine - https://cloud.google.com/appengine/ 
  
## How to Run <a name="run"/>

## License <a name="license"/>

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

