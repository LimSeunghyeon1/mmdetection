# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp
from typing import List, Optional

from mmengine.dataset import BaseDataset
from mmengine.fileio import load
from mmengine.utils import is_abs

from ..registry import DATASETS


@DATASETS.register_module(force=True)
class ArtiDataset(CustomDataset):
    pass