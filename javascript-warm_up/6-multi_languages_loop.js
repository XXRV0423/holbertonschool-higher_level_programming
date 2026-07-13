#!/usr/bin/node
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let message = '';

for (const language of languages) {
  message += `${language}\n`;
}

console.log(message.trimEnd());