# Project Setup

## Requirements

1. Docker
2. Docker Compose
3. ComfyUI

## Instructions

1. **Obtain a Cloudflare Domain (Optional):**
   - If you want your project to be exposed via a Cloudflare domain, obtain one and create a `.env` file based on the `.env.example` template. Set the `TOKEN` variable in the `.env` file.

2. **Run ComfyUI Locally:**
   - Start ComfyUI on your local machine with the `--listen` option to bind it to `0.0.0.0:8188`.

3. **Enable API Access to Localhost:**
   - Ensure API access to the local host is enabled in your Docker Compose setup. This is already configured in your `docker-compose.yml` file:
     ```yaml
     extra_hosts:
       - "host.docker.internal:host-gateway"
     ```

4. **Start the Docker Containers:**
   - Use the following command to build and run all the services:
     ```bash
     docker compose up -d --build
     ```

5. **Access the Service:**
   - **If you have configured a Cloudflare domain:**
     - Navigate to your Cloudflare domain to access the service.
   - **If you are using the server IP:**
     - Access the service via `http://localhost:8000` or `http://<your-server-ip>:8000`.
