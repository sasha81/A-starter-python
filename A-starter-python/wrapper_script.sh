#!/bin/bash

# Start the first process
python ./src/amqp_adapter_one/main.py --mode=prod

# Start the second process
#python ./src/grpc_adapter_one/main.py --mode=prod &
#
#python ./src/rest_adapter_one/main.py --mode=prod &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?