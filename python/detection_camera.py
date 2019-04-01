from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join( execution_path, "output.avi"),output_file_path=os.path.join(execution_path, "output2"), frames_per_second=29, log_progress=True)
a = video_path
print(a)
print(video_path)

