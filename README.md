# Cotton_leaf_Disease_Detection
The project sent was more of a demo and didn't include the actual detection part. 

The models folder didn't have .h5 extension files for the models. They simply gave the .ipynb files, which means we have to train our own models and save it in .h5 extension. This explains why it took a bit longer than expected. Each model took around 20 minutes to train. With a total of 4 models, you get the idea.
All models have been trained separately.
app.py had huge modifications in it for the detection part. 
This project now detects the actual disease rather than being a broiler plate to write our own logic.



Steps to get it running:

Download the .zip file from the gdrive link as sent with this message.

Extract using winrar (please use winrar. Windows' default extraction is broken)

Drag or open the folder in vscode. 

Go to app.py 

In the terminal of vscode, type 
"python app.py" (without quotes of course) and hit enter (if you can't find the terminal, click on the bottom left corner of your screen (assuming you have vscode open in full screen)) 

Now your development server will start. In the same terminal look for the url to go to. It would look something like
https://127.0.0.1/5000
When you find this link in the terminal, hold down the ctrl key and left click on the link to open in your default browser. (Do not use ctrl + c to copy the link because that's a shortcut to stop the server)

Once opened, upload any image of a leaf from the val folder in the same project and click on detect.

It also works with random google images.

Note: 
Segmentation was removed completely as no code for training the model has been given.
On an unrelated note: I have no idea why it was named as "cotton" leaf detection :P

Anyway, here is the gdrive link:
https://drive.google.com/file/d/174OCz9GZr-QdhU_5FgBMvXYSe3Aj5fz9/view?usp=sharing
