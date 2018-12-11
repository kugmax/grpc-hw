pip install grpcio <br />
pip install grpcio-tools <br />
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto <br />
