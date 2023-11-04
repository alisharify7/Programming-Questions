
function Exit() {
    throw Error("Exit Dudo");

}


function EquationTwo(a, b, c) {
    this.a = 0;
    this.b = 0;
    this.c = 0;
    this.values = { "a": 0, "b": 0, "c": 0, "delta": 0, "answer": 0 };


    this.get_a_b_c = () => {
        let value = ["a", "b", "c"];
        function getFloat(message) {
            while (true) {
                let tmp = prompt(message);
                if (tmp === "q") {
                    Exit()
                }
                let v = parseFloat(tmp);
                switch (v) {

                    case !v:
                        continue
                    case 0:
                        return v;
                    default:
                        if (v >= -100) {
                            if (v <= 100) {
                                return v;
                            }
                        }

                }
            }
        }
        value.forEach(e => {
            let v = getFloat(`Enter ${e}: `);
            this.values[e] = v;
        })
    }



    this.calculateDelta = () => {

        /*
        delta = (b ** 2) - (4 * a * c)
        b ^ 2 - 4ac
        */
        let a = this.values["a"];
        let b = this.values["b"];
        let c = this.values["c"];
        if (a !== 0 && b !== 0) {
            this.values["delta"] = (b ** 2) - (4 * a * c);
        }
        else {
            alert("IMPOSSIBLE");
            Exit();

        }
    }



    this.print_answer = () => {

        let a = this.values["a"];
        let b = this.values["b"];
        let c = this.values["c"];
        let delta = this.values["delta"];

        if (delta > 0) {

            /*
            - (b) + (delta) ** 0.5 / 2a
            - (b) - (delta) ** 0.5 / 2a
            */
            x1 = (-b + (delta ** 0.5)) / (2 * a)
            x2 = (-b - (delta ** 0.5)) / (2 * a)

            alert(`X1: ${(x1).toFixed(3)}`)
            alert(`X2: ${(x2).toFixed(3)}`)
            Exit()
        }
        else if (delta == 0) {

            x = -b / (2 * a)
            alert(`X: ${(x).toFixed(3)}`)
            Exit()
        }
        else {

            alert("IMPOSSIBLE")
            Exit()
        }

    }
}


function main() {
    let e2 = new EquationTwo()
    e2.get_a_b_c()
    e2.calculateDelta()
    e2.print_answer()
}


main()