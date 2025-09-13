import functions_framework
import json
import logging

@functions_framework.http
def symphony_cloud_function(request):
    """HTTP Cloud Function that processes sensor data."""
    try:
        request_json = request.get_json(silent=True)

        if request_json and isinstance(request_json, dict):
            # Log the received data
            logging.info(f"Received data: {json.dumps(request_json)}")

            # You can process the data here
            # For this project, we are only logging it

            return 'Data received and logged successfully!', 200
        else:
            # Handle cases where the request is not JSON or is empty
            logging.error("No data received in the request or invalid JSON payload.")
            return 'No data received in the request.', 400
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return f"An error occurred: {e}", 500
