from __future__ import print_function
import logging

import grpc
import TemperatureService_pb2
import TemperatureService_pb2_grpc

import const


def Client():
    with grpc.insecure_channel(const.IP + ':' + const.PORT) as channel:
        stub = TemperatureService_pb2_grpc.TemperatureServiceStub(channel)

        print('1 - Insert data')
        print('2 - Search by ID')
        print('3 - Search by date')
        print('4 - Search by local')
        print('5 - List all data')
        option = int(input('Choose an option: '))

        if option == 1:
            id = int(input("Input an ID: "))
            date = input("Input a date: ")
            local = input("Input a local: ")
            temperature = input("Input a temperature: ")

            response = stub.CadastrarTemperature(
                TemperatureService_pb2.Temperature(id=id, date=date, local=local, temperature=temperature))
            print('Insert data: ' + str(response));
        
        elif option == 2:
            id_search = int(input('Input an ID: '))
            response = stub.GetTemperatureByID(TemperatureService_pb2.Id(id=id_search))
            print('Search by ID: \n' + str(response));
        
        elif option == 3:
            date_search = input('Input a date=e: ')
            response = stub.GetTemperatureByDate(TemperatureService_pb2.date(date=date_search))
            print('Search by date: ' + str(response));
        
        elif option == 4:
            local_search = input("Input a local: ")
            response = stub.GetTemperatureByLocal(
                TemperatureService_pb2.local(local=local_search))
            print('Search by local: ' + str(response));
        
        elif option == 5:
            response = stub.ListAllData(TemperatureService_pb2.EmptyMessage())
            print('All data: ' + str(response));


if __name__ == '__main__':
    logging.basicConfig()
    Client()