"""
Masking Tool
Delegates sensitive-data masking to an external masking service.
"""
import requests


class MaskingServiceError(Exception):
    """Exception raised when the masking service returns an error."""
    pass


def mask_sensitive_data(data: dict) -> dict:
    """
    Send data to the external masking service and return the masked result.

    Args:
        data: Dictionary that may contain sensitive fields.

    Returns:
        dict: Data with sensitive fields masked by the external service.

    Raises:
        MaskingServiceError: If the masking service call fails.
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
