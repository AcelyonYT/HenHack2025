import requests

def search_providers(postal_code:str, taxonomy_description:str):
    """
    Searches for providers using the NPPES API given a postal_code and taxonomy description.
    """
    url = "https://npiregistry.cms.hhs.gov/api/"
    params = {
        "version": "2.1",
        "postal_code": postal_code,
        "taxonomy_description": taxonomy_description,
    }
    try:
        response = requests.get(url, params=params)
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
        provider_list = []
        for prov in data["results"]:
            basic_info = prov.get("basic", {})
            first_name = basic_info.get("first_name", "Not available")
            last_name = basic_info.get("last_name", "Not available")
            full_name = f"{first_name} {last_name}".strip()
            if not full_name.strip():
                continue  # Skip if name is not available

            addresses = prov.get("addresses", [])
            if addresses:
                primary = addresses[0]
                address_line = primary.get("address_1", "Not available")
                city_addr = primary.get("city", "Not available")
                state_addr = primary.get("state", "Not available")
                postal_code = primary.get("postal_code", "Not available")
                telephone_number = primary.get("telephone_number", "Not available")
                location_info = f"{address_line}, {city_addr}, {state_addr} {postal_code}"
            else:
                location_info = "No address provided."
                telephone_number = "Not available"

            email = "Not available"
            if prov.get("endpoints"):
                email = prov["endpoints"][0].get("endpoint", "Not available")
            provider_info = f"""
            Name: {full_name} Location: {location_info}  Phone: {telephone_number} Email: {email}
            """
            provider_list.append(provider_info.strip())
            
        # Join the provider list into one big string with new lines
        provider_string = "\n\n".join(provider_list)
        return provider_string

# Example usage
if __name__ == "__main__":
    providers = get_healthcare_info("16870", "Gastroenterology")
    print(providers)