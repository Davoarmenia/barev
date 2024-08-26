import socket
import threading

# Server configuration
HOST = input("Enter server IP address: ")  # Server's IP address
PORT = 65432  # Server's port

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        
        # Start a thread to receive messages
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def receive_messages(self):
        while True:
            try:
                message = self.socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f"Received: {message}")
            except Exception as e:
                print(f"Error receiving message: {e}")
                break
        self.socket.close()

    def send_message(self, message):
        try:
            self.socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error sending message: {e}")

def main():
    host = input("Enter server IP address: ")
    port = 65432  # Server's port
    
    client = ChatClient(host, port)
    
    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break
        client.send_message(message)

    print("Closing client.")
    client.socket.close()

if __name__ == '__main__':
    main()
