const ipValid = "1.1.1.1123"
const ipInvalid = "192.168.1.256"


console.log(validate_ip(ipValid))
console.log(validate_ip(ipInvalid))



function validate_ip(ip){
    const validatorRegex = /^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$/

    let validResult = validatorRegex.test(ip)
    if (validResult === true)
    {
        let splitedIP = ip.split(".");
        let is_ok = true;
        
        splitedIP.forEach((e)=>{
            e = parseInt(e);
            if (!(e > 0 && e  <= 255)){
                is_ok = false;
                return;
            }
        })
        
        return is_ok;
    }
    else
    {
        return false;
    }
}