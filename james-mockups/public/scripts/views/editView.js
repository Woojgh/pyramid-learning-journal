(function() {
  const editView = {
    initEditPage : () => {
      let template = Handlebars.compile($('#author-template').text());
      Entry.numWordsByAuthor().forEach(stat => $('.author-stats').append(template(stat)));
      $('#blog-stats .entries').text(Entry.all.length);
      $('#blog-stats .words').text(Entry.numWordsAll());
    }
  };

  Entry.fetchAll(editView.initEditPage);
})();