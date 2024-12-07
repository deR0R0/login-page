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
    
    async function signup(username, password) {
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
            const response = await fetch(`https://backend-duuy.onrender.com/login-page/api/signup?username=${username}&password=${password}`, {method: "POST"})

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
            if(json.status == 200) {
                status.style.display = "none"
                alert("You have been successfully signed up! You are able to now login!")
            } else {
                console.log("Username already exists")
                status.style.display = "block"
                status.innerHTML = "Username already exists... Sorry"
                spinner.style.display = "none";
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
        signup(usernameContainer.value, passwordContainer.value)
    })
})