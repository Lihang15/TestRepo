function a() {
            let i,j
             for (i = 2; i <= 100; i++) {

                for (j = 2; j < i; j++) {
                        if (i % j == 0){
                            break;
                        }       
                    }
                if (j == i){
                    console.log(j)
                }
                   

                
           }
        }

a()

var a = 123
function b(){
    a = 345
}
b()
console.log(a)