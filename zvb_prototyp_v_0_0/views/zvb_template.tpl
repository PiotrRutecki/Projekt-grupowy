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
	%if (local_vbox_version != None):
		VirtualBox version: {{local_vbox_version}}
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
			<br>{{name}}: <a href="/starting_vm/{{hostname}}/{{name}}">run</a>, <a href="/delete_vm/{{hostname}}/{{name}}">delete</a>
		%end
	%end	
	<br>
	<a href="/create_vm/">Create new VM: </a>
	
</p1>


<p>
<!-- to do -->
	Known hosts part ===============================
	<button id="hide2">Hide</button>
	<button id="show2">Show</button>
	<!-- <br> <p2>Not yet implemented.</p2> -->
	<!--   -->
	
	%for key, value in remote_vms.iteritems():
		%if (key != hostname):
			<br> {{key}} 
			<br> |__vboxversion: {{remote_vbox[key]}}
			%for i in value:
				%for name in i:
					<br> |__nazwa maszyny: {{name}} <a href="/starting_vm/{{key}}/{{name}}">run</a>, <a href="/delete_vm/{{key}}/{{name}}">delete</a>
				%end
			%end
			
			
		%end
	%end
</p>
<form method="post">
<input type="submit" value="refresh">
</form>
</body>
</html>


