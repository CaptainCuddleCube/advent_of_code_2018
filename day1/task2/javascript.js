
function solver(args){
    let freqs = [0]
    let acc = 0
    let duplicate = false
    let seen = []
    let iteration = 0
    let trigger_time = 10000
    while(!duplicate){
        iteration += 1
        for( let i = 0; i < args.length; i++){
            acc += Number(args[i])
            freqs.push(acc)
        }
        if(iteration % trigger_time === 0){
            console.log("Printing interation ", iteration)
            console.log("freqs length", freqs.length)
            for(let i = 0; i<freqs.length; i++){
                if(seen.indexOf(freqs[i])>=0){
                    duplicate = true;
                    acc = freqs[i];
                    break;
                }
                else{
                    seen.push(freqs[i])
                }
            }
            seen=[]
        }
    }
    return acc
}



console.log(solver(process.argv.slice(2, process.argv.length)))