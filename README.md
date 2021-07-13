# faraday-grpc-client
A python grpc client for LL Faraday (Node Stats)

This is a wrapper around the default grpc interface that handles setting up credentials (including macaroons.

## Dependencies
- Python 3.6+
- Working LND lightning node, take note of its ip address.
- Copy your pool.macaroon and tls.cert files from `~/.faraday/mainnet` to a directoy on your machine. 


## Installation
```bash
pip install faraday-grpc-client
```

## Generating LND Proto Files
```bash
virtualenv lnd
source lnd/bin/activate
pip install grpcio grpcio-tools googleapis-common-protos sh
git clone https://github.com/lightningnetwork/lnd.git
mkdir genprotos
git clone https://github.com/googleapis/googleapis.git

python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. frdgrpc/compiled/*.proto
```

```python
from pathlib import Path
import shutil
import sh

for proto in list(Path("../lnd/lnrpc").rglob("*.proto")):
    shutil.copy(proto, Path.cwd())

protos = list(Path(".").glob("*.proto"))

for protofile in protos:
    try:
        sh.python("-m", "grpc_tools.protoc", "--proto_path=.", "--python_out=.", "--grpc_python_out=.", str(protofile))
        protos.remove(protofile)
    except Exception as e:
        print(f"Error in proto: {protofile}")
```

Last Step:
In File: verrpc_pb2_grpc.py
Change:
import verrpc_pb2 as verrpc__pb2
To:
from lndgrpc import verrpc_pb2 as verrpc__pb2

## Deploy to Test-PyPi
```bash
poetry build
twine check dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```