<!DOCTYPE html>
<html>
<head>
<title>ZVB</title>
</head>
<body>
<h1>ZVB</h1>

%if (hostname != None):
Host: {{hostname}}
%end

<p>
%if (local_vms != None):
Vms on this host:
{{local_vms}}
%end
</p>

Wanna do sth?
%for vm in local_vms:
%for name in vm:
<p>{{name}}: <a href="/starting_vm/{{name}}">run</a>, <a href="/delete_vm/{{name}}">delete</a></p>
%end
%end
</body>
</html>


