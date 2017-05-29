'use strict';

(function(module) {
  const entController = {};
  entController.index = () => {
    Entry.fetchAll(entView.initIndexPage);

    $('main > section').hide();
    $('#entries').show();
  };

  module.entController = entController;
})(window);
