/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */


var cancellable = function(fn, args, t) {
    var canceled = false;
    
    var timer = setTimeout(function() {
        if (!canceled) {
            fn.apply(null, args);
        }
    }, t);
    
    return function() {
        canceled = true;
        clearTimeout(timer);
    };
};



/**
 *  const result = []
 *
 *  const fn = (x) => x * 5
 *  const args = [2], t = 20, cancelT = 50
 *
 *  const log = (...argsArr) => {
 *      result.push(fn(...argsArr))
 *  }
 *       
 *  const cancel = cancellable(fn, args, t);
 *           
 *  setTimeout(() => {
 *     cancel()
 *     console.log(result) // [{"time":20,"returned":10}]
 *  }, cancelT)
 */