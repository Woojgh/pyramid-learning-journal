'use strict';

(function () {
  const newEntry = {};

  newEntry.initNewEntryPage = function() {
    $('.tab-content').show();
    $('#export-field').hide();
    $('#entry-json').on('focus', function() {
      $(this).select();
    });
    $('#new-form').on('change', newEntry.create);
    $('#new-form').on('submit', newEntry.submit);
  };

  newEntry.create = function() {
    $('#entries').empty();
    let formEntry = new Entry({
      title: $('#entry-title').val(),
      author: $('#entry-author').val(),
      authorUrl: $('#entry-author-url').val(),
      category: $('#entry-category').val(),
      body: $('#entry-body').val(),
      publishedOn: new Date().toISOString()
    });
    $('#entries').append(formEntry.toHtml('#entry-template'));
    $('pre code').each((i, block) => hljs.highlightBlock(block));
  };

  newEntry.submit = function(event) {
    event.preventDefault();
    let entry = new Entry({
      title: $('#entry-title').val(),
      author: $('#entry-author').val(),
      authorUrl: $('#entry-author-url').val(),
      category: $('#entry-category').val(),
      body: $('#entry-body').val(),
      publishedOn: new Date().toISOString()
    });

    entry.insertRecord();
  }

  newEntry.initNewEntryPage();
})();
