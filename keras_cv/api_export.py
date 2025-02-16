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

import types

from keras_cv.backend import keras

try:
    import namex
except ImportError:
    namex = None


def maybe_register_serializable(symbol):
    if isinstance(symbol, types.FunctionType) or hasattr(symbol, "get_config"):
        keras.saving.register_keras_serializable(package="keras_cv")(symbol)


if namex:

    class keras_cv_export(namex.export):
        def __init__(self, path):
            super().__init__(package="keras_cv", path=path)

        def __call__(self, symbol):
            maybe_register_serializable(symbol)
            return super().__call__(symbol)

else:

    class keras_cv_export:
        def __init__(self, path):
            pass

        def __call__(self, symbol):
            maybe_register_serializable(symbol)
            return symbol
