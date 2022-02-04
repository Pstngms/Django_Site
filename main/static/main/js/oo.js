document.onclick = function(e) {
  const t = e.target
  if (t.tagName === 'BUTTON') {
    t.innerHTML = (t.innerHTML | 0) + 1
  }
}