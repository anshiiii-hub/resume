// Scroll progress + nav background + back to top
const navbar=document.getElementById('navbar');
const progress=document.getElementById('scroll-progress');
const backTop=document.getElementById('back-to-top');
window.addEventListener('scroll',()=>{
  const st=window.scrollY, h=document.documentElement.scrollHeight-window.innerHeight;
  progress.style.width=(st/h*100)+'%';
  navbar.classList.toggle('scrolled',st>40);
  backTop.classList.toggle('show',st>600);
},{passive:true});
backTop.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));

// Mobile nav
const navToggle=document.getElementById('navToggle');
const navLinks=document.getElementById('navLinks');
navToggle.addEventListener('click',()=>navLinks.classList.toggle('mobile-open'));
document.querySelectorAll('.nav-links a').forEach(a=>a.addEventListener('click',()=>navLinks.classList.remove('mobile-open')));

// Reveal on scroll
const revealObs=new IntersectionObserver((entries)=>{
  entries.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); revealObs.unobserve(e.target);} });
},{threshold:0.15});
document.querySelectorAll('.reveal').forEach(el=>revealObs.observe(el));

// Animated counters
const counters=document.querySelectorAll('.counter-num');
const countObs=new IntersectionObserver((entries)=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      const el=e.target, target=+el.dataset.count;
      let cur=0; const step=Math.max(1,Math.ceil(target/30));
      const tick=()=>{ cur=Math.min(cur+step,target); el.textContent=cur; if(cur<target) requestAnimationFrame(tick); };
      tick(); countObs.unobserve(el);
    }
  });
},{threshold:0.5});
counters.forEach(c=>countObs.observe(c));

// Bar chart fill animation
const bars=document.querySelectorAll('.bar-fill');
const barObs=new IntersectionObserver((entries)=>{
  entries.forEach(e=>{ if(e.isIntersecting){ e.target.style.width=e.target.dataset.w+'%'; barObs.unobserve(e.target); } });
},{threshold:0.4});
bars.forEach(b=>barObs.observe(b));

// Smooth anchor scroll offset
document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click',function(e){
    const id=this.getAttribute('href');
    if(id.length>1){
      const target=document.querySelector(id);
      if(target){ e.preventDefault(); window.scrollTo({top:target.offsetTop-70,behavior:'smooth'}); }
    }
  });
});

// Dark mode toggle
const themeToggle=document.getElementById('themeToggle');
themeToggle.addEventListener('click',()=>{
  const html=document.documentElement;
  html.setAttribute('data-theme', html.getAttribute('data-theme')==='dark' ? 'light' : 'dark');
});

// Contact form confirmation (mailto submission)
document.getElementById('contactForm').addEventListener('submit',function(){
  const btn=this.querySelector('.btn-submit');
  btn.textContent='Opening your email client...';
});

// Time-of-day personal greeting
(function(){
  const el=document.getElementById('greeting');
  if(!el) return;
  const h=new Date().getHours();
  const part = h<12 ? 'morning' : h<17 ? 'afternoon' : h<21 ? 'evening' : 'night';
  const emoji = h<12 ? '☀️' : h<17 ? '👋' : h<21 ? '🌆' : '🌙';
  el.textContent = `Good ${part}! I'm Anshita ${emoji}`;
})();

// Live IST clock
function updateClock(){
  const el=document.getElementById('liveClock');
  if(!el) return;
  const now=new Date(new Date().toLocaleString('en-US',{timeZone:'Asia/Kolkata'}));
  const hh=String(now.getHours()).padStart(2,'0'), mm=String(now.getMinutes()).padStart(2,'0'), ss=String(now.getSeconds()).padStart(2,'0');
  el.textContent=`${hh}:${mm}:${ss}`;
}
updateClock(); setInterval(updateClock,1000);

// Typewriter role cycling
(function(){
  const dataEl=document.getElementById('typewriter-data');
  const twEl=document.getElementById('typewriter');
  if(!dataEl || !twEl) return;
  let roles;
  try{ roles=JSON.parse(dataEl.textContent); } catch(e){ roles=['Data Science Student.']; }
  let roleIdx=0, charIdx=0, deleting=false;
  function typeLoop(){
    const word=roles[roleIdx];
    if(!deleting){
      charIdx++;
      twEl.textContent=word.slice(0,charIdx);
      if(charIdx===word.length){ deleting=true; setTimeout(typeLoop,1400); return; }
    } else {
      charIdx--;
      twEl.textContent=word.slice(0,charIdx);
      if(charIdx===0){ deleting=false; roleIdx=(roleIdx+1)%roles.length; }
    }
    setTimeout(typeLoop, deleting?40:90);
  }
  typeLoop();
})();
