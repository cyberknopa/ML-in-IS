# Image Steganalysis with Machine Learning Algorithms

### Description 

Steganalysis.ipynb is a code for detecting LSB steganography in monochromatic JPEG images.  
Popular machine learning classifiers are used to classify images into two classes: steganography or clean


### Dataset

This is a dataset consisting of 8 features extracted from 70,000 monochromatic still images adapted from the Genome Project Standford's database, that are labeled in two classes: LSB steganography (1) and without LSB Steganography (0).

These features are Kurtosis, Skewness, Standard Deviation, Range, Median, Geometric Mean, Hjorth Mobility, and Hjorth Complexity, all extracted from the histograms of the still images, including random spatial transformations.

The steganographic function embeds five types of payloads, from 0.1 to 0.5.

[Link to dataset](https://ieee-dataport.org/open-access/steganalysis-still-images-lsb-steganography-features-dataset)

### Results 

The five classifiers were trained with 56,000 images and tested with 14,000 images.  Random Forest Classifier has the best performance on the used dataset.
