import socket


def handle_client(new_socket):
    """接收 并返回固定数据"""
    # 接收数据
    recv_data = new_socket.recv(1024)
    print("*" * 40)
    print("recv_data = ", recv_data.decode())


    # ./在当前文件路径下面查找
    with open("./html/index.html", "rb") as f:
        content = f.read()
    # 构造适合网页格式的响应体
    send_data = "HTTP/1.1 200 OK\r\n"
    send_data += "\r\n"
    # send_data += "ok"

    # 发送数据
    new_socket.send(send_data.encode())
    new_socket.send(content)

    new_socket.close()




def main():
    """返回固定数据"""
    # 创建套接字
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 端口复用
    tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 端口绑定
    tcp.bind(("", 8888))

    # 监听
    tcp.listen(128)

    while True:
        # 取出客户 返回服务套接字
        new_socket, cli_addr = tcp.accept()
        print(cli_addr, "连接上来咯！")

        handle_client(new_socket)

        # 关闭监听套接字
    tcp.close()








if __name__ == '__main__':
    main()