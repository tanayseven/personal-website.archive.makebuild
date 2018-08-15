document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  const sideNavOptions = {};
  const sideNavInstances = M.Sidenav.init(elems, sideNavOptions);
  var elems = document.querySelectorAll('.collapsible');
  const collapsibleOptions = {accordion: true};
  const collapsibleInstances = M.Collapsible.init(elems, collapsibleOptions)
});

