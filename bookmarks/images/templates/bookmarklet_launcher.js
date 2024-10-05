(function() {
    if (!window.bookmarklet) {
        var bookmarklet_js = document.createElement('script');
        bookmarklet_js.src = '//127.0.0.1:8000/static/js/bookmarklet.js?r=' + Math.floor(Math.random() * 9999999999999999);
        bookmarklet_js.onload = function() {
            console.log('Script loaded, launching bookmarklet...');
            bookmarkletLaunch(); // Now safe to call after the script has loaded
        };
        document.body.appendChild(bookmarklet_js);
        window.bookmarklet = true;
    } else {
        bookmarkletLaunch(); // If already loaded, just launch
    }
})();
