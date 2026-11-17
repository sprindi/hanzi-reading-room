(()=>{'use strict';
const body=document.body,toggle=document.querySelector('#toggle-bookshelf');
const header=document.querySelector('body>header');
function sizeLibrary(){document.documentElement.style.setProperty('--library-top',`${Math.ceil(header.getBoundingClientRect().height)}px`);}
sizeLibrary();
new ResizeObserver(sizeLibrary).observe(header);
function library(open){const panel=document.querySelector('#lesson-library'),restoreFocus=panel.contains(document.activeElement);sizeLibrary();panel.hidden=!open;body.classList.toggle('bookshelf-open',open);toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Hide lesson library':'Show lesson library');if(open){panel.scrollTop=0;document.querySelector('#search').focus({preventScroll:true});}else if(restoreFocus)toggle.focus({preventScroll:true});}
toggle.onclick=()=>library(!body.classList.contains('bookshelf-open'));
document.querySelector('#close-bookshelf').onclick=()=>library(false);
document.querySelector('#lesson-list').addEventListener('click',e=>{if(e.target.closest('[data-lesson]')){library(false);window.scrollTo({top:0,behavior:'smooth'});}});
document.addEventListener('keydown',e=>{if(e.key==='Escape')library(false);});
document.querySelectorAll('header nav button').forEach(b=>b.addEventListener('click',()=>{library(false);window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth'});}));
document.querySelector('#nav-method').textContent='Study guide';
document.querySelector('.brand').onclick=e=>{e.preventDefault();document.querySelector('#nav-read').click();};
})();
