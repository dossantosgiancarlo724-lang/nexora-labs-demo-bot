const products = [
  {id:1,name:'Aero Wireless Headphones',category:'tech',price:129,image:'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=900&q=85',tag:'BESTSELLER'},
  {id:2,name:'Studio Smart Watch',category:'tech',price:189,image:'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=900&q=85',tag:'NEW'},
  {id:3,name:'Urban Runner',category:'lifestyle',price:119,image:'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=85',tag:'LIMITED'},
  {id:4,name:'Minimal Phone Pro',category:'tech',price:799,image:'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=900&q=85',tag:'NEW'},
  {id:5,name:'Everyday Backpack',category:'lifestyle',price:89,image:'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=900&q=85',tag:''},
  {id:6,name:'Essential Sunglasses',category:'lifestyle',price:69,image:'https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=900&q=85',tag:''},
  {id:7,name:'Portable Speaker',category:'tech',price:99,image:'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&w=900&q=85',tag:''},
  {id:8,name:'Classic Timepiece',category:'lifestyle',price:149,image:'https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=900&q=85',tag:''}
];
let activeFilter='all';
let cart=[];

function productCard(p){return `<article class="product"><div class="product-img">${p.tag?`<span class="tag">${p.tag}</span>`:''}<img src="${p.image}" alt="${p.name}" loading="lazy"><button class="quick" onclick="addToCart(${p.id})">Add to bag +</button></div><div class="product-info"><h3>${p.name}</h3><p>${p.category==='tech'?'Technology':'Lifestyle'}</p><p class="price">€${p.price.toFixed(2)}</p></div></article>`}

function renderProducts(){
  const q=(document.getElementById('search')?.value||'').toLowerCase();
  const filtered=products.filter(p=>(activeFilter==='all'||p.category===activeFilter)&&p.name.toLowerCase().includes(q));
  document.getElementById('allProducts').innerHTML=filtered.map(productCard).join('')||'<p>No products found.</p>';
  document.getElementById('featuredProducts').innerHTML=products.slice(0,4).map(productCard).join('');
}

document.querySelectorAll('.filter').forEach(btn=>btn.addEventListener('click',()=>{document.querySelectorAll('.filter').forEach(b=>b.classList.remove('active'));btn.classList.add('active');activeFilter=btn.dataset.filter;renderProducts()}));

function addToCart(id){const p=products.find(x=>x.id===id);const existing=cart.find(x=>x.id===id);if(existing)existing.qty++;else cart.push({...p,qty:1});updateCart();showToast(`${p.name} added to bag`)}
function removeFromCart(id){cart=cart.filter(x=>x.id!==id);updateCart()}
function updateCart(){
  document.getElementById('cartCount').textContent=cart.reduce((s,p)=>s+p.qty,0);
  const box=document.getElementById('cartItems');
  if(!cart.length){box.innerHTML='<div style="padding:45px 0;text-align:center;color:#777;font-size:13px">Your bag is empty.<br><br>Explore the collection to add products.</div>';document.getElementById('subtotal').textContent='€0.00';return}
  box.innerHTML=cart.map(p=>`<div class="cart-row"><img src="${p.image}" alt=""><div><h4>${p.name}</h4><p>Qty ${p.qty} · €${(p.price*p.qty).toFixed(2)}</p></div><button class="remove" onclick="removeFromCart(${p.id})">×</button></div>`).join('');
  document.getElementById('subtotal').textContent='€'+cart.reduce((s,p)=>s+p.price*p.qty,0).toFixed(2);
}
function toggleCart(){document.getElementById('cart').classList.toggle('open');document.getElementById('overlay').classList.toggle('show')}
function focusSearch(){document.getElementById('search').focus();document.getElementById('search').scrollIntoView({behavior:'smooth',block:'center'})}
function checkout(){if(!cart.length){showToast('Add a product before checkout');return}showToast('Demo checkout — no payment processed');}
function showToast(msg){const t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');clearTimeout(window.toastTimer);window.toastTimer=setTimeout(()=>t.classList.remove('show'),2200)}
renderProducts();updateCart();
