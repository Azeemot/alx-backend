#!/usr/bin/env python3
"""
Main file
"""

class Server:
    def __init__(self):
        # Initialize your server here
        self.__indexed_dataset = {}  # Replace with your dataset initialization

    def indexed_dataset(self):
        # Implement your indexed_dataset method here
        pass

    def get_hyper_index(self, index: int = None, page_size: int = 10):
        # Modify the get_hyper_index method to accept index and page_size parameters
        # with default values
        if index is None:
            # Handle the case when index is not provided
            # Implement your logic here
            pass
        else:
            # Handle the case when index is provided
            # Implement your logic here
            pass

# Create an instance of the Server class
server = Server()

server.indexed_dataset()

try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print("AssertionError raised when out of range")

index = 3
page_size = 2

print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 1- request first index
res = server.get_hyper_index(index, page_size)
print(res)

# 2- request next index
print(server.get_hyper_index(res.get('next_index'), page_size))

# 3- remove the first index
del server._Server__indexed_dataset[res.get('index')]
print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 4- request again the initial index -> the first data retrieves are not the same as the first request
print(server.get_hyper_index(index, page_size))

# 5- request again initial next index -> same data page as the request 2-
print(server.get_hyper_index(res.get('next_index'), page_size))

