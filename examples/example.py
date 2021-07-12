from pathlib import Path
import json
from pprint import pprint
import os
import base64
from time import sleep
from datetime import datetime, timedelta

# Pip installed Modules
from frdgrpc import FaradayClient
from protobuf_to_dict import protobuf_to_dict

credential_path = Path("/home/skorn/.faraday/mainnet")

mac = str(credential_path.joinpath("faraday.macaroon").absolute())
tls = str(credential_path.joinpath("tls.cert").absolute())


frd = FaradayClient(
	"127.0.0.1:8465",
	macaroon_filepath=mac,
	cert_filepath=tls
)

frd.channel_insights()