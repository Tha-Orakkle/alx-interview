#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie data', error);
    } else if (response.statusCode !== 200) {
      console.error('Failed to retrieve movie data. Status code:', response.statusCode);
    } else {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;

      const characters = characterUrls.map(
        url => new Promise((resolve, reject) => {
          request(url, (charErr, _, charBody) => {
            if (charErr) {
              reject(charErr);
            }
            resolve(JSON.parse(charBody).name);
          });
        }));

      Promise.all(characters)
        .then(names => console.log(names.join('\n')))
        .catch(err => console.error(err));
    }
  });
}
