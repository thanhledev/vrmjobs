from vrmjobs import *
import jsonpickle
from uuid import uuid4

if __name__ == '__main__':
    node_cpu_filter_info = FilterInfo('cpu', [{'field_name': 'mode', 'field_value': 'idle', 'regex': '='}])
    node_disk_filter_info = FilterInfo('disk', [{'field_name': 'mounpoint', 'field_value': '/', 'regex': '='}])
    node_disk_io_filter_info = FilterInfo('disk_io',
                                          [{'field_name': 'device', 'field_value': '^.*sda.*$', 'regex': '=~'}])
    node_net_filter_info = FilterInfo('network_io', [{'field_name': 'device', 'field_value': '^wlp.*$', 'regex': '=~'}])

    cadvisor_cpu_filter_info = FilterInfo('cpu', [{'field_name': 'id', 'field_value': '/docker/.+', 'regex': '=~'}])
    cadvisor_mem_filter_info = FilterInfo('memory', [{'field_name': 'id', 'field_value': '/docker/.+', 'regex': '=~'}])
    cadvisor_disk_filter_info = FilterInfo('disk', [{'field_name': 'id', 'field_value': '/docker/.+', 'regex': '=~'}])
    cadvisor_disk_io_filter_info = FilterInfo('disk_io',
                                              [{'field_name': 'id', 'field_value': '/docker/.+', 'regex': '=~'}])
    cadvisor_network_io_filter_info = FilterInfo('network_io',
                                                 [{'field_name': 'id', 'field_value': '/docker/.+', 'regex': '=~'}])

    worker1 = HostInfo('worker1', '192.168.178.156',
                       [PortInfo('workerd', 10500)],
                       HostType.WORKER)

    report = ReportInit('influx_report', 'host_cpu_usage', ['hostname=worker1', 'instance=192.168.178.146'],
                        ['avg_cpu=35.3453'], 1598559679)

    data = jsonpickle.encode(report, unpicklable=False)
    print('{} -> length: {} bytes'.format(data, str(len(data))))
