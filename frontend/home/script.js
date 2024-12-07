window.addEventListener("load", () => {
    const usernameText = document.getElementsByClassName("detail")[0];
    const passwordText = document.getElementsByClassName("detail")[1];
    const tokenText = document.getElementsByClassName("detail")[2];
    const signoutButton = document.getElementsByClassName("signoutbutton")[0];

    async function getUserDetails() {
        // Get the token out of the localstorage and post request
        const r = await fetch(`https://backend-duuy.onrender.com/login-page/api/user?token=${localStorage.getItem("token")}`, {method: "POST"})
        if(!r.ok) {
            console.warn("server responded with" + r.status)
            alert("Err, server probs down. If not, if you're a programmer, check console and fix the error thru prs! Thanks <3")
            return;
        }

        const json = await r.json()
        if(json.status == 403) {
            localStorage.removeItem("token")
            window.location.assign("../")
        }
        console.log(json)
        usernameText.innerHTML = `Username: ${json["name"]}`
        passwordText.innerHTML = `Password: ${json["pass"]}`
        tokenText.innerHTML = `Token: ${json["token"]}`
    }

    async function signOut() {
        const r = await fetch(`https://backend-duuy.onrender.com/login-page/api/signout?token=${localStorage.getItem("token")}`, {method: "POST"})
        if(!r.ok) {
            console.warn("server probably down but status: " + r.status)
            alert("Uhm, server may be down, try again later or look in console and see the status code.")
            return;
        }
    }

    signoutButton.addEventListener("click", () => {
        localStorage.removeItem("token")
        signOut()
        window.location.reload()
    })

    getUserDetails();
})