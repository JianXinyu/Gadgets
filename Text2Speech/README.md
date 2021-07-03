# Text2Speech
Transform multi-language text into speech using Google Cloud Text-To-Speech API. The result is fantastic! Good job, Google.

## Environment 
Windows10, Python 3.7

## Set-up
- Make sure you have deployed a Cloud project, set up authentication, install the cloud SDK and the client library following the [link](https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries).
- [Optional] You can try these [demo](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/texttospeech/cloud-client) provided by google to test your set up. 
- Perhaps your authentication doesn't work. Include
  ```
  import os
  os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="[Your directory of JSON file]"
  ```
  at the head of code.
- Run t2s.py
- You can customize your languages and voices!
  
## About the text
  - The text should be .txt file. 
  - Different languages must be seperated by paragraphs, i.e. '\n'. 
  - Different languages can appear alternately in the text. 
  - Import your own file at Line55.

## About the speech
  - The output format is .mp3
  - Change the output .mp3 file name at Line74
  
