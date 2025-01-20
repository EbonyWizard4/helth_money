document.addEventListener("DOMContentLoaded", ()=>{
    const greeBar = document.querySelector(".bar.green");
    const orangeBar = document.querySelector(".bar.orange");

    setTimeout(()=>{
        greeBar.style.height = greeBar.dataset.height + "%"; // Ajusta a altura final desejada
        orangeBar.style.height = orangeBar.dataset.height + "%" // Ajuste a altura final desejada
    }, 100);
});