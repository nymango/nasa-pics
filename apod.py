import os
import sys
import requests
from datetime import date 

NASA_APOD_URL = "https://api.nasa.gov/planetary/apod" #APOD API endpoint

def get_apod(api_key: str, apod_date: str | None = None) -> dict:
    """Fetch the Astronomy Picture of the Day (APOD) data from NASA's API.
    """
    params = {
        "api_key": api_key
    }
    if apod_date:
        params["date"] = apod_date
    response = requests.get(NASA_APOD_URL, params=params, timeout=30)
    response.raise_for_status() 
    return response.json()

def download_file(url: str, out_path: str) -> None:
    # Download the file from the given URL and save it to the specified path    
    with requests.get(url, stream=True, timeout=30)
        r.raise_for_status()
        with open(out_path,"wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
def main():
    api_key = os.getenv("NASA_API_KEY")
    if not api_key:
        print("Error: NASA_API_KEY environment variable not set.")
        sys.exit(1)

