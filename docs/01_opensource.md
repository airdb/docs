Configuring sources
===================

First Header | Second Header | Third Header
:----------- | :-----------: | -----------:
Left         | Center        | Right
Left         | Center        | Right

They are specified in the command line via the `--source` flag. The flag takes an argument of the form `PREFIX:CONFIG[?OPTIONS]`.

## Current sources
### Kubernetes
To use the kubernetes source add the following flag:

	--source=kubernetes:<KUBERNETES_MASTER>[?<KUBERNETES_OPTIONS>]

```shell
cat <EOF | kubectl create -f -
apiVersion: v1
kind: ServiceAccount
metadata:
  name: heapster
EOF
```

This will generate a token on the API server. You will then need to reference the service account in your Heapster pod spec like this:

```yaml
apiVersion: "v1"
kind: "ReplicationController"
metadata:
  labels:
    name: "heapster"
  name: "monitoring-heapster-controller"
```
