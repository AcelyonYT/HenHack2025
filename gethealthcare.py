import requests

def search_providers(postal_code, taxonomy_description, limit=10):
    """
    Searches for providers using the NPPES API given a postal_code and taxonomy description.
    """
    url = "https://npiregistry.cms.hhs.gov/api/"
    params = {
        "version": "2.1",
        "postal_code": postal_code,
        "taxonomy_description": taxonomy_description,
        "limit": limit
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code.
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
def get_healthcare_info(location, taxonomy):
    """
    Get healthcare provider information based on location and taxonomy.
    """
    data = search_providers(location, taxonomy)
    if data and "results" in data and data["results"]:
        providers = []
        for provider in data["results"]:
            basic_info = provider.get("basic", {})
            first_name = basic_info.get("first_name", "")
            last_name = basic_info.get("last_name", "")
            full_name = f"{first_name} {last_name}".strip()
            # print(basic_info)
            addresses = provider.get("addresses", [])
            # print(data)
            if addresses:
                primary = addresses[0]
                address_line = primary.get("address_1", "")
                city_addr = primary.get("city", "")
                state_addr = primary.get("state", "")
                postal_code = primary.get("postal_code", "")
                location_info = f"{address_line}, {city_addr}, {state_addr} {postal_code}"
            else:
                location_info = "No address provided."
            
            provider_info = {
                "name": full_name,
                "location": location_info
            }
            providers.append(provider_info)
            return providers
    
# Example usage
if __name__ == "__main__":
    providers=get_healthcare_info("16870", "Family Medicine")
    for i in providers:
        print(i)