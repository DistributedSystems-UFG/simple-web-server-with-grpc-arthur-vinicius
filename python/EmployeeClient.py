from __future__ import print_function
import logging

import grpc
import EmployeeService_pb2
import EmployeeService_pb2_grpc

import const


def Client():
    with grpc.insecure_channel(const.IP + ':' + const.PORT) as channel:
        stub = EmployeeService_pb2_grpc.TemperatureServiceStub(channel)

        print('1 - Insert data')
        print('2 - List all data')
        print('3 - Search by ID')
        print('4 - Search by date')
        print('5 - Search by local')
        option = int(input())

        if option == 1:
            id = int(input("Input an ID: "))
            date = input("Input a date: ")
            local = input("Input a local: ")
            temperature = input("Input a temperature: ")

            response = stub.CadastrarTemperature(
                EmployeeService_pb2.Temperature(id=id, date=date, local=local, temperature=temperature))
            print('Insert data: ' + str(response));
        
        elif option == 2:
        	response = stub.ListAllData(EmployeeService_pb2.EmptyMessage())
            print('All data: ' + str(response));
        
        elif option == 3:
        	id_search = int(input('Input an ID: '))
            response = stub.GetTemperatureByID(EmployeeService_pb2.Id(id=id_search))
            print('Search by ID: \n' + str(response));
        
        elif option == 4:
        	date_search = input('Input a date=e: ')
            response = stub.GetTemperatureByDate(EmployeeService_pb2.date(date=date_search))
            print('Search by date: ' + str(response));
        
        elif option == 5:
        	local_search = input("Input a local: ")
            response = stub.GetTemperatureByLocal(
                EmployeeService_pb2.local(local=local_search))
            print('Search by local: ' + str(response));
            


if __name__ == '__main__':
    logging.basicConfig()
    Client()
