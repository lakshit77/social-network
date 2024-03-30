from django.core.cache import cache
from social_network_app.config import RATE_LIMITER_PERIOD, RATE_LIMITER_FRIEND_REQ

def is_rate_limited(user_id):
    """
    Checks if the user exceeded the rate limit of 3 friend requests per minute.
    """
    cache_key = f'friend_requests_{user_id}'
    current_count = cache.get(cache_key, 0)
    
    if current_count >= RATE_LIMITER_FRIEND_REQ:
        return True
    
    # Increment the request count or set it to 1 if it's not set yet
    cache.set(cache_key, current_count + 1, timeout=RATE_LIMITER_PERIOD)
    return False