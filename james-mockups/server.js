'use strict';

const pg = require('pg');
const fs = require('fs');
const express = require('express');
const bodyParser = require('body-parser');
const requestProxy = require('express-request-proxy'); 
const PORT = process.env.PORT || 31337;
const app = express();
const conString = process.env.DATABASE_URL
const user = new pg.Client(conString);
user.connect();
user.on('error', err => console.error(err));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static('./public'));

app.get('/new', (request, response) => response.sendFile('new.html', {root: './public'}));
app.get('/edit', (request, response) => response.sendFile('edit.html', {root: './public'}));
app.get('/entry', (request, response) => {
  user.query(`
    SELECT * FROM entries
    INNER JOIN authors
      ON entries.author_id=authors.author_id;`
  )
  .then(result => response.send(result.rows))
  .catch(console.error);
});

app.post('/entry', (request, response) => {
  user.query(
    'INSERT INTO authors(author, "authorUrl") VALUES($1, $2) ON CONFLICT DO NOTHING',
    [request.body.author, request.body.authorUrl]
  )
  .then(() => {
    user.query(`
      INSERT INTO
      articles(author_id, title, category, "publishedOn", body)
      SELECT author_id, $1, $2, $3, $4
      FROM authors
      WHERE author=$5;
      `,
      [
        request.body.title,
        request.body.category,
        request.body.publishedOn,
        request.body.body,
        request.body.author
      ]
    )
  })
  .then(() => response.send('Insert complete'))
  .catch(console.error);
});

app.put('/entry/:id', (request, response) => {
  user.query(`
    UPDATE authors
    SET author=$1, "authorUrl"=$2
    WHERE author_id=$3
    `,
    [request.body.author, request.body.authorUrl, request.body.author_id]
  )
  .then(() => {
    user.query(`
      UPDATE entries
      SET author_id=$1, title=$2, category=$3, "publishedOn"=$4, body=$5
      WHERE entry_id=$6
      `,
      [
        request.body.author_id,
        request.body.title,
        request.body.category,
        request.body.publishedOn,
        request.body.body,
        request.params.id
      ]
    )
  })
  .then(() => response.send('Update complete'))
  .catch(console.error);
});

app.delete('/entry/:id', (request, response) => {
  user.query(
    `DELETE FROM entries WHERE entry_id=$1;`,
    [request.params.id]
  )
  .then(() => response.send('Delete complete'))
  .catch(console.error);
});

app.delete('/entry', (request, response) => {
  user.query('DELETE FROM entries')
  .then(() => response.send('Delete complete'))
  .catch(console.error);
});

loadDB();

app.listen(PORT, () => console.log(`Server started on port ${PORT}!`));

function loadAuthors() {
  fs.readFile('./public/data/hackerIpsum.json', (err, fd) => {
    JSON.parse(fd.toString()).forEach(ele => {
      user.query(
        'INSERT INTO authors(author, "authorUrl") VALUES($1, $2) ON CONFLICT DO NOTHING',
        [ele.author, ele.authorUrl]
      )
      .catch(console.error);
    })
  })
}

function loadEntries() {
  user.query('SELECT COUNT(*) FROM entries')
  .then(result => {
    if(!parseInt(result.rows[0].count)) {
      fs.readFile('./public/data/hackerIpsum.json', (err, fd) => {
        JSON.parse(fd.toString()).forEach(ele => {
          user.query(`
            INSERT INTO
            articles(author_id, title, category, "publishedOn", body)
            SELECT author_id, $1, $2, $3, $4
            FROM authors
            WHERE author=$5;
          `,
            [ele.title, ele.category, ele.publishedOn, ele.body, ele.author]
          )
          .catch(console.error);
        })
      })
    }
  })
}

function loadDB() {
  user.query(`
    CREATE TABLE IF NOT EXISTS
    authors (
      author_id SERIAL PRIMARY KEY,
      author VARCHAR(255) UNIQUE NOT NULL,
      "authorUrl" VARCHAR (255)
    );`
  )
  .then(loadAuthors)
  .catch(console.error);

  user.query(`
    CREATE TABLE IF NOT EXISTS
    entries (
      entry_id SERIAL PRIMARY KEY,
      author_id INTEGER NOT NULL REFERENCES authors(author_id),
      title VARCHAR(255) NOT NULL,
      category VARCHAR(20),
      "publishedOn" DATE,
      body TEXT NOT NULL
    );`
  )
  .then(loadEntries)
  .catch(console.error);
}
