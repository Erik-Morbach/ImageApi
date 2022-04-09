import io

from fastapi import File, APIRouter
from fastapi.responses import StreamingResponse
from fastapi.exceptions import HTTPException
from model.rotate import Rotate
from model.rescale import Rescale
import cv2

router = APIRouter(prefix="/operation")


@router.post("/rotate/")
def rotate(angle: float, image: list[bytes] = File(...)):
    image = Rotate().execute(image[0], angle=angle)
    res, image = cv2.imencode(".png", image)
    return StreamingResponse(io.BytesIO(image.tobytes()), media_type="image/png")


@router.post("/rescale/")
def rescale(scale: float | None = None, scale_x: float | None = None,
            scale_y: float | None = None, image: list[bytes] = File(...)):
    if scale is None:
        if scale_x is None or scale_y is None:
            return HTTPException(status_code=400, detail="Scale not provided")
    else:
        scale_x = scale
        scale_y = scale

    image = Rescale().execute(image[0], scale_x=scale_x, scale_y=scale_y)
    res, image = cv2.imencode(".png", image)
    return StreamingResponse(io.BytesIO(image.tobytes()), media_type="image/png")
