// Example: https://k6.io/docs/get-started/running-k6/
// Load Test
// 500 reqs/sec for 30 mins

import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    stages: [
        {duration: '30s', target: 2000 },
        {duration: '2m', target: 2000 },
        {duration: '30s', target: 0 },
    ],
};

export default function () {
  http.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
  sleep(1);
}
