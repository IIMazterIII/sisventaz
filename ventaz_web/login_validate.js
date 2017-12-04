function pasuser(form) {
if (form.id.value=="admin") { 
if (form.pass.value=="admin123") {              
location="indexZ.html" 
} else {
alert("Invalid Password")
}
} else {  alert("Invalid UserID")
}
}