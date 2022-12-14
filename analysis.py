import statistics
import math


AMZN = [
    [129.479996,129.820007,133.270004,136.449997,126.82,128.550003,126.279999],
    [123.529999,124.660004,122.190002,118.540001,117.309998,113.779999,115.150002],
    [114.410004,118.010002,114.800003,113,115.879997,121.089996,120.949997],
    [120.300003,114.559998,113.669998,112.209999,112.900002,112.529999,106.900002],
    [113.790001,116.360001,115.07,115.25,119.32,119.82,120.599998],
    [115.660004,110.959999,103.410004,102.440002,96.790001,92.120003,89.300003],
    [90.980003,90.529999,89.980003,86.139999,96.629997,100.790001,98.489998,98.940002]
]

META = [
    [160.389999,162.059998,169.149994,168.960007,153.130005,151.470001,149.550003],
    [146.289993,148.020004,146.089996,142.119995,142.820007,140.410004,136.369995],
    [134.399994,141.610001,136.410004,135.679993,138.610001,140.279999,138.979996],
    [139.070007,133.449997,133.789993,128.539993,127.5,130.289993,126.760002],
    [134.039993,132.800003,133.229996,131.529999,130.009995,129.720001,137.509995],
    [129.820007,97.940002,99.199997,93.160004,95.199997,90.540001,88.910004],
    [90.790001,96.720001,96.470001,101.470001,111.870003,113.019997,114.220001,117.080002]
]


def std_dev_using_stats_lib(company, weeks):
    week_num = 1
    for week in weeks:
        print(week_num, company, round(statistics.stdev(week), 3))
        week_num += 1


def std_dev_from_scratch(name_list, list):
    list_sum = 0
    elements = 0
    for element in list:
        list_sum += element
        elements += 1
    mean = list_sum / elements

    squares = []

    for element in list:
        squared_diff = (mean - element)**2
        squares.append(squared_diff)

    sum_of_squares = sum(squares)

    std_dev = math.sqrt(sum_of_squares / (elements - 1))

    return std_dev


std_dev_using_stats_lib("AMZN", AMZN)

for list in AMZN:
    calc = round(std_dev_from_scratch("AMZN", list), 3)
    print(calc)


std_dev_using_stats_lib("META", META)

for list in META:
    calc = round(std_dev_from_scratch("META", list), 3)
    print(calc)

