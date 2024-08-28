// Example: https://k6.io/docs/get-started/running-k6/

import http from 'k6/http';

export default function () {
  http.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
}
