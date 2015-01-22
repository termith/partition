import partition
import sys

if __name__ == '__main__':

    informer = partition.WindowsInformer()

    if len(sys.argv) == 1:
        print("Disk Size")
        for d in informer.disk_list():
            print("%s\t%s" % (d[0], d[1]))
    else:
        print("Partition Size")
        for p in informer.partition_list(sys.argv[1]):
            print("%s\t%s" % (p[0], p[1]))



