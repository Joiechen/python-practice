import json

class Account(object):
    num_accounts = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    def del_account(self):
        Account.num_accounts -= 1

    def deposit(self, amt):
        self.balance = self.balance + amt

    def withdraw(self, amt):
        self.balance = self.balance - amt

    def inquiry(self):
        return "Name={}, balance={}".format(self.name, self.balance)

    @classmethod
    def from_json(cls, params_json):
        params = json.loads(params_json)
        return cls(params.get("name"), params.get("balance"))

    @staticmethod
    def type():
        return "Current Account"

if __name__ == '__main__':
    acct = Account("obi", 10)
    print(acct.inquiry())