# new

[コンピュータ上で DynamoDB をローカルでデプロイする \- Amazon DynamoDB](https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)

[【DynamoDB Local】快適なDynamoDBのローカル開発環境を構築する – Hacker's High](https://hackers-high.com/aws/dynamodb-local-development/)

[コンテナ利用者に捧げる AWS Lambda の新しい開発方式 \! \- 変化を求めるデベロッパーを応援するウェブマガジン \| AWS](https://aws.amazon.com/jp/builders-flash/202103/new-lambda-container-development/?awsf.filter-name=*all)


[AWS Lambda の新機能 – コンテナイメージのサポート \| Amazon Web Services ブログ](https://aws.amazon.com/jp/blogs/news/new-for-aws-lambda-container-image-support/)

## local without dynamodb

```
docker build -t sampleapp:0.1.0 .
docker run -p 9000:8080 sampleapp:0.1.0
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

## use docker-compose

```
docker-compose --build
```

```
aws dynamodb create-table --cli-input-json file://user.json  --endpoint-url http://localhost:8000
```