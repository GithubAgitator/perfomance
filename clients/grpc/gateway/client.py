from grpc import Channel, insecure_channel, intercept_channel
from clients.grpc.interceptors.locust_interceptor import LocustInterceptor
from locust.env import Environment

def build_gateway_grpc_client()-> Channel:
    return insecure_channel("localhost:9003")

def build_gateway_locust_grpc_client(enviroment: Environment)-> Channel:
    locust_interception = LocustInterceptor(environment=enviroment)
    channel = insecure_channel("localhost:9003")
    return intercept_channel(channel, locust_interception)

