from controllers.comfyui.comfyui_controller import ComfyUIController
from requests.comfyui_request import Input

def router(app):

    # Description
    @app.post("/comfyui/get-image")
    def get_image(input: Input):
        return ComfyUIController().get_image(input)
