import model.filter
import cv2


class BWTransform(model.filter.Filter):
    def execute(self, image, **kwargs):
        image = super().execute(image, **kwargs)
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
