document.querySelectorAll('oembed[url]').forEach(element => {
    const anchor = document.createElement('a');

    anchor.setAttribute('href', element.getAttribute('url'));
    anchor.className = 'embedly-card';

    element.appendChild(anchor);
});