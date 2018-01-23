from locust import HttpLocust,TaskSet

def login(l):
    l.client.post("/doLogin.htm",{
        "username":"hhhhkkk",
        "password":"123123qq",
        "captcha" :""
    })

def index(l):
    l.client.get("/index.htm")

def userhome(l):
    l.client.get("/userHome.htm")

class UserBehavior(TaskSet):
    tasks = {login:1,userhome:2}

    def on_start(self):
        index(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000