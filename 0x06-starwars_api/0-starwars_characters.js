#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const starWarsUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to get characters from the movie
function getCharacters (callback) {
  request.get(starWarsUrl, (error, response, body) => {
    if (error) {
      callback(error);
    } else {
      const result = JSON.parse(body).characters;
      callback(null, result);
    }
  });
}

// Function to process each character
function processCharacter (character, innerCallback) {
  request.get(character, (error, response, body) => {
    if (error) {
      innerCallback(error);
    } else {
      const personName = JSON.parse(body).name;
      console.log(personName);
      innerCallback();
    }
  });
}

// Main logic
getCharacters((error, characters) => {
  if (error) {
    console.error(error);
    return;
  }

  // Process each character in series
  let index = 0;
  function processNextCharacter () {
    if (index < characters.length) {
      processCharacter(characters[index], (innerError) => {
        if (innerError) {
          console.error(innerError);
        }
        index++;
        processNextCharacter();
      });
    }
  }

  processNextCharacter();
});
