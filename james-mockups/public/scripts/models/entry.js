'use strict';

(function(module) {
  function Entry(rawDataObj) {
    Object.keys(rawDataObj).forEach(key => this[key] = rawDataObj[key]);
  }

  Entry.all = [];

  Entry.prototype.toHtml = function() {
    let template = Handlebars.compile($('#entry-template').text());

    this.daysAgo = parseInt((new Date() - new Date(this.publishedOn))/60/60/24/1000);
    this.publishStatus = this.publishedOn ? `published ${this.daysAgo} days ago` : '(draft)';
    this.body = marked(this.body);

    return template(this);
  };

  Entry.loadAll = rows => {
    rows.sort((a,b) => (new Date(b.publishedOn)) - (new Date(a.publishedOn)));
    Entry.all = rows.map(ele => new Entry(ele));
  };

  Entry.fetchAll = callback => {
    $.get('/entries')
    .then(
      results => {
        Article.loadAll(results);
        callback();
      }
    )
  };

  Entry.numWordsAll = () => {
    return Entry.all.map(entry => entry.body.match(/\b\w+/g).length)
                      .reduce((a, b) => a + b)
  };

  Entry.allAuthors = () => {
    return Entry.all.map(entry => entry.author)
                      .reduce((names, name) => {
                        if (names.indexOf(name) === -1) names.push(name);
                        return names;
                      }, []);
  };

  Entry.numWordsByAuthor = () => {
    return Entry.allAuthors().map(author => {
      return {
        name: author,
        numWords: Entry.all.filter(a => a.author === author)
                             .map(a => a.body.match(/\b\w+/g).length)
                             .reduce((a, b) => a + b)
      }
    })
  };

  Entry.stats = () => {
    return {
      numEntries: Entry.all.length,
      numWords: Entry.numWordsAll(),
      Authors: Entry.allAuthors(),
    }
  };

  Entry.truncateTable = callback => {
    $.ajax({
      url: '/entries',
      method: 'DELETE',
    })
    .then(console.log)
    .then(callback);
  };

  Entry.prototype.insertRecord = function(callback) {
    $.post('/entries', {author: this.author, authorUrl: this.authorUrl, body: this.body, category: this.category, publishedOn: this.publishedOn, title: this.title})
    .then(console.log)
    .then(callback);
  };

  Entry.prototype.deleteRecord = function(callback) {
    $.ajax({
      url: `/entries/${this.entry_id}`,
      method: 'DELETE'
    })
    .then(console.log)
    .then(callback);
  };

  Entry.prototype.updateRecord = function(callback) {
    $.ajax({
      url: `/entries/${this.entry_id}`,
      method: 'DELETE',
      data: {
        author: this.author,
        authorUrl: this.authorUrl,
        body: this.body,
        category: this.category,
        publishedOn: this.publishedOn,
        title: this.title,
        author_id: this.author_id
      }
    })
    .then(console.log)
    .then(callback);
  };

  module.Entry = Entry;
})(window);