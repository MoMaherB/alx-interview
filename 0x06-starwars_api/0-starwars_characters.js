#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  const printCharacterName = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        resolve();
      });
    });
  };

  (async () => {
    for (const characterUrl of characters) {
      await printCharacterName(characterUrl);
    }
  })();
});

