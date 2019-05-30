import threading, requests, time
from contextlib import closing

from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtCore import Qt

# 测试用的下载链接
# https://dldir1.qq.com/qqfile/qq/PCQQ9.1.3/25323/QQ9.1.3.25323.exe
# https://download.jetbrains.8686c.com/python/pycharm-professional-2019.1.2.tar.gz
# http://issuecdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduYunGuanjia_6.7.4.exe


class HuiWan_Downloader:
    def __init__(self, list_tree, url):
        self.download_path = "./pyqtDownload"
        self.item = QTreeWidgetItem()
        self.list_tree = list_tree
        self.url = url
        self.file_name = None
        self.remaining_time = 0
        self.total_size = 0
        self.size = 0
        self.speed = 0

    def start(self):
        print("download start: ", self.url)
        # 1. url parse
        if self.url_parse() is None:
            print("url line edit is null")
            return

        print("find if the {} is in the list".format(self.file_name))
        items = self.list_tree.findItems(self.file_name, Qt.MatchContains, column=1)
        if len(items) == 1:
            print("The item is in the list: ", items[0].text(0), items[0].text(1), items[0].text(2), items[0].text(3))

            return

        # 2. update list
        self.list_append()

        self.refresh_start()

        # 3. 准备用以下3种方式完成下载功能
        # 3.1 threading
        self.threads_download_start()

        # 3.2 multiprocessing
        # self.processes_download_start()

        # 3.3 coroutine
        # self.coroutine_download_start()

    def refresh_start(self):
        t = threading.Thread(target=self.refresh_loop)
        t.setDaemon(True)
        t.start()

    def refresh_loop(self):
        print("find item by name: ", self.item.text(1))
        print(self.list_tree.topLevelItemCount())
        print(self.list_tree.topLevelItem(0).text(0))
        print(self.list_tree.topLevelItem(0).text(1))
        print(self.list_tree.topLevelItem(0).text(2))
        print(self.list_tree.topLevelItem(0).text(3))
        items = self.list_tree.findItems(self.item.text(1), Qt.MatchContains, column=1)
        print("%d this name file(s) downloading" % len(items))
        if len(items) == 1:
            print("size: {}, total size: {}".format(self.size, self.total_size))
            while True:
                time.sleep(1)
                if self.total_size == 0:
                    continue

                items[0].setText(2, "30s")
                items[0].setText(3, "%.1f%%" % (100*self.size / self.total_size))

                if self.size >= self.total_size:
                    break

    def url_parse(self):
        self.file_name = self.url.split('/')[-1]
        print("file_name: **%s**" % self.file_name)
        if self.file_name == "":
            self.file_name = "unknown"
            print("url invalid")
            return None
        return self.file_name

    def list_append(self):
        self.item.setText(0, str(self.list_tree.topLevelItemCount() + 1))   # No.
        self.item.setText(1, self.file_name)                                # file_name
        self.item.setText(2, "--")                                          # remaining time
        self.item.setText(3, "--")                                          # percent
        self.list_tree.addTopLevelItem(self.item)

    def threads_download_start(self):

        tdl = threading.Thread(target=self.download_handler)
        # t = threading.Thread(target=Handler, kwargs={'start': start, 'end': end, 'url': url, 'filename': file_name})
        tdl.start()

    def download_handler(self):
        # 1. request header
        self.header_request()
        # 2. create null file
        with open(self.file_name, 'wb') as f:
            f.truncate(self.total_size)

        # 3. start download task
        start = 0
        end = -1
        piece_size = self.total_size // 5   # 无论多大的文件都用5条线程进行下载, 待改进
        for i in range(6):
            start = end + 1
            end = self.total_size if(i == 5) else (i+1)*piece_size

            t = threading.Thread(target=self.download, kwargs={'start': start, 'end': end})
            t.setDaemon(True)
            t.start()

        # 4. main thread waiting every child thread
        main_thread = threading.current_thread()
        for t in threading.enumerate():
            if t is main_thread:
                continue
            t.join()

    def download(self, start, end):

        headers = {'Range': "bytes=%d-%d" % (start, end)}

        print("request headers: ", headers)

        with closing(requests.get(self.url, headers=headers, stream=True)) as res:
            print("requests send")
            with open(self.file_name, 'r+b') as f:
                f.seek(start)
                f.tell()
                for data in res.iter_content(chunk_size=65536):  # chunk_size default 1
                    f.write(data)
                    self.size += len(data)
                    # print("file current size: ", self.size)

        print("download done")

    def header_request(self):
        with closing(requests.head(self.url)) as r:
            self.total_size = int(r.headers['content-length'])
            print("file's total size: ", self.total_size)

