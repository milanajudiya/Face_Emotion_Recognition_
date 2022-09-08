# Face_Emotion_Detection

# Project Introduction and Problem Statement
<p>The Indian education landscape has been undergoing rapid changes for the past 10 years owing to
the advancement of web-based learning services, specifically, eLearning platforms.
Global E-learning is estimated to witness an 8X over the next 5 years to reach USD 2B in 2021. India
is expected to grow with a CAGR of 44% crossing the 10M users mark in 2021. Although the market
is growing on a rapid scale, there are major challenges associated with digital learning when
compared with brick and mortar classrooms. One of many challenges is how to ensure quality
learning for students. Digital platforms might overpower physical classrooms in terms of content
quality but when it comes to understanding whether students are able to grasp the content in a live
class scenario is yet an open-end challenge.
In a physical classroom during a lecturing teacher can see the faces and assess the emotion of the
class and tune their lecture accordingly, whether he is going fast or slow. He can identify students who
need special attention. Digital classrooms are conducted via video telephony software program (ex: Zoom) where it’s not possible for medium scale class (25-50) to see all students and access the
mood. Because of this drawback, students are not focusing on content due to lack of surveillance.
While digital platforms have limitations in terms of physical surveillance but it comes with the power of
data and machines which can work for you. It provides data in the form of video, audio, and texts
which can be analysed using deep learning algorithms. Deep learning backed system not only solves
the surveillance issue, but it also removes the human bias from the system, and all information is no
longer in the teacher’s brain rather translated in numbers that can be analysed and tracked.<p>
  
# Dataset FER2013
<p> This dataset contains 48*48 pixels grayscale image faces. The faces are autimatically registered so that the faces are more or less centered in each image and take up around some amount of area. The sevent categories of emotion are (0=Angry,1=Disgust,2=Fear,3=Happy,4=Sad,5=Surprised,6=Neutral), dataset contains 28,709 training sets and 3589 test sets.<p>
  
# File Description
<p><b> Face Emotion Recognition.ipynb</b> = this is the google colab notebook contains data summay , Exploratory Data Analysis, and Modeling.<p>
<p><b> real_time.py</b> = Real Time emotion Detection Locally using opencv-python.<p>
<p><b> app.py</b> = streamlit WebApp file.<p>
  
#Output File
<p><b>emotion_detection_model</b> = CNN model trained on FER2013 Data.<p>

# CNN Model
<p>Convolutional layers convolve the input and pass its result to the next layer. This is similar to the response of a neuron in the visual cortex to a specific stimulus.Each convolutional neuron processes data only for its receptive field. Although fully connected feedforward neural networks can be used to learn features and classify data, this architecture is generally impractical for larger inputs such as high-resolution images. It would require a very high number of neurons, even in a shallow architecture, due to the large input size of images, where each pixel is a relevant input feature.<p>


# Exploratory Data Analysis
![image](https://user-images.githubusercontent.com/98526274/188885400-c5eb267e-636c-46f2-94b5-46fcd29af273.png)
 <p> As in graph number of data of Happy images is more and very less data of Disgust.<p>

# Instruction to run Locally
<p>1 ==> Create project Folder<p>
<p>2 ==> Download real_time.py, emotion_detection_model.h5, haarcascade_frontalface_default.xml in that folder.<p>
<p>3 ==> create virtual environment.<p>
<p>4 ==> install dependencies from requirement.txt file.<p>
<p>5 ==> Run real_time.py<p>

# Web App Deployment
Streamlit: https://milanajudiya-face-emotion-recognition--app-ag8i7m.streamlitapp.com/

# Real Time Emotion Detection Detection
![neutral](https://user-images.githubusercontent.com/98526274/188883768-4f587996-04d8-4428-be86-07834cac4b87.jpg)
![happy](https://user-images.githubusercontent.com/98526274/188884267-96385b98-0057-4b3e-ab60-f262b3e8bdf1.jpg)
![image](https://user-images.githubusercontent.com/98526274/188884608-8d234d7d-ab22-4640-9acd-4e5055c906d9.png)
![image](https://user-images.githubusercontent.com/98526274/188884716-7e964a1a-8ba2-4e89-917a-8695fa08ae59.png)
![image](https://user-images.githubusercontent.com/98526274/188884805-33378747-a32f-461e-b291-ec96f561a0dd.png) 
<p> This model gives the accuracy of 0.67 on test data. so model perform well on unseen data as well. Hear shows some of the emotions of real time test.<p>



