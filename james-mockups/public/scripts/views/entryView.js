'use strict';

(function (module) {
  const entryView = {};

  entryView.populateFilters = function() {
    $('entry').each(function() {
      if (!$(this).hasClass('template')) {
        let val = $(this).find('address a').text();
        let optionTag = `<option value="${val}">${val}</option>`;

        if ($(`#author-filter option[value="${val}"]`).length === 0) {
          $('#author-filter').append(optionTag);
        }

        val = $(this).attr('data-category');
        optionTag = `<option value="${val}">${val}</option>`;
        if ($(`#category-filter option[value="${val}"]`).length === 0) {
          $('#category-filter').append(optionTag);
        }
      }
    });
  };

  entryView.setTeasers = function() {
    $('.entry-body *:nth-of-type(n+2)').hide();
    $('entry').on('click', 'a.read-on', function(e) {
      e.preventDefault();
      if ($(this).text() === 'Read on →') {
        $(this).parent().find('*').fadeIn();
        $(this).html('Show Less &larr;');
      } else {
        $('body').animate({
          scrollTop: ($(this).parent().offset().top)
        },200);
        $(this).html('Read on &rarr;');
        $(this).parent().find('.entry-body *:nth-of-type(n+2)').hide();
      }
    });
  };

  entryView.initIndexPage = () => {
    $('#ajax-spinner').fadeOut();
    $('#filters').fadeIn();
    Entry.all.forEach(entry => {
      $('#entries').append(entry.toHtml('#entry-template'));
      if($(`#category-filter option:contains("${entry.category}")`).length === 0) {
        $('#category-filter').append(entry.toHtml('#category-filter-template'));
      }
      if($(`#author-filter option:contains("${entry.author}")`).length === 0) {
        $('#author-filter').append(entry.toHtml('#author-filter-template'));
      }
    });

    entryView.populateFilters();
    entryView.handleCategoryFilter();
    entryView.handleAuthorFilter();
    entryView.setTeasers();
  };

  Entry.fetchAll(entryView.initIndexPage);
  module.entryView = entryView;
})(window);
