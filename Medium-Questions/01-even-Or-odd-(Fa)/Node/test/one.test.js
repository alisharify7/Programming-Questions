const validationFuntion = require("../src/one");
const except = require("chai").expect;

describe("Testing Even or Odd Number", () => {
  it("Test 1: Number => 2", (done) => {
    except(validationFuntion(2)).to.equal("valid - Even Number");
    done();
  });

  it("Test 2: Number => 21", (done) => {
    except(validationFuntion(21)).to.equal("not valid - Odd Number");
    done();
  });

  it("Test 3: Number => 101", (done) => {
    except(validationFuntion(101)).to.equal(
      "Invalid Number - Number must Between 1 to 100"
    );
    done();
  });

  it("Test 4: Number => 0", (done) => {
    except(validationFuntion(0)).to.equal(
      "Invalid Number - Number must Between 1 to 100"
    );
    done();
  });
});
