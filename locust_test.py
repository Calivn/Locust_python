from locust import Locust, events, task, TaskSet
import websocket,time


class WebSocketClient():
    def __init__(self, host, port):
        self.host = host
        self.port = port


class WebSocketLocust(Locust):
    def __init__(self, *args, **kwargs):
        self.client = WebSocketClient("smile.gljava.com", 80)


class UserBehavior(TaskSet):
    def on_start(self):
        self.ws = websocket.WebSocket()
        self.ws.connect(
            "ws://smile.gljava.com/ws?deviceCode=WEF0VEdjOXp2Q0MrR3FCUkpQRVBmZHowWDhrejlvYzZKYWpKalBmRnVrND0=")

    @task(1)
    def send(self):
        try:
            start_time = time.time()
            self.ws.send('{"actionCode":0}')
            result = self.ws.recv()
        except xmlrpclib.Fault as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="tcp", name="send", response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="tcp", name="send", response_time=total_time,
                                        response_length=0)


class ApiUser(TcpLocust):
    min_wait = 1000
    max_wait = 2000

    task_set = UserBehavior
