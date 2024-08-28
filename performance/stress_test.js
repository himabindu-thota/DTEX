// Example: https://k6.io/docs/get-started/running-k6/
// Load Test
// 500 reqs/sec for 30 mins

import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    stages: [
        {duration: '1m', target: 200 }, // ramp up
        {duration: '5m', target: 200 }, // stable
        {duration: '1m', target: 800 }, // increase load
        {duration: '5m', target: 800 }, // stable
        {duration: '1m', target: 1000 }, // increase load
        {duration: '5m', target: 1000 }, // stable
        {duration: '5m', target: 0 }, //ramp down
    ],
    thresholds: {
        http_req_duration: ['p(99)<100'], // 99% of requests should come back within 50 ms
    }
};

export default function () {
  http.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
  sleep(1);
}
