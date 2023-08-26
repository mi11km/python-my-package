import socket
from datetime import datetime

# socket: 実行中のプログラム間でデータの送受信を行うための標準的な仕組みの一つ。アドレスとポートを使用。ネットワークプログラミングの最下層。
# UDP: 送られてくるパケットの順序がバラバラだったり、届かなかったりするが、高速通信
# TCP: 順序もコネクションもちゃんと確立して、重複なく送る。寿命が長い接続向き。

server_address = ("localhost", 6789)
max_size = 4096


def socket_server(protocol=socket.SOCK_DGRAM):
    if type(protocol) is not socket.SocketKind:
        raise ValueError("invalid argument")
    print("Starting the server at ", datetime.now())
    print("Waiting for a client call.")
    server = socket.socket(socket.AF_INET, protocol)  # IPソケット、UDP
    server.bind(server_address)  # そのIPアドレスとポートに届いたあらゆるデータをListenする
    if protocol == socket.SOCK_DGRAM:  # UDP
        data, client = server.recvfrom(max_size)
        print("At", datetime.now(), client, "said", data)
        server.sendto(b"Are you talking to me?", client)
    elif protocol == socket.SOCK_STREAM:  #  TCP
        server.listen(5)  # キューに5個クライアント接続が溜まったら新しい接続を拒否
        client, addr = server.accept()
        data = client.recv(max_size)
        print("At", datetime.now(), client, "said", data)
        client.sendall(b"Are you talking to me?")
        client.close()
    server.close()


def socket_client(protocol=socket.SOCK_DGRAM):
    if type(protocol) is not socket.SocketKind:
        raise ValueError("invalid argument")
    print("Starting the client at", datetime.now())
    client = socket.socket(socket.AF_INET, protocol)
    if protocol == socket.SOCK_DGRAM:  # UDP
        client.sendto(b"Hey!", server_address)
        data, server = client.recvfrom(max_size)
        print("At", datetime.now(), server, "said", data)
    elif protocol == socket.SOCK_STREAM:  # TCP
        client.connect(server_address)
        client.sendall(b"Hey!")
        data = client.recv(max_size)
        print("At", datetime.now(), "someone replied", data)
    client.close()


if __name__ == "__main__":
    # socket_server(protocol=socket.SOCK_STREAM)
    socket_client(protocol=socket.SOCK_STREAM)
