import socket
import ssl

def run_secure_client():
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_sock = context.wrap_socket(sock, server_hostname='localhost')

    try:
        print("Menghubungkan ke server aman...")
        secure_sock.connect(('localhost', 10023))
        print(f"Cipher digunakan: {secure_sock.cipher()}")

        secure_sock.send(b"Halo Kanjeng Ratu, ini pesan rahasia CIA.")
        response = secure_sock.recv(1024)
        print(f"Balasan Server: {response.decode()}")

    finally:
        secure_sock.close()

if __name__ == "__main__":
    run_secure_client()