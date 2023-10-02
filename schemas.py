from typing import List

# Schema for the task_1
schema = {
    'package_name': object,
    'market_status': object,
    'category': object,
    'cat_key': object,
    'cat_keys': List[object],
    'cat_type': int,
    'title': object,
    'description': object,
    'short_desc': object,
    'icon': object,  # URL
    'icon_72': object,  # URL
    'market_url': object,  # URL
    'what_is_new': object,
    'downloads': object,
    'downloads_min': int,
    'downloads_max': int,
    'market_update': object,  # Date in ISO8601 extended format
    'created': object,  # Date in ISO8601 extended format
    'promo_video': object,  # URL
    'promo_video_image': object,  # URL
    'rating': float,
    'size': int,
    'screenshots': List[object],  # List of URLs
    'version': object,
    'version_code': int,
    'website': object,  # URL
    'privacy_policy': object,  # URL
    'developer': object,
    'content_rating': object,
    'number_ratings': int,
    'ratings_1': int,
    'ratings_2': int,
    'ratings_3': int,
    'ratings_4': int,
    'ratings_5': int,
    'price_currency': object,
    'price_numeric': float,
    'price': object,
    'iap': bool,
    'iap_min': float,
    'iap_max': float,
    'lang': object,  # List of language codes
    'similar': List[object],  # List of package names
    'from_developer': List[object],  # List of package names
    'badges': List[object],  # List of badges
    'interactive_elements': List[object],  # List of interactive elements
    'content_descriptors': List[object],  # List of content descriptors
    'contains_ads': bool,
    'age_approved_by_teachers': object,  # Age approved by teachers
    'i18n': dict,  # Object
    'app_availability': dict,  # Object
    'permissions': List[object],  # List of permissions
    'sdks': List[object],  # List of used sdks
    'physical_address': object,
    'email': object,  # Email
    'stores': dict  # Object
}
