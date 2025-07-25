# Copyright (c) ONNX Project Contributors

# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import numpy as np

from onnx.reference.op_run import OpRun


class Trilu(OpRun):
    def _run(self, x, k=None, upper=None):
        k = 0 if k is None else k.item()
        if upper:
            return (np.triu(x, k),)
        return (np.tril(x, k).astype(x.dtype),)
