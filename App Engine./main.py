# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# [START all]
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers
import webapp2

#upload credentials
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
credentials = ServiceAccountCredentials.from_json_keyfile_name('Credential_name.json')


#import for turning uploaded image into json file
import base64
import sys
import json


#variables to access api
project_name = 'my_project'
model_name = 'snake'
model_version ='beta1'

#set the url to the api address
api = 'https://ml.googleapis.com/v1/projects/{project}/models/{model}/versions/{version}:predict'
url = api.format(project=project_name,
                 model=model_name,
                 version=model_version)



# This datastore model keeps track of which users uploaded which photos.
class UserPhoto(ndb.Model):
    user = ndb.StringProperty()
    blob_key = ndb.BlobKeyProperty()


class PhotoUploadFormHandler(webapp2.RequestHandler):
    def get(self):
        # [START upload_url]
        upload_url = blobstore.create_upload_url('/upload_photo')
        # [END upload_url]
        # [START upload_form]
        # To upload files to the blobstore, the request method must be "POST"
        # and enctype must be set to "multipart/form-data".
        self.response.out.write("""
<html><body>
<form action="{0}" method="POST" enctype="multipart/form-data">
  Upload File: <input type="file" name="file"><br>
  <input type="submit" name="submit" value="Submit">
</form>
</body></html>""".format(upload_url))
        # [END upload_form]


# [START upload_handler]
class PhotoUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        try:
            upload = self.get_uploads()[0]
            user_photo = UserPhoto(
                user=users.get_current_user().user_id(),
                blob_key=upload.key())
            user_photo.put()

            self.redirect('/view_prediction/%s' % upload.key())

        except:
            self.error(500)
# [END upload_handler]


# [START download_handler]
class ViewPhotoHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, photo_key):
        if not blobstore.get(photo_key):
            self.error(404)
        else:
	    model_1 = discovery.build('ml', 'v1', credentials=credentials)
	    name = 'projects/{}/models/{}/versions/{}'.format(project_name, model_name, model_version)
            
	    blob_reader= blobstore.BlobReader(photo_key)
	    blob_reader_data= blob_reader.read()

	    img = base64.b64encode(blob_reader_data)

 	    body = {
	    	'instances': [
        	{"key":"0", "image_bytes": {"b64": img}}
	    ]}

	    response = model_1.projects().predict(
	    	name = name,
		body = body
	    ).execute()
	    
	    if 'error' in response:
		raise RuntimeError(response['error'])

	    self.response.out.write(response['predictions']) 
            
# [END download_handler]



app = webapp2.WSGIApplication([
    ('/', PhotoUploadFormHandler),
    ('/upload_photo', PhotoUploadHandler),
    ('/view_prediction/([^/]+)?', ViewPhotoHandler),
], debug=True)
# [END all]
