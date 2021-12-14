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
Time taken for tests:   37.040 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      3590000 bytes
HTML transferred:       1820000 bytes
Requests per second:    269.98 [#/sec] (mean)
Time per request:       185.198 [ms] (mean)
Time per request:       3.704 [ms] (mean, across all concurrent requests)
Transfer rate:          94.65 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   93 1183.8      0   19658
Processing:     3   92 205.3     75   19622
Waiting:        3   92 205.3     75   19622
Total:          3  185 1197.8     76   19709

Percentage of the requests served within a certain time (ms)
  50%     76
  66%     95
  75%    122
  80%    140
  90%    175
  95%    204
  98%    272
  99%    394
 100%  19709 (longest request)
