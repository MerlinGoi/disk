function xmass_tree() {
    console.log("Xmas tree script loaded");
    //users_input = document.getElementById("users_input").value;
    users_input = 0;
    for(i = 1; i <= users_input; i++){
        let spaces = ' '.repeat(users_input - i);
        let stars = '*'.repeat(2 * i - 1);
        console.log(spaces + stars);

    }
}
xmass_tree();