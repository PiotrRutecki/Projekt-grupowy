<!DOCTYPE html>
<html>
<head>
<title>ZVB</title>
</head>
<body>

<h1>ZVB</h1>
<br>
Create Virtual Machine:
<form method="post">
      <table>
	  
        <tr>
          <td class="label">
            VM name:
          </td>
          <td>
            <input type="text" name="vmname" value="{{vmname}}">
          </td>
        </tr>
		
		<tr>
			<td>
				VM type:
			</td>
			<td>
				<input type="radio" name="vmtype" value="{{vmtype}}" checked> Windows
				<br>
				<input type="radio" name="vmtype" value="{{vmtype}}"> Linux
			</td>
		</tr>
       

      </table>

      <input type="submit" value="accept">
</form>

<p> Go to <a href="/">Main page</a></p>

</body>
</html>


