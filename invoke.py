import requests

EVENT = """{
  "version": "2.0",
  "routeKey": "$default",
  "rawPath": "/",
  "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
  "cookies": [
    "cookie1",
    "cookie2"
  ],
  "headers": {
    "Header1": "value1",
    "Header2": "value1,value2"
  },
  "queryStringParameters": {
    "parameter1": "value1,value2",
    "parameter2": "value"
  },
  "requestContext": {
    "accountId": "123456789012",
    "apiId": "api-id",
    "authentication": {
      "clientCert": {
        "clientCertPem": "CERT_CONTENT",
        "subjectDN": "www.example.com",
        "issuerDN": "Example issuer",
        "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",
        "validity": {
          "notBefore": "May 28 12:30:02 2019 GMT",
          "notAfter": "Aug  5 09:36:04 2021 GMT"
        }
      }
    },
    "authorizer": {
      "jwt": {
        "claims": {
          "claim1": "value1",
          "claim2": "value2"
        },
        "scopes": [
          "scope1",
          "scope2"
        ]
      }
    },
    "domainName": "id.execute-api.us-east-1.amazonaws.com",
    "domainPrefix": "id",
    "http": {
      "method": "GET",
      "path": "/",
      "protocol": "HTTP/1.1",
      "sourceIp": "192.168.0.1/32",
      "userAgent": "agent"
    },
    "requestId": "id",
    "routeKey": "$default",
    "stage": "$default",
    "time": "12/Mar/2020:19:03:58 +0000",
    "timeEpoch": 1583348638390
  },
  "body": "eyJ0ZXN0IjoiYm9keSJ9",
  "pathParameters": {
    "parameter1": "value1"
  },
  "isBase64Encoded": true,
  "stageVariables": {
    "stageVariable1": "value1",
    "stageVariable2": "value2"
  }
}"""

FASTAPI_MANGUM_URL = ""
HTTP_API_LAMBDA_URL = ""


# invoke both lambdas 100 times
for i in range(0, 100):
    response = requests.get(HTTP_API_LAMBDA_URL, data=EVENT)
    print(f"http-api-lambda: status code: {response.status_code}, response: {response.text}")

    response = requests.get(FASTAPI_MANGUM_URL, data=EVENT)
    print(f"fastapi-mangum: status code: {response.status_code}, response: {response.text}")