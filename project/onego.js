let hambu=document.getElementById('ham')
let menu=document.getElementById('menu')
hambu.addEventListener('click',function(){
    if(menu.style.display=='flex'){
        menu.style.display='none';
    }else{
        menu.style.display='flex';
    }
})