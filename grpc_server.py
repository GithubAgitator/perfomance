import grpc
from concurrent import futures
import greeting_pb2
import greeting_pb2_grpc


class GreeterServicer(greeting_pb2_grpc.GreeterServicer):
    def SayHello(self, request: greeting_pb2.HelloRequest, context):
        name = request.name
        message = f"Hello {name}!"
        return greeting_pb2.HelloReply(message=message)


def serve():
    # Создаём gRPC-сервер с пулом потоков на 10 воркеров
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Регистрируем наш сервис на сервере
    greeting_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

    # Назначаем порт, на котором будет слушать сервер
    server.add_insecure_port('[::]:50051')  # [::] — для IPv4/IPv6

    print("Запуск сервера на порту 50051...")
    server.start()  # Запуск сервера
    server.wait_for_termination()  # Ожидание завершения (бесконечно)


if __name__ == '__main__':
    serve()
