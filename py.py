from minio import Minio
from minio.error import ResponseError

client = Minio('192.168.38.230:9000',
                access_key='1234567890',
                secret_key='1234567890',
                secure=False)

try:
    response = client.get_partial_object('data2_test', 'test (1).jpg', 1000)
    file = open("test_fixed2.jpg", "w")
    file.write(response.read())
    file.close()
except ResponseError as err:
    print(err)
