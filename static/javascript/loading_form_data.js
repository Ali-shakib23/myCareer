document.addEventListener("DOMContentLoaded" , () => {
    const ids = ["full_name", "email", "phone", "cover_letter"];
    for (let id of ids) {
        let element = document.getElementById(id);    
        const saved = localStorage.getItem(id);
        if (saved){
            element.value = saved;
        }

        element.onchange = () => localStorage.setItem(id, element.value);
    }
    const submit_btn = document.querySelector(".submit-btn");
    submit_btn.onclick = () => {
        for (let id of ids) 
        {
            localStorage.removeItem(id)
        };
    };
})



