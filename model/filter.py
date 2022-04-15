import cv2
import numpy as np

from model.operations_type import OperationsEnum
from model.operation import Operation


class Filter(Operation):
    operation_type = OperationsEnum.FILTER

    def execute(self, image, **kwargs):
        image = super().execute(image)
        return image
