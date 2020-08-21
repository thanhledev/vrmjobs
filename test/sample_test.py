from vrmjobs import *

if __name__ == '__main__':
    psutil_disk_filter_info = FilterInfo('disk', [{'mounpoint': '/rootfs'}, {'device': '/dev/sda'}])
    psutil_net_filter_info = FilterInfo('network', [{'interface': 'enp0s8'}])
    psutil_query_info = QueryInfo('psutil', [psutil_disk_filter_info, psutil_net_filter_info])

    node_disk_filter_info = FilterInfo('disk', [{'mounpoint': '/rootfs'}, {'device': '/dev/sda'}])
    node_net_filter_info = FilterInfo('network', [{'interface': 'enp0s8'}])
    node_query_info = QueryInfo('node', [node_disk_filter_info, node_net_filter_info])

    print(query_info)
    worker1 = HostInfo('worker1', '192.168.178.156',
                       [PortInfo('workerd', 10500)],
                       [psutil_query_info, node_query_info],
                       HostType.WORKER)
