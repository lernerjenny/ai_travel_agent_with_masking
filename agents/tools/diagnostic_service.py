"""
Diagnostic Service Integration
Sends user details to a diagnostic service for analysis.
"""

from agents.tools.masking_tool import mask_sensitive_data


class DiagnosticServiceError(Exception):
    """Exception raised when diagnostic service returns an error."""
    pass


def send_to_diagnostic_service(user_details: dict) -> dict:
    """
    Send user details to the diagnostic service.
    
    Args:
        user_details: Dictionary containing user information
        
    Returns:
        dict: Response from diagnostic service
        
    Raises:
        DiagnosticServiceError: If the service returns an error
    """
    # This is a placeholder implementation
    # In production, this would make an actual API call to the diagnostic service
    
    # Simulate checking for sensitive data
    sensitive_fields = ['api_key', 'email', 'phone', 'credit_card', 'ssn', 'passport']
    has_sensitive_data = any(field in str(user_details).lower() for field in sensitive_fields)
    
    if has_sensitive_data:
        raise DiagnosticServiceError(
            "Diagnostic service detected sensitive data in user details. "
            "Data must be masked before processing."
        )
    
    # If no sensitive data, return success
    return {
        'status': 'success',
        'message': 'User details processed successfully',
        'data': user_details
    }


def send_with_masking(user_details: dict, context: str = "operation") -> dict:
    """
    Send user details to diagnostic service with automatic masking on error.
    
    This is a convenience function that handles the complete flow:
    1. Try sending original details
    2. If error due to sensitive data, mask and retry
    3. Return response or raise exception
    
    Args:
        user_details: Dictionary containing user information
        context: Description of the operation (for logging)
        
    Returns:
        dict: Response from diagnostic service
        
    Raises:
        DiagnosticServiceError: If the service fails even after masking
    """
    try:
        print(f'Sending {context} details to diagnostic service...')
        response = send_to_diagnostic_service(user_details)
        print(f'Diagnostic service response: {response}')
        return response
        
    except DiagnosticServiceError as e:
        print(f'Diagnostic service error: {e}')
        print('Masking sensitive data and retrying...')
        
        # Mask sensitive information and retry
        masked_details = mask_sensitive_data(user_details)
        try:
            response = send_to_diagnostic_service(masked_details)
            print(f'Diagnostic service accepted masked details: {response}')
            return response
        except DiagnosticServiceError as retry_error:
            print(f'Diagnostic service still failed after masking: {retry_error}')
            raise

# Made with Bob
