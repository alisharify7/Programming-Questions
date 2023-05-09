// Input: [19, 19, 15, 5, 3, 5, 5, 2] Output: True
// Input: [19, 15, 15, 5, 3, 3, 5, 2] Output: False
// Input: [19, 19, 5, 5, 5, 5, 5] Output: True


const listOne = [19, 19, 15, 5, 3, 5, 5, 2] 
const listTwo = [19, 15, 15, 5, 3, 3, 5, 2] 
const listThere = [19, 19, 5, 5, 5, 5, 5]


function validate_list(list){
    let fives = 0;
    let nineten = 0;
    list.forEach(e => {
        if(e == 19){
            nineten += 1;
        }
        else if(e == 5){
            fives += 1;
        }
    });
    return fives >= 3 && nineten == 2 ? true : false
}

console.log(`List One: ${listOne}` ,validate_list(listOne))
console.log(`List Two: ${listTwo}` ,validate_list(listTwo))
console.log(`List There: ${listThere}` ,validate_list(listThere))



