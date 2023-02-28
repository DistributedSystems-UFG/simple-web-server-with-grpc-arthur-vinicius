from concurrent import futures
import logging

import grpc
import TemperatureService_pb2
import TemperatureService_pb2_grpc

all_data = [    
    {        
        'id': 1,        
        'date': '15/01/2023',        
        'local': 'Recife',        
        'temperature': 31    
    },    
    {        
        'id': 2,        
        'date': '20/12/2022',        
        'local': 'Salvador',        
        'temperature': 28    
    },    
    {        
        'id': 3,        
        'date': '22/12/2022',        
        'local': 'Manaus',        
        'temperature': 25    
    },    
    {        
        'id': 4,        
        'date': '25/12/2022',        
        'local': 'Rio de Janeiro',        
        'temperature': 30    
    },    
    {        
        'id': 5,        
        'date': '26/12/2022',        
        'local': 'Fortaleza',        
        'temperature': 32    
    },    
    {        
        'id': 6,        
        'date': '27/12/2022',        
        'local': 'Brasilia',        
        'temperature': 15    
    },    
    {        
        'id': 7,        
        'date': '01/01/2023',        
        'local': 'Porto Alegre',        
        'temperature': 18    
    },    
    {        
        'id': 8,        
        'date': '05/01/2023',        
        'local': 'Goiânia',        
        'temperature': 25    
    },    
    {        
        'id': 9,        
        'date': '10/01/2023',        
        'local': 'Sao Paulo',        
        'temperature': 20    
    },    
    {        
        'id': 10,        
        'date': '15/01/2023',        
        'local': 'Belo Horizonte',        
        'temperature': 27    
    }
]

class TemperatureService(TemperatureService_pb2_grpc.TemperatureServiceService):
    def InsertTemperature(self, request, context):
        data = {
            'id': request.id,
            'date': request.date,
            'local': request.name.local,
            'temperature': request.temperature
        }
        all_data.append(data)
        return TemperatureService_pb2.StatusReply(status='OK')

    def GetTemperatureByID(self, request, context):
        usr = [item for item in all_data if (item['id'] == request.id)]

        return TemperatureService_pb2.Temperature(id=usr[0]['id'], date=usr[0]['date'], local=usr[0]['local'],
                                                  temperature=usr[0]['temperature'])

    def GetTemperatureByDate(self, request, context):
        filtered_list = [item for item in all_data if (item['date'] == request.date)]
        list = TemperatureService_pb2.TemperatureList()
        for item in filtered_list:
            emp_date = TemperatureService_pb2.Temperature(id=item['id'], date=item['date'],
                                                          local=item['local'],
                                                          temperature=item['temperature'])
            list.temperature_data.append(emp_date)
        return list

        return TemperatureService_pb2.TemperatureList(filtered_list)

    def GetTemperatureByLocal(self, request, context):
        filtered_list = [item for item in all_data if (item['local'] == request.local)]
        list = TemperatureService_pb2.TemperatureList()
        for item in filtered_list:
            emp_date = TemperatureService_pb2.Temperature(id=item['id'], date=item['date'],
                                                          local=item['local'],
                                                          temperature=item['temperature'])
            list.temperature_data.append(emp_date)
        return list

    def ListAllData(self, request, context):
        list = TemperatureService_pb2.TemperatureList()
        for item in all_data:
            emp_date = TemperatureService_pb2.Temperature(id=item['id'], date=item['date'],
                                                          local=item['local'],
                                                          temperature=item['temperature'])
            list.temperature_data.append(emp_date)
        return list


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TemperatureService_pb2_grpc.add_TemperatureServiceService_to_server(TemperatureService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()