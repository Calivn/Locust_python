from locust import HttpLocust, TaskSet, task,events
import requests,time,json


class WebsiteTasks(TaskSet):
    @task
    def saveForm(self):
        start_time = time.time()
        with self.client.post("/bookstore/phone/Index/saveForm.json", {
            "nickname": "abc11",
            "tag": "dull",
            "answers": "abc",
            "book": "dull",
            "analysis": "abc",
            "comment": "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
        }, catch_response=True) as response:
            ab = response.json().get('status')
            if ab != "True":
                response.success()


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://118.178.178.1"
    min_wait = 1000
    max_wait = 5000
