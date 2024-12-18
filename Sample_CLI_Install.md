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
