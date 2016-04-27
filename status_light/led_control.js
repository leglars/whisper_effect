// var five = require("johnny-five");
// var board = new five.Board();

// board.on("ready", function(){
// 	var rgb = new five.Led.RGB([6, 5, 3]);
// 	var index = 0;
// 	var rainbow = ["FF0000", "FF7F00", "FFFF00", "00FF00", "0000FF", "4B0082", "8F00FF"];

// 	this.loop(1000, function(){
// 		if (index + 1 === rainbow.length) {
// 			index = 0;
// 		}
// 		rgb.color(rainbow[index++]);

// 		this.wait(5000, function(){
// 			rgb.fadeOut();
// 		})
// 	});
// });

// var temporal = require("temporal");
// var five = require("johnny-five");
// var board = new five.Board();

// board.on("ready", function() {

//   // Initialize the RGB LED
//   var led = new five.Led.RGB([6, 5, 3]);

//   // Set to full intensity red
//   console.log("100% red");
//   led.color("#FF0000");

//   temporal.queue([{
//     // After 3 seconds, dim to 30% intensity
//     wait: 3000,
//     task: function() {
//       console.log("30% red");
//       led.intensity(30);
//     }
//   }, {
//     // 3 secs then turn blue, still 30% intensity
//     wait: 3000,
//     task: function() {
//       console.log("30% blue");
//       led.color("#0000FF");
//     }
//   }, {
//     // Another 3 seconds, go full intensity blue
//     wait: 3000,
//     task: function() {
//       console.log("100% blue");
//       led.intensity(100);
//     }
//   }, ]);
// });

// var five = require("johnny-five");
// var board = new five.Board();

// board.on("ready", function() {

//   var led = new five.Led(6);

//   led.fadeIn();

//   // Toggle the led after 5 seconds (shown in ms)
//   this.wait(5000, function() {
//     led.fadeOut();
//   });
// });

// var five = require("johnny-five");
// var board = new five.Board();

// board.on("ready", function() {

//   // Create a standard `led` component
//   // on a valid pwm pin
//   var led = new five.Led(6);

//   // Instead of passing a time and rate, you can
//   // pass any valid Animation() segment opts object
//   // https://github.com/rwaldron/johnny-five/wiki/Animation#segment-properties
//   led.pulse({
//     easing: "linear",
//     duration: 3000,
//     cuePoints: [0, 0.2, 0.4, 0.6, 0.8, 1],
//     keyFrames: [0, 10, 0, 50, 0, 255],
//     onstop: function() {
//       console.log("Animation stopped");
//     }
//   });

//   // Stop and turn off the led pulse loop after
//   // 12 seconds (shown in ms)
//   this.wait(12000, function() {

//     // stop() terminates the interval
//     // off() shuts the led off
//     led.stop().off();
//   });
// });

var five = require("johnny-five");
var board = new five.Board();

board.on("ready", function() {

  var led = new five.Led(6);

  led.fade({
    easing: "linear",
    duration: 1000,
    cuePoints: [0, 0.2, 0.4, 0.6, 0.8, 1],
    keyFrames: [0, 250, 25, 150, 100, 125],
    onstop: function() {
      console.log("Animation stopped");
    }
  });

  // Toggle the led after 2 seconds (shown in ms)
  this.wait(2000, function() {
    led.fadeOut();
  });
});