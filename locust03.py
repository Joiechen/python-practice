from locust import HttpLocust,TaskSet,task

class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post("/doLogin.htm",{
        "username":"hhhhkkk",
        "password":"123123qq",
        "captcha" :""
    })

    @task(2)
    def index(self):
        self.client.get("")