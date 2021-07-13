from pathlib import Path
import json
from pprint import pprint
import os
import base64
from time import sleep
from datetime import datetime, timedelta

# Pip installed Modules
from frdgrpc import FaradayClient
from frdgrpc.client import faradayrpc
from protobuf_to_dict import protobuf_to_dict

credential_path = Path("/home/skorn/.faraday/mainnet")

mac = str(credential_path.joinpath("faraday.macaroon").absolute())
tls = str(credential_path.joinpath("tls.cert").absolute())


frd = FaradayClient(
	"127.0.0.1:8465",
	macaroon_filepath=mac,
	cert_filepath=tls
)


# Example commands
frd.channel_insights()

frd.close_report(channel_point="abcd1234:1")

frd.exchange_rate(timestamps=[1626115601,1523115601,1426115601],granularity=8,fiat_backend=2)

frd.node_audit(
    end_time=int(datetime.now().timestamp()),
    start_time=int((datetime.now()-timedelta(days=60)).timestamp())
)

frd.outlier_recommendations(
    outlier_multiplier=1,
    rec_request=faradayrpc.CloseRecommendationRequest(minimum_monitored=10000,metric=5)
)