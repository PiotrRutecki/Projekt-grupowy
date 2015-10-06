<!DOCTYPE html>
<html>
<head>
<title>ZVB</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script>
$(document).ready(function(){
    $("#hide1").click(function(){
        $("p1").hide();
    });
    $("#show1").click(function(){
        $("p1").show();
    });
    $("#hide2").click(function(){
        $("p2").hide();
    });
    $("#show2").click(function(){
        $("p2").show();
    });
});
</script>
</head>
<body>
<h1>ZVB</h1>


Local host part =================================
<button id="hide1">Hide</button>
<button id="show1">Show</button>

<p1>
	<br>
	%if (hostname != None):
		Host: {{hostname}}
	%end

	<br>
	%if (local_vms != None):
		Vms on this host: {{local_vms}}
	%end
	

	<br>
	%if (known_hosts != None):
		Known hosts in network: {{known_hosts}}
	%end
	
	<br>
	Wanna do sth?
	%for vm in local_vms:
		%for name in vm:
			<br>{{name}}: <a href="/starting_vm/{{name}}">run</a>, <a href="/delete_vm/{{name}}">delete</a>
		%end
	%end	
	<br>
	<a href="/create_vm/">Create new VM: </a>
	
</p1>


<p>
	Known hosts part ===============================
	<button id="hide2">Hide</button>
	<button id="show2">Show</button>
	<br> <p2>Not yet implemented.</p2>
</p>
<form method="post">
<input type="submit" value="refresh">
</form>
</body>
</html>


