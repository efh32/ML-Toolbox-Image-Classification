#import mltoolbox image classification model as your model
import mltoolbox.image.classification as model
from google.datalab.ml import *

#set bucket with either a new bucket name or existing bucket name
bucket = 'gs://my-bucket'
preprocess_dir = bucket + '/preprocesseddata'
model_dir = bucket + '/model'
staging_dir = bucket + '/staging'


#set training_data to images collected into bucket
training_data = CsvDataSet('gs://my-bucket/snake_images_train'
			, schema='image_url:STRING,label:STRING')

#preprocess the training_data into the preprocess_dir
preprocess_job = model.preprocess_async(training_data, preprocess_dir, cloud={'num_workers':10})
preprocess_job.wait()

#Take images from preprocess_dir and send to model_dir
#batch size 30, max_steps 1000 (number of steps to train)
train_job = model.train_async(preprocess_dir, 30, 1000, model_dir, cloud=CloudTrainingConfig('us-central1', 'BASIC'))
train_job.wait() 

#Deploy the model on google cloud in model_dir
Models().create('snake')
ModelVersions('snake').deploy('beta1', model_dir)



