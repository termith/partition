import partition
import sys

if __name__ == '__main__':

    informer = partition.WindowsInformer()

    if len(sys.argv) == 1:
        print(informer.disk_list())
    else:
        print(informer.partition_list(sys.argv[1]))



