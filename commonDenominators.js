// function convertFrac(lst) {
//     const numerator = lst.map(item => item[0]);
//     const denominators = lst.map(item => item[1]);
//     const denom_sorted = [...denominators].sort((a, b) => a - b); // Create a copy before sorting
//     const largest_number = denom_sorted[denom_sorted.length - 1];
//     let multiplier = 1;
//     let lcm;
//     let finalString = '';
//     const newNumerators = [];

//     while (true) {
//         let dom_check = denom_sorted.every(num => (largest_number * multiplier) % num === 0);
//         if (dom_check === true) {
//             lcm = largest_number * multiplier;
//             break;
//         }
//         multiplier++;
//     }
   
//     for (let i = 0; i < numerator.length; i++) {
        
//         const mult = lcm / denominators[i];
//         const newNum = mult * numerator[i];
//         newNumerators.push(newNum);
//     }

//     newNumerators.forEach(element => {
//         finalString += `(${element},${lcm})`;
//     });

//     return finalString;
// }

function convertFrac(lst) {
    const numerators = lst.map(item => item[0]);
    const denominators = lst.map(item => item[1]);
    const lcm = findLCM(denominators);
    const newNumerators = numerators.map((num, i) => (lcm / denominators[i]) * num);
    return newNumerators.map(num => `(${num},${lcm})`).join('');
}

function findLCM(denominators) {
    const maxDenom = Math.max(...denominators);
    let multiplier = 1;
    while (true) {
        const candidateLCM = maxDenom * multiplier;
        if (denominators.every(denom => candidateLCM % denom === 0)) {
            return candidateLCM;
        }
        multiplier++;
    }
}
var lst = [[69, 130], [87, 1310], [3, 4]];

console.log(convertFrac(lst));

