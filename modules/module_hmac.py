import hmac
import hashlib
import base64
from typing import Dict, Optional, Tuple
from datetime import datetime, timedelta, timezone

"""
The hmac module is practical for:
- API request signing and verification
- Webhook signature validation
- Secure token generation
- Data integrity verification

Common use cases for BI/Data Engineers:
- Validating data from external APIs
- Signing requests to cloud services (AWS, Azure, etc.)
- Securing webhooks from SaaS platforms
- Implementing custom authentication schemes
"""



def generate_api_signature(
    secret_key: str,
    payload: str,
    timestamp: Optional[str] = None,
    algorithm: str = 'sha256'
) -> Tuple[str, str]:
    """    
    Use case: Sign outgoing API requests to prove authenticity (similar to AWS Signature V4).
    
    Args:
        secret_key: Shared secret between client and server
        payload: Request body or parameters as string
        timestamp: ISO format timestamp (auto-generated if None)
        algorithm: Hash algorithm ('sha256', 'sha512', etc.)
    
    Returns:
        Tuple of (signature, timestamp) for inclusion in request headers
        
    Example:
        >>> signature, ts = generate_api_signature("my_secret", '{"user_id": 123}')
        >>> headers = {"X-Signature": signature, "X-Timestamp": ts}
    """
    if timestamp is None:
        timestamp = datetime.now(timezone.utc).isoformat()
    
    # Combine timestamp with payload to prevent replay attacks
    message = f"{timestamp}:{payload}"
    
    # Select hash algorithm
    hash_func = getattr(hashlib, algorithm)
    
    # Generate HMAC
    signature = hmac.new(
        key=secret_key.encode('utf-8'),
        msg=message.encode('utf-8'),
        digestmod=hash_func
    ).hexdigest()
    
    return signature, timestamp


def verify_api_signature(
    secret_key: str,
    payload: str,
    received_signature: str,
    timestamp: str,
    algorithm: str = 'sha256',
    max_age_seconds: int = 300
) -> bool:
    """
    Use case: Validate incoming webhook or API calls to prevent tampering.
    
    Args:
        secret_key: Shared secret
        payload: Received request body
        received_signature: Signature from request headers
        timestamp: Timestamp from request headers
        algorithm: Hash algorithm used
        max_age_seconds: Maximum allowed age of request (prevents replay attacks)
    
    Returns:
        True if signature is valid and not expired, False otherwise
        
    Example:
        >>> is_valid = verify_api_signature(
        ...     "my_secret",
        ...     request.body,
        ...     request.headers["X-Signature"],
        ...     request.headers["X-Timestamp"]
        ... )
    """
    # Check timestamp to prevent replay attacks
    try:
        request_time = datetime.fromisoformat(timestamp)
        age = (datetime.now(timezone.utc) - request_time).total_seconds()
        if age > max_age_seconds or age < 0:
            return False
    except (ValueError, TypeError):
        return False
    
    # Recreate the expected signature
    expected_signature, _ = generate_api_signature(
        secret_key, payload, timestamp, algorithm
    )
    
    # Use compare_digest to prevent timing attacks
    return hmac.compare_digest(expected_signature, received_signature)


def sign_webhook_payload(
    secret: str,
    payload: bytes,
    encoding: str = 'hex'
) -> str:
    """
    Use case: Verify webhooks from SaaS platforms like Stripe, Twilio, etc.
    
    Args:
        secret: Webhook secret provided by the service
        payload: Raw webhook payload (bytes)
        encoding: Output encoding ('hex', 'base64')
    
    Returns:
        Signature string in specified encoding
        
    Example:
        >>> # When receiving webhook
        >>> signature = request.headers.get('X-Hub-Signature-256', '').split('=')[1]
        >>> expected = sign_webhook_payload(WEBHOOK_SECRET, request.get_data())
        >>> if hmac.compare_digest(signature, expected):
        ...     process_webhook(request.json)
    """
    signature = hmac.new(
        key=secret.encode('utf-8'),
        msg=payload,
        digestmod=hashlib.sha256
    ).digest()
    
    if encoding == 'hex':
        return signature.hex()
    elif encoding == 'base64':
        return base64.b64encode(signature).decode('utf-8')
    else:
        raise ValueError(f"Unsupported encoding: {encoding}")


def verify_data_integrity(
    data: bytes,
    expected_hmac: str,
    secret_key: str
) -> bool:
    """
    Use case: Verify integrity of cached data, files, or database records.
    
    Args:
        data: The data to verify
        expected_hmac: The HMAC that should match
        secret_key: Secret key used for HMAC generation
    
    Returns:
        True if data integrity verified, False otherwise
        
    Example:
        >>> # Store data with HMAC
        >>> data = b"sensitive_configuration"
        >>> mac = generate_data_hmac(data, "secret_key")
        >>> # Later, verify integrity
        >>> if verify_data_integrity(data, mac, "secret_key"):
        ...     use_configuration(data)
    """
    computed_hmac = hmac.new(
        key=secret_key.encode('utf-8'),
        msg=data,
        digestmod=hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(computed_hmac, expected_hmac)


def generate_secure_token(
    user_id: str,
    secret_key: str,
    expiry_hours: int = 24
) -> str:
    """
    Use case: Create temporary access tokens for data exports, reports, etc.
    
    Args:
        user_id: Unique identifier for the user/resource
        secret_key: Server-side secret key
        expiry_hours: Token validity period
    
    Returns:
        Base64-encoded token containing user_id, expiry, and HMAC
        
    Example:
        >>> token = generate_secure_token("user123", "server_secret")
        >>> # Send token to user for temporary access
        >>> # Later verify with verify_secure_token()
    """
    expiry = datetime.now(timezone.utc) + timedelta(hours=expiry_hours)
    expiry_str = expiry.isoformat()
    
    # Create payload
    payload = f"{user_id}:{expiry_str}"
    
    # Generate HMAC
    mac = hmac.new(
        key=secret_key.encode('utf-8'),
        msg=payload.encode('utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()
    
    # Combine and encode
    token_data = f"{payload}:{mac}"
    return base64.urlsafe_b64encode(token_data.encode('utf-8')).decode('utf-8')


def verify_secure_token(
    token: str,
    secret_key: str
) -> Optional[str]:
    """
    Args:
        token: Token generated by generate_secure_token()
        secret_key: Server-side secret key
    
    Returns:
        user_id if token is valid and not expired, None otherwise
        
    Example:
        >>> user_id = verify_secure_token(token, "server_secret")
        >>> if user_id:
        ...     grant_access(user_id)
    """
    try:
        # Decode token
        token_data = base64.urlsafe_b64decode(token.encode('utf-8')).decode('utf-8')
        parts = token_data.rsplit(':', 1)
        
        if len(parts) != 2:
            return None
        
        payload, received_mac = parts
        user_id, expiry_str = payload.split(':', 1)
        
        # Verify HMAC
        expected_mac = hmac.new(
            key=secret_key.encode('utf-8'),
            msg=payload.encode('utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()
        
        if not hmac.compare_digest(expected_mac, received_mac):
            return None
        
        # Check expiry
        expiry = datetime.fromisoformat(expiry_str)
        if datetime.now(timezone.utc) > expiry:
            return None
        
        return user_id
        
    except (ValueError, TypeError, AttributeError):
        return None


def create_signed_url_params(
    params: Dict[str, str],
    secret_key: str
) -> Dict[str, str]:
    """
    Add signature to URL parameters for tamper-proof links.
    
    Use case: Generate signed URLs for data exports, reports, or embedded dashboards.
    
    Args:
        params: Dictionary of URL parameters
        secret_key: Secret key for signing
    
    Returns:
        Original params with added 'signature' parameter
        
    Example:
        >>> params = {"user_id": "123", "report": "sales_2024"}
        >>> signed = create_signed_url_params(params, "secret")
        >>> url = f"https://api.example.com/export?{urlencode(signed)}"
    """
    # Sort params for consistent signing
    sorted_params = sorted(params.items())
    param_string = '&'.join(f"{k}={v}" for k, v in sorted_params)
    
    # Generate signature
    signature = hmac.new(
        key=secret_key.encode('utf-8'),
        msg=param_string.encode('utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()
    
    result = params.copy()
    result['signature'] = signature
    return result


def verify_signed_url_params(
    params: Dict[str, str],
    secret_key: str
) -> bool:
    """
    Verify signature in URL parameters.
    
    Args:
        params: Dictionary of URL parameters including 'signature'
        secret_key: Secret key for verification
    
    Returns:
        True if signature is valid, False otherwise
    """
    if 'signature' not in params:
        return False
    
    received_signature = params.pop('signature')
    
    # Recreate signature
    sorted_params = sorted(params.items())
    param_string = '&'.join(f"{k}={v}" for k, v in sorted_params)
    
    expected_signature = hmac.new(
        key=secret_key.encode('utf-8'),
        msg=param_string.encode('utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(expected_signature, received_signature)


if __name__ == "__main__":
    print("=== HMAC Module Examples ===\n")
    
    # Example 1: API Signature
    print("1. API Request Signing:")
    api_secret = "my_api_secret_key"
    payload = '{"action": "fetch_data", "user_id": 123}'
    sig, ts = generate_api_signature(api_secret, payload)
    print(f"   Signature: {sig[:32]}...")
    print(f"   Timestamp: {ts}")
    print(f"   Valid: {verify_api_signature(api_secret, payload, sig, ts)}\n")
    
    # Example 2: Webhook Verification
    print("2. Webhook Signing:")
    webhook_secret = "webhook_secret_123"
    webhook_data = b'{"event": "payment.success", "amount": 99.99}'
    webhook_sig = sign_webhook_payload(webhook_secret, webhook_data)
    print(f"   Signature: {webhook_sig[:32]}...\n")
    
    # Example 3: Secure Token
    print("3. Secure Token Generation:")
    token_secret = "token_secret_xyz"
    token = generate_secure_token("user_456", token_secret, expiry_hours=1)
    print(f"   Token: {token[:40]}...")
    verified_user = verify_secure_token(token, token_secret)
    print(f"   Verified User ID: {verified_user}\n")
    
    # Example 4: Signed URL
    print("4. Signed URL Parameters:")
    url_params = {"report_id": "Q4_2024", "format": "pdf"}
    signed_params = create_signed_url_params(url_params, "url_secret")
    print(f"   Signed Params: {signed_params}")
    print(f"   Valid: {verify_signed_url_params(signed_params.copy(), 'url_secret')}")