import socket


def main():
    # 创建TCP套接字（监听，链接套接字）
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口复用
    tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定
    tcp.bind(("", 8888))
    # 监听
    tcp.listen(128)

    # 重复取出成功链接的客户
    while True:
        # 取出客户，返回一个新的套接字（服务套接字）
        new_socket, cli_addr = tcp.accept()
        print(cli_addr, "连上来咯！")  # 链接上来的时候打印

        # 接收客户端的数据
        recv_data = new_socket.recv(1024)
        print(cli_addr, ">>>>>", recv_data.decode())

        # 拼接应答体 响应报文
        # 组成状态行
        send_data = "HTTP/1.1 200 OK\r\n"
        # 空行
        send_data += "\r\n"
        # 响应包体
        send_data += "ok"

        # 发送按照网页格式组成的内容给客户端浏览器
        # 浏览器显示：ok
        new_socket.send(send_data.encode())

        # 关闭服务套接字
        new_socket.close()

    # 关闭链接套接字
    tcp.close()







if __name__ == '__main__':
    main()