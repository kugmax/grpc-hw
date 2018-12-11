import grpc
from concurrent import futures
import time

import calculator_pb2_grpc, calculator_pb2
import calculator


class CalculatorService(calculator_pb2_grpc.CalculatorServicer):
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)

    print("Starting server. Listening on port 50051")
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)