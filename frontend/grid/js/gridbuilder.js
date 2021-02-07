// import * as Tone from '../node_modules/tone/build/Tone.js'


export function buildGrid(id) {
    let container = document.getElementById(id);
    let notes = ["C", "D", "E", "F", "G", "A", "B"];
    let finalNotes = [];
    for (let j = 0; j < 8; j++) {
        for (const key in notes) {
            finalNotes.push(notes[key] + j)
        }
    }
    console.log(finalNotes)

    for (let i = 0; i < 50 * 20; i++) {

        let element = document.createElement("div");
        element.classList.add("item");
        if (i % Math.floor(Math.random() * 10) == 0) {
            element.classList.add("disabled");
        }
        // element.innerHTML = parseInt(i+1);
        container.appendChild(element);
    }

    // event delegation
    container.onclick = (event) => {
        //create a synth and connect it to the main output (your speakers)
        const synth = new Tone.Synth();
        let target = event.target;

        if (target.classList.contains("container")){
            return;
        }

        if (target.classList.contains("disabled") == false) {
            let noteAssigned = null;
            if (target.classList.contains("active") == false) {
                //play a middle 'C' for the duration of an 8th note
                target.classList.add("A0")
                target.classList.add("active")
                target.innerText = "A0";
                noteAssigned = "A0";
            } else if (target.classList.contains("active") == true) {
                let found = false;
                for (let note of finalNotes) {
                    if (!found && target.classList.contains(note) == true){
                        target.classList.remove(note)
                        target.innerText = "";
                        found = true;
                    }
                    else if (found){
                        target.classList.add(note)
                        target.innerText = note;
                        noteAssigned = note;
                        break;
                    }
                }
            }

            if (noteAssigned != null){
                target.onmouseover = () => {
                    console.log(noteAssigned)
                    synth.toDestination().triggerAttackRelease(noteAssigned, "8n");
                }
            }

        }
    }

    // // event delegation
    // container.onmouseover = (event) => {
    //     //create a synth and connect it to the main output (your speakers)
    //     const synth = new Tone.Synth();
    //     let target = event.target;

    //     if (target.classList.contains("clicked")) {
    //         //play a middle 'C' for the duration of an 8th note
    //         synth.toDestination().triggerAttackRelease("C4", "8n");
    //     } else if (target.classList.contains("active") == false) {
    //         //play a middle 'C' for the duration of an 8th note
    //         synth.toDestination().triggerAttackRelease("E4", "8n");
    //     } else if (target.classList.contains("active")) {
    //         synth.toDestination().triggerAttackRelease("A2", "8n");
    //     }
    // }
}

