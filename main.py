# Copyright 2016 Google Inc.
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

# import webapp2


# class MainPage(webapp2.RequestHandler):
#     def get(self):
#         self.response.headers["Content-Type"] = "text/plain"
#         self.response.write("Hello, World! BSSE")


# app = webapp2.WSGIApplication(
#     [
#         ("/", MainPage),
#     ],
#     debug=True,
# )


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("index.html")  # Serve the HTML file
    #return "Hello, World! BSSE"

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080)
    
    

