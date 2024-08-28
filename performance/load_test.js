// Example: https://k6.io/docs/get-started/running-k6/
// Load Test
// 500 reqs/sec for 30 mins

import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    stages: [
        {duration: '2m', target: 500 },
        {duration: '20m', target: 500 },
        {duration: '30s', target: 0 },
    ],
    thresholds: {
        http_req_duration: ['p(99)<100'], // 99% of requests should come back within 50 ms
    }
};

export default function () {
  http.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
  sleep(1);
}
