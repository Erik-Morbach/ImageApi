import model.filter
import cv2


class Blur(model.filter.Filter):

    def execute(self, image, **kwargs):
        image = super().execute(image, **kwargs)
        ksize = kwargs.get('ksize')
        anchor = kwargs.get('anchor')

        return cv2.blur(image, ksize, anchor)
