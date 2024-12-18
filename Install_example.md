# Example Install

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





