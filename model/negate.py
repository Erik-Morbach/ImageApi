import model.filter
import cv2


class Negate(model.filter.Filter):
    def execute(self, image, **kwargs):
        image = super().execute(image, **kwargs)
        return cv2.bitwise_not(image)
