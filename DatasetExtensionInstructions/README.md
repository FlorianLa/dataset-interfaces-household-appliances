## Extending the Dataset
The first step to extending the dataset is the collection of new images. We chose to collect videos of devices instead of single images. Here, we also instructed contributers to circle around the interface while filming so that we can extract images with different angles. Contributers were also asked to submit different videos of the same device under different lighting conditions.  

We added a template for the instructions sent to potential contributers (English) and a template for the grant of rights of use (English and German).

For collecting the images, we used a Google form where contributers first had to enter their name and agree to the grant of rights of use. Then we presented a upload form for a video along with optinal text fields for type, lighting, manufacturer, and model. Then, we asked contributers to indicate if they have more videos and if so, presented a new page similar to the last one. Otherwise, we completed the form.

The collected videos were split into images using the frameExtraction.py script.

The single images were then labled manually using LabelImg, which can be found here: https://github.com/tzutalin/labelImg

Additional image information was collected in an excel table generated with the excelCreation.py script.
