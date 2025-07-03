
import Augmentor
import sys




path = 'dataset_jpg'
p = Augmentor.Pipeline(path)
p.rotate_random_90(0.9)
p.rotate90(0.5)

#p.random_brightness(0.4,0.9,1)
p.rotate(probability=0.9, max_left_rotation=20, max_right_rotation=20)
p.sample(400)