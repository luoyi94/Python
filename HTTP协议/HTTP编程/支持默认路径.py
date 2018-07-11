import socket
import re


def handle_client(new_socket):
    """接收 并返回固定数据"""
    # 接收数据
    recv_data = new_socket.recv(1024).decode()
    print("*" * 40)
    print("recv_data = ", recv_data)
    # 接收到浏览器后面的用户请求内容：http://127.0.0.1:8888/index.html
    # 实际：已经经过浏览器包装HTTP格式的请求报文  下面是解析这些报文
    # 以行为单位切割
    recv_list = recv_data.splitlines()
    # GET /index.html HTTP/l.1   ====> recv_list[0]
    # [^/]+(/[^ ]+).*
    # 请求头部
    # 空行
    # 请求包体

    # 通过正则匹配请求的index.html
    print(recv_list[0])
    firstLine = recv_list[0]

    fileName = re.match(r"[^/]+(/[^ ]*)", firstLine).group(1)
    print(fileName)

    # 支持默认路径
    if fileName == "/":
        fileName = "/index.html"

    # 组成路径    ./   当前路径下查找html文件夹
    # 本页代码 的路径 有一个html文件夹，要访问的页面在html页面下面
    filePath = "./html1" + fileName
    print(filePath)



    try:
        with open(filePath, "rb") as f:
            content = f.read()
    except Exception as ret:
        # 没有这个请求的资源 404
        send_data = "HTTP/1.1 404 NOT FOUND\r\n"
        send_data += "\r\n"
        content = "file not found".encode()
    else:
        # 有这个请求对应的资源 200
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
        print("%s连接上来咯！" % cli_addr[0])

        handle_client(new_socket)

        # 关闭监听套接字
    tcp.close()








if __name__ == '__main__':
    main()