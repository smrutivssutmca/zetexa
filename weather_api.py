import requests
import json

cities = ["Hyderabad", "Mumbai", "Delhi"]


def fetch_weather(city):
    try:
        response = requests.get(f"http://api.weatherapi.com/v1?q={city}", timeout=5)
        response.raise_for_expection()
        data = response.json()
    except Exception as e:
        print("Error occured while fetching the response")
        
    return {
        "city": data["city"]
        "temperature": data["temperature"]
        "humidity": data["humidity"]
    }
    
    
def save_json_data(cities):
    result = []
    
    for city in cities:
        data = fetch_weather(city)
        
        if data:
            result.append(data)
            
    try:
        with open("result.json", "w") as file:
            json.dumps(result, file, indent=4)
    except Exception as e:
        print("Error occured while writing the file : ", str(e))
            
            
            
            
            
            
            
            
            
            
            
    
    
