#!/usr/bin/env python

# Copyright 2019 Daytum
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import unittest
import numpy as np
import nbconvert

with open('IntakeExercise.ipynb') as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)

    
with open('IntakeExercise.py', 'w') as f:
    f.write(python_file)

from IntakeExercise import get_well_latitude_and_longitude_by_api

class TestSolution(unittest.TestCase):


    def test_get_well_latitude_and_longitude_by_api_1(self):

        lat, long = get_well_latitude_and_longitude_by_api(api='42003368340000')

        np.testing.assert_allclose(lat, 32.126361, atol=0.001)
        np.testing.assert_allclose(long, -102.713077, atol=0.001)
        
    def test_get_well_latitude_and_longitude_by_api_2(self):

        lat, long = get_well_latitude_and_longitude_by_api(api='42103010410000')

        np.testing.assert_allclose(lat, 31.612632, atol=0.001)
        np.testing.assert_allclose(long, -102.488526, atol=0.001)



if __name__ == "__main__":
    unittest.main()
