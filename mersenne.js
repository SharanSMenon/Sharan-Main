const inp = require('readline-sync');
let isPrime = num => {
    for (var i = 2; i < num; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}
let primes = array => {
    var primes = []
    var indexes = []
    for (let i = 1; i < array.length; i++) {
        if (isPrime(array[i])) {
            primes.push(array[i])
            indexes.push(array.indexOf(array[i]));
        }
    }
    return [primes, indexes];
};
let mersenne = limit => {
    var pArray = [];
    for (let p = 0; p < limit; p++) {
        pArray.push(p);
    }
    var prime = primes(pArray)[0];
    var possibleMersennes = [];
    var mersenneFor = []
    for (let i = 0; i < prime.length; i++) {
        mersenneFor.push(`2^${prime[i]} - 1`)
        possibleMersennes.push(Math.pow(2, prime[i]) - 1);
    }
    // console.log(possibleMersennes);
    var mersenne = primes(possibleMersennes);
    var corrFor = [];
    for (let i = 0; i < mersenne[1].length; i++) {
        corrFor.push(mersenneFor[mersenne[1][i]]);
    }
    // console.log(mersenne[0]);
    // console.log(mersenne[1]);
    // console.log(corrFor);
    var mersennes = {};
    for (let k = 0; k < corrFor.length; k++) {
        mersennes[corrFor[k]] = mersenne[0][k];

    }
    return mersennes;
};
var retrn = mersenne(100);
console.log(retrn);
// console.log(retrn.length);