(()=>{'use strict';
const body=document.body,toggle=document.querySelector('#toggle-bookshelf');
function library(open){document.querySelector('#lesson-library').hidden=!open;body.classList.toggle('bookshelf-open',open);toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Hide lesson library':'Show lesson library');if(open)document.querySelector('#search').focus();}
toggle.onclick=()=>library(!body.classList.contains('bookshelf-open'));
document.querySelector('#close-bookshelf').onclick=()=>library(false);
document.querySelector('#lesson-list').addEventListener('click',e=>{if(e.target.closest('[data-lesson]')){library(false);window.scrollTo({top:0,behavior:'smooth'});}});
document.addEventListener('keydown',e=>{if(e.key==='Escape')library(false);});
document.querySelectorAll('header nav button').forEach(b=>b.addEventListener('click',()=>{library(false);window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth'});}));
document.querySelector('#nav-method').textContent='Study guide';
document.querySelector('.brand').onclick=e=>{e.preventDefault();document.querySelector('#nav-read').click();};
})();
