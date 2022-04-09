import cv2
import numpy as np

from model.operations_type import OperationsEnum
from model.operation import Operation


class Rescale(Operation):
    operation_type = OperationsEnum.RESCALE

    def execute(self, image, **kwargs):
        image = super().execute(image)
        scale_x = kwargs.get("scale_x")
        scale_y = kwargs.get("scale_y")
        size = np.shape(image)[:2]
        width = int(size[0] * scale_x)
        height = int(size[1] * scale_y)
        new_size = (width, height)
        return cv2.resize(image, new_size, cv2.INTER_CUBIC)
