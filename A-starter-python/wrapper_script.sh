#!/bin/bash

# Start the first process
python ./myproject/amqp_adapter_one/main.py --mode=prod &

# Start the second process
python ./myproject/grpc_adapter_one/main.py --mode=prod &

python ./myproject/rest_adapter_one/main.py --mode=prod &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?