console.log("file J1")
const display_img = document.getElementById('user_view_img')
const add_img = document.querySelector('#id_user_img')


add_img.addEventListener('change', () => {
    console.log("change the img")
    let reload_img = new FileReader()
    reload_img.readAsDataURL(add_img.files[0]);
    console.log("reloading the img")
    reload_img.addEventListener('load', () => {
        document.getElementById('user_view_img').src = reload_img.result


    });

});