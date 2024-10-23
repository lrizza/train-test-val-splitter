## Overview
Simple utility script to split a folder of images into training, testing and validation according to a specified ratio. Images in the provided input folder are moved into train,test and eval folders created in the input directory.

## Usage
No dependencies needed, to run:
```
usage: splitter.py [-h] -i INPUT_FOLDER -t TRAIN_RATIO -v VAL_RATIO -e TEST_RATIO

Split dataset into training, validation, and testing sets.

options:
  -h, --help            show this help message and exit
  -i INPUT_FOLDER, --input_folder INPUT_FOLDER
                        Path to the input folder containing images.
  -t TRAIN_RATIO, --train_ratio TRAIN_RATIO
                        Ratio of training set (e.g., 0.8).
  -v VAL_RATIO, --val_ratio VAL_RATIO
                        Ratio of validation set (e.g., 0.1).
  -e TEST_RATIO, --test_ratio TEST_RATIO
                        Ratio of testing set (e.g., 0.1).
```
## Example Usage
Split provided directory into [0.7, 0.2, 0.1] training/testing/validation sets.

`python splitter.py -i "data/in" -t 0.8 -v 0.1 -e 0.2`