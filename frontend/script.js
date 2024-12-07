window.addEventListener("load", () => {
    const allowedChars = `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`;
    const usernameContainer = document.getElementsByClassName("input")[0];
    const passwordContainer = document.getElementsByClassName("input")[1];
    const loginButton = document.getElementById("login-button");

    const spinner = document.getElementsByClassName("spinner")[0];
    const status = document.getElementsByClassName("status")[0];

    // Check if their token is valid or not

    // End of it

    function checkInput(input) {
        for(let i=0; i<input.length; i++) {
            if(!allowedChars.includes(input[i])) {
                return false
            }
        }
        return true
    }
    
    async function login(username, password) {
        try {
            // Check username empty
            if(username == null || username == "") {
                console.log("username empty")
                status.style.display = "block"
                status.innerHTML = "Username Empty"
                makeRed(true, false);
                return
            }
            // Check password empty
            if(password == null || password == "") {
                console.log("Password empty")
                status.style.display = "block"
                status.innerHTML = "Password Empty"
                makeRed(false, true);
                return
            }

            // Try to santize input
            if(!checkInput(username)) {
                console.log("Username cannot contain special chars")
                status.style.display = "block"
                status.innerHTML = "Username cannot contain special chars"
                makeRed(true, false)
                return
            }
            status.style.display = "none"
            spinner.style.display = "inline";
            // Fetch
            const response = await fetch(`https://backend-duuy.onrender.com/login-page/api/login?username=${username}&password=${password}`, {method: "POST"})

            // Check if error code is anything except for ok!
            // If not ok, log it into the console (even though the user can't see it)
            if(!response.ok) {
                console.warn("Server responded with the following status code: " + response.status)
                // aosidjfaposdjfaosdjfoasjdfoajsdofpij
                status.style.display = "block"
                status.innerHTML = `Unknown Error: ${response.status}`
                spinner.style.display = "none";
                return
            }
            const json = await response.json();
            // Get response
            if(json.status == 403) { // This is where the user isn't found
                // Status stuff
                status.style.display = "block"
                status.innerHTML = `Invalid Username/Password`
                spinner.style.display = "none";
            } else if(json.status == 200) {
                // Status stuff
                status.style.display = "none"
                // Set token in localstorage
                localStorage.setItem("token", json.token)
                // Redirect here
                setTimeout(() => {
                    window.location.assign("./home")
                }, 500)
            }

        } catch(error) {
            if(error.message == "Failed to fetch") {
                console.log("Server Down")
                status.style.display = "block"
                status.innerHTML = "Server Down"
                spinner.style.display = "none";
            }
        }
    }

    async function checkToken() {
        try {
            const token = localStorage.getItem("token")
            const response = await fetch(`https://backend-duuy.onrender.com/login-page/api/user?token=${token}`, {method: "POST"})
            if(!response.ok) {
                console.warn("Server responded with the following status code: " + response.status)
                return false
            }
            const json = await response.json();
            if(json.status == 200) {
                window.location.assign("./home")
            }
        } catch(error) {
            console.warn("Server Down")
            status.style.display = "block"
            status.innerHTML = "Server Down"
            spinner.style.display = "none";
        }
    }

    checkToken()

    function makeRed(userContainer, passContainer) {
        if(userContainer) {
            usernameContainer.focus()
        }
        if(passContainer) {
            passwordContainer.focus()
        }
    }



    passwordContainer.addEventListener("keypress", (event) => {
        // Check key code and then click the login button for user easy :)
        if(event.key === "Enter") {
            event.preventDefault();
            loginButton.click();
        }
    })
    
    loginButton.addEventListener("click", () => {
        // idk
        login(usernameContainer.value, passwordContainer.value)
    })
})