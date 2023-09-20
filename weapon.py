Converting xml file to csv file

def xml_to_csv(path): xml_list = []
value =(root.find('filename').text, int(root.find('size')[0].text), int(root.find('size')[1].text),

member[0].text, int(member[4][0].text), int(member[4][1].text), int(member[4][2].text), int(member[4][3].text))

xml_list.append(value)

#attributes of dataset

column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax'] xml_df = pd.DataFrame(xml_list, columns=column_name)
return xml_df def main():
for folder in ['train','test']:

image_path = os.path.join(os.getcwd(), ('images/' + folder))

#Converting xml to csv file by providing image

xml_df = xml_to_csv(image_path)

xml_df.to_csv(('images/' + folder + '_labels.csv'), index=None) print('Successfully converted xml to csv.')
Converting csv file to record file

filename = group.filename.encode('utf8') image_format = b'jpg'
xmins = []

xmaxs = []
 
ymins = [] ymaxs = [] classes_text = [] classes = []
for index, row in group.object.iterrows(): xmins.append(row['xmin'] / width) xmaxs.append(row['xmax'] / width) ymins.append(row['ymin'] / height) ymaxs.append(row['ymax'] / height) classes_text.append(row['class'].encode('utf8')) classes.append(class_text_to_int(row['class']))
Training the algorithm train_input_reader: { tf_record_input_reader {
#providing training record file

input_path: "train.record"

}

label_map_path: "training/labelmap.pbtxt"

}

eval_input_reader: { tf_record_input_reader {
#providing testing record file

input_path: "test.record"

}

label_map_path: "training/labelmap.pbtxt" }
 
Sending email after predicting

def sendemail():

try:

#login to the server by providing mail id
server.login("bunny.sheelam@gmail.com", "surdkpekkdkzcvcr") server.sendmail("bunny.sheelam@gmail.com","bunny.sheelam@gmail.com","Weapon
Detected")

def run_inference_for_single_image(image, graph):

#Giving input as video

vs = cv2.VideoCapture("mygeneratedvideo.avi") output_dict['detection_boxes’], output_dict['detection_classes’], output_dict['detection_scores’],
Alarm raising after predicting

if isfound:

if not ALARM_ON: ALARM_ON = True ALARM_ON = False sendemail()
