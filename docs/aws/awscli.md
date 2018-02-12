Aws cli Common Use
==================

# lambda 
查询 lambda

    [work@iz624k8ymw3z.airdb.com ~]$ aws lambda  list-functions --query Functions[].FunctionName
    [
        "Hello", 
        "HelloGo"
    ]


上传代码

    [work@iz624k8ymw3z.airdb.com ~] go build main.go
    [work@iz624k8ymw3z.airdb.com ~] zip main.zip main
    [work@iz624k8ymw3z.airdb.com ~]$ aws lambda   update-function-code  --function-name HelloGo --zip-file fileb://main.zip


执行 lambda

    [work@iz624k8ymw3z.airdb.com ~]$ aws lambda invoke --function-name HelloGo   lambda.log

模板合法性检查

    aws cloudformation  validate-template --template-body  file://relay.template 


创建 cloudformation

    aws cloudformation  create-stack --stack-name relay   --template-body  file://relay.template
    aws cloudformation  create-stack --stack-name relay   --template-url  https://s3.amazonaws.com/airdb.me/aws/cloudformation/relay.template

更新 stack
    aws cloudformation  update-stack  --stack-name  relay  --template-body  file://relay.template

查看 stack 部署的资源

    aws cloudformation   list-stack-resources   --stack-name   relay
