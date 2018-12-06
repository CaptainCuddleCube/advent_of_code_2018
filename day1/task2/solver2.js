function solver(args){
    let freqs = {'0':1}
    let acc = 0
    while(true){
        for(var i = 0, len = args.length; i < len; i++){
            acc += args[i]
            if(freqs[acc])
                return acc
            freqs[acc] = 1
        }
    }
}


console.log(solver(process.argv.slice(2, process.argv.length).map(val=>{
    return Number(val)
})))