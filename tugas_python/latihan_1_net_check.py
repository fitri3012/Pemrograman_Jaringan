import socket

def dns_lookup(domain):
    print("=== DNS Lookup Tool ===")
    try:
        # Mengubah domain menjadi IP Address
        ip_address = socket.gethostbyname(domain)

        print(f"Domain     : {domain}")
        print(f"IP Address : {ip_address}")

    except socket.gaierror as e:
        # Menangani error jika domain tidak ditemukan
        print(f"Gagal melakukan DNS lookup: {e}")

if __name__ == "__main__":
    # Ganti domain sesuai kebutuhan
    domain = "google.com"
    dns_lookup(domain)
