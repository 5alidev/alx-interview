#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
let movieId = '1';

if (args.length > 0) {
  movieId = args[0];
}

const starWarsApiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
const promise = new Promise((resolve, reject) => {
  request(starWarsApiUrl, (error, response, body) => {
    if (error) reject(error);
    const movieObject = JSON.parse(body);
    const characters = movieObject.characters;
    resolve(characters);
  });
});
promise.then((characters) => {
  const characterPromises = characters.map(charUrl => {
    return new Promise((resolve, reject) => {
      request(charUrl, (err, res, bd) => {
        if (err) reject(err);
        const characterObject = JSON.parse(bd);
        resolve(characterObject.name);
      });
    });
  });

  Promise.all(characterPromises).then(names => {
    names.forEach(name => console.log(name));
  }).catch(err => console.log(err));
});
