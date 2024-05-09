function deafGrandma() {

    let goodbyCounter = 0
    let input = ""
    let response = ""

    // grandma start conversation
    alert("HEY KID!")

    while (goodbyCounter <= 1) { // continue talking to grandma so long as we haven't said goodbye more than once

        input = window.prompt("Respond to grandma:")

        // say nothing
        if (input === "") {
            response = "WHAT?!"
            // any lower case in input
        } else if (input.toUpperCase() !== input) {
            response = "SPEAK UP, KID!"
            // normal question in all caps
        } else if (input === "GOODBYE!") {
            goodbyCounter++

            if (goodbyCounter > 1) { // we've said goobye once before
                response = "LATER, SKATER!"
            }
            else { // this is the first time we're saying goodbye
                response = "LEAVING SO SOON?"
            }

        } else {
            response = "NO, NOT SINCE 1946!"
        }

        alert(response)
    }
}

deafGrandma();
