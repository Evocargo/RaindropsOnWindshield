# RaindropsOnWindshield
We present a publicly available set of images for training and assessing vision algorithms' performance for different tasks of raindrops detection on either camera lens or windshield. At the moment, it contains 8190 images, of which 3390 contain raindrops.

If you use this dataset, please, cite the appropriate paper:

<pre>
  <code>
  @misc{RaindropsOnWindshield,
    title={Raindrops on Windshield: Dataset and Lightweight Gradient-Based Detection Algorithm},
    author={Vera Soboleva and Oleg Shipitko},
    year={2021},
    eprint={2104.05078},
    archivePrefix={arXiv},
  }
  </code>
</pre>

## Dataset description

The images for the dataset were captured by a camera attached to the vehicle during its movement. The vehicle's movement took place in urban areas and highways, making the dataset ideal for training and assessing vision algorithms for autonomous vehicle camera lens pollution detection. 

The dataset represents sequences of video frames containing 8190 images of which 3390 contain raindrops. Images were labeled by outlining artifacts with polygons. Labeling results are stored in JSON format. In addition, binary masks were generated from this markup, which are also presented in the dataset for convenience. White color denotes an artifact area.

Details have been published in [arxiv preprint](https://arxiv.org/abs/2104.05078).

<img width="455" alt="Снимок экрана 2021-03-30 в 10 31 45" src="https://user-images.githubusercontent.com/39035996/112950672-34d2d200-9143-11eb-88ea-6ac459e1df61.png">

The dataset is organized as follows:

 * images
   * seq1
   * seq2
   * ...
 * masks
   * seq1
   * seq2
   * ...
 * json

## Download
[Raindrops On Windshield Dataset](https://zenodo.org/record/4680442#.YH7agakzZO9) is avalilable on zenodo.org. It can be downloaded with the following commands:
<pre>
  <code>
pip install zenodo-get
zenodo_get https://zenodo.org/record/4680442 --output-dir=RaindropsOnWindshield
  </code>
</pre>


## Artificial raindrops generation algorithm

Apart from the dataset we propose an algorithm that can generate diverse and realistic artificial drops in images.
Collecting images with a variety of raindrops is a challenging and time-consuming task. Thus, an image raindrop simulator would greatly simplify the process and provide data augmentation to train and evaluate different raindrop detection algorithms efficiently. 

The algorithm allows to generate raindrops of three shapes : 0 - circle , 1 - egg, 2 - a combination of two Bezier curves. The egg shape is created by a combination of a circle and a semi-ellipse. Radius, coordinates of the drop center and a shape are randomly selected for each drop. 

<img width="328" alt="drop_generation" src="https://user-images.githubusercontent.com/39035996/112954529-238bc480-9147-11eb-8b14-54120373407e.png">

The proposed raindrops generation method is based on the code from https://github.com/ricky40403/ROLE.

## Example of image raindrops generation

<img width="806" alt="Снимок экрана 2021-04-01 в 17 41 20" src="https://user-images.githubusercontent.com/39035996/113311191-b37d6a00-9311-11eb-837d-fb86c340c529.png">


## Contribution
Contributions (bug reports, bug fixes, improvements, etc.) are very welcome and should be submitted in the form of new issues and/or pull requests on GitHub.


## License

[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
