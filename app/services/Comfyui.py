# This is an example that uses the websockets api to know when a prompt execution is done
# Once the prompt execution is done it downloads the images using the /history endpoint

# NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import websocket
import uuid
import json
import urllib.request
import urllib.parse

server_address = "host.docker.internal:8188"
client_id = str(uuid.uuid4())

def queue_prompt(prompt):
    p = {"prompt": prompt, "client_id": client_id}
    data = json.dumps(p).encode('utf-8')
    req = urllib.request.Request(
        "http://{}/prompt".format(server_address), data=data)
    return json.loads(urllib.request.urlopen(req).read())


def get_image(filename, subfolder, folder_type):
    data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    url_values = urllib.parse.urlencode(data)
    with urllib.request.urlopen("http://{}/view?{}".format(server_address, url_values)) as response:
        return response.read()


def get_history(prompt_id):
    with urllib.request.urlopen("http://{}/history/{}".format(server_address, prompt_id)) as response:
        return json.loads(response.read())


def get_images(ws, prompt):
    prompt_id = queue_prompt(prompt)['prompt_id']
    output_images = {}
    while True:
        out = ws.recv()
        if isinstance(out, str):
            message = json.loads(out)
            if message['type'] == 'executing':
                data = message['data']
                if data['node'] is None and data['prompt_id'] == prompt_id:
                    break  # Execution is done
        else:
            continue  # previews are binary data

    history = get_history(prompt_id)[prompt_id]
    for o in history['outputs']:
        for node_id in history['outputs']:
            node_output = history['outputs'][node_id]
            if 'images' in node_output:
                images_output = []
                for image in node_output['images']:
                    image_data = get_image(
                        image['filename'], image['subfolder'], image['type'])
                    images_output.append(image_data)
            output_images[node_id] = images_output

    return output_images

def get_prompt():
    return open("/app/storage/comfyui/workflows/comfyui workflow.json").read()

def get_comfyui_image(text, seed):
    prompt_text = get_prompt()
    prompt = json.loads(prompt_text)
    # set the text prompt for our positive CLIPTextEncode
    prompt["6"]["inputs"]["text"] = text
    prompt["10"]["inputs"]["noise_seed"] = seed
    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
    images = get_images(ws, prompt)
    ws.close()
    return images

# Commented out code to display the output images:

# for node_id in images:
#     for image_data in images[node_id]:
#         from PIL import Image
#         import io
#         image = Image.open(io.BytesIO(image_data))
#         image.show()
