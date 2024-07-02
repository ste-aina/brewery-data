import requests
import json
import boto3
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter as credenciais da AWS das variáveis de ambiente
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

def extract_brewery_data(s3_bucket_name, s3_prefix="brewery_data/"):
    """
    Extracts brewery data from Open Brewery DB API with pagination and saves to S3.

    Args:
        s3_bucket_name (str): Name of the S3 bucket to store the data.
        s3_prefix (str, optional): Prefix for S3 object keys within the bucket. Defaults to "brewery_data/".
    """
    api_url = "https://api.openbrewerydb.org/breweries"
    page = 1
    all_data = []

    while True:
        # Construct URL with page parameter
        paginated_url = f"{api_url}?page={page}"
        response = requests.get(paginated_url)

        if response.status_code == 200:
            try:
                # Request successful, process data
                data = response.json()
                if not data:
                    break  # No data on this page, signifies end of results
                all_data.extend(data)
                page += 1  # Move to next page
            except json.JSONDecodeError:
                print(f"Error decoding JSON for page {page}.")
                break
        else:
            # Handle error
            print(f"API request failed: {response.status_code}")
            break  # Stop processing on error

    if all_data:
        # Save data to a local file first
        local_filename = f"breweries_data.json"
        with open(local_filename, "w") as outfile:
            json.dump(all_data, outfile)
        print(f"Data saved locally to {local_filename}")

        # Upload to S3
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        s3_filename = f"{s3_prefix}breweries_data.json"  # Use a single file for all data
        s3_client.upload_file(local_filename, s3_bucket_name, s3_filename)
        print(f"Extracted data saved to S3: {s3_filename}")

        # Remove the local file after uploading to S3
        os.remove(local_filename)
    else:
        print("No data extracted.")

# S3 bucket name
s3_bucket_name = "abinbev-raw-brewery-data"
extract_brewery_data(s3_bucket_name)
