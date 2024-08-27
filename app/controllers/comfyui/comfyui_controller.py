from services.Comfyui import get_comfyui_image
from PIL import Image
import io
from fastapi import Response
from requests.comfyui_request import Input

class ComfyUIController:

    def __init__(self):
        pass        

    def get_image(self, input: Input):
        output_images = []
        images = get_comfyui_image(input.text, input.seed)
        for node_id in images:
            for image_data in images[node_id]:
                # Save images to disk /storage/comfyui/images
                # image = Image.open(io.BytesIO(image_data))
                # image.save("/app/storage/comfyui/images/comfyui_image.png")
                output_images.append(image_data)
        
        return Response(content=output_images[0], media_type="image/png")
