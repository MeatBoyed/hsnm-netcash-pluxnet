import xml.etree.ElementTree as ET

def extract_payment_url(response_xml: str) -> str:
    """
    Parses the SOAP XML response and extracts the payment URL.
    
    Args:
        response_xml (str): The SOAP response in XML format.
    
    Returns:
        str: The extracted payment URL or an empty string if not found.
    """
    try:
        root = ET.fromstring(response_xml)
        
        # Loop through payment methods
        for payment_method in root.findall(".//PaymentMethod"):
            type_element = payment_method.find("Type")
            if type_element is not None and type_element.text in ["CreditCard", "QR"]:
                # Extract the URL
                for entry in payment_method.findall(".//Entry"):
                    name = entry.find("Name")
                    value = entry.find("Value")
                    if name is not None and name.text == "Url":
                        return value.text

    except ET.ParseError as error:
        print("Error parsing XML response", error)

    return ""  # Return empty string if no URL is found
