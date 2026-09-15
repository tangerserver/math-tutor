const CACHE = "mt-v2";
const ASSETS = ["/", "/mt.js", "/manifest.json", "/icon-192.png", "/icon-512.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", e => {
  const url = new URL(e.request.url);
  const isDoc = e.request.mode === "navigate" || url.pathname.endsWith("index.html");
  const isCode = url.pathname.endsWith("/mt.js");
  // HTML 與題庫 JS：每次優先連網抓最新（修改即時生效），斷線才用快取
  if (isDoc || isCode) {
    e.respondWith(
      fetch(e.request)
        .then(res => {
          const copy = res.clone();
          caches.open(CACHE).then(c => c.put(e.request, copy)).catch(() => {});
          return res;
        })
        .catch(() => caches.match(e.request).then(r => r || caches.match("/")))
    );
    return;
  }
  // 靜態資源（icon/manifest）：快取優先，離線可用
  e.respondWith(
    caches.match(e.request).then(r =>
      r || fetch(e.request).then(res => {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(e.request, copy)).catch(() => {});
        return res;
      })
    )
  );
});