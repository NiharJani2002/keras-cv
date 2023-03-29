# Copyright 2023 The KerasCV Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
random_crop_demo.py shows how to use the RandomCrop preprocessing layer for
object detection.
"""
import demo_utils
import tensorflow as tf

from keras_cv.layers.preprocessing import RandomCrop


def main():
    dataset = demo_utils.load_voc_dataset(bounding_box_format="xyxy")
    random_crop = RandomCrop(height=256, width=256, bounding_box_format="xyxy")
    result = dataset.map(random_crop, num_parallel_calls=tf.data.AUTOTUNE)
    demo_utils.visualize_data(result, bounding_box_format="xyxy")


if __name__ == "__main__":
    main()
