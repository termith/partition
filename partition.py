import abc
from subprocess import Popen, PIPE


class PartitionInformer(object):

    @abc.abstractmethod
    def disk_list(self):
        pass

    @abc.abstractmethod
    def partition_list(self, n):
        pass


class WindowsInformer(PartitionInformer):

    def disk_list(self):
        diskpart = Popen("diskpart", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        out, err = diskpart.communicate("list disk")
        if err != '':
            raise "Error!"

        disk_list = []
        for idx, line in enumerate(out.split('\r')):
            if idx < 9 or idx == len(out.split('\r'))-1:
                continue
            disk_list.append([line.split()[1], line.split()[4]])

        diskpart.kill()

        return disk_list

    def partition_list(self, n):
        diskpart = Popen("diskpart", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        diskpart.communicate("select disk %d"), n

        out, err = diskpart.communicate("list partition")
        if err != '':
            raise "Error"

        partition_list = []
        for idx, line in enumerate(out.split('\r')):
            if idx < 3 or idx == len(out.split('\r'))-1:
                continue
            partition_list.append([line.split()[1], line.split()[3]])

        return partition_list
