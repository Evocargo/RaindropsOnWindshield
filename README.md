# RaindropsOnWindshield
We present a publicly available set of images containing 8190 images of which 3390 contain raindrops. Images are annotated with the binary mask representing areas with raindrops.

## Dataset description

The images for the dataset were captured by a camera attached to the vehicle during its movement. The vehicle's movement took place in urban areas and highways, making the dataset ideal for training and assessing vision algorithms for autonomous vehicle camera lens pollution detection. 

The dataset represents sequences of video frames containing 8190 images of which 3390 contain raindrops. Images were labeled by outlining artifacts with polygons. Labeling results are stored in JSON format. In addition, binary masks were generated from this markup, which are also presented in the dataset for convenience. White color denotes an artifact area.

Details have been published in:

[Dataset]()
 * [images]()
   * seq1
   * seq2
   * ...
 * [masks]()
   * seq1
   * seq2
   * ...
 * [json]()

<img width="455" alt="Снимок экрана 2021-03-30 в 10 31 45" src="https://user-images.githubusercontent.com/39035996/112950672-34d2d200-9143-11eb-88ea-6ac459e1df61.png">

## Download

## Artificial raindrops generation algorithm

Apart from the dataset we propose an algorithm that can generate diverse and realistic artificial drops in images.
Collecting images with a variety of raindrops is a challenging and time-consuming task. Thus, an image raindrop simulator would greatly simplify the process and provide data augmentation to train and evaluate different raindrop detection algorithms efficiently. 

The algorithm allows to generate raindrops of three shapes : 0 - circle , 1 - egg, 2 - a combination of two Bezier curves. The egg shape is created by a combination of a circle and a semi-ellipse. Radius, coordinates of the drop center and a shape are randomly selected for each drop. 

<img width="328" alt="drop_generation" src="https://user-images.githubusercontent.com/39035996/112954529-238bc480-9147-11eb-8b14-54120373407e.png">

## Example of image raindrops generation

<img width="806" alt="Снимок экрана 2021-04-01 в 17 41 20" src="https://user-images.githubusercontent.com/39035996/113311191-b37d6a00-9311-11eb-837d-fb86c340c529.png">


## Contribution
Contributions (bug reports, bug fixes, improvements, etc.) are very welcome and should be submitted in the form of new issues and/or pull requests on GitHub.


## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]
