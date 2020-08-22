from vrmjobs import *
from uuid import uuid4
import jsonpickle

if __name__ == '__main__':
    psutil_disk_filter_info = FilterInfo('disk', [{'field_name': 'mounpoint', 'field_value': '/rootfs', 'regex': '='},
                                                  {'field_name': 'device', 'field_value': '^.*/dev/sda.*$',
                                                   'regex': '=~'}])
    psutil_net_filter_info = FilterInfo('network', [{'field_name': 'interface', 'field_value': 'enp0s8', 'regex': '='}])
    psutil_query_info = QueryInfo('psutil', [psutil_disk_filter_info, psutil_net_filter_info])

    node_disk_filter_info = FilterInfo('disk', [{'field_name': 'mounpoint', 'field_value': '/rootfs', 'regex': '='},
                                                {'field_name': 'device', 'field_value': '^.*/dev/sda.*$',
                                                 'regex': '=~'}])
    node_net_filter_info = FilterInfo('network', [{'field_name': 'interface', 'field_value': 'enp0s8', 'regex': '='}])
    node_query_info = QueryInfo('node', [node_disk_filter_info, node_net_filter_info])

    cadvisor_cpu_filter_info = FilterInfo('cpu', [{'field_name': 'id', 'field_value': '/docker/.+', 'regex': '=~'}])
    cadvisor_mem_filter_info = FilterInfo('memory', [{'field_name': 'id', 'field_value': '/docker/.+', 'regex': '=~'}])
    cadvisor_disk_filter_info = FilterInfo('disk', [{'field_name': 'id', 'field_value': '/docker/.+', 'regex': '=~'}])
    cadvisor_disk_io_filter_info = FilterInfo('disk-io',
                                              [{'field_name': 'id', 'field_value': '/docker/.+', 'regex': '=~'}])
    cadvisor_network_io_filter_info = FilterInfo('network-io',
                                                 [{'field_name': 'id', 'field_value': '/docker/.+', 'regex': '=~'}])

    print(psutil_query_info)
    worker1 = HostInfo('worker1', '192.168.178.156',
                       [PortInfo('workerd', 10500)],
                       [psutil_query_info, node_query_info],
                       HostType.WORKER)

    worker1_psutil_query_ack = QueryAck(str(uuid4()),
                                        'worker1', 'psutil',
                                        [psutil_disk_filter_info, psutil_net_filter_info],
                                        VrmType.QUERY_ACK)

    print('worker1_psutil_query_ack: {} - length {}'.format(worker1_psutil_query_ack,
                                                            str(len(jsonpickle.encode(worker1_psutil_query_ack)))))

    data = jsonpickle.encode(worker1_psutil_query_ack)
    print(data)

    worker1_cadvisor_query_ack = QueryAck(str(uuid4()),
                                          'worker1', 'cadvisor',
                                          [cadvisor_cpu_filter_info, cadvisor_mem_filter_info,
                                           cadvisor_disk_filter_info, cadvisor_disk_io_filter_info,
                                           cadvisor_network_io_filter_info], VrmType.QUERY_ACK)

    print('worker1_cadvisor_query_ack: {} - length {}'.format(worker1_cadvisor_query_ack,
                                                              str(len(jsonpickle.encode(worker1_cadvisor_query_ack)))))
