# pool-grpc-client
A python grpc client for Lightning Pool (Lightning Network Daemon) ⚡⚡⚡

This is a wrapper around the default grpc interface that handles setting up credentials (including macaroons.

## Dependencies
- Python 3.6+
- Working LND lightning node, take note of its ip address.
- Copy your pool.macaroon and tls.cert files from `~/.pool/mainnet` to a directoy on your machine. 


## Installation
```bash
# NOT ON PYPI YET
pip install pool-grpc-client
```




## Basic Usage
The api mirrors the underlying lnd grpc api (http://api.lightning.community/) but methods will be in pep8 style. ie. `.GetInfo()` becomes `.get_info()`.

```python
from pathlib import Path
import json
from poolgrpc.client import PoolClient

credential_path = Path("/home/skorn/.pool/mainnet/")

mac = str(credential_path.joinpath("pool.macaroon").absolute())
tls = str(credential_path.joinpath("tls.cert").absolute())

pool = PoolClient(
	macaroon_filepath=mac,
	cert_filepath=tls
)

pool.get_info()

pool.get_lsat_tokens()
```

### Specifying Macaroon/Cert files
By default the client will attempt to lookup the `readonly.macaron` and `tls.cert` files in the mainnet directory. 
However if you want to specify a different macaroon or different path you can pass in the filepath explicitly.

```python
lnd = LNDClient(
    macaroon_filepath='~/.lnd/invoice.macaroon', 
    cert_filepath='path/to/tls.cert'
)
```

## Generating LND Proto Files
```bash
virtualenv lnd
source lnd/bin/activate
pip install grpcio grpcio-tools googleapis-common-protos sh
git clone https://github.com/lightningnetwork/lnd.git
mkdir genprotos
git clone https://github.com/googleapis/googleapis.git

# python -m grpc_tools.protoc --proto_path=googleapis:. --python_out=. --grpc_python_out=. rpc.proto
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