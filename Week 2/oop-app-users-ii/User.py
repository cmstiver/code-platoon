class User():
    def __init__(self, name, email, license_num):
        self.name = name
        self.email = email
        self.license_num = license_num
        self.posts = []

    def post(self, message):
        self.posts.append(message)
        return

    def del_post(self, message):
        try:
            self.posts.remove(message)
        except:
            print("Input invalid.")


jane = User("Jane", "jane@email.com", "1234")
josh = User("Josh", "jane@email.com", "1234")


print(jane.posts)

jane.post("A message")

print(jane.posts)

print(josh.posts)

jane.del_post('A message')

print(jane.posts)
