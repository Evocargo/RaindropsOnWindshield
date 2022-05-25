"""
Arguments:
maxR -- maximum drop radius
minR -- minimum drop radius
maxDrops -- maximum number of drops in the image
minDrops -- minimum number of drops in the image
edge_darkratio -- brightness reduction factor for drops edges
return_label -- flag defining whether a label will be returned or just an image with generated raindrops
A, B, C, D -- 4 tuples defining coordinates of Bezier control points in Alpha Map in drop radius scale
"""

cfg = {
	'maxR': 100, # max not more then 150
	'minR': 1,
	'maxDrops': 100,
	'minDrops': 90,
	'edge_darkratio': 0.6,
	'return_label': True,
	'label_thres': 128,
	'A': (1, 4.5),
	'B': (3, 1),
	'C': (1, 3),
	'D': (3, 3)
}
