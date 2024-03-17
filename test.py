import requests

def search_incident_address(partial_address):
    url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
    params = {
        "$where": f"incident_address like '%{partial_address}%'"
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data:
        incidents = [{'full_address': record['incident_address'], 'descriptor': record.get('descriptor', 'N/A')} for record in data if 'incident_address' in record]
        return incidents
    else:
        return []

# Usage
partial_address = input("Enter partial incident address: ")
incidents = search_incident_address(partial_address)
if incidents:
    for incident in incidents:
        print("Full Incident Address:", incident['full_address'])
        print("Descriptor:", incident['descriptor'])
else:
    print("No matching incident address found.")