import httpx

files = {"file": ("example.txt", open("example.txt", "rb"))}

response = httpx.post("https://httpbin.org/post", files=files)

print(response.json())


client = httpx.Client(
    base_url="https://jsonplaceholder.typicode.com",
    headers={"Autorization": "Bear my secret token"}
)
response1 = client.get("/todos/1")
response2 = client.get("/todos/2")

print(response1.json())  # Данные первой задачи
print(response2.json())  # Данные второй задачи