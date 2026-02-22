/* ============================================================
   Lightbox para imagens — RevealJS Slides UEFS
   Clique em qualquer figura → zoom (lightbox)
   Botão para abrir em nova aba do navegador
   ESC ou clique fora para fechar
   ============================================================ */

(function () {
  "use strict";

  function initLightbox() {
    /* --- Overlay HTML --- */
    var overlay = document.createElement("div");
    overlay.id = "img-lightbox-overlay";
    overlay.innerHTML =
      '<div id="img-lightbox-backdrop"></div>' +
      '<div id="img-lightbox-wrap">' +
        '<img id="img-lightbox-img" src="" alt="">' +
        '<div id="img-lightbox-bar">' +
          '<a id="img-lightbox-newtab" href="" target="_blank" rel="noopener" title="Abrir imagem em nova aba">' +
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>' +
            ' Nova aba' +
          '</a>' +
          '<button id="img-lightbox-close" title="Fechar (ESC)">' +
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>' +
            ' Fechar' +
          '</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(overlay);

    /* --- CSS injetado --- */
    var css = document.createElement("style");
    css.textContent =
      /* cursor de zoom nas figuras dos slides */
      ".reveal .slides img:not(.slide-logo):not([src*='logo']) { cursor: zoom-in; transition: opacity 0.15s; }" +
      ".reveal .slides img:not(.slide-logo):not([src*='logo']):hover { opacity: 0.88; }" +

      /* overlay / backdrop */
      "#img-lightbox-overlay { display:none; position:fixed; inset:0; z-index:99999; }" +
      "#img-lightbox-overlay.active { display:flex; justify-content:center; align-items:center; }" +
      "#img-lightbox-backdrop { position:absolute; inset:0; background:rgba(0,0,0,0.88); cursor:zoom-out; }" +

      /* container da imagem */
      "#img-lightbox-wrap { position:relative; z-index:1; display:flex; flex-direction:column; align-items:center; max-width:94vw; max-height:94vh; }" +
      "#img-lightbox-img { max-width:92vw; max-height:84vh; object-fit:contain; border-radius:6px; box-shadow:0 8px 32px rgba(0,0,0,0.6); }" +

      /* barra de ações */
      "#img-lightbox-bar { display:flex; gap:12px; margin-top:14px; }" +
      "#img-lightbox-bar a, #img-lightbox-bar button { " +
        "display:inline-flex; align-items:center; gap:6px; " +
        "color:#fff; background:rgba(255,255,255,0.12); " +
        "border:1px solid rgba(255,255,255,0.25); " +
        "padding:7px 18px; border-radius:6px; " +
        "font-size:13px; font-family:inherit; " +
        "text-decoration:none; cursor:pointer; " +
        "transition: background 0.2s; }" +
      "#img-lightbox-bar a:hover, #img-lightbox-bar button:hover { background:rgba(255,255,255,0.28); }";
    document.head.appendChild(css);

    /* --- Referências --- */
    var lbImg     = document.getElementById("img-lightbox-img");
    var lbLink    = document.getElementById("img-lightbox-newtab");
    var lbClose   = document.getElementById("img-lightbox-close");
    var lbBack    = document.getElementById("img-lightbox-backdrop");

    /* --- Abrir lightbox --- */
    function openLightbox(src) {
      lbImg.src  = src;
      lbLink.href = src;
      overlay.classList.add("active");
    }

    /* --- Fechar lightbox --- */
    function closeLightbox() {
      overlay.classList.remove("active");
      lbImg.src = "";
    }

    /* --- Eventos de fechar --- */
    lbBack.addEventListener("click", closeLightbox);
    lbClose.addEventListener("click", closeLightbox);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && overlay.classList.contains("active")) {
        closeLightbox();
        e.stopPropagation();
      }
    });

    /* --- Delegar clique em imagens dos slides --- */
    document.addEventListener("click", function (e) {
      var img = e.target;
      if (img.tagName !== "IMG") return;

      /* Ignorar logo e ícones pequenos */
      if (img.classList.contains("slide-logo")) return;
      if (img.naturalWidth < 80 || img.naturalHeight < 80) return;
      if (img.closest(".slide-logo, .reveal > .backgrounds")) return;

      /* Só imagens dentro dos slides */
      if (!img.closest(".reveal .slides")) return;

      e.preventDefault();
      e.stopPropagation();
      openLightbox(img.src);
    }, true);  /* useCapture = true para interceptar antes do RevealJS */
  }

  /* --- Inicializar quando o DOM estiver pronto --- */
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initLightbox);
  } else {
    initLightbox();
  }
})();
