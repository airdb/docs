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