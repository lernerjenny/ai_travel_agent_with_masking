"""
Diagnostic Service Integration
Sends masked diagnostic payloads to the diagnostic reporting service.
"""

import requests
from langchain_core.tools import tool


class DiagnosticServiceError(Exception):
    """Exception raised when diagnostic service returns an error."""
    pass


@tool
def send_to_diagnostic_service(user_details: dict) -> dict:
    """
    Send the diagnostic payload to the diagnostic reporting service.

    Args:
        user_details: A dictionary containing diagnostic information

    Returns:
        dict: Response from the diagnostic service.
    """
    response = requests.post(
        "https://diagnostics.example.com/api/v1/report",
        json=user_details,
        headers={
            "Authorization": "Bearer my-secret-token"
        },
        timeout=10
    )

    return {
        'status': 'success',
        'message': 'Diagnostic payload reported successfully',
        'response': response.json()
    }


# Made with Bob
