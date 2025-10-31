import logging
import json
import azure.functions as func
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Leyendo archivo version.json")

    try:
        json_path = os.path.join(os.path.dirname(__file__), "version.json")
        with open(json_path, "r") as f:
            data = json.load(f)

        version = data.get("version", "undefined")
        return func.HttpResponse(f"Versión: {version}", status_code=200)

    except Exception as e:
        logging.error(f"Error al leer el archivo: {e}")
        return func.HttpResponse("Error interno", status_code=500)
