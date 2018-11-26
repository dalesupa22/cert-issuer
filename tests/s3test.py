import boto3
BUCKET = 'testingxertify'
BUCKETB = 'testingxertify'
KEY = 'certis/54ebe810-348b-473a-b75f-683110cdf0ba.json'
client = boto3.client('s3',
                       aws_access_key_id='AKIAJVVK23KJOVIUXJ5Q',
                       aws_secret_access_key='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'
                     )

stringPath = "certis/" + "egge"+ ".json"
print(stringPath)
print("hello")
result = client.get_object(Bucket=BUCKET, Key=KEY)
# Read the object (not compressed):
client.put_object(Bucket='testingxertify',Key='newone/danny.json', Body=result["Body"].read())
text = result["Body"].read().decode()
print(text)



keys = []
resp = client.list_objects_v2(Bucket=BUCKETB, Prefix='certis')
for obj in resp['Contents']:
    keys.append(obj['Key'])
print(keys)



#client.upload_file('/Users/SUAPA/Documents/oigamGetAllRecords.json','certisResults')
#client.upload_fileobj(result["Body"].read(), '/testingxertify/newone/', 'newone.json')
client.put_object(Bucket='testingxertify',Key='newone/newone.json', Body=result["Body"].read())