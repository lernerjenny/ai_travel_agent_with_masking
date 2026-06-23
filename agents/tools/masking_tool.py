"""
Masking Tool
Masks sensitive information in user details before sending to diagnostic service.
"""
import re


def mask_email(email: str) -> str:
    """Mask email address, keeping first character and domain."""
    if '@' in email:
        local, domain = email.split('@', 1)
        if len(local) > 1:
            return f"{local[0]}***@{domain}"
        return f"***@{domain}"
    return "***"


def mask_phone(phone: str) -> str:
    """Mask phone number, keeping last 4 digits."""
    digits = re.sub(r'\D', '', phone)
    if len(digits) > 4:
        return f"***-***-{digits[-4:]}"
    return "***"


def mask_credit_card(card: str) -> str:
    """Mask credit card number, keeping last 4 digits."""
    digits = re.sub(r'\D', '', card)
    if len(digits) > 4:
        return f"****-****-****-{digits[-4:]}"
    return "****"

def mask_api_key(card: str) -> str:
    """Mask fully"""
    return "****"


def mask_sensitive_data(user_details: dict) -> dict:
    """
    Mask sensitive information in user details.
    
    Args:
        user_details: Dictionary containing user information
        
    Returns:
        dict: User details with sensitive information masked
    """
    masked_details = user_details.copy()
    
    # Define masking rules for different field types
    masking_rules = {
        'email': mask_email,
        'phone': mask_phone,
        'phone_number': mask_phone,
        'credit_card': mask_credit_card,
        'card_number': mask_credit_card,
        'api_key': mask_api_key,
        'ssn': lambda x: f"***-**-{x[-4:]}" if len(x) >= 4 else "***",
        'passport': lambda x: f"***{x[-4:]}" if len(x) >= 4 else "***",
    }
    
    # Apply masking to matching fields
    for key, value in masked_details.items():
        if isinstance(value, str):
            key_lower = key.lower()
            for field_name, mask_func in masking_rules.items():
                if field_name in key_lower:
                    masked_details[key] = mask_func(value)
                    break
    
    return masked_details

# Made with Bob
