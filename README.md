# MINIO_S3
MinoIO S3 Bucket bucket information

Use this for documentation on how how to install, test, and use MinIO software.
MinIO is an lightweight, high-performance, S3 compatible object store, and is open sourced.

OpenIO for Linux and Windows can be found here: 
https://github.com/minio/minio
https://github.com/minio/minio.git

### Features:
* S3-compatible API.
* Easy setup and single-node support.
* Supports encryption, versioning, and other advanced S3 features.
* Web UI for management.


# Install for Linux:
* MinIO provides a simple binary that can be run directly on Linux.
* It supports Docker, Kubernetes, and standalone installations.

### Step 1. Download MinIO binary
```bash
wget https://dl.min.io/server/minio/release/linux-amd64/minio
```
```bash
chmod +x minio
```
### Step 2. Run MinIO (defaults to port 9000)
```bash
./minio server /data
```
#### Install Example Link:
https://github.com/yen5004/MINIO_S3/blob/3ed5d962a5c454a1b10107bd31d2eac827a39417/Install_example.md


### Step 3. Install CLI MINIO
In this example the bucket name is **`pocbucket`**
Sample of install found here: https://github.com/yen5004/MINIO_S3/blob/da468ded2ca6f20f92da54f8c59470799a846372/Sample_CLI_Install.md

```bash
wget https://dl.min.io/client/mc/release/linux-amd64/mc
```
```bash
chmod +x mc
```
Put in path:
```bash
sudo mv mc /usr/local/bin/mc
```

### Step 4: Configure MinIO Client (mc)
After installing the mc client, you need to configure it to point to your MinIO server.
Set alias
```bash
mc alias set myminio http://localhost:9000 YOUR_ACCESS_KEY YOUR_SECRET_KEY
```
Configure MinIO Client with your MinIO server endpoint (replace YOUR_ACCESS_KEY and YOUR_SECRET_KEY with the credentials you set when running MinIO):
* myminio: The alias you're giving to this MinIO instance.
* http://localhost:9000: Replace this with your MinIO server URL if it's running on a different machine or port.
* YOUR_ACCESS_KEY and YOUR_SECRET_KEY: These should match the credentials you set up when you started the MinIO server.

### Step 5: Test Your Bucket (pocbucket)
Once mc is configured, you can test the bucket by running a few commands.

1. **List Buckets:** Verify that your pocbucket exists and can be accessed:
```bash
mc ls myminio
```
This will list all buckets in your MinIO instance. Ensure that pocbucket appears in the list.

2. **Check Bucket Status:** To check if your specific bucket pocbucket exists and is accessible:
```bash
mc ls myminio/pocbucket
```
If the bucket exists, this will list the contents of **`pocbucket`**

3. **Upload a Test File:** To test uploading an object into pocbucket, create a simple text file (e.g., test.txt), and upload it to the bucket:
Create test file:
```bash
echo "This is a test file" > test.txt
```
Copy test file into bucket:
```bash
mc cp test.txt myminio/pocbucket/
```
This will upload test.txt into pocbucket.

4. **Verify the Upload:** After uploading, list the contents of the bucket to ensure the file was successfully uploaded:
```bash
mc ls myminio/pocbucket
```
You should see the *`test.txt`* file listed.

5. **Download the File to Verify:** To further verify that the file was uploaded correctly, you can download the file back from the bucket:
Download file from bucket onto local host:
```bash
mc cp myminio/pocbucket/test.txt ./downloaded_test.txt
```
Then check the contents of the downloaded file:
```bash
cat downloaded_test.txt
```







