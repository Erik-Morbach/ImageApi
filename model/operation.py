import cv2
from pydantic import BaseModel
import datetime
import numpy as np

from model.operations_type import OperationsEnum


class Operation(BaseModel):
    operation_type: OperationsEnum

    def add_to_log(self):
        print(datetime.datetime.utcnow(), " :: ", self.operation_type.value)

    def execute(self, image, **kwargs):
        self.add_to_log()
        image = np.frombuffer(image, dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image
