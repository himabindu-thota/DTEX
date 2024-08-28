// Example: https://k6.io/docs/get-started/running-k6/

import http from 'k6/http';
import { sleep } from 'k6';
export const options = {
  vus: 10,
  duration: '10s',
};
export default function () {
  http.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
  sleep(1);
}
