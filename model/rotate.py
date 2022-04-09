import imutils

from model.operations_type import OperationsEnum
from model.operation import Operation


class Rotate(Operation):
    operation_type = OperationsEnum.ROTATE

    def execute(self, image, **kwargs):
        image = super().execute(image)
        angle = kwargs.get("angle")
        return imutils.rotate_bound(image, angle)
