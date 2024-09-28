
# Project Title

This project aims to detect and recognize vehicle number plates using OpenCV and Python. It uses various image processing techniques to locate number plates in images or video streams and extracts the text using Optical Character Recognition (OCR).


## Features

- Number Plate Detection: Identifies and locates vehicle number plates in images or video feeds.
- Character Segmentation: Segments the characters on the detected number plate.
- OCR Integration: Uses Tesseract OCR to recognize and extract text from the segmented characters.
- Real-time Processing: Capable of processing video feeds for real-time number plate detection.

## Pretrained model

You may need to download pre-trained models for number plate detection (e.g., Haar cascades). You can download them from the OpenCV GitHub repository or use a custom-trained model.

harcascade = "model/haarcascade_russian_plate_number.xml"
## Usage/Examples

- Image Detection
    python detect_plate.py --image path/to/your/image.jpg

- Video Detection
    python detect_plate.py --video path/to/your/video.mp4

- Real-time Detection
    python detect_plate.py --camera 0

Note: Use --camera 1 if you have multiple cameras connected.




## Directory Structure

number-plate-detection/
│
├── data/                   # Sample images and videos for testing
├── models/                 # Pre-trained models for number plate detection
├── outputs/                # Directory to store output images and videos
├── src/                    # Source code files
│   ├── detect_plate.py     # Main script for number plate detection
│   └── utils.py            # Helper functions for detection and preprocessing
├── requirements.txt        # Required Python packages
└── README.md               # This README file

## Configuration

- Detection Threshold: Minimum confidence level to filter out weak detections.
## Results
You can view the detected number plates in the outputs/ directory, where the images/videos are saved with bounding boxes around the detected number plates.
## Future Enhancements
- Improved Detection Model
- Character Recognition Enhancement
- Localization and Tracking
- Integration with Databases
- Real-time Enhancements
- Web Interface 
- Multi-language Support
## References

- OpenCV Documentation