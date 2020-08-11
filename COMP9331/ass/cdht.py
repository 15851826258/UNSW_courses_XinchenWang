import socket
import sys
import threading
import time
# transfer the message into bytes.
import pickle
import random

ip = 'localhost'


# 包 处理
class packet_class():
    def __init__(self, ping, quit, data1, data2, msg, seq, res_con, ask, miss):
        self.ping = ping
        self.quit = quit
        self.data1 = data1
        self.data2 = data2
        self.msg = msg
        self.source = int(sys.argv[1])
        self.seq = seq
        self.res_con = res_con
        self.ask = ask
        self.miss = miss


class peer_class:
    def __init__(self, cur, next1, next2, MSS, drop_prob):
        # input value
        self.cur = cur
        self.next1 = next1
        self.next2 = next2
        self.MSS = MSS
        self.drop_prob = drop_prob
        # port number
        self.numvalue = 50000
        self.cur_port = self.cur + self.numvalue
        self.next1_port = self.next1 + self.numvalue
        self.next2_port = self.next2 + self.numvalue

        #peer for transfer
        self.ack=0
        self.seq=1

        # pre of peer
        self.pre1 = 0
        self.pre2 = 0

        # leave detect tag
        self.rec_condition_1 = 0
        self.rec_condition_2 = 0

        # UDP
        self.sendsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receivesocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receivesocket.bind(("", self.cur + self.numvalue))
        self.receivesocket.settimeout(11)
        self.responsesocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # receive thread
        # UDP
        UDP_receive_thread = threading.Thread(target=self.udp_rec)
        UDP_receive_thread.setDaemon(True)
        UDP_receive_thread.start()

        # TCP
        TCP_receive_thread = threading.Thread(target=self.tcp_rec)
        TCP_receive_thread.setDaemon(True)
        TCP_receive_thread.start()

        # ping thread
        ping_thread = threading.Thread(target=self.ping)
        ping_thread.setDaemon(True)
        ping_thread.start()

        # receive from keyboard
        self.input()

        #sup value
        self.cishu=0
        self.sendfile=[]

    def pack_data(self, ping, quit, next1, next2, msg, seq, res_con, ask, miss):
        packet = packet_class(ping, quit, next1, next2, msg, seq, res_con, ask, miss)
        packet = pickle.dumps(packet)
        return packet

    def unpack(self, packet):
        return pickle.loads(packet)

    def ping(self):
        while True:
            ping_msg = 'A ping request was received from Peer ' + str(self.cur)
            # print('-----------------')
            # seq是1 代表 下一个
            packet_1 = self.pack_data(1, 0, 0, 0, ping_msg, 1, 0, 0, 0)
            self.sendsocket.sendto(packet_1, (ip, self.next1 + self.numvalue))
            self.rec_condition_1 += 1
            # print('1情况是'+ str(self.rec_condition_1))
            if (self.rec_condition_1 == 4):
                # print('丢下个拉')
                # print(f'Peer {self.next1} is no longer alive')
                packet_ask = self.pack_data(0, 0, self.next1, 0, 0, 0, 0, 2, self.next1)
                tcp_ask_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcp_ask_socket.connect((ip, self.next2 + self.numvalue))  # 发给我的下家询问
                tcp_ask_socket.send(packet_ask)
                tcp_ask_socket.close()
            # print('send to ' + str(self.next1))
            # seq是2 代表 上一个
            packet_2 = self.pack_data(1, 0, 0, 0, ping_msg, 2, 0, 0, 0)
            self.sendsocket.sendto(packet_2, (ip, self.next2 + self.numvalue))
            self.rec_condition_2 += 1
            # print('2情况是' + str(self.rec_condition_2))
            if (self.rec_condition_2 == 4):
                # print('丢了下下个')
                # print(f'Peer {self.next2} is no longer alive')
                miss = self.next2  # 丢了的那个
                packet_ask = self.pack_data(0, 0, self.next2, 0, 0, 0, 0, 1, self.next2)
                tcp_ask_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcp_ask_socket.connect((ip, self.next1 + self.numvalue))  # 发给我的下家询问
                tcp_ask_socket.send(packet_ask)
                tcp_ask_socket.close()
            # print('send to ' + str(self.next2))
            # print('-----------------')
            time.sleep(5)

    def file_trans(self, destination, filename):  # request 2012
        # print('发向了', destination)
        trans_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        trans_socket.bind(('', self.cur + 6000))
        # 设置超时时间
        trans_socket.settimeout(1)
        # 拼出文件名
        com_filename = str(filename) + '.pdf'
        # total_len = self.filesize(com_filename)
        # print('文件长度',total_len)
        file = open(com_filename, 'rb')  # read binary 二进制读
        destination = int(destination)
        seq = 1
        sendtime = 0
        #print('进了传文件的方法')
        while True:
            file_read = file.read(self.MSS)
            if file_read:
                content = file_read.decode('ISO-8859-1')
                #print('文件转码成功')
                # trans_pkt = self.pack_data(0, 0, file, seq, len(file_read), content, 0, 1500, 0)
                #print('打包完成', destination)
                tranpkt = self.pack_data(0, 0, com_filename, seq, 0, content, 0, 1500, 0)
                #file name 在data1 里
                self.sendsocket.sendto(tranpkt, (ip, destination + self.numvalue))
                #print('发出了一部分')
                data, addr = trans_socket.recvfrom(2048)
                data = self.unpack(data)
                ack = data.data1
                #print('ack收到了', ack)
            else:
                print('The file is sent.')
                break

    def filesize(self,filename):
        #print('方法里')
        f=open(filename,'rb')
        f_con=f.read()
        result=len(f_con)
        f.close()
        #print(result)
        return result

    def udp_rec(self):
        global lv
        while True:
            try:
                ping_msg, address = self.receivesocket.recvfrom(2048)
                ping_msg = self.unpack(ping_msg)
                if (ping_msg.ask == 1500):
                    #print(len(ping_msg.seq))
                    #print('到这里了')
                    self.ack = self.seq + len(ping_msg.seq)
                    #ping_msg.seq这个是文件的内容
                    ack = self.ack
                    self.seq = self.ack
                    #print('ack准备')
                    ack_pack = self.pack_data(0, 0, ack, 0, 0, 0, 0, 0, 0)
                    self.sendsocket.sendto(ack_pack, (ip, ping_msg.source + 6000))
                    #print('ack',ack)
                    #print("收到文件了",ack)
                    filename=ping_msg.data1
                    #print('filename',filename)
                    len_file = self.filesize(filename)
                    #print('filesize',len_file)
                    neirong=ping_msg.seq
                    #print('内容是',type(neirong),neirong)
                    lv.append(neirong)
                    if (ack-1)==len_file:
                        #print('##########')
                        with open('receive.pdf','wb') as file:
                            print('The file is received.')
                            for ele in lv:
                                file.write(ele.encode('ISO-8859-1'))




                if (ping_msg.ping == 1):
                    msg = ping_msg.msg
                    seq_num = ping_msg.seq
                    # print('-----------------')
                    print(msg)
                    # print('-----------------')
                    res_msg = 'A ping response message was received from Peer ' + str(self.cur) + '.'
                    # print(seq_num)
                    if seq_num == 1:

                        if (ping_msg.res_con == 0):
                            packet_1 = self.pack_data(1, 0, 0, 0, res_msg, 1, 1, 0, 0)
                            self.sendsocket.sendto(packet_1, (ip, ping_msg.source + self.numvalue))
                            self.pre1 = ping_msg.source
                            # print(f'当前 {self.cur},上个{self.pre1}')
                        if (ping_msg.res_con == 1):
                            self.rec_condition_1 -= 1

                            # print('1情况是' + str(self.rec_condition_1))
                    if seq_num == 2:

                        if (ping_msg.res_con == 0):
                            packet_2 = self.pack_data(1, 0, 0, 0, res_msg, 2, 1, 0, 0)
                            self.sendsocket.sendto(packet_2, (ip, ping_msg.source + self.numvalue))
                            self.pre2 = ping_msg.source
                            # print(f'当前 {self.cur},上上个{self.pre2}')
                        if (ping_msg.res_con == 1):
                            self.rec_condition_2 -= 1
                            # print('2情况是' + str(self.rec_condition_2))

            except Exception:
                # print('peer dead')
                pass

    def input(self):
        while True:
            content = input("")
            # 去掉前后多余的空格
            content.strip()
            content_list = content.split()
            if content == 'quit':
                self.quit()
            # 去掉自身的空格 切割分开
            elif content_list[0] == 'request':  # request 2999
                # print('收到request请求')
                try:
                    # 文件处理
                    filename = int(content_list[1])
                    #print('filename是' + content_list[1])
                    # filename 校验
                    if filename < 0 or filename > 9999:
                        print('filename not right range')
                        raise ValueError
                    # 调用file处理方法 传入参数filename
                    self.tcp_hash(filename, self.cur)
                    print(f'File request for {filename} has been sent to my successor')
                except:
                    print('Filename is invalid')
            else:
                # input 方法只接受 quit 和 request文件 两个指令 其余报错
                print('Invalid input')

    def quit(self):
        try:
            print('Peer ' + str(self.cur) + ' will depart from the network.')
            # 发给最靠近的前一个
            packet_quit_1 = self.pack_data(0, 1, self.next1, self.next2, 0, 1, 0, 0, 0)
            # print(' 删除 ' + str(self.cur) + ' 此节点的后两个 ' + str(self.next1) + str(self.next2) + ' 发到 ' + str(self.pre1))
            quit_send_packet_socket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            quit_send_packet_socket_1.connect((ip, (self.pre1 + self.numvalue)))
            quit_send_packet_socket_1.send(packet_quit_1)
            quit_send_packet_socket_1.close()
            # 发给前前个
            packet_quit_2 = self.pack_data(0, 1, self.next1, self.next2, 0, 2, 0, 0, 0)
            # print(' 删除 ' + str(self.cur) + ' 此节点的后两个 ' + str(self.next1) + str(self.next2) + ' 发到 ' + str(self.pre2))
            quit_send_packet_socket_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            quit_send_packet_socket_2.connect((ip, (self.pre2 + self.numvalue)))
            quit_send_packet_socket_2.send(packet_quit_2)
            quit_send_packet_socket_2.close()
            # 退出
            sys.exit(0)
        except:
            sys.exit(0)

    def tcp_rec(self):
        tcp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_recv_socket.bind((ip, self.cur + self.numvalue))
        tcp_recv_socket.listen()
        while True:
            socket_ob, addr = tcp_recv_socket.accept()
            packet = socket_ob.recv(2048)
            msg = self.unpack(packet)
            try:
                if msg.quit == 1:
                    # 处理紧邻的前一个
                    if msg.seq == 1:
                        self.next1 = msg.data1
                        # print(msg.data1)
                        self.next2 = msg.data2
                        # print(msg.data2)
                        # print('对于节点' + str(self.cur))
                        # print('&&&&&&&&&&&&&&&&&&')
                        print(f'Peer {msg.source} will depart from the network.')
                        print('My first successor is now peer ' + str(self.next1))
                        print('My second successor is now peer ' + str(self.next2))
                        # print('&&&&&&&&&&&&&&&&&&')
                    elif msg.seq == 2:
                        # print( + str(self.cur))
                        self.next2 = msg.data1
                        # print('&&&&&&&&&&&&&&&&&&')
                        print(f'Peer {msg.source} will depart from the network.')
                        print('My first successor is now peer ' + str(self.next1))
                        print('My second successor is now peer ' + str(self.next2))
                        # print('&&&&&&&&&&&&&&&&&&')
                if msg.ask == 1:
                    miss_ob = msg.miss
                    source = msg.data1
                    # print('问的内容是 ' + str(miss_ob))
                    if (self.next1 == miss_ob):
                        # print('还没改哦')
                        packet_ans = self.pack_data(0, 0, source, 0, 0, 0, 0, 10, self.next2)  # 发回自己的下下个
                        tcp_ask_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        tcp_ask_socket.connect((ip, self.pre1 + self.numvalue))  # 发给我的上家回答
                        tcp_ask_socket.send(packet_ans)  # 发我的回答过去
                        tcp_ask_socket.close()
                    else:
                        # print('改掉了')
                        packet_ans = self.pack_data(0, 0, source, 0, 0, 0, 0, 11, self.next1)  # 发回自己的下个
                        tcp_ask_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        tcp_ask_socket.connect((ip, self.pre1 + self.numvalue))  # 发给我的上家回答
                        tcp_ask_socket.send(packet_ans)  # 发我的回答过去
                        tcp_ask_socket.close()
                if msg.ask == 2:
                    miss_ob = msg.miss
                    source = msg.data1
                    # print('问的内容是 ' + str(miss_ob))
                    packet_ans = self.pack_data(0, 0, source, 0, 0, 0, 0, 12, self.next1)  # 发回自己的下下个
                    tcp_ask_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    tcp_ask_socket.connect((ip, self.pre2 + self.numvalue))  # 发给我的上家回答
                    tcp_ask_socket.send(packet_ans)  # 发我的回答过去
                    tcp_ask_socket.close()
                if msg.ask == 10 or msg.ask == 11:  # 不管下家改没改动 上家都要更新第二个
                    # print('收到 下家 给我的回答')
                    miss_ob = msg.miss
                    self.next2 = miss_ob
                    # print('&&&&&&&&&&&&&&&&&&')
                    print(f'Peer {msg.data1} is no longer alive')
                    print('My first successor is now peer ' + str(self.next1))
                    print('My second successor is now peer ' + str(self.next2))
                    # print('&&&&&&&&&&&&&&&&&&')
                    # print('改过之后 下下个是 ' + str(self.next2))
                if msg.ask == 12:  # 改动走掉的点 前一个
                    miss_ob = msg.miss
                    self.next2 = miss_ob
                    self.next1 = msg.source
                    # print('&&&&&&&&&&&&&&&&&&')
                    print(f'Peer {msg.data1} is no longer alive')
                    print('My first successor is now peer ' + str(self.next1))
                    print('My second successor is now peer ' + str(self.next2))
                    # print('&&&&&&&&&&&&&&&&&&')
                    # print('改过之后 下个是 ' + str(self.next1))
                    # print('改过之后 下下个是 ' + str(self.next2))
                if msg.ask == 99:
                    # 这个是文件问hash的部分
                    # print(msg.miss)
                    hash = int(msg.miss) % 256
                    filename = msg.miss
                    # print('hash值是', hash)
                    source = msg.data1
                    hash_check_result = self.hash_check(hash, filename)
                    # 不在此处 向后继续寻找文件
                    if hash_check_result == 0:
                        # print('now',self.pre1)
                        source = msg.data1
                        # 调用方法继续朝后寻找
                        self.tcp_hash(filename, source)
                        # 在检查的方法里print了
                    # 文件就应该在这里
                    else:
                        #print('&&&&&&&&&&&&&&&&&&')
                        print(f'File {msg.miss} is here.')
                        #print('&&&&&&&&&&&&&&&&&&')
                        print(f'A response message, destined for peer {msg.data1}, has been sent.')
                        print('We now start sending the file .........')
                        # print('cur的', self.cur, '发给', msg.data1)
                        # 传文件的入口
                        show = self.pack_data(0, 0, filename, 0, 0, 0, 0, 12345, 0)
                        # print('send tcp请求 去了', msg.data1,filename)
                        # print(' 删除 ' + str(self.cur) + ' 此节点的后两个 ' + str(self.next1) + str(self.next2) + ' 发到 ' + str(self.pre2))
                        showsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        showsocket.connect((ip, msg.data1 + self.numvalue))
                        # print('send tcp请求 去了' ,msg.data1)
                        showsocket.send(show)
                        showsocket.close()

                        self.file_trans(msg.data1, msg.miss)
                        # file trans thread
                        # UDP_trans_thread = threading.Thread(target=self.file_trans)
                        # UDP_trans_thread.setDaemon(True)
                        # UDP_trans_thread.start()

                if msg.ask==12345:
                    filename=msg.data1
                    #print('show')
                    print(f'Received a response message from peer {msg.source}, which has the file {filename}.')
                    print('We now start receiving the file .........')
                    global lv
                    lv = []


            except:
                pass

    def tcp_hash(self, filename, source):  # use tcp to transmit
        # 发消息给我的下家
        hash_packet = self.pack_data(0, 0, source, 0, 0, 0, 0, 99, filename)
        hash_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hash_socket.connect((ip, self.next1 + self.numvalue))
        # print("在发包 问我的下家 他该不该要文件", filename, self.next1)
        hash_socket.send(hash_packet)
        hash_socket.close()

    def hash_check(self, hash, filename):
        if hash == self.cur:
            # print('一样大，可存')
            return True
        if self.cur > hash > self.pre1:
            # print('我就是下一个，可存')
            return True
        elif hash > self.pre1 > self.cur:
            # print('是环的结尾了 可存',self.pre1,self.cur)
            return True
        elif hash < self.cur < self.pre1:
            return True
        print(f'file {filename} is not stored here.')
        print(f'File request message has been forwarded {filename} to my successor.')
        return False


if __name__ == "__main__":
    peer = peer_class(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]))
