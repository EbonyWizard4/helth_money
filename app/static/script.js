document.addEventListener("DOMContentLoaded", ()=>{
    const greeBar = document.querySelector(".bar.green");
    const orangeBar = document.querySelector(".bar.orange");

    setTimeout(()=>{
        greeBar.style.height = "70%"; // Ajuste a altura final desejada
        orangeBar.style.height = "50%" // Ajuste a altura final desejada
    }, 100);
});