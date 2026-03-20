import requests
import os

def download_latest_release(owner, repo, asset_name=None, save_dir="."):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    assets = data.get("assets", [])

    if not assets:
        raise Exception("No assets found in the latest release.")
    
    if asset_name:
        asset = next((a for a in assets if a["name"] == asset_name), None)
        if not asset:
            raise Exception(f"Asset '{asset_name}' not found.")
    else:
        asset = assets[0]

    download_url = asset["browser_download_url"]
    filename = asset["name"]
    filepath = os.path.join(save_dir, filename)
    print(f"Downloading {filename}...")

    with requests.get(download_url, stream=True) as r:
        r.raise_for_status()
        with open(filepath, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    print(f"Saved to: {filepath}")