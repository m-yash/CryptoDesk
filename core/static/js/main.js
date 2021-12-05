/**==== MENU SHOW ====**/
const showMenu = (toggleId, navID) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navID)

    if(toggle && nav){
        toggle.addEventListener('click',()=>{
            nav.classList.toggle('show')
        })
    }
}

showMenu('nav-toggle','nav-menu')