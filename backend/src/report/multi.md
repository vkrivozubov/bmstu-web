This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)


Server Software:        CarsAPI
Server Hostname:        127.0.0.1
Server Port:            8080

Document Path:          /api/v1/dealership/dealerships
Document Length:        182 bytes

Concurrency Level:      50
Time taken for tests:   35.876 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      3590000 bytes
HTML transferred:       1820000 bytes
Requests per second:    278.74 [#/sec] (mean)
Time per request:       179.381 [ms] (mean)
Time per request:       3.588 [ms] (mean, across all concurrent requests)
Transfer rate:          97.72 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0  100 1218.1      0   20133
Processing:     2   79 123.0     33    6728
Waiting:        2   79 123.0     33    6728
Total:          2  179 1219.6     50   20159

Percentage of the requests served within a certain time (ms)
  50%     50
  66%    100
  75%    117
  80%    138
  90%    210
  95%    244
  98%    359
  99%    954
 100%  20159 (longest request)
