// Lectorium: lets the site install on a phone. Always asks the network first, so readers
// get new texts and fixes at once; a saved copy of the page and texts is used only offline.
// Audio is never stored here (too large).
const CACHE = 'lectorium-v1';
self.addEventListener('install', e => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;
  if (url.pathname.includes('/audio/') || /\.(mp3|wav|ogg)$/.test(url.pathname)) return;
  e.respondWith(
    fetch(req).then(res => {
      if (res.ok) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)).catch(() => {}); }
      return res;
    }).catch(() => caches.match(req).then(r => r || caches.match('./')))
  );
});
