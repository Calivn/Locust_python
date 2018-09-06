from locust import HttpLocust, TaskSet, task, events
import requests, time


class WebsiteTasks(TaskSet):
    @task
    def saveForm(self):
        start_time = time.time()
        response = self.client.post("/bookstore/phone/Index/saveForm.json", {
            "nickname": "abc1133",
            "tag": "dull",
            "answers": "abc",
            "book": "dull",
            "analysis": "abc",
            "comment": "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
        })
        total_time = int((time.time() - start_time) * 1000)
        if response.status_code != 200:
            events.request_failure.fire(request_type="Custom", name="test", response_time=total_time,
                                        exception=response.status_code)


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://118.178.178.1"
    min_wait = 1000
    max_wait = 5000
