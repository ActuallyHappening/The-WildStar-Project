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
uploadESP32 = function (done) {
  console.log("Uploading Code ...");
  exec("cd \"/Users/smartguy88-home/Desktop/The-WildStar-Project/IOT Integration Code/MicroPython/Integration Code/Code\" && ampy -p /dev/tty.usbserial-0001 -d1 put networking.py networking.py && ampy -p /dev/tty.usbserial-0001 -d1 put main.py main.py && ampy -p /dev/tty.usbserial-0001 -d1 put secrets.plsgitignore.py secrets.py && ampy -p /dev/tty.usbserial-0001 -d1 put AIO.py AIO.py", (error, stdout, stderr) => {
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
uploadESP32.description = "Upload your files to ESP32!"
__test__.description = "__test__ description!"
module.exports.__test__ = __test__
module.exports.uploadESP32 = uploadESP32

//gulp.task("hello", helloWorld);