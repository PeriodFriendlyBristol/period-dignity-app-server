import requests


def postcode_to_coordinates(postcode):
    """Converts a postcode to latitude, longitude using an external API.
    :param postcode: A valid UK postcode
    :type postcode: str
    :return: Latitude and longitude in a list of that order
    :rtype: list
    """
    # Pull postcode from the query and find the coordinates.
    response = requests.get(f"http://api.getthedata.com/postcode/{data['postcode']}").json()
    if "error" in response:
        raise ValueError(response["error"])

    # Ensure the response has the necessary data.
    if "data" not in response:
        raise KeyError("Key 'data' missing from postcode lookup API")
    for key in ["latitude", "longitude"]:
        if key not in response["data"]:
            raise KeyError(f"Key 'data.{key}' missing from postcode lookup API")

    # Pull coordinates from the response.
    return [float(response["data"]["latitude"]), float(response["data"]["longitude"])]
