
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

print("\nListing blobs...")

# List the blobs in the container
blob_list = container_client.list_blobs()
for blob in blob_list:
    print("\t" + blob.name)