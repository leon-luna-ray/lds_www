// var app = new Vue({
//     delimiters: ["[[", "]]"],
//     el: '#app',
//     data: {
//       message: 'Hello Vue!'
//     }
//   })

import { createApp } from 'https://unpkg.com/petite-vue?module';

createApp({
  $delimiters: ['[[', ']]'],
  el: '#app',
  data: {
    message: 'Hello Vue!',
  },
  clickEvent(){
    console.log('clicked!')
  }
}).mount('#app');
