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

      // characterUrls.forEach(url => {
      //   request(url, (charErr, charResponse, charBody) => {
      //     if (charErr) {
      //       console.error('Error fetching character data', error);
      //     } else if (charResponse.statusCode != 200) {
      //       console.error('Failed to retrieve character data. Status code:', charResponse.statusCode);
      //     } else {
      //       characterData = JSON.parse(charBody);
      //       console.log(characterData.name);
      //     }
      //   })
      // });

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
