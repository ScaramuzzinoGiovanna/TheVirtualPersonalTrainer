# The virtual personal trainer
>This virtual personal trainer can help you with your rehabilitation 

## Installation

1. Clone and install [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)<br>
2. Clone this repository with:
```sh
git clone https://github.com/jabosso/ElaboratoIVA.git 
```
2.1 Download our dataset https://drive.google.com/open?id=1053dYWbOHf1AigDokQbTMU20y6-5Zxq9 and creates a 'Data' folder in which insert this files (Inside data/Name_of_exercise_/model there are the videos used as Personal trainers, the others are videos that can be used as tests) <br>
3. On **Ubuntu**: you must create a symbolic link inside this folder that points to pyopenpose (library  created after installing OpenPose)

4. Prerequisites for run this code:
    * OpenCV  
    * scipy   
    * numpy 
    * math 
    * argparse 
    * time
  
   You can install these using pip or Anaconda

## Usage for the user
In the Data folder you can see the types of exercises performed by your personal trainer (you have to unzip the folder to see the videos).<br>
Choose your exercise and record and save your video!<br>
**Recommendations**:<br> 
         1. Opencv does not read video metadata, a landscape shot is appropriate<br>
         2. Use a quality camera, the webcam is not recommended
    
## You are curious to know how you performed the exercise?
To run the code insert to command line, inside the directory containing the files:
```sh
python match.py -v >Path_of_your_video> -e <Name_of_model_exercise_>
```
*Note*: <Name_of_model_exercise> is the name of the video file choose without the video extension

## How to add exercises performed by a personal trainer?
1. Record a video and save it in the Data folder. Give a name to the file that you remember the exercise done<br>
2. In the directory move/models create a folder with the name of the exercise given to the video<br>
3. In the newly create folder insert a .txt file containing the parts of the body essential for the exercise. In the example file total_point.txt all parts of the body that you can insert in your .txt file are indicated<br>

To run the code for creating the model, insert to command line, inside the directory containing the files:
```sh
python Model_Acquisition.py -v <Path_of_file_video> -e <Name_of_model_exercise>
```
*Note*: <Name_of_model_exercise> is the name of your video file, insert into Data folder, without the video extension. This name is also the same as the folder created in move/models

## Run the code with/without sampling 
There is a _sampling_ flag for sampling the frames of each identified pose. By default it is set to false, but you can change it by setting it to True into files: 'Model_Acquisition.py' and 'Match.py'.

## Requirements
The use of a GPU is recommended for processing performed by Openpose. We used a **GTX 1060**

## Contributors

The entire project was made by [Giovanna Scaramuzzino](https://github.com/ScaramuzzinoGiovanna) and [Johan Andrey Bosso](https://github.com/jabosso)

