#
# Copyright (C) Fraunhofer-Institut for Photonic Microsystems (IPMS)
# Maria-Reiche-Str. 2
# 01109 Dresden
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# 
# \author phil.seipt@ipms.fraunhofer.de
# \date 28.05.2021
# 
#
# Copyright (C) 2018 ETH Zurich and University of Bologna
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Authors: Germain Haugou, ETH (germain.haugou@iis.ee.ethz.ch)
# Authors: Phil Seipt, Fraunhofer IPMS (phil.seipt@ipms.fraunhofer.de)
#       * Remove unused chips


from bridge.default_debug_bridge import *
import bridge.chips.usoc_v1 as usoc_v1


def get_bridge(config, binaries=[], verbose=False):

    chip_config = config.get('**/board/chip')
    if chip_config is None:
        raise Exception('Wrong JSON configuration, do not contain any chip information')

    chip = config.get('**/board/chip').get('name').get()

    if chip == 'usoc_v1':
        bridge_class = usoc_v1.usoc_v1_debug_bridge
    else:
        bridge_class = debug_bridge

    return bridge_class(config=config, binaries=binaries, verbose=verbose)
