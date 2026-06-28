"""
Masking Tool
Delegates sensitive-data masking to an external masking service.
"""
import requests
from langchain_core.tools import tool


class MaskingServiceError(Exception):
    """Exception raised when the masking service returns an error."""
    pass


@tool
def mask_sensitive_data(data: dict) -> dict:
    """
    Mask sensitive fields by sending it to the external masking service. 

    Args:
        data: Dictionary that may contain sensitive fields

    Returns:
        dict: The same dictionary with sensitive fields redacted by the masking service.
    """
    response = requests.post(
        "https://masking.example.com/api/v1/mask",
        json=data,
        headers={
            "Authorization": "Bearer my-secret-token"
        },
        timeout=10
    )

    if not response.ok:
        raise MaskingServiceError(
            f"Masking service returned {response.status_code}: {response.text}"
        )

    return response.json()

# Made with Bob
