let navbar = document.getElementById("nav")
let upBtn = document.getElementById("up")
let menuBtn = document.getElementById("menu")
let mobileMenu = document.getElementById("mobile")

window.addEventListener("scroll",()=>{
    if(window.scrollY>60){
        navbar.classList.add("scroll")
    }
    else{
        navbar.classList.remove("scroll")
    }
    if(window.scrollY>120){
        upBtn.style.opacity="1"
    }
    else{
        upBtn.style.opacity="0"
    }
})
upBtn.addEventListener("click",()=>{
    window.location.href="#main"
})

menuBtn.addEventListener("click",()=>{
    let result=menuBtn.classList.toggle("active")
    if(result){
        mobileMenu.classList.add("sidebar-open")
    }
    else{
        mobileMenu.classList.remove("sidebar-open")
    }
})