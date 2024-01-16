#!/usr/bin/node

const request = require('request');
const async = require('async');

const movieId = process.argv[2];

const starWarsUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;


async.waterfall([
  function (callback) {
    request.get(starWarsUrl, (error, response, body) => {
      if (error) {
        callback(error);
      } else {
        const result = JSON.parse(body).characters;
        callback(null, result);
      }
    });
  },
  function (characters, callback) {
    async.eachSeries(
      characters,
      function (character, innerCallback) {
        request.get(character, (error, response, body) => {
          if (error) {
            innerCallback(error);
          } else {
            const personName = JSON.parse(body).name;
            console.log(personName);
            innerCallback();
          }
        });
      },
      function (error) {
        if (error) {
          callback(error);
        } else {
          callback();
        }
      }
    );
  }
], function (error) {
  if (error) {
    console.error(error);
  }
});
