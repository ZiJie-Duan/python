
def simple_generator():
    received = yield "Hello"
    received2 = yield
    yield f"World {received + received2}"

gen = simple_generator()
print(next(gen))  # 输出 "Hello"

response = gen.send("from the caller")
print(response)  # 输出 "World from the caller"

input()