from boto import connect_s3
from disco.comm import open_url


def input_stream(fd, size, url, params):
    """Opens the url locally on the node."""
    assert url.startswith('s3://')
    bucketname, keyname = url[5:].split('/', 1)
    access_key = params.get('aws_access_key_id')
    secret_key = params.get('aws_secret_access_key')
    s3 = connect_s3(access_key, secret_key)
    bucket = s3.get_bucket(bucketname, validate=False)
    key = bucket.get_key(keyname)
    url = key.generate_url(500)
    return open_url(url), key.size, url
