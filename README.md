# MINIO_S3
MinoIO S3 Bucket bucket information

Use this for documentation on how how to install, test, and use MinIO software.
MinIO is an lightweight, high-performance, S3 compatible object store, and is open sourced.

OpenIO for Linux and Windows can be found here: 
https://github.com/minio/minio
https://github.com/minio/minio.git

## Features:
* S3-compatible API.
* Easy setup and single-node support.
* Supports encryption, versioning, and other advanced S3 features.
* Web UI for management.

## Install for linux:
* MinIO provides a simple binary that can be run directly on Linux.
* It supports Docker, Kubernetes, and standalone installations.

### Download MinIO binary
```bash
wget https://dl.min.io/server/minio/release/linux-amd64/minio
```
```bash
chmod +x minio
```
### Run MinIO (defaults to port 9000)
./minio server /data

#### Example Install
```bash
root@ip-10-10-120-245:~# wget https://dl.min.io/server/minio/release/linux-amd64/minio
--2024-12-18 12:34:39--  https://dl.min.io/server/minio/release/linux-amd64/minio
Resolving dl.min.io (dl.min.io)... 178.128.69.202, 138.68.11.125
Connecting to dl.min.io (dl.min.io)|178.128.69.202|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 115691672 (110M) [application/octet-stream]
Saving to: \u2018minio\u2019

minio               100%[===================>] 110.33M  18.6MB/s    in 7.1s    

2024-12-18 12:34:47 (15.5 MB/s) - \u2018minio\u2019 saved [115691672/115691672]

root@ip-10-10-120-245:~# ls
burp.json   Downloads     new       Rooms    thinclient_drives
CTFBuilder  Instructions  Pictures  Scripts  Tools
Desktop     minio         Postman   snap
root@ip-10-10-120-245:~# sudo chmod +x minio
root@ip-10-10-120-245:~# ./minio server /data
INFO: Formatting 1st pool, 1 set(s), 1 drives per set.
INFO: WARNING: Host local has more than 0 drives of set. A host failure will result in data becoming unavailable.
MinIO Object Storage Server
Copyright: 2015-2024 MinIO, Inc.
License: GNU AGPLv3 - https://www.gnu.org/licenses/agpl-3.0.html
Version: RELEASE.2024-12-13T22-19-12Z (go1.23.4 linux/amd64)

API: http://10.10.120.245:9000  http://172.17.0.1:9000  http://127.0.0.1:9000 
   RootUser: minioadmin 
   RootPass: minioadmin 

WebUI: http://10.10.120.245:39325 http://172.17.0.1:39325 http://127.0.0.1:39325      
   RootUser: minioadmin 
   RootPass: minioadmin 

CLI: https://min.io/docs/minio/linux/reference/minio-mc.html#quickstart
   $ mc alias set 'myminio' 'http://10.10.120.245:9000' 'minioadmin' 'minioadmin'

Docs: https://docs.min.io
WARN: Detected default credentials 'minioadmin:minioadmin', we recommend that you change these values with 'MINIO_ROOT_USER' and 'MINIO_ROOT_PASSWORD' environment variables
```






## Install CLI MINIO
In this example the bucket name is **`pocbucket`**

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

#### Step 2: Configure MinIO Client (mc)
After installing the mc client, you need to configure it to point to your MinIO server.
Set alias
```bash
mc alias set myminio http://localhost:9000 YOUR_ACCESS_KEY YOUR_SECRET_KEY
```
Configure MinIO Client with your MinIO server endpoint (replace YOUR_ACCESS_KEY and YOUR_SECRET_KEY with the credentials you set when running MinIO):
* myminio: The alias you're giving to this MinIO instance.
* http://localhost:9000: Replace this with your MinIO server URL if it's running on a different machine or port.
* YOUR_ACCESS_KEY and YOUR_SECRET_KEY: These should match the credentials you set up when you started the MinIO server.

#### Step 3: Test Your Bucket (pocbucket)
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

5. *Download the File to Verify:* To further verify that the file was uploaded correctly, you can download the file back from the bucket:
Download file from bucket onto local host:
```bash
mc cp myminio/pocbucket/test.txt ./downloaded_test.txt
```
Then check the contents of the downloaded file:
```bash
cat downloaded_test.txt
```

### Install CLI MINIO Example:
```bash
root@ip-10-10-120-245:~# wget https://dl.min.io/client/mc/release/linux-amd64/mc
--2024-12-18 14:24:20--  https://dl.min.io/client/mc/release/linux-amd64/mc
Resolving dl.min.io (dl.min.io)... 138.68.11.125, 178.128.69.202
Connecting to dl.min.io (dl.min.io)|138.68.11.125|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 27996312 (27M) [application/octet-stream]
Saving to: \u2018mc\u2019

mc                  100%[===================>]  26.70M  8.69MB/s    in 4.5s    

2024-12-18 14:24:25 (5.87 MB/s) - \u2018mc\u2019 saved [27996312/27996312]

root@ip-10-10-120-245:~# chmod +x mc
root@ip-10-10-120-245:~# sudo mv mc /usr/local/bin/mc
root@ip-10-10-120-245:~# mc alias set myminio http://localhost:9000 CicOiKxCxrYDMrFW6S6V jIKrv8Pz7nBJJWyx3oW4pKbHeiIZQtp44Aeml2kl
Added `myminio` successfully.
root@ip-10-10-120-245:~# mc ls myminio
[2024-12-18 12:38:18 GMT]     0B pocbucket/
root@ip-10-10-120-245:~# echo "This is a test file" > test.txt
root@ip-10-10-120-245:~# mc cp test.txt myminio/pocbucket/
...t/test.txt: 20 B / 20 B \u2503\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2503 1.06 KiB/s 0sroot@ip-10-10-120-245:~# mc ls myminio
[2024-12-18 12:38:18 GMT]     0B pocbucket/
root@ip-10-10-120-245:~# mc ls myminio/pocbucket
[2024-12-18 14:26:41 GMT]    20B STANDARD test.txt
[2024-12-18 12:43:01 GMT]    15B STANDARD testfile.txt
root@ip-10-10-120-245:~# mc cp myminio/pocbucket/test.txt ./downloaded_test.txt
...t/test.txt: 20 B / 20 B \u2503\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2503 1.10 KiB/s 0sroot@ip-10-10-120-245:~# cat downloaded_test.txt 
This is a test file
root@ip-10-10-120-245:~# 
```





