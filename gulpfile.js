const gulp = require("gulp");
const { exec } = require('child_process');

__test__ = function(done) {
  console.log("TESTING yey gulfile!");
  exec("cp -R -f \"/Users/smartguy88-home/Desktop/The-WildStar-Project/IOT Integration Code/CircuitPython/dev env/AH_Integration\" \"/Users/smartguy88-home/Desktop/The-WildStar-Project/IOT Integration Code/CircuitPython/dev env/CIRCUITPY\"", (error, stdout, stderr) => {
    if (error) {
        console.log(`error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.log(`stderr: ${stderr}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
  });
  done();
}
__test__.description = "__test__ description!"
module.exports.__test__ = __test__

//gulp.task("hello", helloWorld);