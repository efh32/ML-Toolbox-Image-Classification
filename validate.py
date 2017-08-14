#import mltoolbox image classification model as your model
import mltoolbox.image.classification as model
from google.datalab.ml import *


#set the validation_data to the validation data on google cloud
validation_data = CsvDataSet('gs://my-bucket/snake_images_validation'
			, schema='image_url:STRING,label:STRING')

#perform a prediction on the validation set
#create a big query table for the validation results
batch_predict_job = model.batch_predict_async(validation_data, model_dir, output_bq_table='snake.validation_results_full',
                                              cloud={'temp_location': staging_dir})
batch_predict_job.wait()

