# A-starter-python
Here are instructions to launch the python part of the starter, described in [this paper](https://dzone.com/articles/a-starter-for-a-distributed-multi-language-analyti).
## PyCharm
### Install dependencies
+ Open file `requirements.txt` in the `A-starter-python` folder. Then click `install dependencies`.
+ In case PyCharm can't import project modules, run `pip install -e .` command.
+ For the gRPC app to work, run `python3 -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./protoc/api.proto`. Then copy the generated files `api_pb2.py` and `api_pb2_grpc.py` to the `grpc_adapter_one` folder. 
### Run configurations
The app follows hexagonal architecture. Every inbound adapter has its own `main.py` method and a PyCharm run configuration. These configurations are as follows.
#### AMQP
+ Name: AMQP
+ Script path: `<absolute-path-to-A-starter-python>/A-starter-python/src/amqp_adapter_one/main.py`,
+ Parameters: `--mode=develop`,
+ Environment variables: `PYTHONUNBAFFERED=1`,
+ Python interpreter: `Python 3.10 (A-starter-python)`,
+ Working directory: `<absolute-path-to-A-starter-python>/A-starter-python/src/amqp_adapter_one`,
+ Add content roots to PYTHONPATH: checked,
+ Add source roots to PYTHONPATH: checked,
+ Everything else is unchecked.
#### gRPC
+ Name: gRPC
+ Script path: `<absolute-path-to-A-starter-python>/A-starter-python/src/grpc_adapter_one/main.py`,
+ Parameters: `--mode=develop`,
+ Environment variables: `PYTHONUNBAFFERED=1;grpc.port=50001`,
+ Python interpreter: `Python 3.10 (A-starter-python)`,
+ Working directory: `<absolute-path-to-A-starter-python>.A-starter-python/src/grpc_adapter_one`,
+ Add content roots to PYTHONPATH: checked,
+ Add source roots to PYTHONPATH: checked,
+ Everything else is unchecked. 
#### GraphQL
+ Name: GraphQL
+ Script path: `<absolute-path-to-A-starter-python>/A-starter-python/src/graphql_adapter_one/main.py`,
+ Parameters: `--mode=develop`,
+ Environment variables: `PYTHONUNBAFFERED=1`,
+ Python interpreter: `Python 3.10 (A-starter-python)`,
+ Working directory: `<absolute-path-to-A-starter-python>/A-starter-python/src/graphql_adapter_one`,
+ Add content roots to PYTHONPATH: checked,
+ Add source roots to PYTHONPATH: checked,
+ Everything else is unchecked. 
#### Rest
+ Name: Rest
+ Script path: `<absolute-path-to-A-starter-python>/A-starter-python/src/rest_adapter_one/main.py`,
+ Parameters: `--mode=develop`,
+ Environment variables: `PYTHONUNBAFFERED=1`,
+ Python interpreter: `Python 3.10 (A-starter-python)`,
+ Working directory: `<absolute-path-to-A-starter-python>/A-starter-python/src/rest_adapter_one`,
+ Add content roots to PYTHONPATH: checked,
+ Add source roots to PYTHONPATH: checked,
+ Everything else is unchecked. 
## Docker
From `A-starter-main` (NOT `A-starter-python`!) folder, run `docker compose up python-app`.
