let answer = document.getElementById("answer");
let input_user = prompt("Enter name: ").toString();

function text_factory(name)
{   
    let revesed_txt = "";
    for (let i = (name.length - 1) ; i >= 0 ; i--)
    {
        // iterate over end to start of string and add it to 
        // revesed_txt
        revesed_txt += name[i];
    }
    return revesed_txt;
}

answer.innerHTML += `<br/> reversed name: ${text_factory(input_user)} `;