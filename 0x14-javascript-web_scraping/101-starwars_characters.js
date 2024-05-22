#!/usr/bin/node

const { argv } = require('process');
const request = require('request-promise-native');

const api = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request(api, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  async function fetchAllData (bc) {
    for (const idx in bc) {
      try {
        const body = await request({ uri: bc[idx], json: true });
        console.log(body.name);
      } catch (err) {
        console.error(err);
      }
    }
  }

  fetchAllData(body.characters);
});
