
const Minio = require('minio');

// Set up MinIO Client 
const minioClient = new Minio.Client({
  endpoint: 'http://localhost',
  port: 9000,
  useSSL: false,
  accessKey: 'minioadmin',
  secretKey: 'minioadmin',
  s3ForcePathStyle: true,  // Needed for MinIO
  signatureVersion: 'v4'
});

// List all buckets in your MinIO server
minioClient.listBuckets(function (err, buckets) {
  if (err) {
    return console.log('Error listing buckets:', err);
  }

  console.log('Buckets:');
  buckets.forEach(bucket => {
      console.log(bucket.name);
 });
});

## ensure this module is installed:
## npm install -g minio
