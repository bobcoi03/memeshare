let profile_pic_button = document.getElementById("user-menu-button")
let profile_dropdown_menu = document.getElementById("profile-dropdown-menu")

function toggle_profile_dropdown_menu() {
    if (profile_dropdown_menu.style.display == 'none') {
        profile_dropdown_menu.style.display = 'inline'
    } else {
        profile_dropdown_menu.style.display = 'none'
    }
}