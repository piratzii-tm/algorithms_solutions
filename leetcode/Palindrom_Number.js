/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let y = String(x).split("")
    x = String(x).split("")
    for(let i =0;i<y.length;i+=1){
        if(y[i]!=x[y.length-1-i]){return false}
    }
    return true
};